# Contributing to Plain English Summarization of Contracts

Thank you for your interest in contributing to this research dataset! This repository contains the dataset used in our NAACL NLLP Workshop paper on plain English summarization of legal contracts.

## About This Dataset

This is a research dataset consisting of 446 legal text and summary pairs from tldrlegal.com and tosdr.org. The dataset supports research in legal text summarization and natural language processing.

## Ways to Contribute

### Reporting Issues

If you find problems with the dataset, please open an issue with:

- **Data Quality Issues**: Incorrect text, parsing errors, or mismatched summaries
- **Documentation Issues**: Unclear descriptions or missing information
- **Format Issues**: JSON structure problems or encoding errors

When reporting issues, please include:
- The specific file (all_v1.json, tldrlegal_v1.json, or tosdr_annotated_v1.json)
- The UID of the affected entry
- A clear description of the problem
- Suggested correction (if applicable)

### Suggesting Enhancements

We welcome suggestions for:
- Additional metadata that would be useful for research
- Improved documentation or examples
- Tools or scripts for working with the dataset

### Data Corrections

If you identify errors in the dataset:

1. Fork the repository
2. Create a branch for your correction (`git checkout -b fix/data-correction`)
3. Make your changes to the appropriate JSON file
4. Ensure the JSON remains valid (use a JSON validator)
5. Submit a pull request with:
   - Clear description of the issue
   - Explanation of your correction
   - Reference to the original source if possible

### Code Contributions

If you develop tools, scripts, or analysis code that works with this dataset:

1. Consider sharing them in a separate repository
2. Link to your work by opening an issue or pull request to update the README
3. Ensure your code includes appropriate documentation and examples

## Dataset Guidelines

### Data Format

When making changes to the JSON files, maintain the existing structure:

**Required fields for all entries:**
- `uid`: Unique identifier
- `original_text`: The source legal text
- `reference_summary`: The plain English summary
- `doc`: Document name

**TL;DRLegal specific fields:**
- `title`: Title of the entry

**TOS;DR specific fields:**
- `note`: Additional notes
- `urls`: Company URL
- `case_text`, `case_code`: Case information and annotation
- `title_text`, `title_code`: Title information and annotation
- `tldr_text`, `tldr_code`: TL;DR information and annotation

### Annotation Codes

When working with TOS;DR annotations, understand the code format:
- Number prefix: Ranking of text quality (annotator's choice)
- `s`: Standard text appearing in multiple sets
- `j`: Jurisdiction-related text
- `q-`: Quote or excerpt from original text
- `d`: Description of original text content

### Quality Standards

Contributions should maintain:
- **Accuracy**: Text should match original sources
- **Completeness**: All required fields must be present
- **Consistency**: Follow existing formatting and structure
- **Validity**: JSON must be properly formatted

## Pull Request Process

1. **Fork and Branch**: Create a feature branch from master
2. **Make Changes**: Edit the appropriate files
3. **Validate**: Ensure JSON files are valid
4. **Document**: Clearly describe your changes in the PR description
5. **Reference**: Link to any related issues
6. **Wait for Review**: Maintainers will review and provide feedback

## Citation

If you use this dataset in your research, please cite:

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

## Questions?

If you have questions about contributing, please:
- Check existing issues to see if your question has been answered
- Open a new issue with the "question" label
- Refer to the README.md for dataset documentation

## Code of Conduct

Please be respectful and constructive in all interactions. This is an academic research project, and we value:
- Professional and courteous communication
- Constructive feedback
- Collaborative problem-solving
- Recognition of others' contributions

Thank you for helping improve this research dataset!
