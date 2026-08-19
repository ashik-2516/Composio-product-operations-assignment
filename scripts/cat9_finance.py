# scripts/cat9_finance.py
# Category 9: Finance and Fintech (Apps 81 - 90)

def get_cat9_apps():
    return [
        {
            "app": "Stripe",
            "category": "Finance and Fintech",
            "description": "Financial infrastructure platform for payment processing, subscription billing, payouts, and financial services.",
            "auth_methods": ["API Key (Secret Key)", "OAuth 2.0 (Stripe Connect)", "Restricted API Key"],
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
            "secondary_blockers": ["Idempotency-Key header requirement for mutate safety", "PCI compliance rules for raw card processing"],
            "evidence": [
                {
                    "claim": "Stripe authenticates API requests using Secret API Keys passed in Authorization: Bearer header and OAuth 2.0.",
                    "url": "https://docs.stripe.com/api/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Stripe Docs specify Bearer token header format, test vs live keys, and restricted key permissions."
                },
                {
                    "claim": "Developers can sign up for free and generate test keys immediately in Stripe Dashboard.",
                    "url": "https://dashboard.stripe.com/test/apikeys",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Dashboard provides instant test mode keys (sk_test_...) without business verification."
                }
            ],
            "confidence": 1.0,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["The gold standard of API design; official Stripe Agent Toolkit and MCP server available."]
        },
        {
            "app": "Plaid",
            "category": "Finance and Fintech",
            "description": "Open banking financial network connecting bank accounts to consumer fintech applications.",
            "auth_methods": ["API Key (Client ID & Secret Headers)", "Bearer Token (Link Token)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Sandbox environment with 100 free test items upon signup.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/plaid-mcp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Plaid Link UI workflow required for frontend bank credential handoff"],
            "evidence": [
                {
                    "claim": "Plaid API authenticates using PLAID-CLIENT-ID and PLAID-SECRET headers or JSON request body fields.",
                    "url": "https://plaid.com/docs/api/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Plaid API documentation details header authentication and Sandbox environment keys."
                },
                {
                    "claim": "Developers can sign up for free and access the Sandbox environment immediately.",
                    "url": "https://dashboard.plaid.com/signup",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Dashboard grants instant Sandbox and Development API keys without sales calls."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Highly structured REST API for account verification, balances, and transactions."]
        },
        {
            "app": "Binance",
            "category": "Finance and Fintech",
            "description": "Global cryptocurrency exchange platform for spot, futures, margin trading, and market data.",
            "auth_methods": ["API Key", "HMAC-SHA256 Signature", "RSA Key", "Ed25519"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free account creation with Spot Testnet and public market data APIs requiring no auth.",
            "api": {
                "availability": "REST",
                "type": ["REST", "WebSocket Streams"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/binance/binance-mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Cryptographic HMAC timestamped query signature requirement (X-MBX-APIKEY + signature)"],
            "evidence": [
                {
                    "claim": "Binance Spot API authenticates using X-MBX-APIKEY header and HMAC-SHA256 / RSA cryptographic signatures.",
                    "url": "https://binance-docs.github.io/apidocs/spot/en/#general-api-information",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Binance API documentation specifies endpoint security types (TRADE, USER_DATA) and signature generation."
                },
                {
                    "claim": "Developers can create API keys self-serve in Binance account settings or use the free Spot Testnet.",
                    "url": "https://testnet.binance.vision/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Binance provides dedicated Testnet with instant API keys for trading bot testing."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["High throughput REST and WebSocket endpoints; signature hashing required for state-changing orders."]
        },
        {
            "app": "Paygent Connect",
            "category": "Finance and Fintech",
            "description": "Payment gateway and merchant transaction orchestration platform (often deployed with NMI integration).",
            "auth_methods": ["API Key", "Basic Authentication (Merchant ID / Secret)"],
            "credential_access": "ADMIN_APPROVAL",
            "free_or_trial_access": "Merchant contract / payment processor underwriting required; no public self-serve sandbox.",
            "api": {
                "availability": "REST",
                "type": ["REST", "NMI Gateway Direct Post / Three-Step"],
                "breadth": "MEDIUM",
                "documentation_quality": "MEDIUM"
            },
            "mcp": {
                "status": "NO_MCP_FOUND",
                "official": "None",
                "url": ""
            },
            "buildability": "MEDIUM",
            "primary_blocker": "Merchant underwriting and account approval requirement",
            "secondary_blockers": ["Legacy parameter-based transaction protocols"],
            "evidence": [
                {
                    "claim": "Paygent Connect / NMI-powered gateways use Merchant Security Keys or HTTP Basic Authentication.",
                    "url": "https://www.nmi.com/docs/api/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Gateway documentation specifies security key parameter (security_key) or Basic Auth for Direct Post transactions."
                },
                {
                    "claim": "Merchant account access requires underwriting and administrative provisioning.",
                    "url": "https://www.paygent.co.jp/en/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Payment processor requires commercial merchant agreement for production gateway credentials."
                }
            ],
            "confidence": 0.90,
            "human_verification_required": True,
            "uncertainties": ["Exact developer sandbox availability without active ISO/reseller sponsorship"],
            "research_notes": ["Traditional payment gateway; requires merchant underwriting to obtain live processing keys."]
        },
        {
            "app": "iPayX",
            "category": "Finance and Fintech",
            "description": "AI-driven financial audit and payment analysis platform for foreign exchange and cross-border transactions.",
            "auth_methods": ["Bearer Token", "API Key"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier with 10 audits per day per API key; paid tier for unlimited audits.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "NO_MCP_FOUND",
                "official": "None",
                "url": ""
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Daily audit limit on free tier"],
            "evidence": [
                {
                    "claim": "iPayX API authenticates using Bearer API keys in Authorization: Bearer <ipx_key> header.",
                    "url": "https://ipayx.ai/docs",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official iPayX documentation specifies Bearer token format (ipx_live_ / ipx_test_) and audit endpoints."
                },
                {
                    "claim": "Developers can generate API keys self-serve in the iPayX dashboard with a free 10 audits/day tier.",
                    "url": "https://ipayx.ai/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation confirms self-serve key generation and free daily audit allocation."
                }
            ],
            "confidence": 0.96,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Focused fintech audit API; simple Bearer token integration."]
        },
        {
            "app": "QuickBooks",
            "category": "Finance and Fintech",
            "description": "Small business accounting software for invoicing, expense tracking, payroll, and bookkeeping.",
            "auth_methods": ["OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Intuit Developer account with permanent Sandbox company environments.",
            "api": {
                "availability": "REST",
                "type": ["REST (QuickBooks Online Accounting API v3)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/quickbooks-mcp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["OAuth 2.0 token refresh required every 60 minutes", "App Assessment Questionnaire for production keys"],
            "evidence": [
                {
                    "claim": "QuickBooks Online API uses OAuth 2.0 with Authorization Code flow and Bearer tokens.",
                    "url": "https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Intuit Developer documentation outlines OAuth 2.0 scopes (com.intuit.quickbooks.accounting) and Bearer token headers."
                },
                {
                    "claim": "Developers can create free Intuit Developer accounts and sandbox companies immediately.",
                    "url": "https://developer.intuit.com/app/developer/qbo/docs/develop/sandboxes",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation details self-serve sandbox setup with pre-populated company data."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Comprehensive accounting CRUD covering invoices, customers, vendors, accounts, and payments."]
        },
        {
            "app": "Xero",
            "category": "Finance and Fintech",
            "description": "Cloud accounting platform for small businesses, accountants, and bookkeepers to manage finances.",
            "auth_methods": ["OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Xero Developer account with Demo Company sandboxes.",
            "api": {
                "availability": "REST",
                "type": ["REST (Accounting API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/xero-mcp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["xero-tenant-id header required in all API calls", "Short access token lifespan (30 min)"],
            "evidence": [
                {
                    "claim": "Xero API authenticates using OAuth 2.0 Authorization Code flow with PKCE or Client Credentials.",
                    "url": "https://developer.xero.com/documentation/guides/oauth2/overview/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Xero Developer documentation details OAuth 2.0 Bearer tokens and xero-tenant-id header routing."
                },
                {
                    "claim": "Developers can register apps for free in Xero Developer Portal with access to Demo Company.",
                    "url": "https://developer.xero.com/app/manage",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Self-serve developer portal allows instant app creation and sandbox connections."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["High quality API docs with active OpenAPI 3.0 support and certified SDKs."]
        },
        {
            "app": "Brex",
            "category": "Finance and Fintech",
            "description": "Corporate card, spend management, business banking, and travel platform for growing companies.",
            "auth_methods": ["User Token (Bearer)", "Service Account Token", "OAuth 2.0"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "Requires active Brex customer account (admin access) to generate developer tokens.",
            "api": {
                "availability": "REST",
                "type": ["REST (v1 API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/brex-mcp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "Brex customer account / admin access required",
            "secondary_blockers": ["User tokens tied to admin employee account status"],
            "evidence": [
                {
                    "claim": "Brex API authenticates using User Tokens or OAuth 2.0 Bearer tokens in Authorization header.",
                    "url": "https://developer.brex.com/docs/authentication/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Brex Developer documentation outlines User Tokens, OAuth 2.0 flows, and Idempotency-Key headers."
                },
                {
                    "claim": "API tokens can be generated self-serve under Company Settings > Developer in Brex dashboard.",
                    "url": "https://developer.brex.com/docs/quickstart/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Quickstart guide details token generation inside active customer accounts."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Modern REST API with OpenAPI specifications covering expenses, payments, budgets, and transactions."]
        },
        {
            "app": "Ramp",
            "category": "Finance and Fintech",
            "description": "Corporate card and financial automation platform designed to control spend and automate accounting.",
            "auth_methods": ["OAuth 2.0", "API Key (Client ID / Secret)"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "Requires active Ramp customer organization to register developer applications.",
            "api": {
                "availability": "REST",
                "type": ["REST (Developer API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/ramp-mcp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "Ramp customer organization / admin access required",
            "secondary_blockers": ["Granular OAuth permission scopes (cards:write, transactions:read)"],
            "evidence": [
                {
                    "claim": "Ramp Developer API authenticates using OAuth 2.0 Bearer tokens generated via Client ID and Secret.",
                    "url": "https://docs.ramp.com/developer-api/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Ramp documentation specifies OAuth 2.0 authorization code and client credentials token endpoints."
                },
                {
                    "claim": "Developer apps can be created under Company Settings > Developer in Ramp dashboard.",
                    "url": "https://docs.ramp.com/developer-api/getting-started",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Getting started guide outlines self-serve app creation for organization administrators."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Very clean developer portal with REST endpoints for virtual cards, limits, and transactions."]
        },
        {
            "app": "PitchBook",
            "category": "Finance and Fintech",
            "description": "Financial market research database covering private capital, venture capital, PE, and M&A transactions.",
            "auth_methods": ["API Key", "Basic Authentication", "Bearer Token"],
            "credential_access": "PARTNER_OR_SALES_GATED",
            "free_or_trial_access": "Enterprise direct sales contract required ($20,000+/year); no public free tier or self-serve sandbox.",
            "api": {
                "availability": "REST",
                "type": ["REST (PitchBook Direct Data API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "NO_MCP_FOUND",
                "official": "None",
                "url": ""
            },
            "buildability": "LOW",
            "primary_blocker": "Enterprise direct sales contract gate ($20k+/yr paywall)",
            "secondary_blockers": ["Strict commercial licensing forbidding unauthorized scraping or third-party syndication"],
            "evidence": [
                {
                    "claim": "PitchBook provides Direct Data API access for enterprise customers under custom licensing agreements.",
                    "url": "https://pitchbook.com/products/data/direct-data",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "PitchBook product page details Direct Data API, feed delivery formats, and enterprise sales contact requirements."
                },
                {
                    "claim": "Access requires commercial enterprise sales contract; no self-serve developer portal exists.",
                    "url": "https://pitchbook.com/request-a-free-trial",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Trial requests require enterprise corporate email and direct contact with sales team."
                }
            ],
            "confidence": 0.96,
            "human_verification_required": True,
            "uncertainties": ["Custom REST endpoint schemas per bespoke enterprise feed contract"],
            "research_notes": ["Heavily gated financial database; buildable only for licensed enterprise customers."]
        }
    ]
