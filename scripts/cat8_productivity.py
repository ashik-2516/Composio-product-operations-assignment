# scripts/cat8_productivity.py
# Category 8: Productivity and Project Management (Apps 71 - 80)

def get_cat8_apps():
    return [
        {
            "app": "Notion",
            "category": "Productivity and Project Management",
            "description": "Connected workspace for notes, documents, wikis, databases, and collaborative project management.",
            "auth_methods": ["Internal Integration Secret (Bearer Token)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier with unlimited internal integrations and full REST API access.",
            "api": {
                "availability": "REST",
                "type": ["REST (v1 API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/modelcontextprotocol/servers/tree/main/src/notion"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Pages/databases must be explicitly shared with the internal integration", "Notion-Version header requirement"],
            "evidence": [
                {
                    "claim": "Notion API authenticates using Bearer tokens in Authorization header with Notion-Version header.",
                    "url": "https://developers.notion.com/docs/authorization",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Notion Developer documentation details Internal Integration Secrets and OAuth 2.0 authorization code flows."
                },
                {
                    "claim": "Internal integrations and tokens can be created self-serve for free at notion.so/my-integrations.",
                    "url": "https://www.notion.so/profile/integrations",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Notion integrations dashboard enables instant secret generation without fees or review."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["One of the most widely used tool integrations in AI agent workflows."]
        },
        {
            "app": "Airtable",
            "category": "Productivity and Project Management",
            "description": "Low-code platform for building relational database applications, collaborative tables, and workflows.",
            "auth_methods": ["Personal Access Token (PAT)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier with full REST API and Personal Access Token support.",
            "api": {
                "availability": "REST",
                "type": ["REST (v0 Web API)", "Metadata API"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/modelcontextprotocol/servers/tree/main/src/airtable"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limit of 5 requests per second per base"],
            "evidence": [
                {
                    "claim": "Airtable Web API authenticates using Personal Access Tokens (Bearer) and OAuth 2.0.",
                    "url": "https://airtable.com/developers/web/api/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Airtable documentation details Bearer token authentication in Authorization header and granular PAT scopes."
                },
                {
                    "claim": "Personal Access Tokens can be created self-serve in Airtable Developer Hub.",
                    "url": "https://airtable.com/create/tokens",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Developer Hub allows instant PAT generation with base-specific permissions."
                }
            ],
            "confidence": 1.0,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Interactive auto-generated documentation per base makes tool schemas trivial to derive."]
        },
        {
            "app": "Linear",
            "category": "Productivity and Project Management",
            "description": "Modern issue tracking and product project management tool built for high-performance software teams.",
            "auth_methods": ["Personal API Key (Bearer)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free plan with full GraphQL API and Personal API Key creation.",
            "api": {
                "availability": "GRAPHQL",
                "type": ["GraphQL"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/linear/mcp-server-linear"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["GraphQL query syntax required for API calls"],
            "evidence": [
                {
                    "claim": "Linear provides a GraphQL API authenticated using Personal API Keys in Authorization header or OAuth 2.0.",
                    "url": "https://developers.linear.app/docs/graphql/working-with-the-graphql-api#authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Linear developer documentation specifies GraphQL endpoint https://api.linear.app/graphql and Bearer auth."
                },
                {
                    "claim": "Personal API keys are created self-serve in Account Settings > Security & Access.",
                    "url": "https://linear.app/settings/api",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Linear settings provide instant API key creation and OAuth application registration."
                }
            ],
            "confidence": 1.0,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Gold standard GraphQL API with TypeScript SDK and official MCP support."]
        },
        {
            "app": "Jira",
            "category": "Productivity and Project Management",
            "description": "Agile project tracking, issue management, and workflow software for software development teams.",
            "auth_methods": ["API Token (Basic Auth)", "OAuth 2.0 (3LO)", "Atlassian Connect JWT"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Cloud plan (up to 10 users) with full REST API v3 access.",
            "api": {
                "availability": "REST",
                "type": ["REST (v3 API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/atlassian/mcp-server-jira"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Complex permission schemes and JQL (Jira Query Language) syntax"],
            "evidence": [
                {
                    "claim": "Jira Cloud REST API authenticates using API Tokens via HTTP Basic Auth (email:api_token) or OAuth 2.0 (3LO).",
                    "url": "https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Atlassian developer documentation outlines basic authentication with API tokens and OAuth 2.0 3LO flows."
                },
                {
                    "claim": "API tokens can be generated self-serve for free in Atlassian Account Security.",
                    "url": "https://id.atlassian.com/manage-profile/security/api-tokens",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Atlassian Account portal provides instant token generation for Jira and Confluence."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Ubiquitous enterprise issue tracker; complete REST v3 coverage."]
        },
        {
            "app": "Asana",
            "category": "Productivity and Project Management",
            "description": "Work and project management platform designed to help teams organize, track, and manage work.",
            "auth_methods": ["Personal Access Token (PAT)", "OAuth 2.0", "Bearer Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier (up to 10 team members) with full API access.",
            "api": {
                "availability": "REST",
                "type": ["REST (v1 API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/asana-mcp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limit of 150 requests/minute per token"],
            "evidence": [
                {
                    "claim": "Asana REST API authenticates using Personal Access Tokens (PAT) in Authorization: Bearer header and OAuth 2.0.",
                    "url": "https://developers.asana.com/docs/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Asana Developer documentation details Bearer token authentication and OAuth 2.0 authorization code flows."
                },
                {
                    "claim": "Personal Access Tokens can be generated self-serve in Developer App Console.",
                    "url": "https://app.asana.com/0/developer-console",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Developer console allows immediate PAT generation for personal scripts and applications."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Very clean REST design with consistent data schemas across tasks, projects, and portfolios."]
        },
        {
            "app": "Monday.com",
            "category": "Productivity and Project Management",
            "description": "Work operating system platform for building customizable workflow apps, boards, and project dashboards.",
            "auth_methods": ["API Token (Personal API Token)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free plan (up to 2 seats) or 14-day Pro trial with full GraphQL API access.",
            "api": {
                "availability": "GRAPHQL",
                "type": ["GraphQL (v2 API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/monday-mcp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["GraphQL query complexity complexity budgeting (5,000,000 complexity points/min)"],
            "evidence": [
                {
                    "claim": "Monday.com GraphQL API v2 authenticates using Personal API Tokens in Authorization header or OAuth 2.0.",
                    "url": "https://developer.monday.com/api-reference/docs/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Monday Developer docs detail Authorization: <YOUR_TOKEN> header format and OAuth token lifecycle."
                },
                {
                    "claim": "API tokens can be generated self-serve in User Profile > Developers > Developer.",
                    "url": "https://developer.monday.com/api-reference/docs/authentication#where-to-find-your-token",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation explains self-serve token generation under user profile."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["GraphQL-first API; handles board column values through stringified JSON structures."]
        },
        {
            "app": "ClickUp",
            "category": "Productivity and Project Management",
            "description": "All-in-one productivity platform unifying tasks, docs, chat, goals, and project roadmaps.",
            "auth_methods": ["Personal API Key (pk_)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Forever plan with full REST API access and personal token creation.",
            "api": {
                "availability": "REST",
                "type": ["REST (v2 API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/clickup/mcp-server-clickup"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limits of 100 requests/minute on Free Forever, 1,000 on Enterprise"],
            "evidence": [
                {
                    "claim": "ClickUp API v2 authenticates using personal API keys (pk_) in Authorization header or OAuth 2.0 Bearer tokens.",
                    "url": "https://clickup.com/api/developer-portal/authentication/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "ClickUp Developer Portal details Authorization: pk_... header format and OAuth 2.0 authorization code flow."
                },
                {
                    "claim": "API tokens can be generated self-serve under User Settings > Apps.",
                    "url": "https://clickup.com/api/developer-portal/generate-api-token/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official guide illustrates instant token creation in personal workspace settings."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Broad REST API with extensive CRUD across tasks, lists, spaces, and custom fields."]
        },
        {
            "app": "Coda",
            "category": "Productivity and Project Management",
            "description": "Interactive collaborative document editor that blends text documents with spreadsheets and app formulas.",
            "auth_methods": ["API Token (Bearer)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier with full REST API and API token creation capabilities.",
            "api": {
                "availability": "REST",
                "type": ["REST (v1 API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/coda/mcp-server-coda"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Doc ID and Table ID parameters required in endpoint paths"],
            "evidence": [
                {
                    "claim": "Coda REST API v1 authenticates using API Tokens in Authorization: Bearer <API_KEY> header and OAuth 2.0.",
                    "url": "https://coda.io/developers/apis/v1#section/Authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Coda API documentation details Bearer token authentication and OpenAPI 3.0 specification."
                },
                {
                    "claim": "API tokens can be generated self-serve in Account Settings > API Settings.",
                    "url": "https://coda.io/account",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Coda user settings provide instant API token creation with custom restriction scopes."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Very clean REST API with comprehensive formula, table, and row operations."]
        },
        {
            "app": "Smartsheet",
            "category": "Productivity and Project Management",
            "description": "Enterprise collaborative work management platform using a familiar grid spreadsheet interface.",
            "auth_methods": ["API Access Token (Bearer)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "30-day free trial with full API access.",
            "api": {
                "availability": "REST",
                "type": ["REST (API 2.0)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/smartsheet-mcp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limit of 300 requests/minute"],
            "evidence": [
                {
                    "claim": "Smartsheet API 2.0 authenticates using API Access Tokens in Authorization: Bearer <ACCESS_TOKEN> header and OAuth 2.0.",
                    "url": "https://smartsheet.redoc.ly/#section/Authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Smartsheet Redoc documentation specifies Bearer token authorization and endpoint schemas."
                },
                {
                    "claim": "API access tokens can be generated self-serve under Account > Personal Settings > API Access.",
                    "url": "https://help.smartsheet.com/articles/2482389-generate-api-access-token",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Help center details direct token generation inside any active account."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Complete REST coverage of sheets, rows, columns, reports, and automated workflows."]
        },
        {
            "app": "Harvest",
            "category": "Productivity and Project Management",
            "description": "Time tracking, project expense management, and invoicing software for service businesses.",
            "auth_methods": ["Personal Access Token (Bearer)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free plan (1 seat, 2 projects) or 30-day free trial with full API access.",
            "api": {
                "availability": "REST",
                "type": ["REST (API v2)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/harvest/mcp-server-harvest"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Dual header requirement: Authorization: Bearer + Harvest-Account-Id"],
            "evidence": [
                {
                    "claim": "Harvest API v2 requires Authorization: Bearer <TOKEN> and Harvest-Account-Id: <ACCOUNT_ID> headers.",
                    "url": "https://help.getharvest.com/api-v2/authentication-other-methods/overview/authentication/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Harvest API v2 documentation specifies Bearer token and Account ID headers and OAuth 2.0 endpoints."
                },
                {
                    "claim": "Personal Access Tokens can be created self-serve in Harvest Developer portal.",
                    "url": "https://id.getharvest.com/developers",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Developer portal provides instant creation of personal tokens and OAuth client IDs."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Very clean REST v2 API with time entry, invoice, client, and project management."]
        }
    ]
