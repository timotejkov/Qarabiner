# Qarabiner

AI-powered test strategy generator that turns PRDs into comprehensive, standards-compliant QA strategies.

Paste a PRD (or a GitHub link) and Qarabiner runs a 4-agent pipeline — Profiler, Researcher, Architect, Critic — to produce a detailed test strategy grounded in ISO 29119, ISO 25010, ISTQB, OWASP, WCAG, and domain-specific standards.

## Quick Start

```bash
cd prototype
pip install -r requirements.txt
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
python run.py
```

Open [http://localhost:8000](http://localhost:8000) in your browser. Paste your PRD and press **Generate Strategy**. That's it — domain, safety level, and regulatory frameworks are inferred automatically.

## How It Works

```
PRD Text / GitHub URL
        │
        ▼
   ┌──────────┐     Haiku — extracts tech stack, infers domain & safety level
   │ Profiler  │
   └────┬─────┘
        ▼
   ┌──────────┐     Sonnet — semantic search across 270+ standards sections
   │Researcher│
   └────┬─────┘
        ▼
   ┌──────────┐     Sonnet — generates full test strategy with citations
   │ Architect│
   └────┬─────┘
        ▼
   ┌──────────┐     Haiku — validates citations, checks completeness
   │  Critic  │
   └──────────┘
        │
        ▼
   Test Strategy (Markdown)
```

The pipeline identifies gaps and asks clarifying questions before generating. If the Critic finds issues, the Architect revises automatically.

## Standards Coverage

Qarabiner includes 270+ indexed sections across 7 standards families:

| Standard | Coverage |
|----------|----------|
| ISO/IEC/IEEE 29119 | Test processes, techniques, documentation (Parts 1-4) |
| ISO/IEC 25010:2023 | Quality model — 8 characteristics, 31 sub-characteristics |
| ISTQB | Foundation + Advanced syllabi, test levels, techniques |
| OWASP | Top 10, ASVS (L1-L3), API Security Top 10, secure dev practices |
| WCAG 2.2 | Perceivable, Operable, Understandable, Robust (Level AA) |
| Medical Device | IEC 62304, FDA CSA, HIPAA, risk management |
| Automotive | ISO 26262 (ASIL A-D), ASPICE, AUTOSAR, SOTIF |

Standards retrieval uses ChromaDB semantic search with keyword fallback.

## Features

- **Zero-config UX** — paste PRD and go; domain/safety/deployment inferred from content
- **GitHub URL support** — paste a link to a GitHub file instead of copy-pasting text
- **Semantic search** — ChromaDB vector store for accurate standards retrieval
- **Citation validation** — Critic agent verifies every standards reference
- **Export** — download strategy as Markdown

## Project Structure

```
prototype/
├── src/
│   ├── agents/        # Profiler, Researcher, Architect, Critic, Orchestrator
│   ├── standards/     # Standards library + ChromaDB vectorstore
│   ├── models/        # Pydantic data models
│   ├── prompts/       # System prompts for each agent
│   ├── parsers/       # Text parser + GitHub fetcher
│   └── app.py         # FastAPI application
├── frontend/
│   └── index.html     # Single-page app (vanilla JS + Tailwind)
├── tests/             # Pytest unit + integration tests
├── features/          # BDD feature tests (Behave)
├── benchmarks/        # Sample PRDs for testing
└── run.py             # Entry point
```

## API

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/strategy/generate` | Generate strategy from PRD text or GitHub URL |
| POST | `/api/strategy/answer` | Submit answers to clarifying questions |
| GET | `/api/strategy/export/{id}` | Export strategy as Markdown |
| GET | `/api/health` | Health check |
| GET | `/docs` | Interactive API docs (Swagger) |

## Configuration

Create `prototype/.env`:

```bash
ANTHROPIC_API_KEY=sk-ant-...       # Required
# Optional model overrides:
LLM_MODEL_PROFILER=claude-haiku-4-5-20251001
LLM_MODEL_RESEARCHER=claude-sonnet-4-5-20250929
LLM_MODEL_ARCHITECT=claude-sonnet-4-5-20250929
LLM_MODEL_CRITIC=claude-haiku-4-5-20251001
```

## License

Private — not licensed for redistribution.
