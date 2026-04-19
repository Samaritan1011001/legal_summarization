# Contributing to Legal Summarization

Thank you for your interest in contributing to the Legal Summarization project! This document provides guidelines and instructions for contributing.

## Table of Contents

- [How To](#how-to)
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)
- [Style Guidelines](#style-guidelines)

## How To

This section provides quick guides for common contribution tasks.

### How to Report a Bug

1. Check if the bug has already been reported in [Issues](https://github.com/Samaritan1011001/legal_summarization/issues)
2. If not, create a new issue with the "bug" label
3. Include a clear title and detailed description
4. Add steps to reproduce, expected vs actual behavior
5. Include your environment details (OS, Python version, etc.)

### How to Suggest a Feature

1. Check existing issues to see if it's already suggested
2. Create a new issue with the "enhancement" label
3. Describe the feature and its benefits
4. Provide use cases and examples if possible

### How to Submit a Pull Request

1. Fork the repository and create a new branch
2. Make your changes following the style guidelines
3. Test your changes thoroughly
4. Commit with clear, descriptive messages
5. Push to your fork and submit a pull request
6. Wait for review and address any feedback

### How to Add a Dataset

1. Ensure the data is legally shareable and properly anonymized
2. Format the data according to the JSON structure (see Style Guidelines)
3. Add documentation describing the dataset
4. Include proper citations and sources
5. Submit a pull request with your dataset

### How to Improve Documentation

1. Identify areas that need clarification or updates
2. Make your changes in a new branch
3. Ensure the documentation is clear and accurate
4. Submit a pull request with your improvements

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/legal_summarization.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`

## How to Contribute

### Types of Contributions

- **Bug fixes**: Fix issues in existing code
- **New features**: Add new functionality
- **Documentation**: Improve or add documentation
- **Data contributions**: Add new legal document datasets
- **Model improvements**: Enhance summarization models

### Dataset Contributions

This project contains legal document datasets. When contributing data:

- Ensure all data is properly anonymized
- Verify that data can be legally shared
- Include proper citations and sources
- Follow the existing JSON format structure
- Add documentation for new datasets

## Development Setup

### Prerequisites

- Python 3.7+
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Samaritan1011001/legal_summarization.git
cd legal_summarization

# Install dependencies (if applicable)
pip install -r requirements.txt  # if requirements.txt exists
```

## Submitting Changes

### Pull Request Process

1. **Update your fork**
   ```bash
   git fetch upstream
   git merge upstream/master
   ```

2. **Make your changes**
   - Write clear, concise commit messages
   - Follow the existing code style
   - Add tests if applicable

3. **Test your changes**
   - Ensure all existing tests pass
   - Add new tests for new features

4. **Submit a pull request**
   - Provide a clear description of the changes
   - Reference any related issues
   - Ensure CI checks pass

### Commit Message Guidelines

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests when relevant

Example:
```
Add support for new legal document format

- Implement parser for format X
- Add tests for new parser
- Update documentation

Fixes #123
```

## Reporting Issues

### Bug Reports

When reporting bugs, please include:

- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, etc.)
- Any relevant logs or error messages

### Feature Requests

When requesting features:

- Provide a clear description of the feature
- Explain the use case and benefits
- Include examples if possible

## Style Guidelines

### Python Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise

### Documentation Style

- Use clear, concise language
- Include code examples where helpful
- Keep documentation up to date with code changes

### JSON Data Format

When contributing datasets, follow the existing structure:

```json
{
  "id": "unique_identifier",
  "text": "legal document text",
  "summary": "document summary",
  "metadata": {
    "source": "source information",
    "date": "YYYY-MM-DD"
  }
}
```

## Questions?

If you have questions about contributing, please:

- Check existing issues and pull requests
- Review the project documentation
- Open a new issue with the "question" label

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project.

## Acknowledgments

Thank you to all contributors who help improve this project!

---

**Note**: This is a research project. Please ensure all contributions maintain academic integrity and proper attribution of sources.
