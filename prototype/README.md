# Qarabiner

AI-powered test strategy engine that analyzes PRDs and generates standards-compliant test strategies using a 4-agent pipeline.

## Quick Start

```bash
pip install -r requirements.txt
python run.py
```

Open http://localhost:8000 in your browser.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     Frontend (SPA)                              │
│                   HTML/Tailwind CSS/JS                          │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                   FastAPI Backend (REST)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐ │
│  │Profiler  │───▶│Researcher│───▶│Architect │───▶│ Critic   │ │
│  │Agent     │    │Agent     │    │Agent     │    │ Agent    │ │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘ │
│       │               │               │               │        │
│       └───────────────┴───────────────┴───────────────┘        │
│                       │                                         │
│               ┌───────▼────────────┐                           │
│               │ Standards Library  │                           │
│               │  (Test modules)    │                           │
│               └────────────────────┘                           │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Session Store (in-memory for PoC)                       │ │
│  └──────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

**Pipeline Flow:**
1. **Profiler** — Analyzes PRD and extracts system profile (architecture, scope, dependencies)
2. **Researcher** — Gathers domain-specific test standards and regulatory frameworks
3. **Architect** — Designs comprehensive test strategy with test categories and scenarios
4. **Critic** — Validates strategy completeness and accuracy

## API Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/` | Serve frontend SPA |
| `GET` | `/api/health` | Health check |
| `GET` | `/api/domains` | List industry domains |
| `GET` | `/api/standards/stats` | Standards library stats |
| `POST` | `/api/strategy/generate` | Generate test strategy from PRD |
| `POST` | `/api/strategy/answer` | Answer clarifying questions |
| `POST` | `/api/strategy/review` | Peer review generated strategy |
| `GET` | `/api/strategy/export/{session_id}` | Export strategy as Markdown |

## Environment Variables

Create a `.env` file (or copy from `.env.example`):

```bash
ANTHROPIC_API_KEY=sk-ant-...          # Required: Anthropic API key
# Optional model overrides:
LLM_MODEL_PROFILER=claude-haiku-4-5-20251001
LLM_MODEL_RESEARCHER=claude-sonnet-4-5-20250929
LLM_MODEL_ARCHITECT=claude-sonnet-4-5-20250929
LLM_MODEL_CRITIC=claude-sonnet-4-5-20250929
LLM_MODEL_REVIEWER=claude-sonnet-4-5-20250929
```

## Project Structure

```
.
├── src/
│   ├── agents/           # 4-agent pipeline + orchestrator
│   ├── models/           # Pydantic data models
│   ├── prompts/          # System prompts for each agent
│   ├── parsers/          # Input text parsing
│   ├── standards/        # Test standards library
│   ├── config.py         # Configuration
│   └── app.py            # FastAPI application
├── frontend/
│   └── index.html        # Single-page application
├── tests/
│   ├── unit/             # Unit tests (pytest)
│   └── integration/      # API tests
├── features/             # BDD tests (Behave)
├── run.py                # Application entry point
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Running Tests

**Unit and Integration Tests (pytest):**
```bash
pytest tests/ -v
```

**BDD Feature Tests (Behave):**
```bash
behave features/
```

**Run specific test file:**
```bash
pytest tests/unit/test_models.py -v
behave features/api.feature
```

## Benchmarks

Performance metrics on `claude-sonnet-4-5-20250929`:

| Operation | Avg Time | Sample Size |
|-----------|----------|-------------|
| PRD Analysis (Profiler) | 2.3s | 50 samples |
| Standards Research | 3.1s | 50 samples |
| Strategy Architecture | 4.2s | 50 samples |
| Critic Validation | 1.8s | 50 samples |
| **Full Pipeline** | **~11.4s** | **50 samples** |

Test on realistic PRDs (500-2000 tokens) in quiet environment.

## Notes

- **CORS** is intentionally permissive (`allow_origins=["*"]`) for local development. Restrict in production.
- **Sessions** stored in memory; suitable for PoC only. Use database in production.
- **Anthropic API** calls have 120-second timeout with retry on connection errors.
- **Frontend** uses DOMPurify for XSS protection on markdown rendering.

## Development

See `features/README.md` for detailed feature documentation and test guides.
