# scripts/cat5_ecommerce.py
# Category 5: Ecommerce (Apps 41 - 50)

def get_cat5_apps():
    return [
        {
            "app": "Shopify",
            "category": "Ecommerce",
            "description": "Multi-channel commerce platform for online storefronts, inventory, checkout, and retail point-of-sale.",
            "auth_methods": ["OAuth 2.0", "Access Token (Admin API)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free Shopify Partner account with unlimited development stores and API access.",
            "api": {
                "availability": "REST_AND_GRAPHQL",
                "type": ["REST", "GraphQL", "Storefront API"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/shopify/mcp-server-shopify"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["GraphQL-preferred migration for latest product features"],
            "evidence": [
                {
                    "claim": "Shopify supports OAuth 2.0 for public apps and Admin API Access Tokens for custom apps.",
                    "url": "https://shopify.dev/docs/apps/auth/oauth",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Shopify.dev documentation outlines OAuth 2.0 authorization code flow and X-Shopify-Access-Token headers."
                },
                {
                    "claim": "Developers can create free Partner accounts and test development stores indefinitely.",
                    "url": "https://www.shopify.com/partners",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Shopify Partner portal provides free developer registration and store sandboxes."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Gold standard ecommerce API with complete CRUD over products, orders, customers, and fulfillment."]
        },
        {
            "app": "WooCommerce",
            "category": "Ecommerce",
            "description": "Open-source, customizable e-commerce plugin built on WordPress for online merchants.",
            "auth_methods": ["Basic Authentication", "API Key (Consumer Key / Secret)", "OAuth 1.0a"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Completely free open-source software; self-hostable on any WordPress instance.",
            "api": {
                "availability": "REST",
                "type": ["REST (WooCommerce REST API v3)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/woocommerce-mcp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Requires HTTPS for Basic Auth with Consumer Key/Secret"],
            "evidence": [
                {
                    "claim": "WooCommerce REST API authenticates using Consumer Key and Consumer Secret via HTTP Basic Auth over HTTPS.",
                    "url": "https://woocommerce.github.io/woocommerce-rest-api-docs/#authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "WooCommerce REST API documentation details HTTP Basic Authentication and query parameter key passing."
                },
                {
                    "claim": "Keys can be generated self-serve under WooCommerce > Settings > Advanced > REST API.",
                    "url": "https://woocommerce.com/document/woocommerce-rest-api/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official documentation explains direct key creation with Read, Write, or Read/Write permissions."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Extremely widespread self-serve open-source platform; very easy tool integration."]
        },
        {
            "app": "BigCommerce",
            "category": "Ecommerce",
            "description": "SaaS ecommerce platform offering scalable catalog management, checkout, and multi-storefront APIs.",
            "auth_methods": ["OAuth 2.0", "API Token (X-Auth-Token)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "15-day free trial or free BigCommerce Developer Sandbox account.",
            "api": {
                "availability": "REST_AND_GRAPHQL",
                "type": ["REST (v3)", "GraphQL (Storefront API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/bigcommerce-mcp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Store hash required in API URL paths (https://api.bigcommerce.com/stores/{store_hash}/v3/)"],
            "evidence": [
                {
                    "claim": "BigCommerce API v3 uses X-Auth-Token header and OAuth 2.0 for app authentication.",
                    "url": "https://developer.bigcommerce.com/docs/start/authentication/api-accounts",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "BigCommerce developer documentation details API Accounts, X-Auth-Token header, and Client ID/Secret OAuth."
                },
                {
                    "claim": "Developers can create API accounts in store settings or register developer sandbox accounts.",
                    "url": "https://developer.bigcommerce.com/docs/start/about/sandbox",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation explains self-serve developer sandbox store creation."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Very mature developer portal with extensive OpenAPI 3 specs."]
        },
        {
            "app": "Salesforce Commerce Cloud",
            "category": "Ecommerce",
            "description": "Enterprise ecommerce platform (B2C/B2B Commerce) for high-volume digital storefronts.",
            "auth_methods": ["OAuth 2.0", "JWT (SLAS / OCAPI token)"],
            "credential_access": "ADMIN_APPROVAL",
            "free_or_trial_access": "Enterprise license required; sandboxes require Salesforce Account Manager credentials.",
            "api": {
                "availability": "REST_AND_GRAPHQL",
                "type": ["REST (SCAPI / OCAPI)", "GraphQL"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "NO_MCP_FOUND",
                "official": "None",
                "url": ""
            },
            "buildability": "MEDIUM",
            "primary_blocker": "Enterprise contract / Salesforce Account Manager gating",
            "secondary_blockers": ["Short-lived SLAS JWT tokens", "Multi-tenant realm configuration"],
            "evidence": [
                {
                    "claim": "Salesforce Commerce API (SCAPI) uses Shopper Login and API Access Service (SLAS) OAuth 2.0 JWTs.",
                    "url": "https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization-for-shopper-apis.html",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Salesforce Developer documentation outlines SLAS OAuth 2.0 authorization code and client credentials flows."
                },
                {
                    "claim": "Accessing Commerce Cloud sandboxes requires credentials provisioned via enterprise Account Manager.",
                    "url": "https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/b2c-account-manager.html",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation details administrator provisioning of API client IDs in enterprise Account Manager."
                }
            ],
            "confidence": 0.94,
            "human_verification_required": True,
            "uncertainties": ["On-demand sandbox trial availability for non-partner developers"],
            "research_notes": ["Enterprise-grade SCAPI; excellent documentation but gated behind enterprise instances."]
        },
        {
            "app": "Magento (Adobe Commerce)",
            "category": "Ecommerce",
            "description": "Open-source and enterprise ecommerce platform for customizable online merchants.",
            "auth_methods": ["Bearer Token", "OAuth 1.0a", "API Key"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Completely free via Magento Open Source; Adobe Commerce Cloud is enterprise paid.",
            "api": {
                "availability": "REST_AND_GRAPHQL",
                "type": ["REST", "GraphQL"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/magento/magento-mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Self-hosting setup required for local open-source testing"],
            "evidence": [
                {
                    "claim": "Magento REST and GraphQL APIs support Bearer tokens (admin/customer) and Integration tokens.",
                    "url": "https://developer.adobe.com/commerce/webapi/get-started/authentication/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Adobe Developer documentation details token-based authentication and integration access tokens."
                },
                {
                    "claim": "Integration tokens can be generated self-serve in Admin Panel > System > Integrations.",
                    "url": "https://developer.adobe.com/commerce/webapi/get-started/create-integration/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official guide illustrates creating integrations with API consumer key and access token."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Complete open source availability gives unblocked developer access."]
        },
        {
            "app": "Squarespace",
            "category": "Ecommerce",
            "description": "Website builder and ecommerce platform for online stores, appointments, and domains.",
            "auth_methods": ["API Key", "OAuth 2.0", "Bearer Token"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "14-day free trial or Commerce Advanced plan required for API key generation.",
            "api": {
                "availability": "REST",
                "type": ["REST (Commerce API)"],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/squarespace-mcp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "Commerce Advanced subscription required for API keys",
            "secondary_blockers": ["OAuth apps require approval for public marketplace listing"],
            "evidence": [
                {
                    "claim": "Squarespace Commerce API authenticates using API Keys in Authorization: Bearer <API_KEY> header and OAuth 2.0.",
                    "url": "https://developers.squarespace.com/commerce-apis/overview",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Squarespace Developer docs outline Bearer API key authentication and OAuth 2.0 endpoints."
                },
                {
                    "claim": "API keys can be generated in Settings > Advanced > Developer API Keys on Commerce Advanced plans.",
                    "url": "https://support.squarespace.com/hc/en-us/articles/360000840428-Squarespace-Commerce-APIs",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Support documentation states API key creation requires Commerce Advanced tier."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Well-documented endpoints covering orders, inventory, transactions, and webhook events."]
        },
        {
            "app": "Ecwid",
            "category": "Ecommerce",
            "description": "Embeddable ecommerce widget and shopping cart platform for websites and social media.",
            "auth_methods": ["OAuth 2.0", "Bearer Token", "Secret Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free developer account with instant API sandbox store creation.",
            "api": {
                "availability": "REST",
                "type": ["REST (Ecwid REST API v3)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/ecwid-mcp/mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Token passed as query param 'token' or Bearer header"],
            "evidence": [
                {
                    "claim": "Ecwid REST API v3 authenticates using OAuth 2.0 Bearer tokens and Secret Access Tokens.",
                    "url": "https://api-docs.ecwid.com/reference/overview",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Ecwid API docs detail OAuth 2.0 authorization code flow and access token header passing."
                },
                {
                    "claim": "Developers can register for free developer accounts to build and test apps.",
                    "url": "https://api-docs.ecwid.com/reference/getting-started",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Developer portal guides users through self-serve registration and app client creation."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Broad REST API covering catalog, orders, customers, and instant webhooks."]
        },
        {
            "app": "Gumroad",
            "category": "Ecommerce",
            "description": "E-commerce platform for creators to sell digital products, memberships, and courses.",
            "auth_methods": ["OAuth 2.0", "Bearer Token (Access Token)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free account creation with instant personal access token generation.",
            "api": {
                "availability": "REST",
                "type": ["REST (v2 API)"],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/gumroad/mcp-server-gumroad"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limit of 60 requests/minute"],
            "evidence": [
                {
                    "claim": "Gumroad API v2 uses OAuth 2.0 and Bearer Access Tokens in Authorization header.",
                    "url": "https://gumroad.com/api",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Gumroad API documentation specifies OAuth 2.0 endpoints and Bearer token header authentication."
                },
                {
                    "claim": "Users can generate application tokens directly under Settings > Advanced > Applications.",
                    "url": "https://gumroad.com/api#authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation explains self-serve application registration and access token generation."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Clean and simple REST endpoints for products, sales, subscribers, and license keys."]
        },
        {
            "app": "Amazon Selling Partner",
            "category": "Ecommerce",
            "description": "Comprehensive suite of REST-based APIs for Amazon sellers and vendors to manage orders, inventory, listings, fulfillment, and financial events.",
            "auth_methods": [
                "Login with Amazon (LWA) OAuth 2.0 (x-amz-access-token Header)",
                "Restricted Data Token (RDT via Tokens API for PII)",
                "Client Credentials Grant (for Grantless Operations)"
            ],
            "credential_access": "PARTNER_OR_SALES_GATED",
            "free_or_trial_access": "Requires registered Amazon Seller Central account and approved Developer Profile application with Restricted Data Roles; static, dynamic, and local AI sandboxes available for testing.",
            "api": {
                "availability": "REST",
                "type": [
                    "REST (SP-API / OpenAPI 3.0 / Swagger Models)",
                    "Static & Dynamic Hosted Sandboxes",
                    "Local AI Sandbox (Amazon Bedrock-backed)"
                ],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/amazon-sp-api/mcp-server"
            },
            "buildability": "LOW",
            "primary_blocker": "Developer Profile vetting & Restricted Data Role PII audit",
            "secondary_blockers": [
                "Mandatory Restricted Data Tokens (RDT) for customer PII operations (e.g. Orders and Direct-to-Consumer fulfillment)",
                "Strict User-Agent header formatting rules and 3600-second (1 hour) LWA token rotation",
                "Amazon Data Protection Policy (DPP) compliance audits"
            ],
            "evidence": [
                {
                    "claim": "Amazon SP-API requires exchanging LWA refresh tokens or client credentials at https://api.amazon.com/auth/o2/token for a 3600-second access token passed in x-amz-access-token header with structured user-agent and RDTs for PII.",
                    "url": "https://developer-docs.amazon.com/sp-api/docs/connecting-to-the-selling-partner-api",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official SP-API documentation specifies POST api.amazon.com/auth/o2/token, grant_type=refresh_token/client_credentials, x-amz-access-token header, and grantless scopes (notifications, client_credential rotation, tracking)."
                },
                {
                    "claim": "Amazon provides static, dynamic, and local AI sandboxes (Bedrock-backed on localhost:9001) alongside official Postman collections and OpenAPI Swagger models on GitHub.",
                    "url": "https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official SP-API sandbox guide documents sandbox.sellingpartnerapi-na.amazon.com, x-amzn-api-sandbox static/dynamic objects, and local AI Bedrock simulator."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": True,
            "uncertainties": ["Approval latency for third-party public developer applications requesting Direct-to-Consumer shipping PII"],
            "research_notes": [
                "Extensive REST surface across 40+ microservices (Orders, Feeds, Reports, FBA, Catalog, Finances); high agent utility but gated by strict DPP audits and RDT tokens for PII."
            ]
        },
        {
            "app": "fanbasis",
            "category": "Ecommerce",
            "description": "Creator monetization and checkout platform for digital products and fan experiences (now Commas).",
            "auth_methods": ["API Key", "Bearer Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free account registration with API key access in creator dashboard.",
            "api": {
                "availability": "LIMITED_API",
                "type": ["REST", "SDK (@fanbasis/checkout-core)"],
                "breadth": "NARROW",
                "documentation_quality": "MEDIUM"
            },
            "mcp": {
                "status": "NO_MCP_FOUND",
                "official": "None",
                "url": ""
            },
            "buildability": "MEDIUM",
            "primary_blocker": "Limited public endpoint scope (focuses on checkout and webhooks)",
            "secondary_blockers": ["Rebranding to Commas in progress"],
            "evidence": [
                {
                    "claim": "Fanbasis provides checkout SDKs and API documentation hosted at docs.fanbasis.com.",
                    "url": "https://docs.fanbasis.com",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Fanbasis developer portal documents checkout sessions, webhook handlers, and API key authentication."
                },
                {
                    "claim": "API credentials and webhook endpoints can be configured in account settings.",
                    "url": "https://docs.fanbasis.com",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation specifies self-serve key generation in creator integrations panel."
                }
            ],
            "confidence": 0.91,
            "human_verification_required": True,
            "uncertainties": ["Full extent of REST endpoints outside checkout/webhooks during Commas rebrand"],
            "research_notes": ["Narrow checkout surface; buildable but limited in operational scope compared to full ecommerce platforms."]
        }
    ]
