# Booksplode Workflow: Universal Book Research System

## Overview

**Booksplode** is a systematic workflow for conducting comprehensive research on business books and applying their principles to specific industries or use cases. The workflow produces a structured repository of insights, examples, critiques, and actionable applications.

## Folder Naming Convention

Each book gets its own folder using the following format:

```
{author-last-name}_{book-title-slug}
```

### Rules:
- **Author name**: Use last name only, lowercase, no spaces
- **Multiple authors**: Use first author's last name only
- **Book title**: Convert to lowercase, replace spaces with hyphens, remove special characters
- **Maximum length**: Keep under 50 characters total

### Examples:
- `heath_made-to-stick`
- `cialdini_influence`
- `kahneman_thinking-fast-and-slow`
- `sinek_start-with-why`
- `collins_good-to-great`

## Standard File Structure

Each book folder contains the following standardized files:

```
{author-last-name}_{book-title-slug}/
├── 01_authors_notes.md
├── 02_core_framework.md
├── 03_case_studies.md
├── 04_real_world_applications.md
├── 05_critiques_and_limitations.md
├── 06_industry_applications.md
├── 07_final_synthesis.md
└── assets/
    └── (images, diagrams, etc.)
```

### File Descriptions

| File | Purpose | Content |
|:-----|:--------|:--------|
| `01_authors_notes.md` | Author background and credibility | Biographical information, expertise, other works, why they're qualified to write this book |
| `02_core_framework.md` | The book's main ideas and framework | Central concepts, principles, models, frameworks presented in the book |
| `03_case_studies.md` | Examples from the book | Case studies, stories, and examples the authors use to illustrate their points |
| `04_real_world_applications.md` | How others have applied the ideas | Success stories, implementations, real-world uses of the book's principles |
| `05_critiques_and_limitations.md` | Critical analysis | Academic critiques, limitations, when the framework doesn't work, common misapplications |
| `06_industry_applications.md` | Specific industry focus | Deep dive into applying principles to target industry (e.g., mortgage, SaaS, healthcare) |
| `07_final_synthesis.md` | Comprehensive report | Executive summary, key takeaways, actionable recommendations, implementation roadmap |

## Research Workflow

### Phase 1: Author Research (30 minutes)
**Goal:** Establish credibility and context

**Tasks:**
- Research author background, credentials, expertise
- Find other books/articles by author
- Identify author's research methodology
- Note any biases or perspectives

**Sources:**
- Author's official website
- LinkedIn profiles
- Academic publications
- Interviews and talks

**Output:** `01_authors_notes.md`

---

### Phase 2: Core Framework Extraction (1 hour)
**Goal:** Understand the book's central ideas

**Tasks:**
- Identify the main framework or model
- Extract key principles and concepts
- Document the "big idea" of the book
- Create visual diagrams if applicable

**Sources:**
- Book introduction and conclusion
- Official book website
- Author's explanation of framework
- Summary articles

**Output:** `02_core_framework.md`

---

### Phase 3: Case Study Collection (1 hour)
**Goal:** Gather examples that illustrate the principles

**Tasks:**
- Document case studies from the book
- Note specific examples and stories
- Identify patterns in successful applications
- Extract quotable insights

**Sources:**
- Book chapters
- Book summaries
- Author's blog posts
- Supplementary materials

**Output:** `03_case_studies.md`

---

### Phase 4: Real-World Applications Research (1-2 hours)
**Goal:** Find how others have applied the ideas

**Tasks:**
- Search for companies using the framework
- Find marketing campaigns based on principles
- Identify success stories and metrics
- Document specific tactics and strategies

**Sources:**
- Marketing blogs and case studies
- Company websites and campaigns
- Reddit discussions
- YouTube implementations

**Output:** `04_real_world_applications.md`

---

### Phase 5: Critical Analysis (1 hour)
**Goal:** Understand limitations and critiques

**Tasks:**
- Search for academic critiques
- Identify when framework fails
- Document common misapplications
- Note oversimplifications or gaps

**Sources:**
- Academic papers
- Critical book reviews
- Reddit discussions
- Industry expert opinions

**Output:** `05_critiques_and_limitations.md`

---

### Phase 6: Industry-Specific Application (2 hours)
**Goal:** Apply principles to target industry

**Tasks:**
- Research industry-specific challenges
- Map book principles to industry pain points
- Develop concrete application strategies
- Create industry-specific examples

**Sources:**
- Industry research reports
- Trade publications
- Industry-specific case studies
- Competitor analysis

**Output:** `06_industry_applications.md`

---

### Phase 7: Synthesis and Recommendations (1-2 hours)
**Goal:** Create actionable final report

**Tasks:**
- Synthesize all research findings
- Create executive summary
- Develop implementation roadmap
- Provide specific recommendations
- Include tables, frameworks, and visuals

**Sources:**
- All previous research files
- Additional synthesis as needed

**Output:** `07_final_synthesis.md`

---

## Total Time Estimate

**Comprehensive Research:** 7-10 hours per book

**Quick Research:** 3-4 hours per book (skip phases 4-5)

## Quality Standards

### Each file should include:
- Clear section headings
- Well-structured paragraphs (not just bullet points)
- Tables for comparative information
- Inline citations with sources
- Blockquotes for key insights
- Concrete examples, not abstractions

### Avoid:
- Excessive bullet points
- Generic summaries without specifics
- Unsourced claims
- Jargon without explanation
- Abstract concepts without concrete examples

## Research Sources Checklist

For each book, consult:

- [ ] Official book website
- [ ] Author's website and blog
- [ ] Book introduction/conclusion
- [ ] 3+ detailed book summaries
- [ ] Author interviews (video/podcast)
- [ ] Academic papers citing the book
- [ ] Reddit discussions about the book
- [ ] Real-world application examples
- [ ] Critical reviews and critiques
- [ ] Industry-specific applications

## Output Formats

### Primary Format
All files use **Markdown (.md)** format for maximum portability and readability.

### Optional Exports
- PDF (for client delivery)
- Presentation slides (for workshops)
- One-page summary (for quick reference)

## Repository Structure

```
booksplode/
├── README.md (Overview of the Booksplode system)
├── WORKFLOW.md (This document)
├── TEMPLATE/ (Template files for new books)
│   ├── 01_authors_notes.md
│   ├── 02_core_framework.md
│   ├── 03_case_studies.md
│   ├── 04_real_world_applications.md
│   ├── 05_critiques_and_limitations.md
│   ├── 06_industry_applications.md
│   └── 07_final_synthesis.md
├── heath_made-to-stick/ (Example: First book)
│   ├── 01_authors_notes.md
│   ├── 02_core_framework.md
│   └── ...
└── [future books]/
```

## Usage Instructions

### Starting a New Book

1. **Create folder** using naming convention: `{author}_{book-slug}`
2. **Copy template files** from `TEMPLATE/` folder
3. **Follow workflow phases** 1-7 in order
4. **Commit after each phase** for version control
5. **Create final synthesis** when all research is complete

### Quick Start Command

```bash
# Create new book folder from template
AUTHOR="author-lastname"
BOOK="book-title-slug"
mkdir -p "$AUTHOR_$BOOK"
cp TEMPLATE/* "$AUTHOR_$BOOK/"
cd "$AUTHOR_$BOOK"
```

## Customization

The workflow can be customized based on:

- **Time available**: Skip phases 4-5 for quick research
- **Industry focus**: Spend more time on phase 6
- **Audience**: Adjust depth and technicality
- **Output format**: Create presentations, workshops, or consulting reports

## Success Metrics

A successful Booksplode research project should:

- ✅ Provide actionable insights, not just summaries
- ✅ Include specific examples with sources
- ✅ Address both strengths and limitations
- ✅ Offer industry-specific applications
- ✅ Be comprehensive yet readable
- ✅ Include visual aids (tables, diagrams)
- ✅ Cite all sources properly

## Future Enhancements

Potential additions to the workflow:

- [ ] Automated book summary extraction
- [ ] AI-powered case study discovery
- [ ] Industry application templates
- [ ] Presentation slide generation
- [ ] Workshop facilitation guides
- [ ] Implementation tracking tools
- [ ] Cross-book synthesis (comparing frameworks)
