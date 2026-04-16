# Plain English Summarization of Contracts


Please cite our [NAACL NLLP Workshop paper](https://www.aclweb.org/anthology/events/ws-2019/#w19-22) as:

```
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

## Files
* all_v1.json: 446 sets from both websites
* tldrlegal_v1.json: 84 sets from [https://tldrlegal.com](https://tldrlegal.com)
* tosdr_annotated_v1.json: 84 sets from [https://tosdr.org/](https://tosdr.org/)

## Data
This dataset consists of the data included in the quantitative analysis as described in the paper. Sets which had a reference summary with more tokens than the original text are excluded.
Each set consists of: 
* uid: unique identification string
* original_text: cleaned & parsed original text
* reference_summary: cleaned & parsed reference summary
* doc: name of the document which the original text is from
### TL;DRLegal
Each tldrlegal set may also have: 
* title: "title" of the set (from website)
### TOS;DR
Each tos;dr set may also have:
* note: Mostly empty, a space for additional notes from the annotator
* urls: URL of the respective company
* case_text: raw text from the "case" (from website)
* case_code: annotation for "case" text 
* title_text: raw text from the "title" (from website)
* title_code: annotation for "title" text 
* tldr_text: raw text from the "tldr" (from website)
* tldr_code: annotation for "tldr" 

A note on annotation: 
* Each code begins with a number, which is the 'ranking' of the quality of the respective text as chosen by the annotator
* A code may also have a letter, which stands for:
  * s: standard -- this exact text (without company names) occurs at least one other time in a different set. 
  * j: jurisdication -- this text deals with jurisdiction
  * q-: quote(-) -- this text is excerpt of the original text
  * d: description -- this text is a description of what the original text talks about, but may not give details

## Getting Started

### Prerequisites

- Python 3.6 or later (no external packages required for basic usage)
- Git

### Clone the Repository

```bash
git clone https://github.com/<your-username>/legal_summarization.git
cd legal_summarization
```

### Loading the Data

Each JSON file is a dictionary keyed by a unique ID (`uid`). You can load and explore the data using Node.js's built-in `fs` module:

```js
const fs = require("fs");

// Load the full dataset (446 sets from both websites)
const raw = fs.readFileSync("all_v1.json", "utf-8");
const data = JSON.parse(raw);

console.log(`Total sets: ${Object.keys(data).length}`);

// Inspect a single entry
const [uid, entry] = Object.entries(data)[0];
console.log(`UID: ${uid}`);
console.log(`Document: ${entry["doc"]}`);
console.log(`Original text: ${entry["original_text"].slice(0, 200)}...`);
console.log(`Reference summary: ${entry["reference_summary"]}`);
```

You can also load the source-specific files:

```python
# TL;DRLegal subset (84 sets)
with open("tldrlegal_v1.json", "r") as f:
    tldrlegal = json.load(f)

# TOS;DR annotated subset (84 sets)
with open("tosdr_annotated_v1.json", "r") as f:
    tosdr = json.load(f)
```

### Example: Basic Dataset Exploration

```python
import json

with open("all_v1.json", "r") as f:
    data = json.load(f)

# List all unique documents in the dataset
documents = set(entry["doc"] for entry in data.values())
print(f"Unique documents: {len(documents)}")
for doc in sorted(documents)[:10]:
    print(f"  - {doc}")

# Compute average lengths of original texts and summaries
avg_orig = sum(len(e["original_text"].split()) for e in data.values()) / len(data)
avg_summ = sum(len(e["reference_summary"].split()) for e in data.values()) / len(data)
print(f"\nAvg original text length: {avg_orig:.1f} words")
print(f"Avg summary length: {avg_summ:.1f} words")
```

## Rebuilding / Reproducing

This repository is a dataset release for the paper *Plain English Summarization of Contracts* (NAACL NLLP Workshop 2019). There is no build system or trained model included. To reproduce the paper's results:

1. Load the dataset using the Python snippets above.
2. Preprocess the text as described in the paper (tokenization, lowercasing, etc.).
3. Train or evaluate a summarization model of your choice on the data. The paper uses extractive and abstractive baselines; refer to Section 4 of the paper for details.
4. Evaluate using ROUGE or other metrics as described in the paper.

A minimal reproduction setup might look like:

```bash
# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install common NLP/summarization dependencies
pip install rouge-score nltk

# Run your evaluation or training script
python your_experiment.py
```

Since this repository contains only the dataset, any model code or evaluation scripts should be implemented separately following the methodology in the paper.
