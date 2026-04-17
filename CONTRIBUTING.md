# Contributing to Plain English Summarization of Contracts

Thank you for your interest in contributing to this research dataset! This repository contains legal text summarization data from tldrlegal.com and tosdr.org, used in our NAACL NLLP Workshop 2019 paper.

## Table of Contents

- [How to Report Issues](#how-to-report-issues)
- [Suggesting Improvements](#suggesting-improvements)
- [Contributing New Data](#contributing-new-data)
- [Data Format Guidelines](#data-format-guidelines)
- [Citation Requirements](#citation-requirements)
- [Code of Conduct](#code-of-conduct)
- [Contact](#contact)

## How to Report Issues

If you discover any issues with the dataset, please help us improve it by reporting:

### Data Quality Issues

When reviewing the dataset for quality problems, here are specific things to look for across the three JSON files (`all_v1.json`, `tldrlegal_v1.json`, `tosdr_annotated_v1.json`):

**Text content problems**
- Corrupted or garbled text in `original_text` or `reference_summary` fields (e.g., leftover HTML entities, broken Unicode characters like malformed accented letters)
- Incomplete text cleaning: residual HTML tags, stray markup, or unnormalized whitespace (extra spaces, tabs, or newlines) in parsed legal text
- Encoding issues with special characters, particularly in legal terms or company names (e.g., "Pok\u00e9mon" should render correctly, not appear as escaped sequences or replacement characters)

**Field-level issues**
- Missing or empty required fields: every entry must have `uid`, `original_text`, `reference_summary`, and `doc`
- Entries where `reference_summary` has more tokens than `original_text` -- these should have been excluded during data preparation
- Duplicate `uid` values within or across files
- Empty `title` fields in `tldrlegal_v1.json` entries where a section title clearly exists in the source

**TOS;DR-specific issues** (in `tosdr_annotated_v1.json`)
- Invalid or malformed annotation codes in `case_code`, `title_code`, or `tldr_code` fields -- valid codes have a number prefix (1, 2, or 3) optionally followed by a comma and letter suffix (`s`, `j`, `q-`, or `d`), e.g., `"1,s"`, `"2,q-"`, `"3"`
- Mismatches between annotation code quality rankings and the actual text quality (e.g., a `1`-ranked text that is clearly low quality)
- Broken or outdated URLs in the `urls` field
- Missing `tldr_text` or `tldr_code` fields in entries that should have TL;DR annotations

**Cross-file consistency**
- Entries present in `tldrlegal_v1.json` or `tosdr_annotated_v1.json` but missing from `all_v1.json`
- Inconsistent `doc` names for entries that reference the same source document across files
- Field mismatches where the same `uid` appears in multiple files with different `original_text` or `reference_summary` content

### Documentation Issues
- Unclear or incorrect documentation
- Missing information about data structure
- Errors in the README or other documentation

**To report an issue:**
1. Check existing issues to avoid duplicates
2. Open a new issue on GitHub with a clear, descriptive title
3. Include:
   - The specific file(s) affected (e.g., `tldrlegal_v1.json`)
   - The `uid` of the problematic entry if applicable
   - A clear description of the problem
   - Expected vs. actual behavior or content
   - Any relevant screenshots or code snippets

## Suggesting Improvements

We welcome suggestions for improving this dataset! You can suggest:

- Additional data sources for legal text summarization
- Improvements to data cleaning or parsing methods
- Enhanced annotation schemes
- Additional metadata fields that would be valuable for research
- Tools or scripts for working with the dataset

**To suggest an improvement:**
1. Open a GitHub issue with the label "enhancement"
2. Clearly describe your suggestion and its benefits
3. If applicable, provide examples or references to support your proposal

## Contributing New Data

We appreciate contributions of new legal text summarization data that align with the dataset's purpose and format.

### Before Contributing Data

1. **Verify licensing**: Ensure you have the right to share the data and that it's compatible with research use
2. **Check relevance**: Data should consist of legal/contract text paired with plain English summaries
3. **Review existing data**: Familiarize yourself with the current dataset structure and quality standards
4. **Discuss first**: Open an issue to discuss your proposed contribution before investing significant effort

### Contribution Process

1. Fork the repository
2. Create a new branch for your contribution
3. Add your data following the [Data Format Guidelines](#data-format-guidelines)
4. Update documentation as needed
5. Submit a pull request with:
   - Clear description of the data source
   - Number of entries added
   - Any relevant metadata or context
   - Confirmation of licensing/permissions

## Data Format Guidelines

All data files use JSON format with the following structure:

### Required Fields (All Datasets)

```json
{
  "unique_id": {
    "uid": "unique_id",
    "original_text": "cleaned and parsed original legal text",
    "reference_summary": "cleaned and parsed plain English summary",
    "doc": "name of the source document"
  }
}
```

### TL;DRLegal Specific Fields

```json
{
  "title": "title of the legal section (optional)"
}
```

### TOS;DR Specific Fields

```json
{
  "note": "additional notes from annotator (mostly empty)",
  "urls": "URL of the respective company",
  "case_text": "raw text from the case field",
  "case_code": "annotation code for case text",
  "title_text": "raw text from the title field",
  "title_code": "annotation code for title text",
  "tldr_text": "raw text from the tldr field",
  "tldr_code": "annotation code for tldr text"
}
```

### Annotation Code Format

Annotation codes follow this structure:
- **Number prefix**: Ranking of text quality (chosen by annotator)
- **Letter suffixes**:
  - `s`: standard (text appears in multiple sets without company names)
  - `j`: jurisdiction (text deals with jurisdictional matters)
  - `q-`: quote (text is an excerpt from original)
  - `d`: description (text describes but may lack details)

### Data Quality Standards

- **Text cleaning**: Remove HTML tags, normalize whitespace, handle special characters properly
- **Completeness**: All required fields must be present
- **Accuracy**: Summaries should accurately reflect the original text
- **Length**: Reference summaries should be shorter than original text (sets violating this are excluded)
- **Encoding**: Use UTF-8 encoding for all text

## Citation Requirements

If you use this dataset in your research, you **must** cite our paper:

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

If you contribute new data or modifications, please also acknowledge the original dataset and any additional sources appropriately in your work.

## Code of Conduct

### Our Standards

We are committed to providing a welcoming and inclusive environment for all contributors. We expect all participants to:

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what is best for the research community
- Show empathy towards other community members

### Unacceptable Behavior

- Harassment, discriminatory comments, or personal attacks
- Trolling, insulting/derogatory comments
- Publishing others' private information without permission
- Other conduct that could reasonably be considered inappropriate in a professional setting

### Enforcement

Instances of unacceptable behavior may be reported to the project maintainers. All complaints will be reviewed and investigated, resulting in a response deemed necessary and appropriate to the circumstances.

## Contact

For questions, suggestions, or discussions about this dataset:

- **Issues**: Open a GitHub issue for bugs, questions, or suggestions
- **Pull Requests**: Submit PRs for proposed changes or contributions
- **Paper**: Refer to our [NAACL NLLP Workshop paper](https://www.aclweb.org/anthology/W19-2201) for research context

For matters that cannot be addressed through GitHub issues, please refer to the contact information provided in the original paper or associated institutional affiliations.

## License

Please note that contributions to this repository will be subject to the same license as the original dataset. Ensure you have the necessary rights to contribute any data or code you submit.

---

Thank you for helping improve this research dataset!
