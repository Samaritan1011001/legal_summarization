# Contributing to Legal Summarization

Thank you for your interest in contributing to the Legal Summarization project! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature or bug fix
4. Make your changes
5. Test your changes thoroughly
6. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.x
- Required dependencies (see requirements.txt)

### Installation

```bash
pip install -r requirements.txt
```

## Usage

This project is a dataset for legal text summarization research. The data is stored as JSON files that can be loaded directly in Python.

### Loading the Data

```python
import json

# Load the combined dataset (446 sets from both sources)
with open("all_v1.json", "r") as f:
    data = json.load(f)

# Or load a source-specific dataset
with open("tldrlegal_v1.json", "r") as f:
    tldrlegal_data = json.load(f)
```

### Accessing Fields

Each entry in the dataset contains the following core fields:

- `uid`: unique identification string
- `original_text`: cleaned and parsed original text
- `reference_summary`: cleaned and parsed reference summary
- `doc`: name of the source document

```python
for entry in data:
    print(entry["uid"])
    print(entry["original_text"][:200])   # first 200 chars of the original
    print(entry["reference_summary"])
    print()
```

Entries from TL;DRLegal may also include a `title` field. Entries from TOS;DR may include additional fields such as `case_text`, `case_code`, `title_text`, `title_code`, `tldr_text`, `tldr_code`, `urls`, and `note`. See the README for full details on these fields and their annotation codes.

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
