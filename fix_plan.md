# Crucible Rebrand Plan

## Overview

This document outlines the complete plan to rebrand this repository from **Booksplode** to **Crucible**.

A crucible is a container in which substances are heated to high temperatures for purification—an apt metaphor for our methodology of rigorously testing and refining ideas from books.

---

## Current State Summary

| Metric | Count |
|--------|-------|
| Files with "booksplode" references | **52** |
| Unique occurrences | **~90** |
| Files requiring rename | **1** |
| Book folders with template text to update | **42** |

---

## Phase 1: Core Identity Files (High Priority)

These files define the project's identity and should be updated first.

### 1.1 Rename Workflow Documentation
- [ ] **Rename file**: `BOOKSPLODE_WORKFLOW.md` → `CRUCIBLE_WORKFLOW.md`
- [ ] **Update content inside**:
  - Line 1: `# Booksplode Workflow Configuration` → `# Crucible Workflow Configuration`
  - Line 11: Table row `| Framework | Booksplode |` → `| Framework | Crucible |`
  - Line 271: Replace "Booksplode" workflow description
  - Lines 285-287: Update repository structure paths from `booksplode/` to `crucible/`
  - Line 342: `A successful Booksplode research project` → `A successful Crucible research project`

### 1.2 Update Root README.md
- [ ] Line 1: `# Booksplode` → `# Crucible`
- [ ] Line 5: Update description paragraph
- [ ] Line 7: `## Why Booksplode?` → `## Why Crucible?`
- [ ] Line 9: Update explanation paragraph
- [ ] Line 28: Update link `[BOOKSPLODE_WORKFLOW.md](BOOKSPLODE_WORKFLOW.md)` → `[CRUCIBLE_WORKFLOW.md](CRUCIBLE_WORKFLOW.md)`
- [ ] Line 33: Update repo structure `booksplode/` → `crucible/`
- [ ] Line 42: Update `└── BOOKSPLODE_WORKFLOW.md` → `└── CRUCIBLE_WORKFLOW.md`

### 1.3 Update READING_LIST.md
- [ ] Line 3: `Books queued for Booksplode research` → `Books queued for Crucible research`
- [ ] Line 134: Update research status description
- [ ] Update workflow link to new filename

---

## Phase 2: GitHub Configuration (High Priority)

These files affect CI/CD and contributions.

### 2.1 Update .github/workflows/ci.yml
- [ ] Line 48: Update required files check from `"BOOKSPLODE_WORKFLOW.md"` → `"CRUCIBLE_WORKFLOW.md"`

### 2.2 Update .github/CONTRIBUTING.md
- [ ] Line 1: `# Contributing to Booksplode` → `# Contributing to Crucible`
- [ ] Line 9: Update workflow file reference to `CRUCIBLE_WORKFLOW.md`

### 2.3 Update .github/workflows/gemini-pr-review.yml
- [ ] Line 187: Update repository description from `Booksplode` to `Crucible`

---

## Phase 3: Scripts (Medium Priority)

### 3.1 Update scripts/openlibrary.py
- [ ] Line 20: Update USER_AGENT:
  ```python
  # FROM:
  USER_AGENT = "Booksplode/1.0 (https://github.com/bigdegenenergy/booksplode)"
  # TO:
  USER_AGENT = "Crucible/1.0 (https://github.com/bigdegenenergy/crucible)"
  ```

### 3.2 Update scripts/fetch_metadata.py
- [ ] Line 3: Update module docstring
- [ ] Line 205: Update regex pattern `r"\n## Booksplode Phases\n"` → `r"\n## Crucible Phases\n"`
- [ ] Line 208: Update comment

### 3.3 Update scripts/metadata_schema.json
- [ ] Line 3: `"title": "Booksplode Book Metadata"` → `"title": "Crucible Book Metadata"`

### 3.4 Update scripts/README.md
- [ ] Line 1: `# Booksplode Scripts` → `# Crucible Scripts`
- [ ] Line 3: Update description

---

## Phase 4: Book Folder READMEs (Medium Priority)

All 42 book folder READMEs follow a template with "Booksplode Phases" sections.

**Files to update (each requires the same change):**
| # | File |
|---|------|
| 1 | `99-bottles-oop_metz/README.md` |
| 2 | `advanced-react_makarevich/README.md` |
| 3 | `agile-manifesto_beck/README.md` |
| 4 | `beyond-vibe-coding_osmani/README.md` |
| 5 | `building-evolutionary-architectures_ford/README.md` |
| 6 | `clean-coder_martin/README.md` |
| 7 | `computer-systems-programmers-perspective_bryant/README.md` |
| 8 | `developers-playbook-llm-security_wilson/README.md` |
| 9 | `devops-handbook_kim/README.md` |
| 10 | `finite-infinite-games_carse/README.md` |
| 11 | `fundamentals-of-data-engineering_reis/README.md` |
| 12 | `generative-ai-design-patterns_tbd/README.md` |
| 13 | `good-news-factory_beck/README.md` |
| 14 | `grokking-concurrency_bobrov/README.md` |
| 15 | `hands-on-gpu-programming_tuomanen/README.md` |
| 16 | `high-performance-python_gorelick/README.md` |
| 17 | `hypermedia-systems_gross/README.md` |
| 18 | `in-the-plex_levy/README.md` |
| 19 | `just-for-fun_torvalds/README.md` |
| 20 | `looks-good-to-me_braganza/README.md` |
| 21 | `make-it-stick_brown/README.md` |
| 22 | `mastering-opentelemetry_flanders/README.md` |
| 23 | `models-of-the-mind_lindsay/README.md` |
| 24 | `philosophy-software-design_ousterhout/README.md` |
| 25 | `practical-deep-learning-cloud-mobile-edge_koul/README.md` |
| 26 | `practice-of-programming_kernighan/README.md` |
| 27 | `radical-candor_scott/README.md` |
| 28 | `recoding-america_pahlka/README.md` |
| 29 | `refactoring_fowler/README.md` |
| 30 | `rework_fried/README.md` |
| 31 | `slow-productivity_newport/README.md` |
| 32 | `software-engineers-guidebook_orosz/README.md` |
| 33 | `staff-engineer_larson/README.md` |
| 34 | `staff-engineers-path_reilly/README.md` |
| 35 | `system-design-interview_xu/README.md` |
| 36 | `tao-of-programming_james/README.md` |
| 37 | `team-topologies_skelton/README.md` |
| 38 | `thinking-in-systems_meadows/README.md` |
| 39 | `thinking-like-llm_sundararajan/README.md` |
| 40 | `tidy-first_beck/README.md` |
| 41 | `twelve-factor-app_wiggins/README.md` |
| 42 | `unicorn-project_kim/README.md` |
| 43 | `unix-history-memoir_kernighan/README.md` |
| 44 | `web-scalability_ejsmont/README.md` |
| 45 | `what-is-chatgpt-doing_wolfram/README.md` |
| 46 | `working-effectively-legacy-code_feathers/README.md` |
| 47 | `worse-is-better_gabriel/README.md` |

**Change required in each file:**
```markdown
# FROM:
## Booksplode Phases

This folder contains the 4-phase Booksplode analysis:

# TO:
## Crucible Phases

This folder contains the 4-phase Crucible analysis:
```

### 4.1 Update TEMPLATE/README.md
- [ ] Lines 29-31: Update template to use "Crucible Phases" for all future books

---

## Phase 5: Verification

After all changes:

- [ ] Run `grep -ri "booksplode" .` to verify no remaining references
- [ ] Run CI pipeline to ensure no broken links
- [ ] Verify all workflow file references are updated
- [ ] Test scripts still function correctly

---

## Execution Order

1. **Phase 1** - Core identity (must be done first, creates renamed workflow file)
2. **Phase 2** - GitHub config (depends on Phase 1 for new filename)
3. **Phase 3** - Scripts (independent but logical after core)
4. **Phase 4** - Book folders (bulk update, can be parallelized)
5. **Phase 5** - Verification (must be last)

---

## Notes

- The repository URL has already been updated to `crucible` in some places (README.md line 71 shows correct clone URL)
- No image/logo assets found that need updating
- LICENSE file contains copyright holder name (not product name), no changes needed
- CODE_OF_CONDUCT.md and SECURITY.md have no branding references

---

## Summary Statistics

| Category | File Count | Changes |
|----------|------------|---------|
| Core Identity | 3 | ~15 text changes + 1 file rename |
| GitHub Config | 3 | ~4 text changes |
| Scripts | 4 | ~6 text changes |
| Book Folders | 47 | ~94 text changes (2 per file) |
| **Total** | **57** | **~119 changes** |
