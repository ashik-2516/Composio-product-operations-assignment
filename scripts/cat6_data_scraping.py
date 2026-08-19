# scripts/cat6_data_scraping.py
# Category 6: Data, SEO and Scraping (Apps 51 - 60)

def get_cat6_apps():
    return [
        {
            "app": "DataForSEO",
            "category": "Data, SEO and Scraping",
            "description": "Comprehensive API provider for search engine optimization, SERP data, keywords, backlinks, and merchant data.",
            "auth_methods": ["Basic Authentication", "API Key"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free test credits ($1.00) upon registration; pay-as-you-go pricing.",
            "api": {
                "availability": "REST",
                "type": ["REST (v3 API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/dataforseo/dataforseo-mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Usage-based billing per request"],
            "evidence": [
                {
                    "claim": "DataForSEO API v3 uses HTTP Basic Authentication with login email and API password/key.",
                    "url": "https://docs.dataforseo.com/v3/appendix/authentication/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official DataForSEO documentation details HTTP Basic Auth header encoding (base64 login:password)."
                },
                {
                    "claim": "Developers can register self-serve and generate API credentials instantly in dashboard.",
                    "url": "https://docs.dataforseo.com/v3/getting-started/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Getting started guide outlines instant self-serve API access and test sandbox."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["API-first architecture; extensive documentation across Google, Bing, Yahoo, and Amazon SERPs."]
        },
        {
            "app": "SE Ranking",
            "category": "Data, SEO and Scraping",
            "description": "All-in-one SEO platform for keyword tracking, website audits, competitor research, and backlink analysis.",
            "auth_methods": ["API Key", "Bearer Token"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "14-day free trial; API access requires Pro or Business subscription.",
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
            "primary_blocker": "Pro / Business subscription required for API access",
            "secondary_blockers": ["Rate limits of 5 requests per second"],
            "evidence": [
                {
                    "claim": "SE Ranking API authenticates using an API Key passed in Authorization: Bearer <API_KEY> header.",
                    "url": "https://seranking.com/api.html",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "SE Ranking API documentation specifies Bearer token authorization and endpoint references."
                },
                {
                    "claim": "API key generation is available in account settings for Pro/Business tier customers.",
                    "url": "https://seranking.com/kb/api/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Knowledge base confirms API keys can be generated under Account Settings > API."
                }
            ],
            "confidence": 0.96,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Clean REST endpoints for rank tracking, site auditing, and keyword research."]
        },
        {
            "app": "Ahrefs",
            "category": "Data, SEO and Scraping",
            "description": "SEO toolset for backlink indexing, keyword discovery, content exploration, and site auditing.",
            "auth_methods": ["API Key", "Bearer Token", "OAuth 2.0"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "Paid Enterprise subscription or API Units plan required; no free developer API tier.",
            "api": {
                "availability": "REST",
                "type": ["REST (API v3)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/ahrefs/ahrefs-mcp"
            },
            "buildability": "MEDIUM",
            "primary_blocker": "High-tier paid plan / API units subscription required",
            "secondary_blockers": ["Credit consumption cost per data row returned"],
            "evidence": [
                {
                    "claim": "Ahrefs API v3 authenticates using Bearer API Keys and OAuth 2.0.",
                    "url": "https://ahrefs.com/api/documentation",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Ahrefs API v3 docs detail Authorization: Bearer <token> authentication and OpenAPI v3 specs."
                },
                {
                    "claim": "API v3 access is available only on paid plans with API Units enabled.",
                    "url": "https://ahrefs.com/api/pricing",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Pricing page specifies that API units must be purchased on top of eligible plans."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["High quality API v3 data; buildable but restricted by high subscription paywall."]
        },
        {
            "app": "MrScraper",
            "category": "Data, SEO and Scraping",
            "description": "Visual web scraper and automated data extraction platform with AI parsing capabilities.",
            "auth_methods": ["API Key", "Bearer Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier available with free monthly scraping credits.",
            "api": {
                "availability": "REST",
                "type": ["REST (v1 API)"],
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
            "secondary_blockers": ["Custom header 'x-api-token' requirement"],
            "evidence": [
                {
                    "claim": "MrScraper API uses x-api-token header for authenticating manual and scheduled scraping runs.",
                    "url": "https://docs.mrscraper.com/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official MrScraper documentation details x-api-token header format and POST /api/v1/scrapers-manual-rerun endpoints."
                },
                {
                    "claim": "API tokens can be created self-serve inside the user account dashboard.",
                    "url": "https://docs.mrscraper.com/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation outlines self-serve token generation under user profile."
                }
            ],
            "confidence": 0.96,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Straightforward REST API for triggering visual scrapers and retrieving JSON results."]
        },
        {
            "app": "Apify",
            "category": "Data, SEO and Scraping",
            "description": "Cloud platform for web scraping, data extraction, and serverless web automation actors.",
            "auth_methods": ["API Key", "Bearer Token", "Personal Access Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free plan ($5 monthly usage credits) with full API and actor access.",
            "api": {
                "availability": "REST",
                "type": ["REST (v2 API)", "WebSocket"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/apify/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Usage limits and actor compute unit consumption"],
            "evidence": [
                {
                    "claim": "Apify API v2 authenticates using API tokens passed in Authorization: Bearer header or token query parameter.",
                    "url": "https://docs.apify.com/api/v2#/reference/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Apify API Reference details token authentication, scopes, and OpenAPI specification."
                },
                {
                    "claim": "API tokens are generated instantly and self-serve in Apify Console > Settings > Integrations.",
                    "url": "https://docs.apify.com/platform/integrations/api",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation guides users through self-serve token generation and secret management."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Top-tier developer ecosystem; official MCP server enables executing 1000s of pre-built web scraping actors."]
        },
        {
            "app": "Firecrawl",
            "category": "Data, SEO and Scraping",
            "description": "Web scraping, crawling, and extraction engine that turns websites into clean LLM-ready markdown.",
            "auth_methods": ["API Key", "Bearer Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier (500 free credits) or completely free open-source self-hosting.",
            "api": {
                "availability": "REST",
                "type": ["REST (v1 API)", "WebSocket"],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/mendableai/firecrawl-mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Credit exhaustion on heavy crawl operations"],
            "evidence": [
                {
                    "claim": "Firecrawl API authenticates using Bearer API keys in Authorization header.",
                    "url": "https://docs.firecrawl.dev/api-reference/introduction",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Firecrawl documentation details Authorization: Bearer <fc-apiKey> header and scrape/crawl endpoints."
                },
                {
                    "claim": "API keys can be generated self-serve upon signing up for Firecrawl Cloud.",
                    "url": "https://www.firecrawl.dev/app/api-keys",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Firecrawl dashboard provides instant API key creation and free trial credits."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Purpose-built for AI agents; native markdown output and official MCP server."]
        },
        {
            "app": "Bright Data",
            "category": "Data, SEO and Scraping",
            "description": "Web data platform providing proxy networks, scraping browsers, web unlockers, and pre-built datasets.",
            "auth_methods": ["API Key", "Bearer Token", "Basic Authentication (Proxy)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free trial balance on signup; pay-as-you-go plans available.",
            "api": {
                "availability": "REST",
                "type": ["REST", "WebSocket (Scraping Browser)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/brightdata/brightdata-mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Compliance verification for certain sensitive proxy domains"],
            "evidence": [
                {
                    "claim": "Bright Data API uses API Tokens passed in Authorization: Bearer header for REST APIs and user:pass for proxies.",
                    "url": "https://docs.brightdata.com/api-reference",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Bright Data documentation outlines Bearer token authorization for Web Scraper and Dataset APIs."
                },
                {
                    "claim": "API tokens can be generated self-serve in User Settings > API Tokens.",
                    "url": "https://docs.brightdata.com/general/account/api-token",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation details self-serve token generation with granular zone permissions."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Broad infrastructure for large-scale web scraping and dataset generation."]
        },
        {
            "app": "Sherlock",
            "category": "Data, SEO and Scraping",
            "description": "Open-source Python CLI tool to find social media accounts by username across 400+ social platforms.",
            "auth_methods": ["None (Open Source CLI)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Completely free open-source software on GitHub; no account or API keys required.",
            "api": {
                "availability": "CLI_ONLY",
                "type": ["CLI", "Python Library"],
                "breadth": "NARROW",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/sherlock-project/sherlock"
            },
            "buildability": "MEDIUM",
            "primary_blocker": "CLI only / No hosted REST API service",
            "secondary_blockers": ["Rate limiting/blocking by target social networks without proxy"],
            "evidence": [
                {
                    "claim": "Sherlock is an open-source CLI program written in Python without a hosted REST API.",
                    "url": "https://github.com/sherlock-project/sherlock",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official GitHub repository documents installation via pip/docker and CLI invocation (sherlock user123)."
                },
                {
                    "claim": "No API keys or authentication required; operates by scanning public endpoints.",
                    "url": "https://github.com/sherlock-project/sherlock/blob/master/README.md",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation confirms open-source MIT license and local script execution."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Must be wrapped as a local tool/subprocess execution rather than HTTP REST API calling."]
        },
        {
            "app": "Waterfall.io",
            "category": "Data, SEO and Scraping",
            "description": "B2B contact and company data enrichment platform providing verified prospect and firmographic intelligence.",
            "auth_methods": ["API Key"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "Free trial with trial credits; credit packs/subscription for ongoing lookups.",
            "api": {
                "availability": "REST",
                "type": ["REST (v1 API)"],
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
            "secondary_blockers": ["Custom header 'x-api-key' requirement"],
            "evidence": [
                {
                    "claim": "Waterfall.io API authenticates requests using x-api-key header at https://api.waterfall.io.",
                    "url": "https://docs.waterfall.io/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official documentation details x-api-key header format and /v1/prospector enrichment endpoints."
                },
                {
                    "claim": "API keys are generated self-serve in the Waterfall.io account dashboard.",
                    "url": "https://docs.waterfall.io/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation outlines self-serve key generation under Settings."
                }
            ],
            "confidence": 0.95,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Standard B2B data enrichment API; high agent suitability for sales workflows."]
        },
        {
            "app": "Clay",
            "category": "Data, SEO and Scraping",
            "description": "AI-powered data enrichment and outbound prospecting platform integrating 50+ data providers.",
            "auth_methods": ["API Key", "Bearer Token", "Webhooks"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "14-day free trial (100 credits) or Starter plan required for API/webhook automation.",
            "api": {
                "availability": "REST",
                "type": ["REST", "Webhook Ingestion"],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/clay-inc/clay-mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Credit consumption across underlying integrated data providers"],
            "evidence": [
                {
                    "claim": "Clay supports incoming webhooks and API Key authentication for programmatic table updates.",
                    "url": "https://library.clay.com/docs/integrations/api",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Clay University docs describe API key authentication, webhook triggers, and row insertion endpoints."
                },
                {
                    "claim": "API keys can be generated self-serve under Workspace Settings > API Keys.",
                    "url": "https://library.clay.com/docs/settings/api-keys",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation details self-serve API key creation on active workspaces."
                }
            ],
            "confidence": 0.96,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Highly composable; powerful for multi-provider waterfall data enrichment."]
        }
    ]
