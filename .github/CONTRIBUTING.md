# Contributing to Crucible

Thank you for your interest in contributing! This guide covers how to add new book research, improve existing analyses, and contribute to the tooling.

## Before You Start

Please familiarize yourself with:

- [README.md](../README.md) — Project overview
- [CRUCIBLE_WORKFLOW.md](../CRUCIBLE_WORKFLOW.md) — The 6-phase research methodology
- [READING_LIST.md](../READING_LIST.md) — Current book queue

## Ways to Contribute

### 1. Add a New Book

This is the most valuable contribution. Pick a book from the reading list (or suggest one) and research it.

**Steps:**

1. Fork the repository
2. Create a branch: `git checkout -b add-{book-title}`
3. Create the book folder using the naming convention:
   ```bash
   mkdir {book-title-slug}_{author-lastname}
   cp TEMPLATE/* {book-title-slug}_{author-lastname}/
   ```
4. Complete the research phases (at minimum Phase 0)
5. Submit a pull request

**Naming Convention:**

- Lowercase, hyphens for spaces: `thinking-in-systems_meadows`
- Use author's last name only
- Keep under 50 characters

### 2. Improve Existing Research

Found an error, outdated information, or have better analysis?

- **Corrections:** Fix factual errors, broken links, or typos
- **Enhancements:** Add better system dynamics models, more counter-evidence, or improved application tactics
- **Sources:** Add citations or verify existing claims

### 3. Contribute to Tooling

The `scripts/` directory contains Python utilities. Contributions welcome for:

- New automation scripts
- Improvements to metadata fetching
- Better validation tools

## Quality Standards

### Content Guidelines

Each research file should include:

- **Structured prose** — Not just bullet points. Write complete paragraphs.
- **Citations** — Link to sources. Avoid unsourced claims.
- **Concrete examples** — Show, don't just tell.
- **Mermaid diagrams** — Especially for Phase 1 (system dynamics).
- **Tables** — For comparisons and structured data.

### Avoid

- Excessive bullet points without explanation
- Generic summaries without specific insights
- Unsourced claims or speculation
- Jargon without context

### File Structure

Each book folder should contain:

```
{book-title}_{author}/
├── 00_vetting.md        # Phase 0: Credibility audit
├── 01_deconstruction.md # Phase 1: System dynamics model
├── 01a_translation.md   # Phase 1.5: Deep comprehension (Steel Man)
├── 02_red_teaming.md    # Phase 2: Adversarial analysis
├── 03_application.md    # Phase 3: Implementation tactics
├── 04_synthesis.md      # Phase 4: Knowledge integration
└── assets/              # Images, diagrams (optional)
```

> **Note:** Phase 1.5 uses `01a_` prefix for proper file sorting.

## Commit Messages

Use conventional commits:

- `feat: add thinking-in-systems_meadows research`
- `fix: correct citation in 99-bottles-of-oop_metz`
- `docs: update READING_LIST with new books`
- `chore: update metadata script dependencies`

## Pull Request Process

1. Ensure your branch is up to date with `main`
2. Run any linting/validation locally if possible
3. Fill out the PR template completely
4. Wait for CI checks to pass
5. Address any review feedback

## Code of Conduct

- Be respectful and constructive
- Focus on the work, not the person
- Welcome newcomers
- Assume good intent

## Questions?

- Open an issue for questions or suggestions
- Reach out on X: [@bigdegenenergyx](https://x.com/bigdegenenergyx)
- GitHub: [@bigdegenenergy](https://github.com/bigdegenenergy)
