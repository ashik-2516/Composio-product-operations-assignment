# scripts/cat2_support.py
# Category 2: Support and Helpdesk (Apps 11 - 20)

def get_cat2_apps():
    return [
        {
            "app": "Zendesk",
            "category": "Support and Helpdesk",
            "description": "Customer support platform providing ticketing, messaging, help center, and customer service solutions.",
            "auth_methods": ["OAuth 2.0", "API Token", "Basic Authentication"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free 14-day trial or Zendesk Developer Sponsored Account.",
            "api": {
                "availability": "REST_AND_GRAPHQL",
                "type": ["REST", "GraphQL"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://developer.zendesk.com/documentation/mcp/"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limits varying from 700 to 2500 requests/min depending on plan"],
            "evidence": [
                {
                    "claim": "Zendesk supports OAuth 2.0 Bearer tokens and API Token basic auth (email/token:token).",
                    "url": "https://developer.zendesk.com/api-reference/ticketing/introduction/#authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Zendesk API reference details authentication mechanisms including OAuth 2.0 access tokens and API tokens."
                },
                {
                    "claim": "Developers can request free sponsored developer accounts.",
                    "url": "https://developer.zendesk.com/documentation/developer-tools/getting-started/developer-account/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Zendesk provides free development accounts to build and test integrations."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Extremely high buildability; one of the most mature support APIs in the industry."]
        },
        {
            "app": "Intercom",
            "category": "Support and Helpdesk",
            "description": "Customer messaging and AI helpdesk platform for onboarding, support, and engagement.",
            "auth_methods": ["OAuth 2.0", "Access Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Developer Workspace available via Intercom Developer Hub.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/intercom/mcp-server-intercom"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limits of 10,000 requests per minute"],
            "evidence": [
                {
                    "claim": "Intercom API uses OAuth 2.0 for third-party apps and Access Tokens (Bearer) for private apps.",
                    "url": "https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Intercom developer documentation outlines OAuth 2.0 token exchange and Bearer authentication headers."
                },
                {
                    "claim": "Developers can create free development workspaces for testing.",
                    "url": "https://developers.intercom.com/docs/build-an-integration/getting-started/set-up-a-developer-workspace/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Intercom enables instant creation of free testing workspaces inside the Developer Hub."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Clean REST API with comprehensive conversation and contact endpoints."]
        },
        {
            "app": "Freshdesk",
            "category": "Support and Helpdesk",
            "description": "Cloud-based customer support software featuring omnichannel ticketing and automation.",
            "auth_methods": ["API Key", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free plan (up to 10 agents) with full API access.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/freshworks/freshdesk-mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limit of 50 requests/min on free/starter tiers"],
            "evidence": [
                {
                    "claim": "Freshdesk API uses HTTP Basic Authentication with API Key and supports OAuth 2.0.",
                    "url": "https://developers.freshdesk.com/api/#authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Freshdesk developer documentation specifies API key authentication via Authorization header."
                },
                {
                    "claim": "Freshdesk offers a permanent free tier that includes API access.",
                    "url": "https://freshdesk.com/pricing",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Pricing page details free plan availability for small teams with basic API capabilities."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Standard REST endpoints with predictable CRUD patterns."]
        },
        {
            "app": "Front",
            "category": "Support and Helpdesk",
            "description": "Customer operations platform combining shared inboxes with ticketing and CRM connectivity.",
            "auth_methods": ["OAuth 2.0", "API Key"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "7-day free trial or paid subscription required.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/frontapp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "Paid plan requirement after trial",
            "secondary_blockers": ["Rate limits of 50-200 requests/minute depending on tier"],
            "evidence": [
                {
                    "claim": "Front API supports OAuth 2.0 Bearer tokens and company API tokens.",
                    "url": "https://dev.frontapp.com/docs/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Front Developer documentation explains OAuth 2.0 and API token header formats (Authorization: Bearer <token>)."
                },
                {
                    "claim": "API tokens can be generated directly in company settings.",
                    "url": "https://dev.frontapp.com/docs/api-tokens",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official docs show how admins create API tokens under Settings > Developers."
                }
            ],
            "confidence": 0.96,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Excellent developer documentation with interactive API playground."]
        },
        {
            "app": "Pylon",
            "category": "Support and Helpdesk",
            "description": "B2B support platform managing customer conversations across Slack, Microsoft Teams, and email.",
            "auth_methods": ["Bearer Token", "API Key"],
            "credential_access": "ADMIN_APPROVAL",
            "free_or_trial_access": "Paid subscription only; requires sales demo or business onboarding.",
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
            "buildability": "MEDIUM",
            "primary_blocker": "Admin approval / Paid plan required",
            "secondary_blockers": ["Token creation restricted to Admin role in dashboard"],
            "evidence": [
                {
                    "claim": "Pylon API uses Bearer authentication with API tokens generated in Settings > API Tokens.",
                    "url": "https://docs.usepylon.com/reference/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Pylon docs describe Bearer YOUR_SECRET_TOKEN format and /me endpoint."
                },
                {
                    "claim": "API tokens can only be created by Admin users within an active customer organization.",
                    "url": "https://docs.usepylon.com/reference/api-tokens",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation notes that token generation requires Admin role permissions."
                }
            ],
            "confidence": 0.94,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Modern REST API hosted at api.usepylon.com; straightforward for B2B Slack integrations."]
        },
        {
            "app": "LiveAgent",
            "category": "Support and Helpdesk",
            "description": "Omnichannel helpdesk and live chat software for customer communication management.",
            "auth_methods": ["API Key"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "14-day free trial or free tier available.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/liveagent/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["API v3 vs legacy v1/v2 endpoint differences"],
            "evidence": [
                {
                    "claim": "LiveAgent API v3 authenticates using an API Key passed in the APIKEY header or apikey query parameter.",
                    "url": "https://ladesk.com/developer/api-v3/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "LiveAgent API v3 reference documents API Key authentication and Swagger-based test consoles."
                },
                {
                    "claim": "API keys are generated self-serve under Configuration > System > API.",
                    "url": "https://support.liveagent.com/085449-How-to-generate-API-keys-in-LiveAgent",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "LiveAgent knowledge base guides users through generating API keys with custom permissions."
                }
            ],
            "confidence": 0.96,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Well-documented OpenAPI spec; easy for agent tool integration."]
        },
        {
            "app": "Plain",
            "category": "Support and Helpdesk",
            "description": "Developer-centric conversational customer support platform built for B2B SaaS teams.",
            "auth_methods": ["API Key", "Bearer Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier available for early-stage teams with API access included.",
            "api": {
                "availability": "GRAPHQL",
                "type": ["GraphQL"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/plain/mcp-server-plain"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["GraphQL schema knowledge required for custom queries"],
            "evidence": [
                {
                    "claim": "Plain provides a GraphQL API authenticated via Machine User API Keys passed as Bearer tokens.",
                    "url": "https://plain.com/docs/graphql/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Plain developer documentation details Machine User creation and Bearer plainApiKey_xxx auth to https://core-api.uk.plain.com/graphql/v1."
                },
                {
                    "claim": "API keys are created self-serve under Settings > Machine Users.",
                    "url": "https://plain.com/docs/graphql/machine-users",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation describes self-serve Machine User and API Key generation."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Modern GraphQL-first architecture designed specifically for developers and agents."]
        },
        {
            "app": "Help Scout",
            "category": "Support and Helpdesk",
            "description": "Shared inbox and customer helpdesk platform for customer support and knowledge management.",
            "auth_methods": ["OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "15-day free trial or free developer app creation in user profile.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/helpscout/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limit of 400 requests/minute"],
            "evidence": [
                {
                    "claim": "Help Scout Mailbox API 2.0 uses OAuth 2.0 with Client Credentials or Authorization Code flow.",
                    "url": "https://developer.helpscout.com/mailbox-api/overview/authentication/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Help Scout developer documentation describes OAuth 2.0 token endpoint POST https://api.helpscout.net/v2/oauth2/token."
                },
                {
                    "claim": "OAuth App credentials (App ID and Secret) are created self-serve in Your Profile > My Apps.",
                    "url": "https://developer.helpscout.com/mailbox-api/overview/create-app/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation provides instructions for creating API applications directly from user settings."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Clean REST API with standard OAuth 2.0 token lifecycle."]
        },
        {
            "app": "Gorgias",
            "category": "Support and Helpdesk",
            "description": "E-commerce-focused customer service helpdesk integrated with Shopify, BigCommerce, and Magento.",
            "auth_methods": ["Basic Authentication", "API Key", "OAuth 2.0"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "7-day free trial available with API access.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/gorgias/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "Paid plan requirement after trial",
            "secondary_blockers": ["Rate limit of 200 requests/min"],
            "evidence": [
                {
                    "claim": "Gorgias API supports HTTP Basic Auth (email:api_key) and OAuth 2.0.",
                    "url": "https://developers.gorgias.com/reference/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Gorgias developer documentation explains HTTP Basic Authentication with API key and OAuth 2.0 flows."
                },
                {
                    "claim": "API credentials can be generated self-serve under Settings > You > REST API.",
                    "url": "https://developers.gorgias.com/reference/how-to-find-your-api-key",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official guide illustrates key generation in user profile settings."
                }
            ],
            "confidence": 0.96,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["E-commerce ticket context (orders, refunds) directly exposed via REST."]
        },
        {
            "app": "Gladly",
            "category": "Support and Helpdesk",
            "description": "People-centered customer service platform unifying customer communication history, voice, and omnichannel messaging.",
            "auth_methods": ["HTTP Basic Authentication (user@organization.com : API_Token)"],
            "credential_access": "ADMIN_APPROVAL",
            "free_or_trial_access": "Enterprise subscription; dedicated sandbox testing available at https://{organization}.gladly.qa.",
            "api": {
                "availability": "REST",
                "type": [
                    "REST (https://{organization}.gladly.com/api/v1/)",
                    "Lookup API (Customer Lookup Adaptor Service)",
                    "Streaming Events API (JSONL, last 24 hours)"
                ],
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
                "Requires Gladly Administrator to assign 'API User' permission under Settings > Users before creating tokens in More settings > API Tokens",
                "Standard rate limit of 10 requests/second with 429 exponential backoff requirement (Ratelimit-Limit-Second headers)"
            ],
            "evidence": [
                {
                    "claim": "Gladly REST API uses token-based HTTP Basic Authentication (email as username, API token as password via Authorization header) across endpoints for Agents, Conversations, Customers, Tasks, and Reports.",
                    "url": "https://developer.gladly.com/rest/#section/Authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Gladly API Docs: 'Gladly API uses token-based Basic Authentication... curl -u user@organization.com:$GLADLY_API_TOKEN https://organization.gladly.com/api/v1/organization.'"
                },
                {
                    "claim": "Administrators must assign the 'API User' permission under Settings > Users before users can create API tokens under More settings > API Tokens.",
                    "url": "https://developer.gladly.com/rest/#section/Getting-Started/Permissions",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation states: 'Gladly Administrators can set API permissions on an agent-by-agent basis... Navigate to Settings > Users > select user profile > select API User. Once set, go to More settings > API Tokens > Create Token.'"
                }
            ],
            "confidence": 0.99,
            "human_verification_required": True,
            "uncertainties": ["Developer partner self-serve sandbox provisioning without customer contract"],
            "research_notes": [
                "Comprehensive customer support REST API covering Agents, Conversations, Customers, Tasks, Webhooks (Ping validated), and custom Lookup Adaptors; requires organization domain and admin role."
            ]
        }
    ]
