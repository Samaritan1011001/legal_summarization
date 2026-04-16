# Plain English Summarization of Contracts

A dataset for the paper "Plain English Summarization of Contracts," presented at the [NAACL NLLP Workshop 2019](https://www.aclweb.org/anthology/events/ws-2019/#w19-22). This dataset pairs original legal text from Terms of Service and software license agreements with plain-English reference summaries, supporting research in legal document summarization and simplification.

## Getting Started

The dataset is stored as JSON files and can be loaded with any JSON-compatible tool or library.

**Python example:**

```python
import json

with open("all_v1.json") as f:
    data = json.load(f)

# data is a dict keyed by unique IDs (e.g. "legalsum01")
for uid, entry in data.items():
    print(uid, entry["doc"])
    print("Original:", entry["original_text"][:100], "...")
    print("Summary:", entry["reference_summary"][:100], "...")
    break
```

**JavaScript (Node.js) example:**

```javascript
const fs = require("fs");

const data = JSON.parse(fs.readFileSync("all_v1.json", "utf8"));

// data is an object keyed by unique IDs (e.g. "legalsum01")
for (const [uid, entry] of Object.entries(data)) {
    console.log(uid, entry.doc);
    console.log("Original:", entry.original_text.slice(0, 100), "...");
    console.log("Summary:", entry.reference_summary.slice(0, 100), "...");
    break;
}
```

## Files

| File | Entries | Description |
|------|---------|-------------|
| `all_v1.json` | 446 | Combined sets from both websites |
| `tldrlegal_v1.json` | 84 | Sets from [TL;DRLegal](https://tldrlegal.com) |
| `tosdr_annotated_v1.json` | 84 | Sets from [TOS;DR](https://tosdr.org/) |

## Data Format

Each file is a JSON object mapping unique IDs to entry objects. Sets where the reference summary had more tokens than the original text are excluded, as described in the paper.

### Common Fields

All entries contain the following fields:

| Field | Description |
|-------|-------------|
| `uid` | Unique identification string (e.g. `legalsum01`) |
| `original_text` | Cleaned and parsed original legal text |
| `reference_summary` | Cleaned and parsed plain-English summary |
| `doc` | Name of the document the original text is from |

### TL;DRLegal-Specific Fields

Entries from TL;DRLegal may also include:

| Field | Description |
|-------|-------------|
| `title` | Title of the set (from the website) |

### TOS;DR-Specific Fields

Entries from TOS;DR may also include:

| Field | Description |
|-------|-------------|
| `note` | Additional notes from the annotator (mostly empty) |
| `urls` | URL of the respective company |
| `case_text` | Raw text from the "case" (from website) |
| `case_code` | Annotation code for "case" text |
| `title_text` | Raw text from the "title" (from website) |
| `title_code` | Annotation code for "title" text |
| `tldr_text` | Raw text from the "tldr" (from website) |
| `tldr_code` | Annotation code for "tldr" text |

### Annotation Codes

Each annotation code begins with a number representing the annotator's ranking of the text quality. A code may also include a letter suffix:

| Code | Meaning |
|------|---------|
| `s` | **Standard** -- this exact text (without company names) occurs at least one other time in a different set |
| `j` | **Jurisdiction** -- this text deals with jurisdiction |
| `q-` | **Quote** -- this text is an excerpt of the original text |
| `d` | **Description** -- this text describes what the original text talks about but may not give details |

## Citation

If you use this dataset, please cite:

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

## License

Please refer to the original data sources ([TL;DRLegal](https://tldrlegal.com), [TOS;DR](https://tosdr.org/)) for licensing information regarding the underlying legal texts and summaries.
