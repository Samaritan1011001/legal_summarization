# Plain English Summarization of Contracts

[![ACL Anthology](https://img.shields.io/badge/ACL-W19--2201-blue)](https://www.aclweb.org/anthology/W19-2201)
[![License](https://img.shields.io/badge/license-CC%20BY%204.0-green)](https://creativecommons.org/licenses/by/4.0/)

## Overview

Legal contracts and terms-of-service agreements are notoriously difficult for ordinary users to read and understand. This dataset supports the task of **automatic plain-English summarization of contract clauses** -- given a passage of legal text, produce a short, human-readable summary of what it actually says.

The dataset was introduced in the paper [*Plain English Summarization of Contracts*](https://www.aclweb.org/anthology/W19-2201) (Manor & Li, NAACL NLLP Workshop 2019). It pairs original legal-text snippets with reference summaries drawn from two crowd-sourced annotation websites:

- **[TL;DRLegal](https://tldrlegal.com)** -- community summaries of open-source software licenses
- **[TOS;DR](https://tosdr.org/)** -- annotated clauses from terms-of-service agreements

Sets where the reference summary was longer than the original text are excluded from the quantitative analysis files included here.

---

## Dataset Statistics

| File | Sets | Source |
|---|---|---|
| `all_v1.json` | 446 | TL;DRLegal + TOS;DR combined |
| `tldrlegal_v1.json` | 85 | TL;DRLegal only |
| `tosdr_annotated_v1.json` | 361 | TOS;DR only |

Additional aggregate statistics (computed over `all_v1.json`):

| Metric | Value |
|---|---|
| Unique source documents | 59 |
| Average original text length | ~102 words |
| Average reference summary length | ~16 words |
| Original text range | 7 -- 1,077 words |
| Summary length range | 1 -- 80 words |

---

## Getting Started

The dataset files are standard JSON objects keyed by a unique identifier. Loading them requires only Python's built-in `json` module:

```python
import json

# Load the combined dataset
with open("all_v1.json") as f:
    data = json.load(f)

# Iterate over all examples
for uid, entry in data.items():
    original = entry["original_text"]
    summary  = entry["reference_summary"]
    document = entry["doc"]
    print(f"[{document}] {original[:80]}...")
    print(f"  Summary: {summary}")
    print()
```

To load a specific subset:

```python
# TL;DRLegal subset only
with open("tldrlegal_v1.json") as f:
    tldrlegal_data = json.load(f)

# TOS;DR subset only
with open("tosdr_annotated_v1.json") as f:
    tosdr_data = json.load(f)
```

---

## Files

| File | Description |
|---|---|
| `all_v1.json` | 446 sets from both TL;DRLegal and TOS;DR |
| `tldrlegal_v1.json` | 85 sets from [tldrlegal.com](https://tldrlegal.com) |
| `tosdr_annotated_v1.json` | 361 sets from [tosdr.org](https://tosdr.org/) |

---

## Data Format

Each JSON file is a dictionary whose keys are unique identifiers and whose values are objects describing one original-text/summary pair.

### Common Fields (all sets)

| Field | Description |
|---|---|
| `uid` | Unique identification string |
| `original_text` | Cleaned and parsed original legal text |
| `reference_summary` | Cleaned and parsed reference summary |
| `doc` | Name of the source document |

### TL;DRLegal-only Fields

| Field | Description |
|---|---|
| `title` | Title of the clause (from the website) |

### TOS;DR-only Fields

| Field | Description |
|---|---|
| `note` | Mostly empty; space for additional annotator notes |
| `urls` | URL of the respective company |
| `case_text` | Raw text from the "case" (from website) |
| `case_code` | Annotation code for the case text |
| `title_text` | Raw text from the "title" (from website) |
| `title_code` | Annotation code for the title text |
| `tldr_text` | Raw text from the "tldr" field (from website) |
| `tldr_code` | Annotation code for the tldr text |

### Annotation Codes (TOS;DR)

Each `*_code` field follows a structured format:

- The leading **number** is the annotator's quality ranking for that text.
- An optional **letter suffix** indicates additional properties:

| Letter | Meaning |
|---|---|
| `s` | **Standard** -- this exact text (without company names) appears in at least one other set |
| `j` | **Jurisdiction** -- the text deals with jurisdiction |
| `q-` | **Quote(-)** -- the text is an excerpt of the original |
| `d` | **Description** -- a description of the original text's topic, but may omit details |

---

## Citation

Please cite our [NAACL NLLP Workshop paper](https://www.aclweb.org/anthology/W19-2201):

```bibtex
@inproceedings{manor-li-2019-plain,
    title = "Plain {E}nglish Summarization of Contracts",
    author = "Manor, Laura  and
      Li, Junyi Jessy",
    booktitle = "Proceedings of the Natural Legal Language Processing Workshop 2019",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W19-2201",
    pages = "1--11",
}
```
