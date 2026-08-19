# Composio AI Product Operations — Research Agent

> **"I built the workflow. The agent did the research. I checked where it could fail. Humans handled the cases that automation could not confidently resolve."**

**Author:** Shaik Ashik ([smdashik2516@gmail.com](mailto:smdashik2516@gmail.com))  
**Repository:** [https://github.com/ashik-2516/Composio-product-operations-assignment](https://github.com/ashik-2516/Composio-product-operations-assignment)  
**Live Case Study & Dashboard:** Open [`index.html`](index.html) in any web browser.

---

## How to Run the Research Agent

### Prerequisites
- **Python 3.10+** (The core workflow uses the Python Standard Library for zero-dependency portability).

### 1. Installation
```bash
# Clone the repository
git clone https://github.com/ashik-2516/Composio-product-operations-assignment.git
cd Composio-product-operations-assignment

# (Optional) Install development dependencies
pip install -r requirements.txt
```

### 2. Audit a Single Application via CLI
```bash
# Run audit for an easy-win self-serve app (Salesforce)
python agent/run.py --app "Salesforce"

# Run audit for an enterprise admin-gated app (DealCloud)
python agent/run.py --app "DealCloud"

# Run audit for a marketing developer token-gated app (Google Ads)
python agent/run.py --app "Google Ads"

# Run audit for a local CLI binary (Sherlock / Mermaid CLI)
python agent/run.py --app "Sherlock"
```

### 3. Audit an Entire Software Category
```bash
# Audit all 10 apps in CRM and Sales
python agent/run.py --category "CRM and Sales"

# Audit Developer Platforms & Cloud Infra
python agent/run.py --category "Developer Platforms, Cloud and Infrastructure"
```

### 4. Run the Full Multi-Pass Pipeline & Rebuild All Deliverables
```bash
# Executes Pass 1 extraction, Pass 2 verification loop, computes metrics, and rebuilds index.html:
python scripts/run_research_agent.py
```

### 5. Validate Schema & Evidence Integrity
```bash
# Validates that all 100 JSON records conform strictly to the required schema:
python scripts/validate_schema.py
```

### 6. View the Interactive Dashboard
Launch a local web server:
```bash
python -m http.server 8000
```
Open **[http://localhost:8000](http://localhost:8000)** in your browser to explore:
- Interactive **Chart.js** visualizations.
- Searchable & filterable **100-app integration matrix**.
- Slide-out **primary evidence drawer** with direct documentation links.
- Interactive **in-browser CLI simulator**.

---

## Repository Structure

```
.
|-- index.html                   # Interactive Case Study & Research Dashboard
|-- README.md                    # Project execution guide
|-- requirements.txt             # Python dependencies
|-- .env.example                 # Environment variable template
|-- .gitignore                   # Git ignore patterns
|
|-- agent/                       # Core Research Agent Codebase
|   |-- run.py                   # Interactive CLI runner (--app, --category, --verify, --all)
|   |-- research_agent.py        # Main ComposioResearchAgent orchestrator class
|   |-- tools.py                 # DocSearchTool, WebScraperTool, and MCPRegistryTool
|   |-- browser_verifier.py      # Live HTTP portal check & heuristic engine
|   `-- config.py                # Agent configuration & logging
|
|-- data/                        # Datasets & Outputs
|   |-- results_final.json       # 100 verified structured records with primary evidence
|   |-- results_pass1.json       # Raw extraction benchmark before calibration
|   |-- metrics.json             # Global statistical metrics & priority distributions
|   |-- verification_queue.json  # 12 representative human verification checks
|   |-- dataset.csv              # Full tabular CSV export
|   `-- apps_input.json          # Input seed list of 100 apps across 10 categories
|
|-- scripts/                     # Pipeline & Dataset Modules
|   |-- run_research_agent.py    # Main pipeline runner (executes audit, verification & assembly)
|   |-- validate_schema.py       # JSON schema validator
|   |-- assemble_html.py         # Dashboard assembler
|   |-- html_header.py           # Dashboard styling & Tailwind CDN
|   |-- html_nav_hero.py         # Navigation, Hero section & KPI cards
|   |-- html_sections.py         # 13 narrative sections, matrix table, and charts
|   |-- html_footer_script.py    # Drawer JS, Chart.js initializer & terminal simulator
|   |-- cat1_crm.py to cat10_ai_media.py # 10 category modules (100 grounded apps)
|   `-- compute_metrics.py       # Metrics calculator & CSV exporter
|
`-- verification/                # Audit & Decision Logs
    |-- claim_audit.csv          # 342 claim-level facts audited
    `-- human_decisions.csv      # Human review decisions log
```

---

## Output Schema

Every record in `data/results_final.json` strictly adheres to the required schema:

```json
{
  "app": "Stripe",
  "category": "Finance, Billing and Operations",
  "description": "Financial infrastructure platform for payment processing, subscription billing, payouts, and financial services.",
  "auth_methods": [
    "API Key (Secret Key)",
    "OAuth 2.0 (Stripe Connect)",
    "Restricted API Key"
  ],
  "credential_access": "SELF_SERVE",
  "free_or_trial_access": "Completely free test mode sandbox with instant API key access; no credit card required to develop.",
  "api": {
    "availability": "REST",
    "type": ["REST"],
    "breadth": "BROAD",
    "documentation_quality": "HIGH"
  },
  "mcp": {
    "status": "OFFICIAL_MCP_SUPPORTED",
    "official": "Vendor-supported",
    "url": "https://github.com/stripe/agent-toolkit"
  },
  "buildability": "HIGH",
  "primary_blocker": "None",
  "secondary_blockers": [
    "Idempotency-Key header requirement for mutate safety",
    "PCI compliance rules for raw card processing"
  ],
  "evidence": [
    {
      "claim": "Stripe authenticates API requests using Secret API Keys passed in Authorization: Bearer header and OAuth 2.0.",
      "url": "https://docs.stripe.com/api/authentication",
      "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
      "evidence_summary": "Stripe Docs specify Bearer token header format, test vs live keys, and restricted key permissions."
    }
  ],
  "confidence": 1.0,
  "human_verification_required": false,
  "uncertainties": [],
  "research_notes": [
    "The gold standard of API design; official Stripe Agent Toolkit and MCP server available."
  ],
  "id": 81
}
```
