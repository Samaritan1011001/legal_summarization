# Plain English Summarization of Contracts

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-NAACL%20NLLP%202019-blue)](https://www.aclweb.org/anthology/W19-2201)

A research dataset for automatic summarization of legal contracts into plain English, enabling more accessible understanding of Terms of Service and legal agreements.

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Dataset Overview](#dataset-overview)
- [Data Structure](#data-structure)
  - [Common Fields](#common-fields)
  - [TL;DRLegal Specific Fields](#tldrlegal-specific-fields)
  - [TOS;DR Specific Fields](#tosdr-specific-fields)
- [Annotation Codes](#annotation-codes)
- [Citation](#citation)
- [License](#license)
- [References](#references)

---

## Overview

Legal documents such as Terms of Service (ToS) and End User License Agreements (EULAs) are often lengthy, complex, and difficult for non-experts to understand. This project provides a dataset for researching automatic summarization techniques that can convert legal jargon into plain, understandable English.

The dataset contains pairs of original legal text excerpts and their corresponding plain English summaries, sourced from community-driven legal simplification websites. This enables training and evaluation of text summarization models specifically tailored to the legal domain.

**Key Features:**
- Curated pairs of legal text and human-written summaries
- Data from two established legal simplification platforms
- Annotations for quality assessment and text categorization
- Suitable for supervised learning approaches to text summarization

---

## Getting Started

### Prerequisites

The dataset is provided in JSON format and can be loaded with any programming language that supports JSON parsing.

### Quick Start (Python)

```python
import json

# Load the complete dataset
with open('all_v1.json', 'r') as f:
    data = json.load(f)

# Access a specific entry
entry = data['legalsum01']
print(f"Document: {entry['doc']}")
print(f"Original: {entry['original_text']}")
print(f"Summary: {entry['reference_summary']}")
```

---

## Dataset Overview

This dataset consists of data included in the quantitative analysis as described in the paper. Sets where the reference summary has more tokens than the original text are excluded.

| File | Description | Number of Sets | Source |
|------|-------------|----------------|--------|
| `all_v1.json` | Combined dataset from both sources | 446 | [TL;DRLegal](https://tldrlegal.com) + [TOS;DR](https://tosdr.org/) |
| `tldrlegal_v1.json` | Software license summaries | 84 | [TL;DRLegal](https://tldrlegal.com) |
| `tosdr_annotated_v1.json` | Terms of Service summaries with annotations | 84 | [TOS;DR](https://tosdr.org/) |

---

## Data Structure

Each entry in the dataset is a JSON object containing the following fields:

### Common Fields

All entries contain these core fields:

| Field | Type | Description |
|-------|------|-------------|
| `uid` | string | Unique identification string for the entry |
| `original_text` | string | Cleaned and parsed original legal text |
| `reference_summary` | string | Cleaned and parsed plain English summary |
| `doc` | string | Name of the source document |

### TL;DRLegal Specific Fields

Entries from TL;DRLegal may include:

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | Title of the set (from the website) |

### TOS;DR Specific Fields

Entries from TOS;DR may include additional fields:

| Field | Type | Description |
|-------|------|-------------|
| `note` | string | Additional notes from the annotator (often empty) |
| `urls` | string | URL of the respective company |
| `case_text` | string | Raw text from the "case" field on the website |
| `case_code` | string | Annotation code for the case text |
| `title_text` | string | Raw text from the "title" field on the website |
| `title_code` | string | Annotation code for the title text |
| `tldr_text` | string | Raw text from the "tldr" field on the website |
| `tldr_code` | string | Annotation code for the tldr text |

---

## Annotation Codes

The TOS;DR entries include annotation codes that provide quality assessments and categorizations of the text. Each code follows a specific format:

### Code Format

```
[number][optional letter]
```

### Numeric Rankings

The number at the beginning of each code represents the annotator's quality ranking of the respective text.

### Letter Codes

| Code | Name | Description |
|------|------|-------------|
| `s` | Standard | This exact text (without company names) occurs at least one other time in a different set |
| `j` | Jurisdiction | This text deals with jurisdiction-related content |
| `q-` | Quote | This text is an excerpt or quotation from the original text |
| `d` | Description | This text describes what the original text discusses but may not provide specific details |

### Example

A code like `2s` would indicate:
- Quality ranking of 2
- The text is standard (appears in multiple sets)

---

## Citation

If you use this dataset in your research, please cite our [NAACL NLLP Workshop paper](https://www.aclweb.org/anthology/W19-2201):

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

---

## License

This project is licensed under the MIT License. See the dataset sources for their respective terms of use.

---

## References

- **Paper**: [Plain English Summarization of Contracts](https://www.aclweb.org/anthology/W19-2201) - NAACL NLLP Workshop 2019
- **TL;DRLegal**: [https://tldrlegal.com](https://tldrlegal.com) - Software license summaries in plain English
- **TOS;DR**: [https://tosdr.org](https://tosdr.org) - Terms of Service; Didn't Read - Rating and summarizing Terms of Service
- **ACL Anthology**: [NAACL NLLP Workshop 2019 Proceedings](https://www.aclweb.org/anthology/events/ws-2019/#w19-22)
