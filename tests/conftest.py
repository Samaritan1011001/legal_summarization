"""Shared pytest fixtures for legal summarization tests."""

import json
import os
import tempfile

import pytest


@pytest.fixture
def sample_record():
    """A single sample record with realistic legal text."""
    return {
        "uid": "legalsum_test01",
        "doc": "Test Terms of Service",
        "original_text": (
            "by using our services you agree to be bound by these terms of service. "
            "if you do not agree to these terms you should not use the service. "
            "we reserve the right to modify these terms at any time without prior notice. "
            "your continued use of the service constitutes acceptance of the modified terms."
        ),
        "reference_summary": (
            "by using the service you agree to the terms. "
            "the company can change terms anytime."
        ),
    }


@pytest.fixture
def sample_dataset():
    """A list of 12 sample records with varied legal text."""
    records = []
    topics = [
        ("Privacy Policy", "we collect personal data", "they collect your data"),
        ("Terms of Service", "by using our services you agree", "you agree by using the service"),
        ("Cookie Policy", "we use cookies to improve experience", "cookies are used on this site"),
        ("DMCA Policy", "we respect intellectual property rights", "they respect copyright"),
        ("Refund Policy", "refunds are available within 30 days", "you can get a refund in 30 days"),
        ("User Agreement", "users must be at least 18 years old", "you must be 18 or older"),
        ("Data Policy", "your data may be shared with partners", "data may be shared with third parties"),
        ("Acceptable Use", "you may not use the service for illegal purposes", "no illegal use allowed"),
        ("Liability Clause", "we are not liable for indirect damages", "they are not responsible for indirect damages"),
        ("Arbitration Clause", "disputes shall be resolved through arbitration", "disputes go to arbitration"),
        ("Termination Clause", "we may terminate your account at any time", "they can close your account anytime"),
        ("Indemnification", "you agree to indemnify and hold harmless", "you must cover their legal costs"),
    ]
    for i, (doc, text, summary) in enumerate(topics):
        records.append({
            "uid": f"legalsum_test{i + 1:02d}",
            "doc": doc,
            "original_text": text + f". this is additional context for record {i + 1} to make the text longer and more realistic for testing purposes.",
            "reference_summary": summary,
        })
    return records


@pytest.fixture
def sample_predictions_and_references():
    """Paired lists of predictions and references for evaluation testing."""
    predictions = [
        "the service collects personal data from users",
        "you agree to the terms by using the service",
        "cookies are used to improve the user experience",
        "refunds are available within thirty days of purchase",
    ]
    references = [
        "they collect your personal data",
        "by using the service you agree to the terms",
        "cookies are used on this site",
        "you can get a refund in 30 days",
    ]
    return predictions, references


@pytest.fixture
def tmp_dataset_file(sample_dataset, tmp_path):
    """Write sample data to a temp JSON file in dict-of-dicts format keyed by uid."""
    data_dict = {record["uid"]: record for record in sample_dataset}
    filepath = tmp_path / "test_dataset.json"
    with open(filepath, "w") as f:
        json.dump(data_dict, f)
    return str(filepath)
