# Contributing to Plain English Summarization of Contracts

Thank you for your interest in contributing to this legal text summarization dataset. This document provides guidelines for reporting issues, submitting new data, and contributing code.

## Reporting Issues

If you find a problem with the dataset or code, please open a GitHub issue and include:

1. A clear, descriptive title.
2. Steps to reproduce the problem (if applicable).
3. The expected behavior and what actually happened.
4. The dataset file(s) involved (e.g., `all_v1.json`, `tldrlegal_v1.json`, `tosdr_annotated_v1.json`).
5. Your Python version and operating system.

For data quality issues (incorrect summaries, encoding errors, duplicate entries), include the `uid` of the affected entry.

## Submitting New Data Entries

New data contributions are welcome. To add entries:

1. Fork the repository and create a feature branch.
2. Add your entries to the appropriate JSON file, or propose a new file if the source is different from the existing ones.
3. Ensure every entry conforms to the data format requirements below.
4. Open a pull request with a description of the data source and how the entries were collected.

## Data Format Requirements

Each dataset file is a JSON dictionary keyed by entry identifiers. Every entry must include the following required fields:

| Field               | Type   | Description                                      |
|---------------------|--------|--------------------------------------------------|
| `uid`               | string | Unique identifier for the entry.                 |
| `original_text`     | string | The cleaned and parsed original legal text.      |
| `reference_summary` | string | The cleaned and parsed reference summary.        |
| `doc`               | string | Name of the document the original text is from.  |

Depending on the data source, entries may also include optional fields such as `title`, `note`, `urls`, `case_code`, `case_text`, `title_code`, `title_text`, `tldr_code`, and `tldr_text`. See the `DatasetEntry` TypedDict in `load_data.py` for the full schema.

Additional data format rules:

- The `uid` must be unique across the entire dataset file.
- The `reference_summary` should not have more tokens than the `original_text` (see the paper for details on this exclusion criterion).
- Text fields should be cleaned and parsed (no raw HTML or markup).
- JSON files must be valid and UTF-8 encoded.

## Code Style

All Python code in this repository must follow these conventions:

- **Type hints**: All function signatures must include type annotations for parameters and return values.
- **Docstrings**: All public modules, classes, and functions must have docstrings. Follow the Google style for docstring formatting (see `load_data.py` for examples).
- **Imports**: Use `from __future__ import annotations` for modern annotation syntax.
- **Formatting**: Keep code readable and consistent with the existing style in the repository.

## Pull Request Process

1. Fork the repository and create a branch from `master` for your changes.
2. Make your changes, ensuring they follow the guidelines above.
3. Test your changes locally:
   - Verify that `load_data.py` can load any modified or new JSON files without errors.
   - Run a quick sanity check: `python load_data.py`
4. Commit with a clear, descriptive message.
5. Open a pull request against `master` and include:
   - A summary of what was changed and why.
   - References to any related issues.
6. A maintainer will review your pull request. Please be responsive to feedback and make requested changes promptly.
