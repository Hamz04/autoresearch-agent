"""AutoResearch Agent - Autonomous LLM-powered research agent."""
import os, asyncio
from datetime import datetime
import httpx

async def web_search(query: str, num_results: int = 5) -> list[dict]:
    async with httpx.AsyncClient() as http:
        resp = await http.get(
            "https://api.duckduckgo.com/",
            params={"q": query, "format": "json", "no_html": 1, "skip_disambig": 1},
            timeout=10.0
        )
        data = resp.json()
        results = []
        if data.get("AbstractText"):
            results.append({"title": data.get("Heading", query), "snippet": data["AbstractText"], "url": data.get("AbstractURL", "")})
        for r in data.get("RelatedTopics", [])[:num_results]:
            if isinstance(r, dict) and r.get("Text"):
                results.append({"title": r.get("Text","")[:60], "snippet": r.get("Text",""), "url": r.get("FirstURL","")})
        return results[:num_results]

async def run_agent(topic: str) -> dict:
    print(f"[AutoResearch] Researching: {topic}")
    results = await web_search(topic)
    lines = [f"# Research Report: {topic}", f"*Generated: {datetime.now().isoformat()}*", ""]
    for i, r in enumerate(results, 1):
        lines += [f"## [{i}] {r['title']}", r['snippet'], f"Source: {r['url']}", ""]
    report = "\n".join(lines)
    os.makedirs("reports", exist_ok=True)
    fname = f"reports/{topic.replace(' ','_')[:40]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(fname, "w") as f:
        f.write(report)
    print(f"[AutoResearch] Saved to {fname}")
    return {"topic": topic, "sources": len(results), "file": fname, "report": report}

if __name__ == "__main__":
    import sys
    topic = " ".join(sys.argv[1:]) or "artificial intelligence trends 2025"
    result = asyncio.run(run_agent(topic))
    print(result["report"])
