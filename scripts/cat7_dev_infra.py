# scripts/cat7_dev_infra.py
# Category 7: Developer, Infra and Data Platforms (Apps 61 - 70)

def get_cat7_apps():
    return [
        {
            "app": "GitHub",
            "category": "Developer, Infra and Data Platforms",
            "description": "Code hosting, Git version control, issue tracking, CI/CD actions, and software collaboration platform.",
            "auth_methods": ["Personal Access Token (PAT)", "OAuth 2.0", "Bearer Token (GitHub App JWT)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free account tier with full API, fine-grained PATs, and GitHub Apps support.",
            "api": {
                "availability": "REST_AND_GRAPHQL",
                "type": ["REST", "GraphQL"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/modelcontextprotocol/servers/tree/main/src/github"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limit of 5,000 requests/hour for authenticated users"],
            "evidence": [
                {
                    "claim": "GitHub REST and GraphQL APIs authenticate using Personal Access Tokens (PAT), OAuth 2.0, and GitHub App tokens.",
                    "url": "https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "GitHub Docs specify Bearer token header format (Authorization: Bearer <TOKEN>) and fine-grained PAT scopes."
                },
                {
                    "claim": "Developers can generate fine-grained Personal Access Tokens self-serve in Settings > Developer settings.",
                    "url": "https://github.com/settings/tokens?type=beta",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "GitHub settings portal provides instant creation of fine-grained tokens with repo-specific permissions."
                }
            ],
            "confidence": 1.0,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["The quintessential developer platform; foundational integration for any coding agent."]
        },
        {
            "app": "Vercel",
            "category": "Developer, Infra and Data Platforms",
            "description": "Frontend cloud platform for static sites, serverless functions, and Next.js web application deployment.",
            "auth_methods": ["Bearer Token (Personal/Team Access Token)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Hobby tier with full REST API access.",
            "api": {
                "availability": "REST",
                "type": ["REST (v9 API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/vercel/mcp-server-vercel"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Team ID query parameter requirement for team-scoped resources"],
            "evidence": [
                {
                    "claim": "Vercel REST API uses Bearer tokens in Authorization header and supports OAuth 2.0 integrations.",
                    "url": "https://vercel.com/docs/rest-api#authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Vercel documentation details Authorization: Bearer <TOKEN> format and teamId query parameter scoping."
                },
                {
                    "claim": "Access tokens are created self-serve under Account Settings > Tokens.",
                    "url": "https://vercel.com/account/tokens",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Vercel dashboard provides instant token creation with custom expiration periods."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Extensive deployment and DNS management capabilities via API."]
        },
        {
            "app": "Netlify",
            "category": "Developer, Infra and Data Platforms",
            "description": "Cloud hosting platform for web developers to build, deploy, and scale web applications and serverless backends.",
            "auth_methods": ["Bearer Token (Personal Access Token)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Starter tier with full API access.",
            "api": {
                "availability": "REST",
                "type": ["REST (OpenAPI v1)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/netlify/mcp-server-netlify"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limit of 500 requests/minute"],
            "evidence": [
                {
                    "claim": "Netlify REST API authenticates using Personal Access Tokens (Bearer) and OAuth 2.0.",
                    "url": "https://docs.netlify.com/api/get-started/#authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Netlify documentation specifies Authorization: Bearer <ACCESS_TOKEN> header and OpenAPI 2.0 definitions."
                },
                {
                    "claim": "Personal access tokens can be generated self-serve in User Settings > Applications.",
                    "url": "https://app.netlify.com/user/applications#personal-access-tokens",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "User dashboard allows immediate token creation for scripts and external tools."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Very clean OpenAPI spec with full control over sites, deploys, DNS, and forms."]
        },
        {
            "app": "Cloudflare",
            "category": "Developer, Infra and Data Platforms",
            "description": "Global cloud network providing DNS, CDN, DDoS protection, edge workers, and AI compute infrastructure.",
            "auth_methods": ["API Token (Bearer)", "API Key (Global API Key)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier with unlimited API token creation and free DNS/Workers usage.",
            "api": {
                "availability": "REST_AND_GRAPHQL",
                "type": ["REST (v4 API)", "GraphQL (Analytics API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/cloudflare/mcp-server-cloudflare"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Granular token permission templates (Zone DNS, Workers, Pages)"],
            "evidence": [
                {
                    "claim": "Cloudflare API v4 authenticates using scoped API Tokens in Authorization: Bearer header.",
                    "url": "https://developers.cloudflare.com/fundamentals/api/get-started/create-token/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Cloudflare Developer docs detail scoped API Token creation with IP filtering and TTLs."
                },
                {
                    "claim": "API tokens can be created instantly in Cloudflare dashboard.",
                    "url": "https://dash.cloudflare.com/profile/api-tokens",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Dashboard enables self-serve creation of tokens using pre-built templates."
                }
            ],
            "confidence": 1.0,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Massive API surface; official Cloudflare MCP server and Workers AI integrations available."]
        },
        {
            "app": "Supabase",
            "category": "Developer, Infra and Data Platforms",
            "description": "Open-source Firebase alternative providing PostgreSQL database, Auth, Storage, Edge Functions, and Realtime.",
            "auth_methods": ["API Key (Anon / Service Role Bearer)", "Personal Access Token (PAT)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier (2 free PostgreSQL projects) or completely free open-source self-hosting.",
            "api": {
                "availability": "REST_AND_GRAPHQL",
                "type": ["REST (PostgREST)", "GraphQL (pg_graphql)", "Management API"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/supabase/mcp-server-supabase"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Row Level Security (RLS) policies must be configured appropriately for keys"],
            "evidence": [
                {
                    "claim": "Supabase provides auto-generated REST APIs (PostgREST) and Management APIs with Bearer token authentication.",
                    "url": "https://supabase.com/docs/guides/api",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Supabase documentation details anon/service_role API keys passed as apikey header and Bearer token."
                },
                {
                    "claim": "API keys and database credentials are generated instantly upon project creation.",
                    "url": "https://supabase.com/dashboard/project/_/settings/api",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Dashboard gives immediate access to project URL, anon key, and service_role secret."
                }
            ],
            "confidence": 1.0,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Prime agent candidate; instant SQL execution, schema inspection, and data storage."]
        },
        {
            "app": "Neo4j",
            "category": "Developer, Infra and Data Platforms",
            "description": "Graph database management system for storing and querying highly connected relational network data.",
            "auth_methods": ["Basic Authentication (username/password)", "Bearer Token", "API Key (Aura API)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Neo4j AuraDB instance in cloud or free Neo4j Desktop / Community Edition.",
            "api": {
                "availability": "REST",
                "type": ["REST (HTTP Query API / Aura API)", "Bolt Binary Protocol"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/neo4j-contrib/mcp-neo4j"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Cypher query language syntax for graph traversals"],
            "evidence": [
                {
                    "claim": "Neo4j supports HTTP Query API with Basic Auth and Aura Cloud Management API using Client ID/Secret.",
                    "url": "https://neo4j.com/docs/http-api/current/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Neo4j HTTP API documentation details POST /db/{database}/query endpoints and Authorization: Basic header format."
                },
                {
                    "claim": "Developers can create a free AuraDB instance self-serve at console.neo4j.io.",
                    "url": "https://neo4j.com/cloud/platform/aura-graph-database/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Aura pricing details permanent free tier instance with immediate connection credentials."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Official MCP server available; great for Knowledge Graph and entity-relation memory in AI agents."]
        },
        {
            "app": "Snowflake",
            "category": "Developer, Infra and Data Platforms",
            "description": "Cloud data platform offering data warehousing, data lake, data engineering, and machine learning infrastructure.",
            "auth_methods": ["OAuth 2.0", "Key Pair (JWT)", "Basic Authentication"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "30-day free trial with $400 worth of compute credits.",
            "api": {
                "availability": "REST",
                "type": ["REST (SQL API v2)", "Python / Node.js Connectors"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/snowflake-labs/mcp-server-snowflake"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Asynchronous query execution model in SQL API for long-running statements"],
            "evidence": [
                {
                    "claim": "Snowflake SQL API v2 authenticates using OAuth 2.0 or JWT Key-Pair authentication in Authorization: Bearer header.",
                    "url": "https://docs.snowflake.com/en/developer-guide/sql-api/authenticating",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Snowflake documentation details Key-Pair JWT generation and OAuth token endpoints for REST SQL API."
                },
                {
                    "claim": "Developers can sign up for a free 30-day trial with full account admin rights.",
                    "url": "https://signup.snowflake.com/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Self-serve registration grants trial credits and access to create users, roles, and warehouses."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["SQL API provides direct query submission and partition result retrieval over HTTP."]
        },
        {
            "app": "MongoDB Atlas",
            "category": "Developer, Infra and Data Platforms",
            "description": "Fully-managed cloud document database service with automated scaling, search, and serverless APIs.",
            "auth_methods": ["API Key (Digest Auth)", "API Key (Data API Bearer Token)", "Database User / Password"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Permanent free M0 sandbox cluster with full Data API and Atlas Admin API access.",
            "api": {
                "availability": "REST",
                "type": ["REST (Atlas Admin API)", "REST (App Services Data API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/mongodb-labs/mcp-server-mongodb"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Digest authentication header format for Atlas Admin API"],
            "evidence": [
                {
                    "claim": "MongoDB Atlas provides REST APIs for administration (Digest Auth) and Data API (apiKey Bearer header).",
                    "url": "https://www.mongodb.com/docs/atlas/api/atlas-admin-api/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Atlas documentation details API keys, HTTP Digest authentication, and Data API endpoints."
                },
                {
                    "claim": "Free M0 clusters can be created self-serve immediately upon registration.",
                    "url": "https://www.mongodb.com/cloud/atlas/register",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Self-serve signup includes free cluster creation and API key generation under Project Access."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Mature document database with official MCP integration."]
        },
        {
            "app": "Datadog",
            "category": "Developer, Infra and Data Platforms",
            "description": "Cloud monitoring, APM, security, and observability platform for cloud infrastructure and applications.",
            "auth_methods": ["API Key", "Application Key"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "14-day free trial with full API and integration capabilities.",
            "api": {
                "availability": "REST",
                "type": ["REST (v1 & v2 APIs)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/datadog-mcp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Dual key requirement: DD-API-KEY (write) + DD-APPLICATION-KEY (read/admin)"],
            "evidence": [
                {
                    "claim": "Datadog API authenticates requests using DD-API-KEY and DD-APPLICATION-KEY headers.",
                    "url": "https://docs.datadoghq.com/api/latest/authentication/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Datadog API documentation outlines header formats and site parameter routing (datadoghq.com, datadoghq.eu)."
                },
                {
                    "claim": "API and Application keys are generated self-serve under Organization Settings > API Keys.",
                    "url": "https://docs.datadoghq.com/account_management/api-app-keys/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation details self-serve key creation with scoped permissions."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Extremely comprehensive metrics, logs, traces, and incident management API."]
        },
        {
            "app": "Sentry",
            "category": "Developer, Infra and Data Platforms",
            "description": "Application performance monitoring and error tracking platform for developers to diagnose bugs.",
            "auth_methods": ["Auth Token (Bearer)", "DSN Key", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Developer tier with full REST API and User Auth Token generation.",
            "api": {
                "availability": "REST",
                "type": ["REST (v0 API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/getsentry/mcp-server-sentry"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limits of 200 requests/minute per token"],
            "evidence": [
                {
                    "claim": "Sentry REST API authenticates using User Auth Tokens in Authorization: Bearer <TOKEN> header and OAuth 2.0.",
                    "url": "https://docs.sentry.io/api/auth/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Sentry API documentation outlines User Auth Token creation, custom scopes (event:read, project:write), and Bearer headers."
                },
                {
                    "claim": "Developers can generate User Auth Tokens self-serve in User Settings > API > User Auth Tokens.",
                    "url": "https://sentry.io/settings/account/api/auth-tokens/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Sentry user dashboard provides instant token generation with granular permission toggles."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Official Sentry MCP server allows agents to triage issues, inspect stack traces, and assign bugs."]
        }
    ]
