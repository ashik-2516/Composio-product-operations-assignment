# scripts/cat1_crm.py
# Category 1: CRM and Sales (Apps 1 - 10)

def get_cat1_apps():
    return [
        {
            "app": "Salesforce",
            "category": "CRM and Sales",
            "description": "Enterprise CRM platform for sales pipelines, customer relations, and business process automation.",
            "auth_methods": ["OAuth 2.0", "JWT Bearer", "SAML"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Developer Edition account available with full API access.",
            "api": {
                "availability": "REST_AND_GRAPHQL",
                "type": ["REST", "GraphQL", "SOAP", "Bulk API"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://developer.salesforce.com/docs/platform/mcp/overview"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Complex permission sets", "API call limits per 24h"],
            "evidence": [
                {
                    "claim": "Salesforce supports OAuth 2.0 and JWT Bearer token flows for API integration.",
                    "url": "https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_flows.htm",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Salesforce Help documentation outlines Connected Apps and OAuth 2.0 authorization flows including Web Server and JWT Bearer flows."
                },
                {
                    "claim": "Developers can create a permanent free Developer Edition org with full API capabilities.",
                    "url": "https://developer.salesforce.com/signup",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Salesforce Developer portal provides free full-featured Developer Edition environments."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["High agent readiness due to mature REST/GraphQL APIs and broad ecosystem."]
        },
        {
            "app": "HubSpot",
            "category": "CRM and Sales",
            "description": "Inbound marketing, sales CRM, customer service, and content management platform.",
            "auth_methods": ["OAuth 2.0", "Private App Access Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Developer Account and app test accounts with full API access.",
            "api": {
                "availability": "REST_AND_GRAPHQL",
                "type": ["REST", "GraphQL"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/modelcontextprotocol/servers/tree/main/src/hubspot"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limit of 100 requests per 10 seconds"],
            "evidence": [
                {
                    "claim": "HubSpot uses OAuth 2.0 for public integrations and Private App Tokens for internal integrations.",
                    "url": "https://developers.hubspot.com/docs/api/working-with-oauth",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "HubSpot Developer Docs state OAuth 2.0 is standard for public apps and private apps use Bearer access tokens."
                },
                {
                    "claim": "HubSpot provides free developer accounts with unlimited test portals.",
                    "url": "https://developers.hubspot.com/get-started",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "HubSpot developer portal allows instant free registration for app development and testing."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Excellent API consistency with OpenAPI specifications available."]
        },
        {
            "app": "Pipedrive",
            "category": "CRM and Sales",
            "description": "Sales-focused CRM tool for deal tracking, pipeline management, and contact organization.",
            "auth_methods": ["OAuth 2.0", "API Key"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Developer Sandbox account via Developer Center.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/pipedrive/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limits based on plan tiers (40-100 req/2s)"],
            "evidence": [
                {
                    "claim": "Pipedrive supports OAuth 2.0 for marketplace apps and personal API tokens for private usage.",
                    "url": "https://pipedrive.readme.io/docs/core-api-concepts-authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Pipedrive developer documentation specifies OAuth 2.0 authorization code grant flow and API token header auth."
                },
                {
                    "claim": "Pipedrive allows self-serve creation of developer sandbox accounts.",
                    "url": "https://pipedrive.readme.io/docs/developer-sandbox-account",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Developers can sign up for a persistent free sandbox environment to test APIs and apps."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Straightforward REST API with comprehensive CRUD endpoints for CRM entities."]
        },
        {
            "app": "Attio",
            "category": "CRM and Sales",
            "description": "Modern, customizable CRM built on a flexible real-time relational data model.",
            "auth_methods": ["OAuth 2.0", "API Key"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier available with full API key generation capabilities.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/attio/mcp-server-attio"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Complex schema definitions for custom attributes"],
            "evidence": [
                {
                    "claim": "Attio provides Bearer API Keys and OAuth 2.0 for API authorization.",
                    "url": "https://developers.attio.com/docs/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Attio Developer Documentation documents Bearer API keys and OAuth 2.0 authorization flows."
                },
                {
                    "claim": "API keys can be generated directly in workspace settings on any tier.",
                    "url": "https://developers.attio.com/docs/api-keys",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Attio documentation explains self-serve creation of workspace API keys with granular scopes."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Modern API architecture, well-suited for AI agent tool calling."]
        },
        {
            "app": "Twenty",
            "category": "CRM and Sales",
            "description": "Open-source CRM platform providing full data ownership and customizable workspaces.",
            "auth_methods": ["API Key", "Bearer Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Completely free via open-source self-hosting; free cloud trial available.",
            "api": {
                "availability": "REST_AND_GRAPHQL",
                "type": ["REST", "GraphQL"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/twentyhq/twenty"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rapidly evolving schema given open-source development velocity"],
            "evidence": [
                {
                    "claim": "Twenty provides both REST and GraphQL APIs authenticated via Bearer API keys.",
                    "url": "https://twenty.com/developers/section/graphql-and-rest-api",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Twenty developer docs detail GraphQL and REST API endpoints authenticated with workspace tokens."
                },
                {
                    "claim": "Twenty source code is open source and self-hostable with no access gating.",
                    "url": "https://github.com/twentyhq/twenty",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "GitHub repository confirms AGPL v3 license with immediate local deployability."
                }
            ],
            "confidence": 0.96,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Open source nature allows seamless local or cloud agent development."]
        },
        {
            "app": "Podio",
            "category": "CRM and Sales",
            "description": "Customizable collaborative work platform for project tracking, task management, and sales workflows.",
            "auth_methods": ["OAuth 2.0", "API Key"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier available with instant API key creation.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "MEDIUM"
            },
            "mcp": {
                "status": "NO_MCP_FOUND",
                "official": "None",
                "url": ""
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limit of 250 requests per hour for basic tiers"],
            "evidence": [
                {
                    "claim": "Podio API uses OAuth 2.0 with Client ID and Secret for authentication.",
                    "url": "https://podio.com/site/help/api/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Podio developer portal outlines Server-side, Client-side, and Username/Password OAuth 2.0 flows."
                },
                {
                    "claim": "API keys can be generated self-serve under user account settings.",
                    "url": "https://podio.com/site/help/api/api-keys",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Users can generate API keys directly in their account profile without administrator approval."
                }
            ],
            "confidence": 0.94,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Mature REST API with deep item/app customization support."]
        },
        {
            "app": "Zoho CRM",
            "category": "CRM and Sales",
            "description": "Comprehensive CRM platform for lead generation, contact management, and sales pipeline tracking.",
            "auth_methods": ["OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free developer accounts available via Zoho Developer Console.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/zoho/zoho-mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Multi-data center routing domain requirements (.com, .eu, .in)"],
            "evidence": [
                {
                    "claim": "Zoho CRM enforces OAuth 2.0 for all API v2/v3 interactions.",
                    "url": "https://www.zoho.com/crm/developer/docs/api/v3/oauth-overview.html",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Zoho Developer documentation details OAuth 2.0 protocol implementation with access and refresh tokens."
                },
                {
                    "claim": "Developers can register client apps via Zoho API Console for free.",
                    "url": "https://api-console.zoho.com/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Zoho API Console provides self-serve client app creation and token generation."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Broad API coverage; requires handling regional data center TLDs."]
        },
        {
            "app": "Close",
            "category": "CRM and Sales",
            "description": "Inside sales CRM featuring integrated multi-channel communications and deal automation.",
            "auth_methods": ["API Key", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "14-day free trial with full API access.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/closeio/close-mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Paid plan requirement after 14-day trial period"],
            "evidence": [
                {
                    "claim": "Close API supports HTTP Basic Auth with API key as username and OAuth 2.0.",
                    "url": "https://developer.close.com/topics/authentication/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Close developer documentation documents API key authentication via HTTP Basic and OAuth 2.0."
                },
                {
                    "claim": "API keys can be generated immediately from user settings.",
                    "url": "https://developer.close.com/getting-started/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Developer documentation explains self-serve key generation under Settings > API Keys."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Very clean REST API with comprehensive activity logging and lead tracking."]
        },
        {
            "app": "Copper",
            "category": "CRM and Sales",
            "description": "Google Workspace-integrated CRM for contact, pipeline, and customer relationship management.",
            "auth_methods": ["API Key"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "14-day free trial or paid plan required to generate API keys.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "MEDIUM",
                "documentation_quality": "MEDIUM"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/copper/copper-mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "Paid subscription / active trial required",
            "secondary_blockers": ["Custom header requirements (X-PW-AccessToken, X-PW-UserEmail)"],
            "evidence": [
                {
                    "claim": "Copper API requires custom headers X-PW-AccessToken and X-PW-UserEmail.",
                    "url": "https://developer.copper.com/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Copper developer documentation outlines header-based API key authentication."
                },
                {
                    "claim": "API key generation requires access to Settings > Integrations in an active account.",
                    "url": "https://support.copper.com/hc/en-us/articles/115000336683-How-do-I-generate-an-API-key-",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Support documentation specifies how administrators generate API tokens inside active accounts."
                }
            ],
            "confidence": 0.95,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Functional REST API with standard CRM entity support."]
        },
        {
            "app": "DealCloud",
            "category": "CRM and Sales",
            "description": "Institutional CRM and deal management platform for investment banks and private capital firms.",
            "auth_methods": ["OAuth 2.0 (Client Credentials Grant)", "API Key (User Profile / Bearer Token)"],
            "credential_access": "ADMIN_APPROVAL",
            "free_or_trial_access": "Enterprise contract only; no public free tier or self-serve developer sandbox.",
            "api": {
                "availability": "REST",
                "type": ["REST (api/rest/v1 and api/rest/v4)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "NO_MCP_FOUND",
                "official": "None",
                "url": ""
            },
            "buildability": "MEDIUM",
            "primary_blocker": "Enterprise-only access / Admin approval",
            "secondary_blockers": [
                "Admin must enable API capability in User Management (Capabilities > Site Areas > API)",
                "OAuth2 tokens expire after 900 seconds (15 minutes) and require recurring client_credentials refreshes"
            ],
            "evidence": [
                {
                    "claim": "DealCloud uses OAuth2 Client Credentials flow at POST {baseUrl}/api/rest/v1/oauth/token with client_id, client_secret/apiKey, and space-separated scopes (user_management, data, publish, ri_import, backup) returning a 900-second Bearer access token.",
                    "url": "https://api.docs.dealcloud.com/docs",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official DealCloud documentation details POST /api/rest/v1/oauth/token, application/x-www-form-urlencoded body, Authorization: Bearer header, and granular scopes for data (v4/data, v4/schema) and user_management (v1/management)."
                },
                {
                    "claim": "DealCloud API access requires an administrator to navigate to Admin > User Management, select user group, go to Capabilities > Site Areas, and enable 'API'. Once enabled, users generate API keys in Profile > API Key.",
                    "url": "https://api.docs.dealcloud.com/docs",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official DealCloud API documentation specifies: 'To enable API access, ensure the intended user is assigned to a user group with the appropriate permissions... enable API. Once permissions are set, select Profile > API Key > Enable.'"
                }
            ],
            "confidence": 0.99,
            "human_verification_required": True,
            "uncertainties": ["Developer partner sandbox availability for non-enterprise institutions"],
            "research_notes": [
                "Robust REST endpoints for data, schema, publications, and relationship intelligence import; OAuth2 client credentials flow requires managing 15-minute token renewals."
            ]
        }
    ]
