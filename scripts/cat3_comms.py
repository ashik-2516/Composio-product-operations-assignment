# scripts/cat3_comms.py
# Category 3: Communications and Messaging (Apps 21 - 30)

def get_cat3_apps():
    return [
        {
            "app": "Slack",
            "category": "Communications and Messaging",
            "description": "Team communication platform providing channels, direct messaging, workflow automations, and bots.",
            "auth_methods": ["OAuth 2.0", "Bot Token", "User Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier with instant developer app and bot token creation.",
            "api": {
                "availability": "REST",
                "type": ["REST", "WebSocket (Socket Mode)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://github.com/modelcontextprotocol/servers/tree/main/src/slack"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Granular bot scope management (chat:write, channels:history)"],
            "evidence": [
                {
                    "claim": "Slack uses OAuth 2.0 and provides Bot User OAuth Tokens (xoxb-) for API calls.",
                    "url": "https://api.slack.com/authentication/oauth-v2",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Slack API documentation details OAuth v2 authorization flow, token scopes, and Bearer token headers."
                },
                {
                    "claim": "Developers can create Slack apps and bots for free on any workspace.",
                    "url": "https://api.slack.com/apps",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Slack App Management portal allows immediate self-serve app creation and token generation."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Benchmark app for AI agent tool integration; high socket mode and web API maturity."]
        },
        {
            "app": "Twilio",
            "category": "Communications and Messaging",
            "description": "Cloud communications platform enabling SMS, voice calls, video, and verification APIs.",
            "auth_methods": ["API Key", "Basic Authentication", "Bearer Token (JWT)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free trial with test credit balance and sandbox phone numbers.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/twilio/twilio-mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Regulatory phone number registration and A2P 10DLC compliance"],
            "evidence": [
                {
                    "claim": "Twilio authenticates API requests using HTTP Basic Auth with Account SID and Auth Token or API Keys.",
                    "url": "https://www.twilio.com/docs/usage/api",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Twilio API reference documents Account SID + Auth Token Basic Auth and API Key secret headers."
                },
                {
                    "claim": "Twilio provides free trial accounts with immediate access to credentials in the Console.",
                    "url": "https://www.twilio.com/try-twilio",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Self-serve signup grants test credentials and sandbox phone numbers."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Gold standard developer experience; extensive SDK support across all languages."]
        },
        {
            "app": "Zoho Cliq",
            "category": "Communications and Messaging",
            "description": "Business team messaging and collaboration platform with audio/video calls and bot tools.",
            "auth_methods": ["OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free plan (up to 100 users) and free Zoho Developer Console.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/zoho/cliq-mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Multi-region data center token endpoints (.com, .eu, .in)"],
            "evidence": [
                {
                    "claim": "Zoho Cliq REST API authenticates using OAuth 2.0 Bearer tokens.",
                    "url": "https://www.zoho.com/cliq/developer/help/rest-apis/oauth2.html",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Zoho Cliq developer documentation outlines OAuth 2.0 scopes, token generation, and authorization headers."
                },
                {
                    "claim": "Developers can configure bots and integrations directly in Cliq developer console.",
                    "url": "https://cliq.zoho.com/company/developer",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Zoho Cliq provides self-serve bot building, webhook creation, and command registrations."
                }
            ],
            "confidence": 0.96,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Good messaging and bot API surface; requires handling multi-region Zoho auth."]
        },
        {
            "app": "Lark (Larksuite)",
            "category": "Communications and Messaging",
            "description": "Enterprise collaboration platform combining chat, video meetings, calendar, and documents.",
            "auth_methods": ["Bearer Token", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier (up to 50 seats) with open developer platform access.",
            "api": {
                "availability": "REST",
                "type": ["REST", "WebSocket"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/larksuite/mcp-server-lark"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Distinction between tenant_access_token, app_access_token, and user_access_token"],
            "evidence": [
                {
                    "claim": "Lark Open Platform uses Bearer tokens obtained via App ID and App Secret (tenant_access_token / app_access_token).",
                    "url": "https://open.larksuite.com/document/home/introduction-to-scope-and-authorization/obtain-app_access_token-or-tenant_access_token",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Lark Open Platform documentation details token exchange APIs and Authorization: Bearer <token> headers."
                },
                {
                    "claim": "Developers can create custom enterprise apps self-serve on Lark Developer Console.",
                    "url": "https://open.larksuite.com/app",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Lark developer portal enables instant custom app creation, permissions configuration, and test deployment."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Very rich API covering messaging, base (tables), calendar, and docs."]
        },
        {
            "app": "Pumble",
            "category": "Communications and Messaging",
            "description": "Team chat and business communication app for team messaging, channels, and file sharing.",
            "auth_methods": ["API Key", "Bearer Token", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free plan available with API addon support.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "MEDIUM",
                "documentation_quality": "MEDIUM"
            },
            "mcp": {
                "status": "NO_MCP_FOUND",
                "official": "None",
                "url": ""
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Dual header requirements for custom apps (x-app-token + token)"],
            "evidence": [
                {
                    "claim": "Pumble supports direct API keys via /api-keys command and SDK header auth (x-app-token and token).",
                    "url": "https://pumble.com/help/api/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Pumble Help Center documents API key generation via API addon and app token authorization."
                },
                {
                    "claim": "Pumble provides a free plan where the API addon can be installed self-serve.",
                    "url": "https://pumble.com/pricing",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Pumble pricing page confirms free tier availability with access to app integrations."
                }
            ],
            "confidence": 0.95,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Straightforward channel and message CRUD API; SDK docs hosted on CAKE.com marketplace."]
        },
        {
            "app": "Discord",
            "category": "Communications and Messaging",
            "description": "Voice, video, and text communication service for community servers and direct messaging.",
            "auth_methods": ["Bot Token", "OAuth 2.0", "Bearer Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Completely free Developer Portal with instant bot creation.",
            "api": {
                "availability": "REST",
                "type": ["REST", "WebSocket (Gateway API)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/modelcontextprotocol/servers/tree/main/src/discord"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Privileged Gateway Intents (Message Content, Server Members) requiring toggle"],
            "evidence": [
                {
                    "claim": "Discord API authenticates bots using Authorization: Bot <Token> and user apps using OAuth 2.0 Bearer tokens.",
                    "url": "https://discord.com/developers/docs/reference#authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Discord Developer documentation outlines Bot token headers, OAuth 2.0 authorization, and rate limits."
                },
                {
                    "claim": "Developers can register applications and bots for free on Discord Developer Portal.",
                    "url": "https://discord.com/developers/applications",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Self-serve developer portal allows immediate bot creation, token resets, and intent configuration."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Exceptional API ecosystem; ideal for AI agent dispatch and interaction."]
        },
        {
            "app": "Telegram",
            "category": "Communications and Messaging",
            "description": "Cloud-based instant messaging platform offering fast, encrypted chat, bots, and channels.",
            "auth_methods": ["Bot API Token", "API Key (App API ID/Hash for MTProto)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Completely free bot creation and unlimited API usage.",
            "api": {
                "availability": "REST",
                "type": ["REST (Bot API)", "MTProto Binary Protocol"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/telegram-mcp/telegram-mcp-server"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Bot token passed in URL path (https://api.telegram.org/bot<token>/METHOD)"],
            "evidence": [
                {
                    "claim": "Telegram Bot API uses HTTP token-based authentication via URL path.",
                    "url": "https://core.telegram.org/bots/api#authorizing-your-bot",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Telegram Core Bot API documentation outlines bot token authorization format and method invocation."
                },
                {
                    "claim": "Bots and tokens are created instantly and for free via @BotFather in Telegram.",
                    "url": "https://core.telegram.org/bots/features#botfather",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official BotFather guide explains instant token generation without credit cards or reviews."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Zero-friction bot creation; one of the easiest APIs to automate with AI agents."]
        },
        {
            "app": "WhatsApp Business",
            "category": "Communications and Messaging",
            "description": "Enterprise customer messaging platform by Meta for business messaging, notifications, and customer support via Cloud API.",
            "auth_methods": [
                "OAuth 2.0 (Meta App Review)",
                "Bearer Token (Permanent System User Access Token)",
                "Temporary Sandbox Access Token"
            ],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "Free sandbox development environment with test phone numbers via Meta for Developers dashboard; production requires Meta Business Portfolio verification.",
            "api": {
                "availability": "REST",
                "type": [
                    "REST (WhatsApp Cloud API v23.0 via Graph API)",
                    "Webhooks (Real-time Message Events & Delivery Receipts)"
                ],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/whatsapp-mcp/mcp-server"
            },
            "buildability": "MEDIUM",
            "primary_blocker": "Meta Business Portfolio Verification & App Review for production live phone numbers",
            "secondary_blockers": [
                "24-hour customer service window rule for non-template messages; pre-approved templates required for outbound business-initiated messages",
                "System User permanent token requires granular permissions: business_management, whatsapp_business_messaging, whatsapp_business_management"
            ],
            "evidence": [
                {
                    "claim": "WhatsApp Cloud API allows developers to send messages via POST https://graph.facebook.com/v23.0/<PHONE_NUMBER_ID>/messages with Bearer authorization and receive real-time webhook payloads for messages and delivery receipts.",
                    "url": "https://developers.facebook.com/docs/whatsapp/cloud-api/get-started",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Meta WhatsApp Cloud API guide documents test phone number provisioning, System User permanent access token generation, 24-hour customer service window, and webhook JSON event payloads."
                },
                {
                    "claim": "Production usage requires Meta Business Portfolio verification, WABA ID association, and business phone number registration.",
                    "url": "https://developers.facebook.com/docs/whatsapp/overview/business-verification",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Meta documentation confirms sandbox testing is immediate, while live customer messaging requires business compliance verification."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": True,
            "uncertainties": ["Timeframe and regional documentation required for Meta Business Portfolio verification approval"],
            "research_notes": [
                "Developers can instantly prototype with test phone numbers in the Meta App Dashboard; scaling to production requires System User token creation and business verification."
            ]
        },
        {
            "app": "Aircall",
            "category": "Communications and Messaging",
            "description": "Cloud-based voice call center and phone system software designed for sales and support teams.",
            "auth_methods": ["Basic Authentication", "API Key", "OAuth 2.0"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "7-day free trial or paid plan required to generate API ID/Token.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/aircall/aircall-mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "Paid plan requirement after trial",
            "secondary_blockers": ["Rate limit of 60 requests/minute per token"],
            "evidence": [
                {
                    "claim": "Aircall API supports HTTP Basic Auth with API ID and API Token, and OAuth 2.0 for public integrations.",
                    "url": "https://developer.aircall.io/tutorials/authenticating-with-the-api/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Aircall developer documentation outlines HTTP Basic Auth (api_id:api_token) and OAuth 2.0 Bearer authentication."
                },
                {
                    "claim": "API credentials can be generated in Dashboard > Company > Integrations & API.",
                    "url": "https://developer.aircall.io/tutorials/creating-api-keys/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation explains self-serve creation of API keys in company dashboard."
                }
            ],
            "confidence": 0.96,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Well-structured REST API covering calls, recordings, contacts, and webhooks."]
        },
        {
            "app": "Vonage",
            "category": "Communications and Messaging",
            "description": "Communications API platform providing SMS, voice, video, verification, and conversational commerce APIs.",
            "auth_methods": ["API Key", "API Secret", "JWT (JSON Web Token)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free developer account with 2 Euro test balance upon registration.",
            "api": {
                "availability": "REST",
                "type": ["REST"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/vonage/vonage-mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Dual auth model: API Key/Secret for SMS vs Private Key/JWT for Voice/VBC"],
            "evidence": [
                {
                    "claim": "Vonage API uses API Key/Secret for SMS/Verify APIs and Application ID + Private Key (JWT) for Voice/Messages APIs.",
                    "url": "https://developer.vonage.com/en/getting-started/concepts/authentication",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Vonage Developer documentation details basic auth key/secret and JWT bearer token generation with private keys."
                },
                {
                    "claim": "Developers can sign up for free and generate API keys immediately in the Vonage API Dashboard.",
                    "url": "https://dashboard.nexmo.com/sign-up",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Vonage Developer dashboard offers self-serve registration and instant API key issuance."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["High quality documentation with interactive API explorers and broad SDK availability."]
        }
    ]
