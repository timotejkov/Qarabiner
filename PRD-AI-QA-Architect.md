# AI QA Architect — Product Requirements & Architecture Document

> **Version:** 2.0 (Post-Review)
> **Date:** 2026-03-05
> **Author:** Timotej Kovacic, with Claude (Anthropic)
> **Status:** Architecture Finalized, Pre-PoC

---

## 1. Product Definition

### 1.1 What It Is

AI QA Architect is a web-based application that generates comprehensive, standards-compliant software test strategies and test plans. Users provide a Product Requirements Document (PRD) or link a Git repository. The system analyzes the input, identifies the technology stack, assesses risk, determines the applicable industry standards, asks clarifying questions where information is insufficient, and produces a complete Test Strategy grounded in traceable references to ISO, ISTQB, OWASP, and domain-specific standards.

The system operates as a **Principal Test Manager** — it performs strategic planning, risk assessment, and scoping. It does not execute tests, write test scripts, or perform penetration testing.

### 1.2 What It Is Not

- Not a test execution engine (no Selenium, Playwright, or automation scripts)
- Not a penetration testing tool (does not scan for vulnerabilities)
- Not a test case management system (does not store or track individual test cases)
- Not a bug tracker or defect management system

### 1.3 Core User Workflow

```
┌─────────────┐    ┌──────────────────┐    ┌─────────────────┐    ┌──────────────┐    ┌──────────────┐    ┌─────────────┐
│  1. Upload   │───▶│ 2. Domain Config  │───▶│  3. AI Profiling │───▶│ 4. Gap Check │───▶│ 5. Strategy  │───▶│  6. Export   │
│  PRD / Repo  │    │  Industry + Regs  │    │  Stack + Risk    │    │  Q&A Loop    │    │  Generation  │    │  PDF/Jira/MD │
└─────────────┘    └──────────────────┘    └─────────────────┘    └──────────────┘    └──────────────┘    └─────────────┘
                                                                                              │
                                                                                    ┌─────────▼──────────┐
                                                                                    │  5b. Validation    │
                                                                                    │  (Critic Agent)    │
                                                                                    └────────────────────┘
```

**Step 1 — Input:** User uploads a PRD (PDF, Markdown, Word, plain text) or provides a Git repository URL (GitHub, GitLab, Bitbucket).

**Step 2 — Domain Configuration:** User selects the industry domain, applicable regulatory frameworks, safety integrity levels, hardware constraints, and deployment environment. The system may also auto-suggest domains based on initial PRD analysis.

**Step 3 — AI Profiling:** The system analyzes the input to extract: technology stack, system architecture, data flow, user roles, data sensitivity classification, and business criticality.

**Step 4 — Gap Check & Iterative Q&A:** The system evaluates whether it has sufficient context to generate a responsible strategy. If critical information is missing (deployment environment, expected load, compliance scope, data classification, etc.), it generates targeted clarifying questions. The number of questions is dynamic — scaled to the complexity of the domain and the gaps detected. The user answers, and the system may ask follow-up questions if answers reveal new gaps.

**Step 5 — Strategy Generation + Validation:** The primary AI model generates the Test Strategy. Before delivery to the user, the Critic Agent validates the output: verifies every standard citation against the Vector DB, checks for hallucinated features or endpoints, confirms structural completeness per the domain-specific template, and ensures risk assessment matches the detected data sensitivity. If validation fails, the system self-corrects or flags weak sections.

**Step 6 — Export:** User receives the strategy rendered in the UI and can export to PDF, Word, Markdown, or push to Jira/Confluence.

### 1.4 Key Differentiators

Compared to existing tools (Wisary, Testomat.io, PractiTest, Virtuoso QA, BrowserStack):

- **Strategy-first, not execution-first.** Competitors focus on generating test scripts or managing test cases. We generate the strategic plan that precedes all of that.
- **Lightweight SPA, not an enterprise platform.** No 6-month onboarding. A QA engineer gets a professional-grade test strategy in minutes.
- **Iterative AI Q&A.** The system asks clarifying questions rather than generating generic output from incomplete information.
- **Standards-traceable output.** Every recommendation cites the specific standard justifying its inclusion. Competitors produce AI-generated text with no traceability.
- **Domain-aware.** Supports regulated industries (medical, automotive, aerospace, etc.) with domain-specific standards and output templates.
- **Internal validation layer.** Output is verified before delivery — no raw LLM output reaches the user.

---

## 2. Standards & Analytical Baseline

### 2.1 Core Standards (Always Active)

These five framework families form the baseline for every analysis, regardless of domain:

| Standard | Purpose | Scope |
|----------|---------|-------|
| **ISO/IEC/IEEE 29119** (Parts 1-5) | Test processes, documentation, organizational strategy | Primary governing standard for software testing. Supersedes IEEE 829. |
| **ISO/IEC 25010:2023** | Software Product Quality model | Defines quality characteristics: Functional Suitability, Performance Efficiency, Compatibility, Usability, Reliability, Security, Maintainability, Portability |
| **ISTQB Syllabi** (full scope) | Test design techniques, risk-based testing, lifecycle management | Foundation, Advanced Test Manager, Advanced Test Analyst, Agile Technical Tester, plus domain-specific syllabi as contextually relevant |
| **OWASP Foundation** (full scope) | Application security | Top 10, ASVS (all levels), API Security Top 10, MASVS (mobile), AI Testing Guide 1.0 |
| **WCAG 2.2 Level AA** | Accessibility compliance | Triggered when web/UI components are detected |

### 2.2 Domain-Specific Standards (Activated by Domain Configuration)

When the user selects an industry domain in Step 2, the system activates the corresponding standards from the Vector DB:

| Domain | Key Standards | Safety/Integrity Metric | ISTQB Specialization |
|--------|--------------|------------------------|---------------------|
| **Medical Devices** | IEC 62304 (Ed.2 due Aug 2026), FDA CSA (Sep 2025), 21 CFR Part 11, HIPAA, ISO 13485 | Risk Class A/B/C | None specific |
| **Automotive** | ISO 26262, ASPICE v3.1+, AUTOSAR, ISO 21448 (SOTIF) | ASIL A–D | CT-AuT v2.1 |
| **Aerospace/Defense** | DO-178C, DO-254, DO-160, DO-326A, DO-278A, MIL-STD-498 | DAL A–E | None specific |
| **Financial Services** | PCI-DSS v4.0, SOX, Basel III/IV, NIST 800-53, GLBA, CCPA/GDPR | Compliance level | None specific |
| **Embedded/IoT** | IEC 61508, IEC 60601, IEC 61131-3 | SIL 1–4 | None specific |
| **Telecommunications** | 3GPP Release 20, TS 38.141, ITU-T, GCF certification | Conformance level | None specific |
| **Railway** | EN 50716 (replaces EN 50128/50657), EN 50126 (RAMS), EN 50129 | SSIL 0–4 | None specific |
| **Nuclear/Energy** | IEC 60880, IEC 61226, IEC 61513, IEEE 1012 | Category A functions | None specific |
| **Gaming/Gambling** | KYC, AML, RNG certification, Responsible Gaming standards | Jurisdictional | Gambling Industry Tester |
| **Government/Public Sector** | FedRAMP 20x, NIST 800-53 v5.2, Common Criteria (ISO 15408), FISMA | KSI / AVA_VAN | None specific |
| **Custom** | User uploads their own internal standards | User-defined | N/A |

**Multi-domain support:** Products that span multiple domains (e.g., a medical IoT device = IEC 62304 + IEC 61508 + connectivity standards) activate all applicable standard sets, and the system merges the requirements into a unified strategy with cross-references.

### 2.3 Standards Architecture Principle

The system prompt provides **steering** — it tells the AI which standard family to consult for which purpose. The Vector Database provides **depth** — the full text of every standard, hierarchically chunked to preserve logical structure. The AI retrieves relevant sections dynamically via tool calling based on the specific tech stack, risk profile, and domain it identifies. Domain-specific syllabi and standards are pulled only when contextually relevant.

**Standards versioning:** The Vector DB must maintain version-aware entries. When multiple versions of a standard coexist (e.g., PCI-DSS v3.2.1 vs v4.0, IEC 62304 Ed.1 vs Ed.2), the system retrieves the most current version by default and flags transitional requirements where both versions may apply.

---

## 3. System Architecture

### 3.1 High-Level Architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│                              FRONTEND (SPA)                              │
│                   React (Next.js) + Tailwind CSS                         │
│  ┌──────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │  Upload   │  │ Domain Config│  │  Chat / Q&A  │  │  Strategy    │    │
│  │  Panel    │  │  Wizard      │  │  Interface   │  │  Viewer      │    │
│  └──────────┘  └──────────────┘  └──────────────┘  └──────────────┘    │
└───────────────────────────────┬──────────────────────────────────────────┘
                                │ REST API / WebSocket (streaming)
┌───────────────────────────────▼──────────────────────────────────────────┐
│                              BACKEND (Python FastAPI)                     │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐    │
│  │                      AGENT ORCHESTRATOR                          │    │
│  │                                                                  │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────────┐ │    │
│  │  │  Agent 1:    │  │  Agent 2:    │  │  Agent 3:    │  │Agent 4:│ │    │
│  │  │  Profiler    │──▶  Researcher  │──▶  Architect   │──▶ Critic │ │    │
│  │  │  (fast model)│  │  (tool call) │  │  (primary)   │  │(valid.)│ │    │
│  │  └─────────────┘  └──────┬──────┘  └─────────────┘  └────────┘ │    │
│  │                          │                                       │    │
│  └──────────────────────────┼───────────────────────────────────────┘    │
│                             │                                            │
│  ┌──────────────────────────▼───────────────────────────────────────┐    │
│  │                    LLM ABSTRACTION LAYER                         │    │
│  │  Providers: Claude API │ Gemini API │ OpenAI API │ Custom        │    │
│  │  Model routing: primary (strategy) │ fast (chat) │ validation    │    │
│  └──────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  ┌─────────────────┐  ┌───────────────┐  ┌──────────────────────────┐   │
│  │  Input Parser    │  │  Git Ingestion │  │  Export Engine           │   │
│  │  PDF/MD/DOCX     │  │  GitHub/GitLab │  │  PDF/DOCX/MD/Jira       │   │
│  └─────────────────┘  └───────────────┘  └──────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────────┘
                    │                              │
     ┌──────────────▼──────────┐    ┌──────────────▼──────────┐
     │    PostgreSQL            │    │    Vector Database       │
     │    Users, projects,      │    │    Standards corpus      │
     │    session history       │    │    (hierarchical chunks) │
     └─────────────────────────┘    └─────────────────────────┘
```

### 3.2 Multi-Agent Workflow (Detail)

The AI core is not a single prompt-and-response. It is a four-agent pipeline:

**Agent 1 — Profiler** (fast/cheap model)
- Input: Raw PRD text or parsed Git repo metadata + user's domain configuration
- Output: Structured JSON profile containing: tech stack, architecture pattern (monolith/microservices/serverless), data sensitivity classification (public/internal/confidential/restricted), business domain, user roles, deployment targets, identified integration points
- Purpose: Converts unstructured input into a structured representation the other agents can operate on

**Agent 2 — Researcher** (tool-calling model)
- Input: Structured profile from Agent 1
- Action: Queries the Vector DB using the `query_qa_standards` tool to retrieve relevant standard sections. Retrieval is driven by: (a) the core standards baseline, (b) the domain-specific standards activated by the user's configuration, (c) the specific tech stack and risk factors identified by the Profiler
- Output: A curated set of standard sections, clauses, and requirements relevant to this specific project
- Purpose: Ensures the Architect Agent works with verified standard content, not its parametric memory

**Agent 3 — Architect** (primary/strongest model)
- Input: Original PRD/repo data + structured profile + retrieved standards + domain-specific output template
- Execution: Follows the system prompt's execution workflow (see Section 4). If gaps are detected, outputs clarifying questions. If sufficient context exists, generates the full Test Strategy using the domain-appropriate template.
- Output: Either a set of clarifying questions (JSON) or a complete Markdown Test Strategy
- Purpose: The core strategic reasoning engine

**Agent 4 — Critic** (validation model, can be cheaper)
- Input: The Architect's output + the retrieved standards from Agent 2
- Validation checks:
  1. **Citation verification:** Extract every standard reference → query Vector DB → confirm the cited section/clause exists. Flag or remove any unverifiable reference.
  2. **Hallucination detection:** Check every mentioned endpoint, feature, or UI element against the original PRD/repo input. Flag anything not present in the source material.
  3. **Structural completeness:** Verify every required section of the domain template is populated with substantive content (not filler).
  4. **Risk-sensitivity alignment:** Confirm the recommended test depth matches the data sensitivity classification from Agent 1.
  5. **Standards coverage:** Verify that every activated domain standard has been addressed in the strategy.
- Output: Validated strategy (passed) or annotated strategy with flagged issues (failed → loops back to Agent 3 for correction, max 2 retries)
- Purpose: Quality gate. No raw LLM output reaches the user.

### 3.3 LLM Abstraction Layer

The architecture is **model-agnostic**. All LLM calls go through an abstraction layer that routes to the appropriate provider and model based on the task:

| Task | Model Role | Recommended Default | Alternatives |
|------|-----------|-------------------|-------------|
| Strategy generation (Agent 3) | Primary / Strongest reasoning | Claude Opus 4 | GPT-4.5, Gemini 2.5 Pro |
| Profiling (Agent 1) | Fast / Cheap | Claude Haiku 4 | Gemini Flash-Lite, GPT-4o-mini |
| Iterative chat / Q&A | Fast / Cheap | Claude Haiku 4 | Gemini Flash-Lite |
| Validation (Agent 4) | Moderate reasoning | Claude Sonnet 4 | GPT-4o, Gemini 2.5 Pro |
| Tool calling (Agent 2) | Strong tool use | Claude Sonnet 4 | Gemini 2.5 Pro |

**Why model-agnostic matters:**
- Enterprise customers in regulated industries may require specific providers (e.g., data residency requirements that prohibit sending data to certain cloud providers)
- Provider outages don't take down the product — automatic fallback
- Cost optimization — different models for different tasks
- Future-proofing — new models can be swapped in without architectural changes

**Why Claude as default primary:** Claude Opus 4.6 benchmarks at 80.9% on SWE-bench Verified (code reasoning), 100% tool-use accuracy, 1M token context window, and has a stable production API. Gemini 3.1 Pro is in preview with documented instability. The original Gemini recommendation was self-serving — Gemini recommended itself.

### 3.4 Tech Stack

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Frontend** | React (Next.js) + Tailwind CSS | SPA with SSR capability, modern UI, wide ecosystem |
| **Backend** | Python FastAPI | Industry standard for AI pipelines, async support, best LLM library ecosystem |
| **Primary DB** | PostgreSQL | User data, project history, session state |
| **Vector DB** | TBD (Pinecone vs Qdrant vs pgvector) | Standards corpus storage and retrieval |
| **Input parsing** | PyMuPDF (PDF), python-docx (Word), markdown-it (MD) | Multi-format PRD ingestion |
| **Git ingestion** | GitHub/GitLab/Bitbucket REST APIs | Clone and extract: README, package manifests, directory structure, core module signatures |
| **Export** | WeasyPrint (PDF), python-docx (Word), Jira REST API | Multi-format strategy delivery |
| **Auth** | OAuth 2.0 (GitHub, Google) | Standard SPA authentication |
| **Deployment** | Vercel (frontend), Docker on Cloud Run/Render (backend) | Easy CI/CD, scalable |
| **Monitoring** | Structured logging, LLM cost tracking per request | Operational visibility and cost control |

### 3.5 Data Pipeline: Standards Ingestion

The Vector Database is populated offline (not at request time) through a standards ingestion pipeline:

1. **Source documents:** ISTQB syllabi (PDF), ISO standards (purchased/licensed), OWASP guides (public), domain-specific standards
2. **Parsing:** Extract text while preserving structural hierarchy (headings, subheadings, clause numbers, definitions, tables)
3. **Hierarchical chunking:** Split into chunks that preserve logical units — a complete clause with its heading, definition, and examples stays together. Parent-child relationships maintained (e.g., "ISO 29119-3 → Section 6 → 6.2.1" preserved as a navigable path)
4. **Embedding:** Generate vector embeddings for each chunk
5. **Storage:** Store in Vector DB with metadata: standard name, version, part/section, domain tags, effective date
6. **Versioning:** Multiple versions of the same standard coexist with version metadata. Retrieval defaults to most current; transitional periods flag both versions.

**Legal consideration (open question):** Licensing for embedding ISO and ISTQB content in a commercial Vector DB needs legal review. OWASP content is open-source. Some ISO standards may require licensing agreements.

---

## 4. System Prompt Architecture

### 4.1 Design Principles

The system prompt was designed using established prompt engineering principles, explicitly rejecting common anti-patterns:

- **No hype words.** Terms like "elite," "expert," "world-class," and "production-ready" are banned. They waste tokens and produce no measurable effect on output quality. Replaced with operational constraints and concrete benchmarks.
- **Explicit state machine.** The prompt enforces a step-by-step execution workflow. The AI cannot skip gap analysis or jump to strategy generation without completing prior steps.
- **Structured markup.** XML tags separate sections (role, workflow, constraints, output formats) for unambiguous parsing by the model.
- **Concrete quality benchmarks.** Instead of "ensure the login works," the prompt demands specificity like "validate JWT token expiration and rate-limiting on the /api/v1/auth endpoint."
- **Dynamic, not rigid.** Question limits and output templates adapt to detected complexity and domain rather than using hardcoded values.

### 4.2 Core System Prompt (Agent 3 — Architect)

```xml
<system_role>
You are an automated Quality Assurance Strategy Engine operating as a Principal Test Manager.
Your function is to perform risk assessment and produce actionable, standard-compliant
Test Strategies for software systems.

Your analytical baseline MUST adhere to:
- ISO/IEC/IEEE 29119 (all parts): test processes, documentation, design techniques
- ISO/IEC 25010:2023: software product quality model
- ISTQB syllabi (full scope): test design techniques, risk-based testing, lifecycle management
- OWASP Foundation (full scope): application security verification
- WCAG 2.2 Level AA: accessibility (when web/UI detected)
- Domain-specific standards as provided in <domain_standards>
</system_role>

<input_definitions>
<user_context>
Contains the PRD, API specs, or Git repository metadata provided by the user.
This is the ONLY source of truth about the system under test.
Do not invent features, endpoints, or UI elements not present here.
</user_context>

<domain_config>
Contains the user's selected industry domain, regulatory requirements,
safety integrity levels, hardware constraints, and deployment environment.
</domain_config>

<retrieved_standards>
Contains specific standard clauses and requirements fetched from the
standards database by the Researcher agent. These are verified references.
You MUST cite from this section. Do NOT fabricate standard references.
</retrieved_standards>

<output_template>
Contains the domain-specific output structure. Follow it exactly.
</output_template>
</input_definitions>

<execution_workflow>
Step 1: PROFILE. Analyze <user_context> and <domain_config> to determine:
  - System architecture and technology stack
  - Data flow and integration points
  - User roles and access patterns
  - Data sensitivity classification (public / internal / confidential / restricted)
  - Business criticality assessment

Step 2: RISK ASSESSMENT. Using ISO 29119-2 risk-based testing principles:
  - Identify technical risks (architecture complexity, third-party dependencies, data handling)
  - Identify business risks (regulatory exposure, data breach impact, availability requirements)
  - Determine required test levels (component, integration, system, acceptance)
  - Map risks to testing priorities

Step 3: QUALITY ATTRIBUTE MAPPING. Using ISO 25010:2023:
  - Select the quality characteristics that MUST be verified for this specific system
  - For each selected characteristic, define measurable acceptance criteria
  - Cross-reference with domain-specific NFR standards from <retrieved_standards>

Step 4: GAP CHECK. Evaluate whether <user_context> contains sufficient information for:
  - Expected peak concurrent users / load profile (for performance strategy)
  - Data privacy classification and applicable regulations (for security/compliance strategy)
  - Deployment environment specifics (for environment planning)
  - Integration points and third-party dependencies (for integration strategy)
  - Domain-specific requirements from <domain_config> that lack detail

  IF critical gaps exist → STOP → output <output_format_questions>
  The number of questions should match the number of genuine gaps detected.
  Do not artificially limit or inflate the question count.

Step 5: STRATEGY SYNTHESIS. If context is sufficient:
  - Map every identified feature/component to specific test types
  - Ground every recommendation in standards from <retrieved_standards>
  - Apply ISTQB test design techniques appropriate to each component
  - Structure output per <output_template>
  - Ensure every section contains substantive, project-specific content
</execution_workflow>

<constraints>
STRATEGIC FOCUS: Do not write individual test cases or test scripts.
Output scopes, methodologies, environments, tools, entry/exit criteria, and risk mitigation.

NO GENERIC ADVICE: Do not output statements like "ensure the login page works."
Instead: "Validate JWT token expiration handling and rate-limiting on the /api/v1/auth
endpoint using boundary value analysis per ISTQB Advanced Test Analyst 3.2.1."

NO HALLUCINATIONS: Do not invent endpoints, features, UI elements, or standard
references not present in <user_context> or <retrieved_standards>.

TRACEABILITY: Every testing recommendation MUST cite the specific standard and
clause from <retrieved_standards> that justifies its inclusion.

RISK-BASED PRIORITIZATION: Order testing recommendations by risk severity.
Critical-risk items first, low-risk items last.

TONE: Objective, technical, declarative. No conversational filler, hedging, or
subjective qualifiers ("might," "could potentially," "it would be advisable to").
</constraints>

<output_format_questions>
Output a JSON array of targeted questions. Each question must:
- Identify which standard or quality attribute requires the missing information
- Be specific enough that a Product Owner can answer in 1-2 sentences
- Not ask for information already present in <user_context>

Format: [
  {"standard": "ISO 25010 - Performance Efficiency", "question": "What is the expected peak concurrent user count?"},
  {"standard": "OWASP ASVS", "question": "Does the application handle PII requiring ASVS Level 2 or 3?"}
]
</output_format_questions>

<output_format_plan>
Follow the structure defined in <output_template> exactly.
All output in strict Markdown with hierarchical headings.
</output_format_plan>
```

### 4.3 Domain-Adaptive Output Templates

The output template is selected based on the user's domain configuration. Each template extends a common base:

**Base Template (all domains):**
```
# 1. System Under Test (SUT) Profile
# 2. Strategic Risk Assessment
# 3. Test Scope & Quality Objectives (ISO 25010 mapping)
# 4. Test Strategy & Methodology (ISO 29119 / ISTQB)
  ## 4.1 Functional Test Approach (with specific module targets)
  ## 4.2 Non-Functional Requirements Strategy
  ## 4.3 Security & Compliance Strategy (OWASP / domain-specific)
# 5. Entry & Exit Criteria (measurable metrics)
# 6. Environment & Tooling Requirements
# 7. Risk Mitigation & Contingency
```

**Domain Extensions:**

| Domain | Additional Sections |
|--------|-------------------|
| Medical Devices | + Verification & Validation Evidence Matrix, + Regulatory Submission Artifacts (IEC 62304), + Risk Class Justification |
| Automotive | + ASIL Decomposition & Coverage Metrics, + ASPICE Process Compliance Map, + SOTIF Analysis |
| Aerospace | + DAL-Specific Verification Objectives, + Tool Qualification Requirements, + Certification Authority Liaison Plan |
| Financial | + Audit Trail & Logging Requirements, + Transaction Integrity Strategy, + PCI-DSS Control Mapping |
| Railway | + SSIL Coverage Requirements, + RAMS Integration, + Formal Methods Applicability |
| Nuclear | + Deterministic Testing Approach, + Category A Function Isolation, + Regulatory Authority Engagement |
| Gambling | + RNG Certification Strategy, + Jurisdictional Compliance Matrix, + KYC/AML Test Approach |
| Government | + FedRAMP Control Mapping, + Authorization Evidence Package, + Continuous Monitoring Strategy |

---

## 5. User-Facing Features

### 5.1 Domain Configuration Wizard (Step 2)

After uploading a PRD or linking a repo, the user is presented with a configuration interface:

**Primary domain selector:** Medical, Automotive, Aerospace, Railway, Nuclear, Financial, Telecom, Embedded/IoT, Gaming/Gambling, Government, General Software, Custom

**Conditional fields (appear based on domain):**
- Safety integrity level: SIL (1-4), ASIL (A-D), SSIL (0-4), DAL (A-E) — selector adapts to domain
- Regulatory frameworks: multi-select from domain-relevant standards
- Deployment jurisdictions: multi-select (triggers GDPR, HIPAA, CCPA, regional gambling law, etc.)
- Hardware constraints: free-text (for embedded systems — memory limits, CPU, real-time requirements)
- Deployment environment: cloud/on-premise/hybrid/edge
- Data classification: public / internal / confidential / restricted

**AI-assisted suggestions:** After the user uploads a PRD, the Profiler Agent runs a quick scan and pre-fills suggested values. The user confirms or overrides. This reduces friction while ensuring accuracy.

### 5.2 Iterative Q&A Interface

When the system identifies gaps, it presents questions in a chat-like interface. Each question includes:
- The standard that requires the missing information (e.g., "ISO 25010 — Performance Efficiency")
- The specific question
- An example of a sufficient answer
- A "Skip" option (the strategy will note this as an acknowledged gap)

The number of questions is not artificially capped. A simple web app PRD might generate 2-3 questions. An ASIL-D automotive ECU PRD might generate 12-15.

### 5.3 Strategy Viewer

The generated strategy is rendered as structured Markdown in the UI with:
- Collapsible sections
- Standard citation links (click a citation to see the full standard text from the Vector DB)
- Confidence indicators on each section (based on how much source material the Critic Agent verified)
- A "Validation Report" sidebar showing what the Critic Agent checked and flagged

### 5.4 Export

Formats: PDF (professional layout), Word (.docx), Markdown, Jira (create epic with linked stories per test scope area), Confluence (structured page)

### 5.5 Project Dashboard

- List of past projects with generation history
- Re-run strategy with updated PRD (diff view showing what changed)
- Team workspace isolation (User A cannot see User B's projects)

---

## 6. Business Model

### 6.1 Pricing

| Tier | Price | Target | Included |
|------|-------|--------|----------|
| **Free** | $0 | Solo QA, evaluators | 3 strategy generations/month (fast model only), General Software domain only, PDF/Markdown export |
| **Pro** | $39/user/month | Startups, mid-size QA teams | 50 generations/month (primary model), all domains, Git repo ingestion, all export formats, Jira integration |
| **Enterprise** | $99+/user/month | Large orgs, regulated industries | Unlimited generations, custom standards upload (own internal QA standards → Vector DB), SSO/SAML, dedicated support, model provider selection, on-premise deployment option |

### 6.2 Unit Economics

- LLM cost per strategy generation: <$0.50 (4-agent pipeline, primary model for Architect only)
- Fixed infrastructure: <$200/month at launch
- Variable AI cost per active user: <$10/month (accounting for iterative Q&A and validation)
- Target gross margin at Pro tier: >85%

### 6.3 Go-to-Market

"Trojan Horse" strategy: The Free tier allows a QA engineer to generate one genuinely impressive, standards-compliant Test Strategy in under 5 minutes. When they show that output to their Engineering Manager, the $39/month expense is approved immediately because it replaces hours of manual work. Enterprise sales target regulated industries where standards compliance is a hard requirement, not a nice-to-have.

---

## 7. Testing the App Itself

### 7.1 AI-Specific Testing

- **RAG retrieval accuracy:** Does the Researcher Agent retrieve the correct standard sections for a given tech stack and domain?
- **Hallucination testing:** Does the Architect Agent invent features, endpoints, or standard references not in the input?
- **Citation verification accuracy:** Does the Critic Agent correctly identify fabricated vs. real standard references?
- **Prompt injection resilience:** Can a malicious PRD cause the system to ignore its instructions or leak the system prompt?
- **Non-determinism tolerance:** Run the same input 10 times — is the structural quality and standards coverage consistent?
- **Token limit handling:** What happens when a Git repo exceeds the context window? Graceful degradation or crash?

### 7.2 Functional Testing

- Input parsing across formats (PDF, Markdown, Word, plain text)
- Git repo ingestion via GitHub, GitLab, Bitbucket APIs
- Domain configuration wizard behavior (conditional fields, pre-fill suggestions)
- Iterative Q&A (context retention across turns, follow-up question logic)
- Export fidelity (PDF layout, Word formatting, Jira ticket structure, Confluence page)
- User management and workspace isolation
- Project history and re-run with updated PRD

### 7.3 Non-Functional Testing

- Concurrent generation load (multiple users generating strategies simultaneously)
- Latency management (LLM calls take 10-60 seconds; UI must stream or show progress)
- Cross-browser compatibility (Chrome, Firefox, Safari, Edge)
- Mobile viewport usability (primary use is desktop but must not break on mobile)

### 7.4 Security Testing

- Data privacy: uploaded PRDs and source code are proprietary — must not be stored beyond session or used for model training
- Broken access control: users cannot access other users' projects
- Input sanitization: uploaded files cannot execute malicious payloads
- API rate limiting: prevent abuse and cost overruns
- Auth token security: JWT expiration, refresh flow, CSRF protection

### 7.5 Integration & E2E Testing

- LLM provider failover: what happens when Claude API is down? Does fallback to secondary provider work?
- Vector DB availability: degraded mode if standards DB is unreachable?
- End-to-end user journeys: upload → configure → Q&A → generate → validate → export

---

## 8. Benchmarking Strategy

### 8.1 Benchmark Suite

The AI core quality is validated against a suite of 8 test scenarios, each testing a different capability:

| # | Scenario | Tests | Pass Criteria |
|---|----------|-------|---------------|
| 1 | **HealthVault** (medical prescription photo app, React Native/Node.js/MongoDB, EU+US launch, PRD only asks for "functional testing of upload button") | Risk sensitivity, gap detection | AI MUST flag HIPAA/GDPR risk, require OWASP ASVS Level 2+, STOP and ask compliance questions |
| 2 | **Automotive ECU** (ASIL-B vs ASIL-D requirements in same system) | Safety integrity differentiation | AI correctly applies different coverage metrics to different ASIL levels |
| 3 | **Self-contradicting PRD** (states "no user data stored" but describes user profile features) | Contradiction detection | AI flags the contradiction and asks for clarification |
| 4 | **Microservices e-commerce platform** (12 services, event-driven, multi-DB) | Architectural complexity handling | AI identifies integration contract testing, event schema validation, distributed tracing needs |
| 5 | **Financial trading platform** (no rollback strategy mentioned) | Critical gap identification | AI flags missing rollback/disaster recovery as strategy-blocking gap |
| 6 | **Embedded sensor device** (32KB RAM, RTOS, battery-powered) | Hardware constraint awareness | AI addresses resource-constrained testing, real-time requirements, power consumption |
| 7 | **Multi-jurisdiction gambling platform** (UK + Malta + Netherlands) | Regulatory complexity | AI generates jurisdiction-specific compliance matrices, flags conflicting requirements |
| 8 | **Minimal PRD** ("We're building a chat app. It should be fast.") | Refusal to generate from insufficient context | AI MUST refuse to generate strategy, produce substantial question set |

### 8.2 Reference Projects

- **Mattermost** (open-source Slack alternative): Compare AI-generated strategy against Mattermost's actual public test guidelines and E2E test scripts
- **OWASP Juice Shop** (intentionally vulnerable web app): Compare AI-generated security strategy against professional penetration test reports written by security firms

### 8.3 Evaluation Metrics

| Category | Metric | Measurement |
|----------|--------|-------------|
| Risk Profiling | SUT Sensitivity Identification | Does AI correctly categorize the application's risk level? |
| Scoping Accuracy | Requirement-to-Test Mapping | Does AI suggest appropriate depth and types of testing? |
| Standards Traceability | Citation Accuracy | % of standard citations that are verified real references |
| Domain Compliance | Standards Coverage | % of applicable domain standards that are addressed |
| Gap Detection | False Negative Rate | % of known gaps that the AI fails to identify |
| Output Quality | Structural Completeness | % of template sections with substantive (non-filler) content |
| Consistency | Cross-Run Variance | How stable is quality across 10 identical runs? |

---

## 9. Development Roadmap

### Phase 1: AI Core PoC (Current)
- Implement Agent 3 (Architect) with full system prompt
- Implement Agent 4 (Critic) with citation verification
- Populate Vector DB with core standards (ISO 29119, ISO 25010, ISTQB Foundation, OWASP Top 10 + ASVS)
- Run benchmark suite scenarios 1, 3, and 8 (gap detection, contradiction detection, minimal PRD)
- Validate model-agnostic abstraction layer works with Claude and at least one alternative

### Phase 2: Full Agent Pipeline
- Implement Agent 1 (Profiler) and Agent 2 (Researcher)
- Wire all four agents into the orchestrator
- Add domain-specific standards to Vector DB (medical, automotive, aerospace — highest Enterprise value)
- Run full benchmark suite
- Implement domain configuration logic and template selection

### Phase 3: Web Application
- Build frontend SPA (upload, domain config wizard, Q&A chat, strategy viewer, export)
- Build backend API (FastAPI, auth, project management)
- Wire frontend to agent pipeline
- Implement Git repo ingestion
- Implement export engines (PDF, Word, Jira, Confluence)

### Phase 4: Testing & Refinement
- Dogfood: use the app to generate its own test strategy
- Run full test suite (AI-specific, functional, NFR, security, integration)
- Prompt refinement based on benchmark results
- Load testing and latency optimization

### Phase 5: Launch
- Deploy frontend (Vercel) and backend (Cloud Run/Render)
- Free tier launch
- Pro tier launch
- Enterprise tier (custom standards upload, SSO, model provider selection)

---

## 10. Open Questions

| # | Question | Impact | Priority |
|---|----------|--------|----------|
| 1 | Which Vector DB? Pinecone vs Qdrant vs pgvector | Architecture, cost, performance | High — blocks Phase 1 |
| 2 | Legal: Can we embed ISO/ISTQB content in a commercial Vector DB? | Business viability for standards corpus | High — blocks Phase 1 |
| 3 | RAG vs full context window for standards | Architecture simplification vs quality trade-off | High — needs empirical testing |
| 4 | Git repo parsing: which files to extract, how to summarize large codebases? | Input quality for code-based analysis | Medium — Phase 2 |
| 5 | Multi-language/polyglot repo handling | Profiler Agent accuracy | Medium — Phase 2 |
| 6 | Standards versioning: how to handle transition periods? | Strategy accuracy during standard transitions | Medium — Phase 2 |
| 7 | Domain config: AI-assisted auto-detect vs purely user-selected? | UX friction vs accuracy trade-off | Medium — Phase 3 |
| 8 | Critic Agent implementation: same model with different prompt, or different model? | Cost vs validation quality | High — Phase 1 |
| 9 | Enterprise custom standards: upload format and chunking approach? | Enterprise tier feasibility | Low — Phase 5 |
| 10 | Multi-domain products: how to merge overlapping standard requirements? | Strategy coherence for complex products | Medium — Phase 2 |
