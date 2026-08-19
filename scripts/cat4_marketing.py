# scripts/cat4_marketing.py
# Category 4: Marketing, Ads, Email and Social (Apps 31 - 40)

def get_cat4_apps():
    return [
        {
            "app": "Google Ads",
            "category": "Marketing, Ads, Email and Social",
            "description": "Online advertising platform for search, display, video, and app campaigns across Google networks with official MCP server and Agent Skills.",
            "auth_methods": [
                "OAuth 2.0 (Bearer Token with scope https://www.googleapis.com/auth/adwords)",
                "Service Account Key (JSON)",
                "Developer Token (22-character developer-token Header)"
            ],
            "credential_access": "ADMIN_APPROVAL",
            "free_or_trial_access": "Test accounts and test developer tokens are free; production access requires approved Developer Token application review.",
            "api": {
                "availability": "REST_AND_GRAPHQL",
                "type": [
                    "REST (googleads.googleapis.com)",
                    "gRPC",
                    "MCP Server (googleads/google-ads-mcp via stdio or Cloud Run)",
                    "Official Agent Skills (google-ads-api-mcp-setup, google-ads-api-quickstart)"
                ],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Google Ads Open Source (googleads/google-ads-mcp)",
                "url": "https://github.com/googleads/google-ads-mcp"
            },
            "buildability": "MEDIUM",
            "primary_blocker": "Developer Token approval review for production access",
            "secondary_blockers": [
                "Dual auth requirement (OAuth 2.0 token / Service Account + developer-token header)",
                "Google Ads Query Language (GAQL) query construction required for search endpoint",
                "Official MCP server is currently strictly read-only"
            ],
            "evidence": [
                {
                    "claim": "Google maintains the official google-ads-mcp server repository providing read-only campaign search and customer discovery tools (list_accessible_customers, search, get_resource_metadata) deployable via stdio or Cloud Run.",
                    "url": "https://github.com/googleads/google-ads-mcp",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Google Ads MCP docs specify FastMCP tools (list_accessible_customers, search, get_resource_metadata), Cloud Run deployment, and stdio pipx invocation."
                },
                {
                    "claim": "Google provides official open Agent Skills (google-ads-api-mcp-setup, google-ads-api-quickstart) and developer assistant CLI (googleads/google-ads-api-developer-assistant).",
                    "url": "https://developers.google.com/google-ads/api/docs/developer-toolkit/agent-skills",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Google documentation details open Agent Skills standard support for Claude Code, Antigravity, and Codex with progressive disclosure."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": True,
            "uncertainties": ["Approval latency for Standard Access production developer tokens"],
            "research_notes": [
                "First-party open source MCP server (googleads/google-ads-mcp) and official Agent Skills make Google Ads exceptionally well-architected for AI assistants, though production traffic requires an approved Developer Token."
            ]
        },
        {
            "app": "Meta Ads",
            "category": "Marketing, Ads, Email and Social",
            "description": "Advertising platform for creating, managing, and optimizing ad campaigns on Facebook and Instagram.",
            "auth_methods": ["OAuth 2.0", "Bearer Token (System User / User Access Token)"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "Free developer app creation in Development Mode; App Review required for Standard/Advanced Access.",
            "api": {
                "availability": "REST",
                "type": ["REST (Graph API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/meta-ads-mcp/mcp-server"
            },
            "buildability": "MEDIUM",
            "primary_blocker": "Meta App Review & Business Verification for production ad management",
            "secondary_blockers": ["Marketing API tier limits (Development vs Standard vs Advanced)"],
            "evidence": [
                {
                    "claim": "Meta Marketing API uses OAuth 2.0 Bearer access tokens via Graph API endpoints.",
                    "url": "https://developers.facebook.com/docs/marketing-apis/overview/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Meta for Developers documentation details access token types, scopes (ads_management, ads_read), and Graph API auth."
                },
                {
                    "claim": "Developers can create test apps instantly, but managing live ads requires App Review.",
                    "url": "https://developers.facebook.com/docs/marketing-apis/access",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation outlines access tier transitions from Development Mode to Advanced Access."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["High API capabilities; access gated behind Facebook Business App Review."]
        },
        {
            "app": "LinkedIn Ads",
            "category": "Marketing, Ads, Email and Social",
            "description": "B2B social advertising platform for sponsored content, messaging ads, and lead gen campaigns.",
            "auth_methods": ["OAuth 2.0 (3-legged Bearer)"],
            "credential_access": "PARTNER_OR_SALES_GATED",
            "free_or_trial_access": "Requires formal application to LinkedIn Marketing Developer Platform (MDP); sandbox test apps available upon approval.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/linkedin-mcp/mcp-server"
            },
            "buildability": "MEDIUM",
            "primary_blocker": "Marketing Developer Platform (MDP) application review & Partner Program approval",
            "secondary_blockers": [
                "Private endpoints (Matched Audiences, Audience Insights, Media Planning, Company Intelligence) require additional approvals",
                "Strict versioned API lifecycle with mandatory migration windows"
            ],
            "evidence": [
                {
                    "claim": "LinkedIn Marketing Developer Platform (MDP) exposes Advertising APIs (Campaigns, Creatives, Reporting), Lead Sync, Event Management, and Conversions APIs via versioned REST endpoints.",
                    "url": "https://learn.microsoft.com/en-us/linkedin/marketing/overview",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Microsoft Learn MDP Documentation details API products: Advertising API (Campaigns, Creatives, Ad Analytics), Lead Sync, Conversions API, Community Management (Posts/Comments), and notes Matched Audiences / Company Intelligence require private approval."
                },
                {
                    "claim": "Access to Marketing API products is governed by LinkedIn API Terms of Use and requires an approved MDP application or LinkedIn Marketing Partner Program membership.",
                    "url": "https://learn.microsoft.com/en-us/linkedin/marketing/increasing-access",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation notes: 'Use of LinkedIn programmatic web APIs is governed by LinkedIn API Terms of Use unless a signed partnership agreement is executed... Matched Audiences and Company Intelligence are private APIs requiring additional approval.'"
                }
            ],
            "confidence": 0.99,
            "human_verification_required": True,
            "uncertainties": ["Approval latency for independent AI toolkit developers without existing large enterprise ad spend"],
            "research_notes": [
                "Comprehensive B2B advertising API suite, but access is gated behind formal MDP application review and Partner Program governance."
            ]
        },
        {
            "app": "GoHighLevel",
            "category": "Marketing, Ads, Email and Social",
            "description": "All-in-one sales, marketing automation, CRM, and funnel management platform for marketing agencies.",
            "auth_methods": ["OAuth 2.0", "Bearer Token", "API Key"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "14-day free trial or paid Agency subscription required to access Developer Marketplace.",
            "api": {
                "availability": "REST",
                "type": ["REST (API v2)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/gohighlevel/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "Paid agency plan requirement for marketplace app creation",
            "secondary_blockers": ["Migration from legacy V1 API keys to V2 OAuth apps with Location scopes"],
            "evidence": [
                {
                    "claim": "GoHighLevel API v2 uses OAuth 2.0 with Authorization Code flow and Bearer tokens.",
                    "url": "https://highlevel.stoplight.io/docs/integrations/00d315668e0e7-authorization",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "HighLevel Stoplight documentation explains OAuth 2.0 authorization, token refreshing, and location access."
                },
                {
                    "claim": "Developers can register Marketplace Apps within their HighLevel agency account.",
                    "url": "https://marketplace.gohighlevel.com/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Marketplace portal enables self-serve app creation for Agency account holders."
                }
            ],
            "confidence": 0.96,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Very popular among marketing agencies; API v2 provides extensive CRM and funnel control."]
        },
        {
            "app": "Mailchimp",
            "category": "Marketing, Ads, Email and Social",
            "description": "Email marketing and automation platform for newsletters, campaigns, and audience segmentation.",
            "auth_methods": ["OAuth 2.0", "API Key", "Basic Authentication"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free account tier and free Mailchimp Developer accounts available.",
            "api": {
                "availability": "REST",
                "type": ["REST (Marketing API v3)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/mailchimp/mcp-server-mailchimp"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Data center prefix in API base URL (https://<dc>.api.mailchimp.com/3.0/)"],
            "evidence": [
                {
                    "claim": "Mailchimp Marketing API supports OAuth 2.0 Bearer tokens and HTTP Basic Auth with API Keys.",
                    "url": "https://mailchimp.com/developer/marketing/guides/access-the-marketing-api/#authenticate-with-an-api-key-or-oauth-2.0",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Mailchimp Developer guides detail OAuth 2.0 and API Key (anystring:apiKey) basic authentication."
                },
                {
                    "claim": "Developers can generate API keys self-serve in Account > Extras > API keys.",
                    "url": "https://mailchimp.com/developer/marketing/guides/quick-start/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Quick start guide explains immediate API key creation on any active account."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Extremely mature API; easy integration for email campaign automation."]
        },
        {
            "app": "Klaviyo",
            "category": "Marketing, Ads, Email and Social",
            "description": "Marketing automation platform specializing in ecommerce email, SMS campaigns, and customer data.",
            "auth_methods": ["API Key", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free account tier (up to 250 contacts) with instant API key creation.",
            "api": {
                "availability": "REST",
                "type": ["REST (JSON:API format)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/klaviyo/mcp-server-klaviyo"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["JSON:API spec payload wrapping requirements"],
            "evidence": [
                {
                    "claim": "Klaviyo API uses Klaviyo-API-Key header authentication for private keys and OAuth 2.0 Bearer tokens.",
                    "url": "https://developers.klaviyo.com/en/docs/authenticate_with_the_klaviyo_api",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Klaviyo developer documentation details header formats (Authorization: Klaviyo-API-Key <key>) and OAuth 2.0."
                },
                {
                    "claim": "API keys can be generated self-serve under Settings > Account > API Keys.",
                    "url": "https://developers.klaviyo.com/en/docs/create_private_api_keys",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation shows how to generate private API keys with granular scopes."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Very consistent modern JSON:API architecture with rich ecommerce event tracking."]
        },
        {
            "app": "systeme.io",
            "category": "Marketing, Ads, Email and Social",
            "description": "All-in-one marketing platform for sales funnels, email marketing, courses, and affiliate management.",
            "auth_methods": ["API Key"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free plan (up to 2000 contacts) with Public API and MCP server access.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP",
                "official": "Vendor-official",
                "url": "https://developer.systeme.io/docs/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Limit of 3 active API keys per account"],
            "evidence": [
                {
                    "claim": "Systeme.io provides an official Public API and official Model Context Protocol (MCP) server.",
                    "url": "https://developer.systeme.io/docs/mcp-server",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Systeme.io developer portal documents official MCP server and REST API reference."
                },
                {
                    "claim": "Public API keys are generated self-serve under Account Settings > MCP & API keys.",
                    "url": "https://developer.systeme.io/reference",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "API reference explains header authentication (x-api-key: YOUR_KEY) and self-serve generation."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["First-party official MCP server makes this an immediate top-tier easy win for AI agents."]
        },
        {
            "app": "Pinterest",
            "category": "Marketing, Ads, Email and Social",
            "description": "Visual discovery and social curation platform offering organic content and advertising APIs.",
            "auth_methods": ["OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free developer account with instant Trial Access; Standard/Production access requires app review.",
            "api": {
                "availability": "REST",
                "type": ["REST (API v5)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/pinterest/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Standard access app review for large scale production campaigns"],
            "evidence": [
                {
                    "claim": "Pinterest API v5 authenticates requests using OAuth 2.0 Bearer tokens.",
                    "url": "https://developers.pinterest.com/docs/api/v5/authentication/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Pinterest Developer documentation outlines OAuth 2.0 authorization code flow, refresh tokens, and headers."
                },
                {
                    "claim": "Developers can register apps and start building in Trial mode immediately.",
                    "url": "https://developers.pinterest.com/docs/getting-started/set-up-app/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Getting started guide details self-serve app setup and instant token generation for development."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Modern OpenAPI v5 spec with granular permissions for organic pins and ad tracking."]
        },
        {
            "app": "Threads (Meta)",
            "category": "Marketing, Ads, Email and Social",
            "description": "Meta's text-based social conversation platform for posting text, media, and replying to threads.",
            "auth_methods": ["OAuth 2.0", "Bearer Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free developer registration via Meta for Developers; development mode available for app testing.",
            "api": {
                "availability": "REST",
                "type": ["REST (Threads API)"],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/threads-mcp/threads-mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["App Review required for public non-developer user access"],
            "evidence": [
                {
                    "claim": "Threads API uses OAuth 2.0 authorization code flow to issue Threads User Access Tokens.",
                    "url": "https://developers.facebook.com/docs/threads/overview",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Meta documentation details Threads API endpoints (posts, replies, media, insights) and OAuth flow."
                },
                {
                    "claim": "Developers can create Threads apps directly in Meta Developer Dashboard.",
                    "url": "https://developers.facebook.com/docs/threads/get-started",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Get started guide explains self-serve setup and token generation for test users."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Clean REST endpoints for publishing and managing text conversations."]
        },
        {
            "app": "SendGrid",
            "category": "Marketing, Ads, Email and Social",
            "description": "Cloud-based customer communication platform for transactional email delivery, marketing, and validation.",
            "auth_methods": ["API Key", "Bearer Token", "Basic Authentication"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free plan (100 emails/day forever) with full API key access.",
            "api": {
                "availability": "REST",
                "type": ["REST (v3 API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/sendgrid/mcp-server-sendgrid"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Sender Identity verification (SPF/DKIM/Single Sender) required before sending"],
            "evidence": [
                {
                    "claim": "SendGrid API v3 authenticates requests using API Keys passed in Authorization: Bearer <API_KEY> header.",
                    "url": "https://docs.sendgrid.com/api-reference/how-to-use-the-sendgrid-v3-api/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "SendGrid documentation specifies Bearer API Key header authentication and permissions."
                },
                {
                    "claim": "API keys can be generated self-serve in Settings > API Keys.",
                    "url": "https://docs.sendgrid.com/ui/account-and-settings/api-keys",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation details self-serve key generation with Full Access or Restricted Access scopes."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Classic reliable transactional API; instant setup for automated emailing."]
        }
    ]
