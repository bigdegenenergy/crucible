"""
Open Library API Client

This module provides a Python client for the Open Library API.
https://openlibrary.org/developers/api

Used to enhance book metadata during the Booksplode review process.
"""

import json
import time
import urllib.request
import urllib.parse
import urllib.error
from dataclasses import dataclass, field, asdict
from typing import Optional


# User-Agent header required by Open Library API
USER_AGENT = "Booksplode/1.0 (https://github.com/bigdegenenergy/booksplode)"

# API endpoints
SEARCH_API = "https://openlibrary.org/search.json"
WORKS_API = "https://openlibrary.org/works"
ISBN_API = "https://openlibrary.org/isbn"
AUTHORS_API = "https://openlibrary.org/authors"
COVERS_API = "https://covers.openlibrary.org/b"


@dataclass
class BookMetadata:
    """Structured book metadata from Open Library."""

    # Basic info
    title: str = ""
    subtitle: str = ""
    authors: list[str] = field(default_factory=list)

    # Identifiers
    isbn_10: list[str] = field(default_factory=list)
    isbn_13: list[str] = field(default_factory=list)
    openlibrary_work_id: str = ""
    openlibrary_edition_id: str = ""

    # Publication info
    publisher: str = ""
    publishers: list[str] = field(default_factory=list)
    publish_date: str = ""
    first_publish_year: Optional[int] = None
    number_of_pages: Optional[int] = None

    # Classification
    subjects: list[str] = field(default_factory=list)
    subject_places: list[str] = field(default_factory=list)
    subject_people: list[str] = field(default_factory=list)
    subject_times: list[str] = field(default_factory=list)

    # Description
    description: str = ""
    first_sentence: str = ""

    # Links
    openlibrary_url: str = ""
    cover_url_small: str = ""
    cover_url_medium: str = ""
    cover_url_large: str = ""

    # Additional
    edition_count: Optional[int] = None
    languages: list[str] = field(default_factory=list)

    # Metadata about the fetch
    fetch_timestamp: str = ""
    data_source: str = "openlibrary"

    def to_dict(self) -> dict:
        """Convert to dictionary, filtering out empty values."""
        data = asdict(self)
        return {k: v for k, v in data.items() if v or v == 0}

    def to_json(self, indent: int = 2) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_dict(), indent=indent)


class OpenLibraryClient:
    """Client for interacting with the Open Library API."""

    def __init__(self, rate_limit_delay: float = 1.0):
        """
        Initialize the client.

        Args:
            rate_limit_delay: Seconds to wait between requests (default 1.0)
        """
        self.rate_limit_delay = rate_limit_delay
        self._last_request_time = 0.0

    def _make_request(self, url: str) -> Optional[dict]:
        """Make a rate-limited HTTP request to the API."""
        # Rate limiting
        elapsed = time.time() - self._last_request_time
        if elapsed < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay - elapsed)

        self._last_request_time = time.time()

        request = urllib.request.Request(
            url,
            headers={"User-Agent": USER_AGENT}
        )

        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            print(f"HTTP Error {e.code}: {url}")
            return None
        except urllib.error.URLError as e:
            print(f"URL Error: {e.reason}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return None

    def search_books(
        self,
        title: Optional[str] = None,
        author: Optional[str] = None,
        query: Optional[str] = None,
        limit: int = 5
    ) -> list[dict]:
        """
        Search for books by title, author, or general query.

        Args:
            title: Book title to search for
            author: Author name to search for
            query: General search query
            limit: Maximum results to return

        Returns:
            List of book result dictionaries
        """
        params = {"limit": str(limit)}

        if title:
            params["title"] = title
        if author:
            params["author"] = author
        if query:
            params["q"] = query

        url = f"{SEARCH_API}?{urllib.parse.urlencode(params)}"
        data = self._make_request(url)

        if data and "docs" in data:
            return data["docs"][:limit]
        return []

    def get_work(self, work_id: str) -> Optional[dict]:
        """
        Get detailed information about a work.

        Args:
            work_id: Open Library work ID (e.g., "OL45804W")

        Returns:
            Work data dictionary or None
        """
        # Clean up the work ID
        if work_id.startswith("/works/"):
            work_id = work_id[7:]

        url = f"{WORKS_API}/{work_id}.json"
        return self._make_request(url)

    def get_work_editions(self, work_id: str, limit: int = 10) -> list[dict]:
        """
        Get editions of a work.

        Args:
            work_id: Open Library work ID
            limit: Maximum editions to return

        Returns:
            List of edition dictionaries
        """
        if work_id.startswith("/works/"):
            work_id = work_id[7:]

        url = f"{WORKS_API}/{work_id}/editions.json?limit={limit}"
        data = self._make_request(url)

        if data and "entries" in data:
            return data["entries"][:limit]
        return []

    def get_by_isbn(self, isbn: str) -> Optional[dict]:
        """
        Get book data by ISBN.

        Args:
            isbn: ISBN-10 or ISBN-13

        Returns:
            Book data dictionary or None
        """
        # Clean ISBN
        isbn = isbn.replace("-", "").replace(" ", "")
        url = f"{ISBN_API}/{isbn}.json"
        return self._make_request(url)

    def get_author(self, author_id: str) -> Optional[dict]:
        """
        Get author information.

        Args:
            author_id: Open Library author ID (e.g., "OL34184A")

        Returns:
            Author data dictionary or None
        """
        if author_id.startswith("/authors/"):
            author_id = author_id[9:]

        url = f"{AUTHORS_API}/{author_id}.json"
        return self._make_request(url)

    @staticmethod
    def get_cover_url(
        cover_id: int,
        size: str = "M",
        key_type: str = "id"
    ) -> str:
        """
        Generate a cover image URL.

        Args:
            cover_id: Cover ID, ISBN, or OLID depending on key_type
            size: S (small), M (medium), or L (large)
            key_type: "id", "isbn", or "olid"

        Returns:
            Cover image URL
        """
        return f"{COVERS_API}/{key_type}/{cover_id}-{size}.jpg"

    def fetch_book_metadata(
        self,
        title: str,
        author: Optional[str] = None,
        isbn: Optional[str] = None
    ) -> Optional[BookMetadata]:
        """
        Fetch comprehensive metadata for a book.

        This is the main method for retrieving book metadata. It will:
        1. Try ISBN lookup first if provided
        2. Fall back to title/author search
        3. Enrich with work and author data

        Args:
            title: Book title
            author: Author name (optional but recommended)
            isbn: ISBN-10 or ISBN-13 (optional, takes priority)

        Returns:
            BookMetadata object or None if not found
        """
        from datetime import datetime

        metadata = BookMetadata()
        metadata.fetch_timestamp = datetime.utcnow().isoformat() + "Z"

        work_data = None
        edition_data = None

        # Strategy 1: ISBN lookup
        if isbn:
            edition_data = self.get_by_isbn(isbn)
            if edition_data:
                # Get associated work
                works = edition_data.get("works", [])
                if works:
                    work_key = works[0].get("key", "")
                    work_data = self.get_work(work_key)

        # Strategy 2: Search by title and author
        if not edition_data:
            results = self.search_books(title=title, author=author, limit=5)

            if results:
                # Find best match
                best_match = self._find_best_match(results, title, author)

                if best_match:
                    # Get work data
                    work_key = best_match.get("key", "")
                    if work_key:
                        work_data = self.get_work(work_key)

                    # Get first edition for detailed info
                    editions = self.get_work_editions(work_key, limit=1)
                    if editions:
                        edition_data = editions[0]

                    # Populate from search result
                    self._populate_from_search(metadata, best_match)

        # Enrich with work data
        if work_data:
            self._populate_from_work(metadata, work_data)

        # Enrich with edition data
        if edition_data:
            self._populate_from_edition(metadata, edition_data)

        # Set cover URLs if we have cover IDs
        if edition_data and edition_data.get("covers"):
            cover_id = edition_data["covers"][0]
            metadata.cover_url_small = self.get_cover_url(cover_id, "S")
            metadata.cover_url_medium = self.get_cover_url(cover_id, "M")
            metadata.cover_url_large = self.get_cover_url(cover_id, "L")

        # Only return if we found something
        if metadata.title or metadata.openlibrary_work_id:
            return metadata

        return None

    def _find_best_match(
        self,
        results: list[dict],
        title: str,
        author: Optional[str]
    ) -> Optional[dict]:
        """Find the best matching result from search."""
        title_lower = title.lower()

        for result in results:
            result_title = result.get("title", "").lower()

            # Exact title match
            if result_title == title_lower:
                return result

            # Title contains search
            if title_lower in result_title or result_title in title_lower:
                # Check author if provided
                if author:
                    authors = result.get("author_name", [])
                    author_lower = author.lower()
                    if any(author_lower in a.lower() for a in authors):
                        return result
                else:
                    return result

        # Return first result as fallback
        return results[0] if results else None

    def _populate_from_search(self, metadata: BookMetadata, data: dict) -> None:
        """Populate metadata from search result."""
        metadata.title = data.get("title", "")
        metadata.subtitle = data.get("subtitle", "")
        metadata.authors = data.get("author_name", [])
        metadata.first_publish_year = data.get("first_publish_year")
        metadata.edition_count = data.get("edition_count")
        metadata.subjects = data.get("subject", [])[:20]  # Limit subjects
        metadata.languages = data.get("language", [])
        metadata.isbn_10 = data.get("isbn", [])[:5]  # Sample ISBNs

        # Work ID
        key = data.get("key", "")
        if key:
            metadata.openlibrary_work_id = key.replace("/works/", "")
            metadata.openlibrary_url = f"https://openlibrary.org{key}"

    def _populate_from_work(self, metadata: BookMetadata, data: dict) -> None:
        """Populate metadata from work data."""
        if not metadata.title:
            metadata.title = data.get("title", "")

        # Description
        desc = data.get("description", "")
        if isinstance(desc, dict):
            desc = desc.get("value", "")
        metadata.description = desc

        # First sentence
        first = data.get("first_sentence", "")
        if isinstance(first, dict):
            first = first.get("value", "")
        metadata.first_sentence = first

        # Subjects
        if not metadata.subjects:
            metadata.subjects = data.get("subjects", [])[:20]

        metadata.subject_places = data.get("subject_places", [])[:10]
        metadata.subject_people = data.get("subject_people", [])[:10]
        metadata.subject_times = data.get("subject_times", [])[:10]

        # Work ID
        key = data.get("key", "")
        if key:
            metadata.openlibrary_work_id = key.replace("/works/", "")
            metadata.openlibrary_url = f"https://openlibrary.org{key}"

    def _populate_from_edition(self, metadata: BookMetadata, data: dict) -> None:
        """Populate metadata from edition data."""
        if not metadata.title:
            metadata.title = data.get("title", "")

        # Publishers
        publishers = data.get("publishers", [])
        metadata.publishers = publishers
        if publishers:
            metadata.publisher = publishers[0]

        # Publication date
        metadata.publish_date = data.get("publish_date", "")

        # Pages
        metadata.number_of_pages = data.get("number_of_pages")

        # ISBNs
        isbn_10 = data.get("isbn_10", [])
        isbn_13 = data.get("isbn_13", [])
        if isbn_10:
            metadata.isbn_10 = isbn_10
        if isbn_13:
            metadata.isbn_13 = isbn_13

        # Edition ID
        key = data.get("key", "")
        if key:
            metadata.openlibrary_edition_id = key.replace("/books/", "")


def main():
    """Example usage of the Open Library client."""
    client = OpenLibraryClient()

    # Example: Fetch metadata for "Thinking in Systems"
    print("Fetching metadata for 'Thinking in Systems'...")
    metadata = client.fetch_book_metadata(
        title="Thinking in Systems",
        author="Donella Meadows"
    )

    if metadata:
        print(metadata.to_json())
    else:
        print("Book not found")


if __name__ == "__main__":
    main()
