import pytest, asyncio, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from unittest.mock import patch

MOCK_RESULTS = [
    {"title": "AI Overview", "snippet": "AI is transforming industries.", "url": "https://example.com/ai"},
    {"title": "ML Trends", "snippet": "ML continues to grow.", "url": "https://example.com/ml"},
]

def test_report_structure(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    import main
    async def fake_search(q, n=5): return MOCK_RESULTS
    with patch.object(main, "web_search", fake_search):
        result = asyncio.run(main.run_agent("test topic"))
    assert result["sources"] == 2
    assert os.path.exists(result["file"])
    with open(result["file"]) as f:
        content = f.read()
    assert "# Research Report" in content
    assert "test topic" in content

def test_empty_search(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    import main
    async def empty(q, n=5): return []
    with patch.object(main, "web_search", empty):
        result = asyncio.run(main.run_agent("empty"))
    assert result["sources"] == 0
