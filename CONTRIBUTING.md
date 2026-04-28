# Contributing to Plain English Summarization of Contracts

Thank you for your interest in this dataset. Contributions from the NLP and legal informatics communities are welcome. This guide explains how to report issues, propose improvements, and submit changes.

---

## Who Should Contribute

This is a research dataset published alongside a NAACL 2019 workshop paper. Contributions are most useful from:

- Researchers who have identified errors or inconsistencies in the annotations
- Practitioners who have found formatting issues or broken records
- Anyone with domain expertise in legal text who can improve data quality

---

## Reporting Issues

If you find a problem with the dataset - such as incorrect annotations, missing fields, formatting errors, or broken records - please open a [GitHub issue](../../issues) and include:

- The affected file name (`all_v1.json`, `tldrlegal_v1.json`, or `tosdr_annotated_v1.json`)
- The `uid` of the affected record(s)
- A clear description of the problem
- The expected correct value, if known

---

## Proposing Improvements

Suggestions for new data, annotation fixes, or enhancements to the dataset structure are welcome. Open a [GitHub issue](../../issues) describing your proposal before submitting a pull request. This allows for discussion before significant effort is invested.

---

## Submitting Pull Requests

1. Fork this repository to your own GitHub account.
2. Create a new branch with a descriptive name (e.g., `fix/uid-abc123-annotation` or `add/tosdr-records`).
3. Make your changes. Keep modifications focused and minimal - one logical change per pull request.
4. Verify that any modified JSON files remain valid and conform to the existing data format described in the README.
5. Submit a pull request against the `main` branch with a clear description of what was changed and why.

Pull requests that address an open issue should reference it in the description (e.g., `Closes #42`).

---

## Citation

If you use this dataset in your research, please cite the original paper:

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

## Code of Conduct

Please keep all interactions respectful and professional. This is a research project maintained on a best-effort basis. Constructive feedback and collaborative discussion are encouraged; dismissive or disrespectful communication is not.

---

## Questions

For questions about the dataset or its use in research, please open a [GitHub issue](../../issues) rather than contacting the authors directly. This keeps discussions visible and searchable for others.
