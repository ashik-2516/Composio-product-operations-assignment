# scripts/cat10_ai_media.py
# Category 10: AI, Research and Media-native (Apps 91 - 100)

def get_cat10_apps():
    return [
        {
            "app": "NotebookLM",
            "category": "AI, Research and Media-native",
            "description": "AI-powered personalized research assistant by Google for querying source documents, generating notes, and audio summaries (Enterprise companion via Gemini for Google Cloud).",
            "auth_methods": [
                "Google Cloud IAM (Service Account Key / ADC)",
                "OAuth 2.0 (Bearer Token)"
            ],
            "credential_access": "ADMIN_APPROVAL",
            "free_or_trial_access": "Consumer app (notebooklm.google.com) is free web-only with zero public APIs; enterprise programmatic companion API requires Google Cloud project enablement and Gemini Enterprise subscriptions.",
            "api": {
                "availability": "LIMITED_API",
                "type": [
                    "REST (https://cloudaicompanion.googleapis.com/v1)",
                    "CLI (gcloud gemini and gcloud beta gemini)"
                ],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "NO_MCP_FOUND",
                "official": "None",
                "url": ""
            },
            "buildability": "LOW",
            "primary_blocker": "No public consumer API; Enterprise companion capabilities require Google Cloud Gemini Enterprise IAM enablement",
            "secondary_blockers": [
                "GCP project location enablement (geminiGcpEnablementSettings and settingBindings)",
                "Service endpoint (cloudaicompanion.googleapis.com) requires IAM service account credentials and discovery spec",
                "Consumer NotebookLM audio overviews/notes remain unexposed to public developer API keys"
            ],
            "evidence": [
                {
                    "claim": "Programmatic AI companion, codebase index management, and tool settings are exposed via the Gemini for Google Cloud API service endpoint https://cloudaicompanion.googleapis.com and gcloud gemini CLI.",
                    "url": "https://docs.cloud.google.com/gemini/docs/api/reference/rest",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Google Cloud API reference documents service cloudaicompanion.googleapis.com, discovery document https://cloudaicompanion.googleapis.com/$discovery/rest?version=v1, and REST resources for codeRepositoryIndexes, repositoryGroups, codeToolsSettings, dataSharingWithGoogleSettings, geminiGcpEnablementSettings, loggingSettings, and releaseChannelSettings."
                },
                {
                    "claim": "Consumer NotebookLM (notebooklm.google.com) is a standalone web application without public developer API keys or REST endpoints.",
                    "url": "https://notebooklm.google.com/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Consumer product FAQ confirms access is limited to web UI without standalone developer API keys."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": True,
            "uncertainties": ["Potential future release of public consumer NotebookLM API endpoints via Google AI Studio / Vertex AI"],
            "research_notes": [
                "Disentangled consumer NotebookLM from enterprise Google Cloud Gemini services (cloudaicompanion.googleapis.com); consumer tool has no public API; enterprise requires GCP IAM."
            ]
        },
        {
            "app": "Otter AI",
            "category": "AI, Research and Media-native",
            "description": "AI meeting assistant that records audio, writes notes, captures slides, and generates meeting summaries.",
            "auth_methods": ["OAuth 2.0", "Bearer Token", "API Key"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "Free Basic plan available; full MCP server and Enterprise API require Business/Enterprise tier.",
            "api": {
                "availability": "REST",
                "type": ["REST", "MCP Server (Official)"],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP",
                "official": "Vendor-official",
                "url": "https://help.otter.ai"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Paid plan required for enterprise transcript search via MCP"],
            "evidence": [
                {
                    "claim": "Otter.ai provides an official Model Context Protocol (MCP) server at https://mcp.otter.ai/mcp.",
                    "url": "https://help.otter.ai",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Otter.ai Help Center documents native MCP server integration using OAuth 2.0 for AI assistants like Claude."
                },
                {
                    "claim": "Otter operates as both an MCP server (exposing meeting transcripts) and MCP client.",
                    "url": "https://help.otter.ai",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Product announcements detail bidirectional MCP connectivity for workspaces."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["First-party official MCP server makes Otter an exceptional candidate for meeting intelligence tools."]
        },
        {
            "app": "Fathom",
            "category": "AI, Research and Media-native",
            "description": "AI meeting recorder and transcription tool for Zoom, Google Meet, and Microsoft Teams that generates notes.",
            "auth_methods": ["API Key (X-Api-Key Header)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier available with self-serve API key generation in user settings.",
            "api": {
                "availability": "REST",
                "type": ["REST", "MCP Server (Official)"],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP",
                "official": "Vendor-official",
                "url": "https://fathom.video"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["Rate limit of 60 calls/minute (30 calls/minute for transcripts)"],
            "evidence": [
                {
                    "claim": "Fathom API authenticates using X-Api-Key header and supports OAuth 2.0 for public integrations.",
                    "url": "https://fathom.video",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Fathom API documentation details X-Api-Key header format, official Python/TypeScript SDKs, and official MCP server."
                },
                {
                    "claim": "API keys can be generated self-serve under User Settings > API Access.",
                    "url": "https://fathom.video",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "User dashboard provides instant API key creation on any active user account."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Official MCP server and simple X-Api-Key authentication make this an easy win."]
        },
        {
            "app": "Consensus",
            "category": "AI, Research and Media-native",
            "description": "AI-powered academic search engine delivering evidence, summaries, and consensus from 200M+ peer-reviewed research papers.",
            "auth_methods": ["OAuth 2.0 (PKCE)", "API Key (x-api-key / Bearer Token)", "No Auth (Public MCP Tier)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free tier with no account required (3 papers/search unlimited) or free account (10 papers/search, 30/mo); official first-party MCP server at https://mcp.consensus.app/mcp.",
            "api": {
                "availability": "REST",
                "type": ["REST (/v1/search)", "MCP Server (Official HTTP Transport)"],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP",
                "official": "Vendor-official",
                "url": "https://mcp.consensus.app/mcp"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": [
                "ChatGPT Deep Research 'fetch' tool currently restricted to ChatGPT client; other MCP clients use 'search' tool",
                "Rate limit backoff (429 handling) required for high-frequency automated batch searches"
            ],
            "evidence": [
                {
                    "claim": "Consensus provides an official vendor-hosted MCP server at https://mcp.consensus.app/mcp supporting OAuth 2.0 and Bearer auth across Claude Desktop, ChatGPT, Claude Code, Cursor, and VS Code Copilot.",
                    "url": "https://docs.consensus.app/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Consensus MCP documentation specifies endpoint https://mcp.consensus.app/mcp (HTTP transport), search/fetch tool definitions, and OAuth sign-in flows."
                },
                {
                    "claim": "Consensus REST API provides OpenAPI 3.1.0 specification for /v1/search with academic filters (study_types, sjr_max, human, sample_size_min, medical_mode, exclude_preprints).",
                    "url": "https://api.consensus.app",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "OpenAPI documentation specifies https://api.consensus.app/v1/search (replacing legacy /v1/quick_search) authenticated via x-api-key header or enterprise Bearer token."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": [
                "First-party vendor MCP server makes Consensus an immediate high-priority research tool for agents; no upfront account needed for basic searches."
            ]
        },
        {
            "app": "Reducto",
            "category": "AI, Research and Media-native",
            "description": "AI-native document parser converting complex PDFs, scans, tables, and forms into LLM-ready markdown.",
            "auth_methods": ["API Key (Bearer Token)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free credits upon signup in Reducto Studio; pay-per-page usage.",
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
            "secondary_blockers": ["Asynchronous parsing jobs for multi-hundred page documents"],
            "evidence": [
                {
                    "claim": "Reducto API authenticates using API keys passed in Authorization: Bearer header (REDUCTO_API_KEY).",
                    "url": "https://docs.reducto.ai/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Reducto documentation details Bearer token authentication and /parse /extract endpoints."
                },
                {
                    "claim": "API keys are generated self-serve at studio.reducto.ai with initial free trial credits.",
                    "url": "https://studio.reducto.ai/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Studio dashboard allows immediate API key generation upon registration."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["High utility for AI agents needing document understanding and table extraction."]
        },
        {
            "app": "Devin",
            "category": "AI, Research and Media-native",
            "description": "Autonomous AI software engineering agent platform by Cognition for building, debugging, and testing code.",
            "auth_methods": ["API Key (Service User Token cog_)", "Bearer Token"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "Paid Devin subscription/seat required to provision Service Users and access API.",
            "api": {
                "availability": "REST",
                "type": ["REST (v3 API)", "MCP Server (Official)"],
                "breadth": "BROAD",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP",
                "official": "Vendor-official",
                "url": "https://docs.devin.ai"
            },
            "buildability": "HIGH",
            "primary_blocker": "Devin paid subscription requirement",
            "secondary_blockers": ["Requires Organization Admin role to create Service User tokens"],
            "evidence": [
                {
                    "claim": "Devin provides an official MCP server at https://mcp.devin.ai/mcp and REST API v3 at docs.devin.ai.",
                    "url": "https://docs.devin.ai/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official Cognition documentation outlines Devin MCP server configuration, session management, and cog_ API keys."
                },
                {
                    "claim": "Service user tokens can be generated under Devin Organization Settings.",
                    "url": "https://docs.devin.ai/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation details self-serve Service User key creation for customer accounts."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Official first-party MCP server allows multi-agent orchestration of Devin coding sessions."]
        },
        {
            "app": "higgsfield",
            "category": "AI, Research and Media-native",
            "description": "Generative AI platform and CLI suite for video generation, character animation, and camera controls.",
            "auth_methods": ["API Key", "Bearer Token (CLI Auth Token)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free credits upon signup; pay-per-generation credits for video models.",
            "api": {
                "availability": "REST",
                "type": ["REST", "CLI (@higgsfield/cli)"],
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
            "secondary_blockers": ["Long generation latency (30-120s) for high-resolution video rendering"],
            "evidence": [
                {
                    "claim": "Higgsfield provides a CLI and REST API authenticated via auth tokens (higgsfield auth login).",
                    "url": "https://github.com/higgsfield-ai/cli",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official GitHub CLI repository details installation, authentication, and programmatic model creation."
                },
                {
                    "claim": "Developers can install the CLI self-serve via npm or brew and generate credentials.",
                    "url": "https://higgsfield.ai/",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Higgsfield portal provides self-serve signup and credit purchasing."
                }
            ],
            "confidence": 0.96,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Video generation models accessible via structured CLI flags and REST endpoints."]
        },
        {
            "app": "Mermaid CLI",
            "category": "AI, Research and Media-native",
            "description": "Command-line interface and programmatic library for converting Mermaid markdown text definitions into SVG, PNG, and PDF diagrams.",
            "auth_methods": ["None (Open Source CLI)"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Completely free open-source software (@mermaid-js/mermaid-cli) on npm and GitHub.",
            "api": {
                "availability": "CLI_ONLY",
                "type": [
                    "CLI (mmdc)",
                    "Node.js API (@mermaid-js/mermaid-cli)",
                    "Docker/Podman (minlag/mermaid-cli, ghcr.io/mermaid-js/mermaid-cli/mermaid-cli)",
                    "npx (-p @mermaid-js/mermaid-cli mmdc)"
                ],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "COMMUNITY_MCP",
                "official": "Community",
                "url": "https://github.com/mermaid-js/mermaid-cli"
            },
            "buildability": "MEDIUM",
            "primary_blocker": "CLI only / No hosted cloud REST API",
            "secondary_blockers": [
                "Puppeteer/Chromium headless sandbox requirements in containerized/server environments",
                "Homebrew distribution deprecated/unsupported; requires npm, npx, Docker, or Node.js API execution"
            ],
            "evidence": [
                {
                    "claim": "Mermaid CLI is executed locally with mmdc command (mmdc -i input.mmd -o output.svg), npx, or Node.js API import { run } from '@mermaid-js/mermaid-cli'.",
                    "url": "https://github.com/mermaid-js/mermaid-cli",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official GitHub repository documents npm install -g @mermaid-js/mermaid-cli, npx runner, Node.js API, and Docker/Podman container images."
                },
                {
                    "claim": "No authentication or cloud account required; 100% open source under MIT license.",
                    "url": "https://github.com/mermaid-js/mermaid-cli/blob/master/LICENSE",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Repository confirms MIT license, offline local execution, custom CSS animation options, and Markdown transform mode."
                }
            ],
            "confidence": 0.99,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": [
                "Must be executed as a local subprocess or containerized tool rather than HTTP API. Agents should invoke via npx or container volume mount (:z for Podman)."
            ]
        },
        {
            "app": "YouTube Transcript",
            "category": "AI, Research and Media-native",
            "description": "Hosted API service for extracting automated and manual transcripts, timestamps, and video metadata.",
            "auth_methods": ["API Key", "Bearer Token"],
            "credential_access": "SELF_SERVE",
            "free_or_trial_access": "Free trial tier available on TranscriptAPI.com; paid plans for high-volume extraction.",
            "api": {
                "availability": "REST",
                "type": ["REST", "MCP Server (Official)"],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP",
                "official": "Vendor-official",
                "url": "https://transcriptapi.com"
            },
            "buildability": "HIGH",
            "primary_blocker": "None",
            "secondary_blockers": ["YouTube anti-scraping countermeasures managed transparently by vendor"],
            "evidence": [
                {
                    "claim": "TranscriptAPI.com provides REST endpoints and an official MCP server for retrieving YouTube video transcripts.",
                    "url": "https://transcriptapi.com",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Official TranscriptAPI documentation outlines Bearer API key authentication and MCP integration guide."
                },
                {
                    "claim": "API keys can be generated self-serve upon creating an account.",
                    "url": "https://transcriptapi.com",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Platform provides instant self-serve API key issuance and quickstart examples."
                }
            ],
            "confidence": 0.98,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Official MCP server and clean JSON structured output make this an immediate easy win."]
        },
        {
            "app": "Grain",
            "category": "AI, Research and Media-native",
            "description": "AI meeting workspace for recording, transcribing, and summarizing customer conversations and sales calls.",
            "auth_methods": ["Bearer Token (Personal / Workspace Access Token)", "OAuth 2.0"],
            "credential_access": "SELF_SERVE_WITH_PLAN_REQUIREMENT",
            "free_or_trial_access": "Free trial available; Business/Enterprise plan required for API token generation.",
            "api": {
                "availability": "REST",
                "type": ["REST (Public API)"],
                "breadth": "MEDIUM",
                "documentation_quality": "HIGH"
            },
            "mcp": {
                "status": "OFFICIAL_MCP_SUPPORTED",
                "official": "Vendor-supported",
                "url": "https://developers.grain.com"
            },
            "buildability": "HIGH",
            "primary_blocker": "Business or Enterprise plan required for API access",
            "secondary_blockers": ["Distinction between Personal Access Tokens (PAT) and Workspace Access Tokens (WAT)"],
            "evidence": [
                {
                    "claim": "Grain Public REST API authenticates using Bearer tokens at https://api.grain.com/_/public-api/.",
                    "url": "https://developers.grain.com",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Grain developer documentation outlines Authorization: Bearer <TOKEN> format and meeting transcript endpoints."
                },
                {
                    "claim": "API access is available on Business and Enterprise plans in Settings > Integrations > API.",
                    "url": "https://developers.grain.com",
                    "source_type": "TIER 1 — OFFICIAL PRIMARY SOURCES",
                    "evidence_summary": "Documentation details plan requirements and self-serve token generation in workspace settings."
                }
            ],
            "confidence": 0.97,
            "human_verification_required": False,
            "uncertainties": [],
            "research_notes": ["Clean REST endpoints for meeting summaries, key highlights, and full speaker-diarized transcripts."]
        }
    ]
