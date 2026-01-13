import pytest
from src.analyze import Analyzer

def test_analyze_snippet_empty():
    analyzer = Analyzer()
    result = analyzer.analyze_snippet("")
    assert "error" in result

def test_analyze_snippet_valid():
    analyzer = Analyzer()
    result = analyzer.analyze_snippet("def foo(): pass")
    assert result["summary"] == "Analysis complete"
    assert len(result["issues"]) > 0
