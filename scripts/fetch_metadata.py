#!/usr/bin/env python3
"""
Booksplode Metadata Fetcher

Fetches and updates book metadata from Open Library API during the review process.
This script can:
- Fetch metadata for a single book
- Update a book's README.md with enhanced metadata
- Process all books in the repository
- Export metadata to JSON files

Usage:
    python fetch_metadata.py <book_folder>           # Fetch and update single book
    python fetch_metadata.py --all                   # Process all books
    python fetch_metadata.py --list                  # List all books
    python fetch_metadata.py --json <book_folder>    # Output JSON only

Examples:
    python fetch_metadata.py meadows_thinking-in-systems
    python fetch_metadata.py --all
    python fetch_metadata.py --json heath_made-to-stick > metadata.json
"""

import argparse
import json
import os
import re
import signal
import sys
from pathlib import Path
from typing import Optional

# Handle broken pipe gracefully (e.g., when piping to head)
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

from openlibrary import OpenLibraryClient, BookMetadata


# Repository root (parent of scripts directory)
REPO_ROOT = Path(__file__).parent.parent.resolve()


def parse_book_folder_name(folder_name: str) -> tuple[str, str]:
    """
    Parse a book folder name into author and title.

    Args:
        folder_name: Folder name like "meadows_thinking-in-systems"

    Returns:
        Tuple of (author_name, book_title)
    """
    parts = folder_name.split("_", 1)
    if len(parts) != 2:
        return folder_name, folder_name

    author = parts[0].replace("-", " ").title()
    title = parts[1].replace("-", " ").title()

    return author, title


def parse_readme_metadata(readme_path: Path) -> dict:
    """
    Parse existing metadata from a README.md file.

    Args:
        readme_path: Path to README.md

    Returns:
        Dictionary with parsed metadata
    """
    metadata = {}

    if not readme_path.exists():
        return metadata

    content = readme_path.read_text()

    # Parse title (first H1)
    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    if title_match:
        metadata["title"] = title_match.group(1).strip()

    # Parse author(s)
    author_match = re.search(r"\*\*Author\(s\):\*\*\s*(.+)$", content, re.MULTILINE)
    if author_match:
        metadata["authors"] = author_match.group(1).strip()

    # Parse category
    category_match = re.search(r"\*\*Category:\*\*\s*(.+)$", content, re.MULTILINE)
    if category_match:
        metadata["category"] = category_match.group(1).strip()

    # Parse ISBN if present
    isbn_match = re.search(r"\*\*ISBN:\*\*\s*(.+)$", content, re.MULTILINE)
    if isbn_match:
        metadata["isbn"] = isbn_match.group(1).strip()

    return metadata


def generate_metadata_section(metadata: BookMetadata) -> str:
    """
    Generate the Open Library metadata section for a README.

    Args:
        metadata: BookMetadata object

    Returns:
        Markdown string for the metadata section
    """
    lines = []
    lines.append("## Open Library Metadata")
    lines.append("")
    lines.append("*Automatically fetched from [Open Library](https://openlibrary.org)*")
    lines.append("")

    # Basic info table
    lines.append("| Field | Value |")
    lines.append("|:------|:------|")

    if metadata.isbn_13:
        lines.append(f"| **ISBN-13** | {metadata.isbn_13[0]} |")
    elif metadata.isbn_10:
        lines.append(f"| **ISBN-10** | {metadata.isbn_10[0]} |")

    if metadata.publisher:
        lines.append(f"| **Publisher** | {metadata.publisher} |")

    if metadata.publish_date:
        lines.append(f"| **Published** | {metadata.publish_date} |")
    elif metadata.first_publish_year:
        lines.append(f"| **First Published** | {metadata.first_publish_year} |")

    if metadata.number_of_pages:
        lines.append(f"| **Pages** | {metadata.number_of_pages} |")

    if metadata.edition_count:
        lines.append(f"| **Editions** | {metadata.edition_count} |")

    if metadata.openlibrary_url:
        lines.append(f"| **Open Library** | [{metadata.openlibrary_work_id}]({metadata.openlibrary_url}) |")

    lines.append("")

    # Cover image
    if metadata.cover_url_medium:
        lines.append("### Cover")
        lines.append("")
        lines.append(f"![Book Cover]({metadata.cover_url_medium})")
        lines.append("")

    # Description
    if metadata.description:
        lines.append("### Description")
        lines.append("")
        # Truncate long descriptions
        desc = metadata.description
        if len(desc) > 1000:
            desc = desc[:997] + "..."
        lines.append(desc)
        lines.append("")

    # Subjects
    if metadata.subjects:
        lines.append("### Subjects")
        lines.append("")
        # Limit to 10 subjects
        subjects = metadata.subjects[:10]
        lines.append(", ".join(f"`{s}`" for s in subjects))
        lines.append("")

    return "\n".join(lines)


def update_readme_with_metadata(readme_path: Path, metadata: BookMetadata) -> bool:
    """
    Update a README.md file with Open Library metadata.

    Args:
        readme_path: Path to README.md
        metadata: BookMetadata object

    Returns:
        True if updated successfully
    """
    if not readme_path.exists():
        print(f"  README not found: {readme_path}")
        return False

    content = readme_path.read_text()

    # Generate new metadata section
    metadata_section = generate_metadata_section(metadata)

    # Check if metadata section already exists
    if "## Open Library Metadata" in content:
        # Replace existing section
        pattern = r"## Open Library Metadata.*?(?=\n## |\n---|\Z)"
        content = re.sub(pattern, metadata_section.rstrip() + "\n", content, flags=re.DOTALL)
    else:
        # Insert after "Why This Book?" section or at the end before Status
        status_match = re.search(r"\n## Status\n", content)
        phases_match = re.search(r"\n## Booksplode Phases\n", content)

        if phases_match:
            # Insert before Booksplode Phases
            insert_pos = phases_match.start()
            content = (
                content[:insert_pos] +
                "\n" + metadata_section + "\n---\n" +
                content[insert_pos:]
            )
        elif status_match:
            # Insert before Status
            insert_pos = status_match.start()
            content = (
                content[:insert_pos] +
                "\n" + metadata_section + "\n---\n" +
                content[insert_pos:]
            )
        else:
            # Append at end
            content = content.rstrip() + "\n\n---\n\n" + metadata_section

    readme_path.write_text(content)
    return True


def save_metadata_json(book_path: Path, metadata: BookMetadata) -> Path:
    """
    Save metadata to a JSON file in the book folder.

    Args:
        book_path: Path to book folder
        metadata: BookMetadata object

    Returns:
        Path to the created JSON file
    """
    json_path = book_path / "metadata.json"
    json_path.write_text(metadata.to_json())
    return json_path


def get_all_book_folders() -> list[Path]:
    """Get all book folders in the repository."""
    folders = []

    for item in REPO_ROOT.iterdir():
        if not item.is_dir():
            continue

        # Skip special directories
        if item.name.startswith(".") or item.name in {"TEMPLATE", "scripts", "assets"}:
            continue

        # Check if it has the expected structure (contains phase files or README)
        if (item / "README.md").exists() or (item / "00_vetting.md").exists():
            folders.append(item)

    return sorted(folders)


def fetch_and_update_book(
    folder_name: str,
    client: OpenLibraryClient,
    json_only: bool = False,
    save_json: bool = True
) -> Optional[BookMetadata]:
    """
    Fetch metadata for a book and update its README.

    Args:
        folder_name: Book folder name
        client: OpenLibraryClient instance
        json_only: If True, only output JSON (don't update README)
        save_json: If True, save metadata.json file

    Returns:
        BookMetadata if successful, None otherwise
    """
    book_path = REPO_ROOT / folder_name

    if not book_path.exists():
        print(f"Error: Book folder not found: {folder_name}", file=sys.stderr)
        return None

    # Parse folder name for search
    author, title = parse_book_folder_name(folder_name)

    # Check for existing metadata in README
    readme_path = book_path / "README.md"
    existing = parse_readme_metadata(readme_path)

    # Use existing metadata if available
    search_title = existing.get("title", title)
    search_author = existing.get("authors", author)
    search_isbn = existing.get("isbn")

    if not json_only:
        print(f"Fetching metadata for: {search_title}")
        print(f"  Author: {search_author}")
        if search_isbn:
            print(f"  ISBN: {search_isbn}")

    # Fetch from Open Library
    metadata = client.fetch_book_metadata(
        title=search_title,
        author=search_author,
        isbn=search_isbn
    )

    if not metadata:
        if not json_only:
            print("  No metadata found on Open Library")
        return None

    if json_only:
        # Just output JSON
        print(metadata.to_json())
        return metadata

    print(f"  Found: {metadata.title}")
    if metadata.first_publish_year:
        print(f"  First published: {metadata.first_publish_year}")
    if metadata.subjects:
        print(f"  Subjects: {', '.join(metadata.subjects[:3])}")

    # Save JSON
    if save_json:
        json_path = save_metadata_json(book_path, metadata)
        print(f"  Saved: {json_path.name}")

    # Update README
    if update_readme_with_metadata(readme_path, metadata):
        print(f"  Updated: README.md")

    return metadata


def list_books() -> None:
    """List all book folders."""
    folders = get_all_book_folders()

    print(f"Found {len(folders)} books:\n")
    for folder in folders:
        author, title = parse_book_folder_name(folder.name)

        # Check for existing metadata
        has_metadata = (folder / "metadata.json").exists()
        status = "[✓]" if has_metadata else "[ ]"

        print(f"  {status} {folder.name}")
        print(f"      {title} by {author}")


def process_all_books(client: OpenLibraryClient) -> dict:
    """
    Process all books in the repository.

    Args:
        client: OpenLibraryClient instance

    Returns:
        Summary statistics
    """
    folders = get_all_book_folders()

    stats = {
        "total": len(folders),
        "success": 0,
        "failed": 0,
        "skipped": 0
    }

    print(f"Processing {len(folders)} books...\n")

    for folder in folders:
        # Check if already has metadata
        if (folder / "metadata.json").exists():
            print(f"Skipping {folder.name} (already has metadata)")
            stats["skipped"] += 1
            continue

        print(f"\n{'='*60}")
        metadata = fetch_and_update_book(folder.name, client)

        if metadata:
            stats["success"] += 1
        else:
            stats["failed"] += 1

    return stats


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Fetch book metadata from Open Library",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        "book_folder",
        nargs="?",
        help="Book folder name (e.g., meadows_thinking-in-systems)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process all books in the repository"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all book folders"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON only (don't update files)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-fetch even if metadata.json exists"
    )

    args = parser.parse_args()

    # List mode
    if args.list:
        list_books()
        return

    # Create client
    client = OpenLibraryClient(rate_limit_delay=1.0)

    # Process all books
    if args.all:
        stats = process_all_books(client)
        print(f"\n{'='*60}")
        print(f"Summary:")
        print(f"  Total: {stats['total']}")
        print(f"  Success: {stats['success']}")
        print(f"  Failed: {stats['failed']}")
        print(f"  Skipped: {stats['skipped']}")
        return

    # Single book mode
    if not args.book_folder:
        parser.print_help()
        sys.exit(1)

    fetch_and_update_book(
        args.book_folder,
        client,
        json_only=args.json
    )


if __name__ == "__main__":
    main()
