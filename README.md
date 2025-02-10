# AutoResearch Agent

![CI](https://github.com/Hamz04/autoresearch-agent/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> Autonomous research agent that searches the web and generates structured Markdown reports.

## Features
- Web search via DuckDuckGo (no API key required)
- Generates timestamped Markdown research reports
- Fully async with asyncio + httpx
- Dockerized for easy deployment
- CI/CD with GitHub Actions

## Quick Start
```bash
git clone https://github.com/Hamz04/autoresearch-agent
cd autoresearch-agent
pip install -r requirements.txt
python main.py "quantum computing breakthroughs"
```

## Docker
```bash
docker build -t autoresearch-agent .
docker run autoresearch-agent "machine learning trends"
```

## Testing
```bash
pytest tests/ -v
```

## License
MIT
