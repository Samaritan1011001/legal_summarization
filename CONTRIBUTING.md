# Contributing to Legal Summarization

Thank you for your interest in contributing to the Legal Summarization project! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature or bug fix
4. Make your changes
5. Test your changes thoroughly
6. Submit a pull request

## How to Use

This repository is a dataset of legal contract texts paired with their plain English summaries. There are no Python scripts to run -- the data is provided as JSON files that you can load and use in your own projects.

### Available Data Files

- `all_v1.json` -- 446 document-summary sets (the full combined dataset)
- `tldrlegal_v1.json` -- 84 document-summary sets sourced from TL;DRLegal
- `tosdr_annotated_v1.json` -- 84 document-summary sets sourced from TOS;DR

### Data Format

Each entry in the JSON files is keyed by a unique identifier and contains the following common fields:

- `uid` -- unique identifier for the entry
- `original_text` -- the full legal contract text
- `reference_summary` -- the plain English summary
- `doc` -- source document name

Source-specific files may include additional fields:

- TL;DRLegal (`tldrlegal_v1.json`): `title`, `id`
- TOS;DR (`tosdr_annotated_v1.json`): `note`, `urls`, `case_text`, `case_code`, `title_text`, `title_code`

### Example: Loading the Data

```python
import json

with open("all_v1.json", "r") as f:
    data = json.load(f)

for key, entry in data.items():
    print(f"UID: {entry['uid']}")
    print(f"Summary: {entry['reference_summary'][:200]}...")
    print()
```

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and modular

## Testing

Before submitting a pull request:

1. Test your changes locally
2. Ensure existing functionality is not broken
3. Add tests for new features when applicable

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Ensure your code follows the project's coding standards
3. Provide a clear description of the changes in your PR
4. Reference any related issues in your PR description

## Reporting Issues

When reporting issues, please include:

- A clear description of the problem
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment details (OS, Python version, etc.)

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Respect differing viewpoints and experiences

## Questions?

If you have questions about contributing, feel free to open an issue for discussion.

Thank you for contributing to Legal Summarization!
