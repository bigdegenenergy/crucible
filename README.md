# Crucible

**A systematic workflow for deep research on business and technical books.**

Crucible goes beyond simple book summaries. It's a forensic, adversarial approach to extracting real value from non-fiction—auditing author credibility, mapping causal systems, achieving deep comprehension, stress-testing arguments, translating concepts into actionable experiments, and integrating insights into your existing knowledge network.

## Why Crucible?

A crucible is a container in which substances are heated to high temperatures for purification and transformation. Most book "summaries" are useless—they regurgitate key points without questioning validity, testing failure modes, or building lasting understanding. Crucible treats every book as raw material to be refined, not gospel to be absorbed.

This system helps you:

- **Filter noise** by vetting author credibility and incentives before investing time
- **Extract signal** by mapping the underlying causal logic, not just the stories
- **Stress-test claims** by identifying logical fallacies and failure modes
- **Take action** by translating theory into context-specific, executable steps

## The 6-Phase Workflow

Each book goes through six distinct phases (including Phase 1.5), transforming information into integrated knowledge:

| Phase         | Name           | Purpose                                             | Output                 |
| :------------ | :------------- | :-------------------------------------------------- | :--------------------- |
| **Phase 0**   | The Gatekeeper | Forensic credibility audit of author and text       | `00_vetting.md`        |
| **Phase 1**   | The Architect  | Extract core logic into system dynamics model       | `01_deconstruction.md` |
| **Phase 1.5** | The Translator | Deep comprehension via Steel Manning                | `01a_translation.md`   |
| **Phase 2**   | The Skeptic    | Red team analysis and fallacy audit                 | `02_red_teaming.md`    |
| **Phase 3**   | The Pragmatist | Context-specific implementation with learning wager | `03_application.md`    |
| **Phase 4**   | The Weaver     | Synthesis and integration into mental model network | `04_synthesis.md`      |

For detailed prompts and methodology, see [CRUCIBLE_WORKFLOW.md](CRUCIBLE_WORKFLOW.md).

> **Note on Phase numbering:** Phase 1.5 uses the filename `01a_translation.md` for proper file sorting.

## Repository Structure

```
crucible/
├── TEMPLATE/                    # Template files for new books
├── {book-title}_{author}/       # Individual book research folders
│   ├── 00_vetting.md
│   ├── 01_deconstruction.md
│   ├── 01a_translation.md
│   ├── 02_red_teaming.md
│   ├── 03_application.md
│   └── 04_synthesis.md
├── scripts/                     # Automation utilities
├── READING_LIST.md              # Queue of 48+ books
└── CRUCIBLE_WORKFLOW.md         # Full methodology docs
```

### Folder Naming Convention

```
{book-title-slug}_{author-last-name}
```

Examples: `thinking-in-systems_meadows`, `staff-engineers-path_reilly`, `99-bottles-of-oop_metz`

## Reading List

Currently tracking **48 books and essays** across categories:

- **AI/ML Engineering** — GenAI Design Patterns, GPU Programming, LLM Security
- **Software Architecture** — Fundamentals of Software Architecture, A Philosophy of Software Design
- **Code Quality** — 99 Bottles of OOP, Refactoring, Working Effectively with Legacy Code
- **Career & Leadership** — Staff Engineer's Path, Radical Candor
- **DevOps** — The DevOps Handbook, Mastering OpenTelemetry
- **Systems Thinking** — Thinking in Systems, Finite and Infinite Games
- **Tech History** — In the Plex, Just for Fun, Unix: A History and a Memoir

Full list: [READING_LIST.md](READING_LIST.md)

## Quick Start

```bash
# Clone the repo
git clone https://github.com/bigdegenenergy/crucible.git
cd crucible

# Create a new book folder
BOOK="your-book-title"
AUTHOR="author-lastname"
mkdir -p "${BOOK}_${AUTHOR}"
cp TEMPLATE/* "${BOOK}_${AUTHOR}/"

# Start with Phase 0 (vetting)
```

## Scripts

The `scripts/` directory contains utilities for automation:

- **`openlibrary.py`** — Open Library API client for fetching book metadata, covers, and ISBNs
- **`fetch_metadata.py`** — CLI tool to enrich book folders with metadata

```bash
# Fetch metadata for a specific book
python scripts/fetch_metadata.py --book thinking-in-systems_meadows

# Fetch metadata for all books
python scripts/fetch_metadata.py --all
```

## Contributing

Contributions are welcome! Here's how you can help:

### Adding a New Book

1. Fork the repository
2. Create a new branch: `git checkout -b add-{book-name}`
3. Create the book folder using the naming convention
4. Copy template files and complete at least Phase 0 (vetting)
5. Submit a pull request

### Improving Existing Research

- Found an error or outdated info? Open an issue or PR
- Have a better system dynamics model? Submit it
- Discovered counter-evidence to a book's claims? Add it to the red teaming phase

### Quality Standards

- Use well-structured prose, not just bullet points
- Include sources and citations
- Add Mermaid.js diagrams for system models
- Provide concrete examples, not abstractions

## Contact

- **X (Twitter):** [@bigdegenenergyx](https://x.com/bigdegenenergyx)
- **GitHub:** [@bigdegenenergy](https://github.com/bigdegenenergy)
- **Issues:** [GitHub Issues](https://github.com/bigdegenenergy/crucible/issues)

Questions, feedback, or book suggestions? Reach out on X or open an issue.

## License

This project is open source. See [LICENSE](LICENSE) for details.

---

_"In a world of endless content, it's not enough to just read a book. You need to audit it, stress-test it, and apply it."_
