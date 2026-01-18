# Booksplode Scripts

Scripts for automating parts of the Booksplode workflow.

## Metadata Fetcher

Fetch and update book metadata from the [Open Library API](https://openlibrary.org/developers/api).

### Requirements

- Python 3.10+
- No external dependencies (uses standard library only)

### Usage

```bash
# Navigate to scripts directory
cd scripts

# Fetch metadata for a single book
python fetch_metadata.py meadows_thinking-in-systems

# List all books and their metadata status
python fetch_metadata.py --list

# Process all books without existing metadata
python fetch_metadata.py --all

# Output JSON only (don't update files)
python fetch_metadata.py --json meadows_thinking-in-systems
```

### What It Does

1. **Searches Open Library** by book title and author
2. **Fetches metadata** including:
   - ISBN (10 and 13)
   - Publisher and publication date
   - Number of pages
   - Subject classifications
   - Book description
   - Cover image URLs
3. **Saves metadata.json** to the book folder
4. **Updates README.md** with a formatted metadata section

### Example Output

After running on a book, you'll see:

```
Fetching metadata for: Thinking in Systems
  Author: Donella Meadows
  Found: Thinking in Systems
  First published: 2008
  Subjects: System theory, Social systems, Environmental policy
  Saved: metadata.json
  Updated: README.md
```

### Files Created

For each book processed:

- `{book_folder}/metadata.json` - Raw API response data
- `{book_folder}/README.md` - Updated with Open Library Metadata section

### Integration with Review Workflow

Run the metadata fetcher at the start of each book review (Phase 0):

```bash
# 1. Create book folder
mkdir -p author_book-title
cp TEMPLATE/* author_book-title/

# 2. Fetch metadata
python scripts/fetch_metadata.py author_book-title

# 3. Continue with Phase 0 vetting...
```

### API Rate Limiting

The script includes built-in rate limiting (1 request per second) to respect Open Library's API guidelines. When processing all books with `--all`, expect ~2 seconds per book.

## Module: openlibrary.py

A reusable Python client for the Open Library API.

### Features

- Search by title, author, or ISBN
- Get work details and editions
- Get author information
- Generate cover image URLs
- Structured `BookMetadata` dataclass

### Example Usage

```python
from openlibrary import OpenLibraryClient

client = OpenLibraryClient()

# Search for a book
results = client.search_books(title="Thinking in Systems", author="Meadows")

# Fetch comprehensive metadata
metadata = client.fetch_book_metadata(
    title="Thinking in Systems",
    author="Donella Meadows"
)

# Output as JSON
print(metadata.to_json())

# Get specific fields
print(f"ISBN: {metadata.isbn_13}")
print(f"Published: {metadata.first_publish_year}")
print(f"Subjects: {metadata.subjects}")
```

## Schema

See `metadata_schema.json` for the JSON schema defining the metadata structure.
