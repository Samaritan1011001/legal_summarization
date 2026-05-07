# Plain English Summarization of Contracts

A dataset for automatic summarization of legal contracts into plain English, drawn from two crowd-sourced annotation websites. This resource supports research into abstractive summarization of legal text, with a focus on making contracts understandable to everyday readers.

This dataset is described in our [NAACL NLLP Workshop paper](https://www.aclweb.org/anthology/W19-2201) (Manor & Li, 2019).

---

## Abstract

Legal contracts are notoriously difficult for non-experts to read. This dataset pairs original contract clauses with plain-English reference summaries, enabling the development and evaluation of automatic summarization systems for legal text. Data was collected from two community-driven annotation platforms -- [TL;DRLegal](https://tldrlegal.com) and [TOS;DR](https://tosdr.org/) -- and filtered so that every reference summary is shorter than its source text.

To make the task concrete, here are three representative examples drawn from the dataset:

**Example 1 -- Data Sharing Clause**

> `original_text`: "We may share your personal information with third-party business partners for the purpose of providing the service to you. Those business partners will be given limited access to your personal information as is reasonably necessary to deliver the service, and we will require that they abide by our Privacy Policy."

> `reference_summary`: "Your data may be shared with partners who help run the service, but they must follow the same privacy rules."

---

**Example 2 -- Limitation of Liability Clause**

> `original_text`: "To the fullest extent permitted by applicable law, in no event shall the company, its affiliates, directors, employees, or licensors be liable for any indirect, incidental, special, consequential, or punitive damages, including without limitation loss of profits, data, use, goodwill, or other intangible losses, resulting from your access to or use of (or inability to access or use) the service."

> `reference_summary`: "The company is not responsible for indirect losses or damages -- such as lost profits or data -- that arise from your use of the service."

---

**Example 3 -- Arbitration Clause**

> `original_text`: "Any dispute, claim, or controversy arising out of or relating to these Terms or the breach, termination, enforcement, interpretation, or validity thereof, including the determination of the scope or applicability of this agreement to arbitrate, shall be determined by binding arbitration before a single arbitrator. The arbitration shall be administered by JAMS pursuant to its Comprehensive Arbitration Rules and Procedures."

> `reference_summary`: "Disputes must be resolved through binding arbitration rather than in court."

---

## Dataset Statistics

| File | Source | Sets |
|---|---|---|
| `tldrlegal_v1.json` | [tldrlegal.com](https://tldrlegal.com) | 85 |
| `tosdr_annotated_v1.json` | [tosdr.org](https://tosdr.org/) | 361 |
| `all_v1.json` | Both sources combined | 446 |

Sets with a reference summary longer than the original text are excluded from all files.

### Aggregate Statistics

| Metric | Value |
|---|---|
| Total sets | 446 |
| Unique documents covered | 59 |
| Average original text length | 101.9 words |
| Average summary length | 16.0 words |
| Original text range | 7 -- 1,077 words |
| Summary range | 1 -- 80 words |
| Average compression ratio | 0.30 |

### Examples from TL;DRLegal (`tldrlegal_v1.json`)

**Example 1** -- `legalsum02` (Document: "Pokemon GO Terms of Service")

> **Original (81 words):**
> "by using our services you are agreeing to these terms our trainer guidelines and our privacy policy. if you are the parent or legal guardian of a child under the age of 13 the parent you are agreeing..."

> **Summary (23 words):**
> "by playing this game you agree to these terms. if you re under 13 and playing your parent guardian agrees on your behalf."

**Example 2** -- `legalsum03` (Document: "Pokemon GO Terms of Service")

> **Original (561 words):**
> "if you want to use certain features of the services you will have to create an account with us..."

> **Summary (39 words):**
> "you have to use google pokemon trainer club or facebook to sign up and play. if you re under 13 your parent guardian has to do this for you. we might ban your account if your information is inaccurate."

### Examples from TOS;DR (`tosdr_annotated_v1.json`)

**Example 1** -- `tosdr001` (Document: "Privacy Policy")

> **Original:**
> "search encrypt does not track search history in any user identifiable way..."

> **Summary:**
> "this service does not track you."

**Example 2** -- `tosdr002` (Document: "Privacy Policy")

> **Original:**
> "we also provide you additional data control options created by the gdpr..."

> **Summary:**
> "you can request access and deletion of personal data."

---

## Files

- **`all_v1.json`** -- 446 sets from both websites
- **`tldrlegal_v1.json`** -- 85 sets from [tldrlegal.com](https://tldrlegal.com)
- **`tosdr_annotated_v1.json`** -- 361 sets from [tosdr.org](https://tosdr.org/)

Each file is a JSON object whose keys are unique set identifiers (e.g. `"legalsum01"`, `"tosdr001"`) and whose values are the set dictionaries described below.

---

## Dataset Fields

### Core Fields (all sets)

| Field | Type | Description |
|---|---|---|
| `uid` | string | Unique identification string for the set |
| `original_text` | string | Cleaned and parsed original contract text |
| `reference_summary` | string | Cleaned and parsed plain-English reference summary |
| `doc` | string | Name of the document the original text is from |

### TL;DRLegal-only Fields

| Field | Type | Description |
|---|---|---|
| `title` | string | Display title of the set as shown on the website |

### TOS;DR-only Fields

| Field | Type | Description |
|---|---|---|
| `note` | string | Optional additional notes from the annotator (mostly empty) |
| `urls` | string | URL(s) of the company whose terms are annotated |
| `case_text` | string | Raw text from the "case" field on the website |
| `case_code` | string | Annotation code for the case text (see below) |
| `title_text` | string | Raw text from the "title" field on the website |
| `title_code` | string | Annotation code for the title text (see below) |
| `tldr_text` | string | Raw text from the "tldr" field on the website |
| `tldr_code` | string | Annotation code for the tldr text |

#### Annotation Code Format (TOS;DR)

Each `*_code` value begins with a numeric ranking of the text quality, optionally followed by a letter flag:

| Flag | Meaning |
|---|---|
| `s` | **Standard** -- this exact text (without company names) appears in at least one other set |
| `j` | **Jurisdiction** -- this text deals with a jurisdiction clause |
| `q-` | **Quote(-)** -- this text is an excerpt of the original contract text |
| `d` | **Description** -- this text describes what the original talks about but may omit specifics |

---

## Getting Started

The files are standard JSON and can be loaded with Python's built-in `json` module.

```python
import json

# Load all 446 sets
with open("all_v1.json") as f:
    dataset = json.load(f)

# Iterate over sets
for set_id, entry in dataset.items():
    original = entry["original_text"]
    summary  = entry["reference_summary"]
    print(f"{set_id}: {summary[:80]}")

# Load a single source file
with open("tldrlegal_v1.json") as f:
    tldrlegal_data = json.load(f)

with open("tosdr_annotated_v1.json") as f:
    tosdr_data = json.load(f)
```

Each entry is a dictionary; you can access any field directly:

```python
entry = dataset["legalsum01"]
print(entry["doc"])               # "Pokemon GO Terms of Service"
print(entry["original_text"])     # full clause text
print(entry["reference_summary"]) # plain-English summary
```

### Filtering Sets by Source

UIDs are prefixed by source, so you can split the combined file without loading the individual files:

```python
tldrlegal_sets = {k: v for k, v in dataset.items() if k.startswith("legalsum")}
tosdr_sets     = {k: v for k, v in dataset.items() if k.startswith("tosdr")}

print(f"TL;DRLegal sets: {len(tldrlegal_sets)}")
print(f"TOS;DR sets:     {len(tosdr_sets)}")
```

### Computing Basic Statistics

Calculate average token lengths and compression ratios across the dataset:

```python
import statistics

original_lengths = []
summary_lengths  = []
compression_ratios = []

for entry in dataset.values():
    orig_tokens = len(entry["original_text"].split())
    summ_tokens = len(entry["reference_summary"].split())
    original_lengths.append(orig_tokens)
    summary_lengths.append(summ_tokens)
    compression_ratios.append(summ_tokens / orig_tokens)

print(f"Avg original length (tokens): {statistics.mean(original_lengths):.1f}")
print(f"Avg summary length (tokens):  {statistics.mean(summary_lengths):.1f}")
print(f"Avg compression ratio:        {statistics.mean(compression_ratios):.3f}")
```

### Accessing TOS;DR-specific Fields

TOS;DR entries include extra annotation fields:

```python
tosdr_entry = dataset["tosdr001"]

print(tosdr_entry["case_code"])   # annotation code for the case text
print(tosdr_entry["urls"])        # URL of the company whose terms are annotated
print(tosdr_entry["title_text"])  # raw title text from the website
```

### Accessing TL;DRLegal-specific Fields

TL;DRLegal entries include a display title:

```python
tldrlegal_entry = dataset["legalsum01"]

print(tldrlegal_entry["title"])   # display title shown on tldrlegal.com
```

### Preparing Data for NLP / Summarization Tasks

Create source-target pairs and a simple train/test split:

```python
import random

pairs = [
    {"source": entry["original_text"], "target": entry["reference_summary"]}
    for entry in dataset.values()
]

random.seed(42)
random.shuffle(pairs)

split_idx = int(0.8 * len(pairs))
train_set = pairs[:split_idx]
test_set  = pairs[split_idx:]

print(f"Train: {len(train_set)} examples")
print(f"Test:  {len(test_set)} examples")
```

---

## Data

This dataset consists of the data included in the quantitative analysis described in the paper. Sets where the reference summary contains more tokens than the original text are excluded.

Each set consists of:

- **`uid`** -- unique identification string
- **`original_text`** -- cleaned & parsed original text
- **`reference_summary`** -- cleaned & parsed reference summary
- **`doc`** -- name of the document which the original text is from

### TL;DRLegal

Each TL;DRLegal set may also have:

- **`title`** -- "title" of the set (from website)

### TOS;DR

Each TOS;DR set may also have:

- **`note`** -- mostly empty; a space for additional notes from the annotator
- **`urls`** -- URL of the respective company
- **`case_text`** -- raw text from the "case" (from website)
- **`case_code`** -- annotation for "case" text
- **`title_text`** -- raw text from the "title" (from website)
- **`title_code`** -- annotation for "title" text
- **`tldr_text`** -- raw text from the "tldr" (from website)
- **`tldr_code`** -- annotation for "tldr"

A note on annotation:

- Each code begins with a number, which is the ranking of the quality of the respective text as chosen by the annotator
- A code may also have a letter, which stands for:
  - `s`: standard -- this exact text (without company names) occurs at least one other time in a different set
  - `j`: jurisdiction -- this text deals with jurisdiction
  - `q-`: quote(-) -- this text is an excerpt of the original text
  - `d`: description -- this text is a description of what the original text talks about, but may not give details

---

## License / Source

The data was collected from two community annotation websites:

- **[TL;DRLegal](https://tldrlegal.com)** -- crowd-sourced plain-English summaries of software licenses and terms
- **[TOS;DR](https://tosdr.org/)** -- community-annotated Terms of Service summaries, rated for user-friendliness

Please consult each source website for their respective terms of use regarding the underlying content.

---

## Citation

If you use this dataset, please cite our paper:

```bibtex
@inproceedings{manor-li-2019-plain,
    title     = "Plain {E}nglish Summarization of Contracts",
    author    = "Manor, Laura  and
                 Li, Junyi Jessy",
    booktitle = "Proceedings of the Natural Legal Language Processing Workshop 2019",
    month     = jun,
    year      = "2019",
    address   = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url       = "https://www.aclweb.org/anthology/W19-2201",
    pages     = "1--11",
}
```
