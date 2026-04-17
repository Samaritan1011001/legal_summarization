"""Tests for CLI module."""

import pytest
from click.testing import CliRunner

from src.cli import cli


@pytest.fixture
def runner():
    """Create a CLI test runner."""
    return CliRunner()


class TestCli:
    """Tests for CLI commands."""
    
    def test_help(self, runner):
        """Test that --help works."""
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Legal text summarization CLI" in result.output
    
    def test_summarize_help(self, runner):
        """Test summarize command help."""
        result = runner.invoke(cli, ["summarize", "--help"])
        assert result.exit_code == 0
        assert "--sample" in result.output
        assert "--text" in result.output
    
    def test_summarize_text(self, runner):
        """Test summarizing custom text."""
        text = (
            "This is a test legal document. "
            "It contains multiple sentences about terms of service. "
            "Users must agree to these terms. "
            "The service provider reserves certain rights."
        )
        result = runner.invoke(cli, ["summarize", "--text", text])
        assert result.exit_code == 0
        assert "Generated Summary" in result.output
    
    def test_summarize_sample(self, runner):
        """Test summarizing a sample from dataset."""
        result = runner.invoke(cli, ["summarize", "--sample"])
        assert result.exit_code == 0
        assert "Original Text" in result.output
        assert "Generated Summary" in result.output
    
    def test_summarize_no_args(self, runner):
        """Test that summarize without args shows error."""
        result = runner.invoke(cli, ["summarize"])
        assert result.exit_code == 1
        assert "Must specify either --sample or --text" in result.output
    
    def test_summarize_both_args(self, runner):
        """Test that summarize with both args shows error."""
        result = runner.invoke(cli, ["summarize", "--sample", "--text", "test"])
        assert result.exit_code == 1
        assert "Cannot use both --sample and --text" in result.output
    
    def test_evaluate_help(self, runner):
        """Test evaluate command help."""
        result = runner.invoke(cli, ["evaluate", "--help"])
        assert result.exit_code == 0
        assert "--dataset" in result.output
        assert "--max-samples" in result.output
    
    def test_evaluate_small_sample(self, runner):
        """Test evaluation on a small sample."""
        result = runner.invoke(cli, ["evaluate", "--max-samples", "5"])
        assert result.exit_code == 0
        assert "EVALUATION RESULTS" in result.output
        assert "rouge1" in result.output
        assert "rouge2" in result.output
        assert "rougeL" in result.output
