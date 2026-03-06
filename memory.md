# AI QA Architect — Project Memory

> **Last updated:** 2026-03-05
> **Owner:** Timotej (timotej@kovacic.pro)
> **Status:** Architecture Finalized, Pre-PoC
> **Primary document:** `PRD-AI-QA-Architect.md` (same folder) — the complete PRD and architecture spec

---

## Quick Context

AI QA Architect is a web-based AI Test Manager SPA. Users upload a PRD or link a Git repo, configure their industry domain and regulatory context, and the system generates a comprehensive, standards-compliant Test Strategy through a 4-agent pipeline (Profiler → Researcher → Architect → Critic). The Critic Agent validates all output before it reaches the user — no raw LLM output is ever delivered.

The full PRD, architecture, system prompt, business model, testing strategy, benchmark suite, and roadmap are in `PRD-AI-QA-Architect.md`.

---

## Development History

**Initial consultation (2026-03-05, Gemini):** Timotej consulted Gemini for initial concept validation, architecture, and development plan. Gemini proposed: React SPA + FastAPI backend + Gemini 3.1 Pro as AI engine + RAG with Vector DB for standards. Produced a static HTML mockup (non-functional), a bare-bones FastAPI skeleton, and a system prompt.

**Critical review (2026-03-05, Claude):** Seven architectural issues identified and resolved:

1. **Model bias** — Gemini recommended itself. Benchmarks showed Claude Opus 4.6 leads on SWE reasoning and tool-use accuracy. → Resolved: model-agnostic architecture, Claude as default primary.
2. **No validation layer** — Single-pass generate → display. → Resolved: Critic Agent (Agent 4) added as mandatory quality gate with citation verification, hallucination detection, structural completeness, and risk-sensitivity alignment checks.
3. **No domain awareness** — Plan assumed generic web apps. → Resolved: Domain Configuration Step added. 10 industry domains mapped with their specific standards (medical/IEC 62304, automotive/ISO 26262, aerospace/DO-178C, railway/EN 50716, nuclear/IEC 60880, financial/PCI-DSS v4.0, telecom/3GPP, embedded/IEC 61508, gambling/KYC+RNG, government/FedRAMP 20x).
4. **Incomplete standards baseline** — Only 5 generic families. → Resolved: expanded to 10+ domain-specific standard ecosystems with safety integrity level mappings (SIL, ASIL, SSIL, DAL).
5. **Rigid prompt structure** — Hardcoded "max 5 questions" and fixed output template. → Resolved: dynamic question limits based on complexity, domain-adaptive output templates with domain-specific sections.
6. **Weak benchmarking** — Single "trap PRD." → Resolved: 8-scenario benchmark suite covering risk sensitivity, ASIL differentiation, contradiction detection, architectural complexity, critical gap identification, HW constraints, regulatory complexity, and minimal-input refusal.
7. **Standards hallucination risk** — No mechanism to catch fabricated standard references. → Resolved: Critic Agent must verify every citation against Vector DB content.

---

## Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-03-05 | AI acts as Test Manager, NOT tester/pentester | Strategic planning and risk assessment, not execution |
| 2026-03-05 | Model-agnostic architecture | Abstract LLM behind interface; Claude Opus 4 default primary; Enterprise customers can specify provider |
| 2026-03-05 | 4-agent pipeline (Profiler → Researcher → Architect → Critic) | Separation of concerns; validation before delivery; cost optimization per task |
| 2026-03-05 | Internal validation layer mandatory | No raw LLM output to user; citation verification, hallucination detection, structural check |
| 2026-03-05 | Domain Configuration Step before analysis | Industry domain + regulatory context fundamentally changes test strategy |
| 2026-03-05 | Standards in full in Vector DB, prompt steers | Avoids limiting scope while preventing hallucination |
| 2026-03-05 | Hierarchical chunking for standards | Preserves logical structure of standard documents |
| 2026-03-05 | Dynamic question limits and domain-adaptive output templates | Rigid limits and templates are inappropriate for diverse domains |
| 2026-03-05 | No hype words in system prompt | Operational constraints, not subjective qualifiers |
| 2026-03-05 | Critic verifies every standard citation against Vector DB | Prevents fabricated standard references |

---

## Current Phase: Pre-PoC

### Next steps (Phase 1 — AI Core PoC):
- [ ] Implement Agent 3 (Architect) with full system prompt
- [ ] Implement Agent 4 (Critic) with citation verification
- [ ] Populate Vector DB with core standards (ISO 29119, ISO 25010, ISTQB Foundation, OWASP Top 10 + ASVS)
- [ ] Run benchmark scenarios 1, 3, 8 (HealthVault, self-contradicting PRD, minimal PRD)
- [ ] Validate model-agnostic abstraction with Claude + one alternative

### Open questions (blocking Phase 1):
- Which Vector DB? (Pinecone vs Qdrant vs pgvector)
- Legal: Can we embed ISO/ISTQB content in a commercial Vector DB?
- RAG vs full context window for standards — needs empirical testing
- Critic Agent: same model with different prompt, or different model?

See `PRD-AI-QA-Architect.md` Section 10 for full open questions list.

---

## Timotej — Working Style

- Critically scrutinizes AI output — expects precision, not hand-waving
- Challenges vague terminology — demands operational definitions
- Values standards compliance and traceability
- Prefers thorough architecture validation before building
- Iterative: refine the AI core first, then build the app
- Spotted Gemini's self-promotion — expects objective, evidence-based analysis
- Claude is the primary development partner going forward
