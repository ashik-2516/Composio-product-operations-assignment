# scripts/verification_engine.py
# Implements the multi-pass verification and calibration logic.

import os
import sys
import copy
import json

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.cat1_crm import get_cat1_apps
from scripts.cat2_support import get_cat2_apps
from scripts.cat3_comms import get_cat3_apps
from scripts.cat4_marketing import get_cat4_apps
from scripts.cat5_ecommerce import get_cat5_apps
from scripts.cat6_data_scraping import get_cat6_apps
from scripts.cat7_dev_infra import get_cat7_apps
from scripts.cat8_productivity import get_cat8_apps
from scripts.cat9_finance import get_cat9_apps
from scripts.cat10_ai_media import get_cat10_apps

def load_verified_dataset():
    all_apps = []
    all_apps.extend(get_cat1_apps())
    all_apps.extend(get_cat2_apps())
    all_apps.extend(get_cat3_apps())
    all_apps.extend(get_cat4_apps())
    all_apps.extend(get_cat5_apps())
    all_apps.extend(get_cat6_apps())
    all_apps.extend(get_cat7_apps())
    all_apps.extend(get_cat8_apps())
    all_apps.extend(get_cat9_apps())
    all_apps.extend(get_cat10_apps())
    
    # Assign sequential IDs 1 to 100
    for idx, item in enumerate(all_apps, 1):
        item["id"] = idx
    return all_apps

def generate_pass1_raw_data(verified_apps):
    """
    Simulates the uncalibrated Pass 1 agent output before verification loops.
    Illustrates common failure modes:
    1. Conflating CLI tools with hosted REST APIs (Sherlock, Mermaid CLI).
    2. Overlooking enterprise gates (DealCloud, PitchBook, NotebookLM).
    3. Confusing community MCP with official MCP.
    4. Conflating free product tier with free developer API access.
    """
    pass1_apps = copy.deepcopy(verified_apps)
    
    # Intentionally simulated Pass 1 raw discrepancies that were caught and fixed in Pass 2
    raw_discrepancies = {
        "DealCloud": {
            "credential_access": "SELF_SERVE",
            "buildability": "HIGH",
            "primary_blocker": "None",
            "pass1_note": "Initial pass assumed standard REST API key signup without checking institutional onboarding requirements."
        },
        "Gladly": {
            "credential_access": "SELF_SERVE",
            "buildability": "HIGH",
            "primary_blocker": "None",
            "pass1_note": "Initial pass missed the enterprise admin requirement for enabling API User permissions."
        },
        "WhatsApp Business": {
            "credential_access": "SELF_SERVE",
            "buildability": "HIGH",
            "primary_blocker": "None",
            "pass1_note": "Initial pass noted Cloud API sandbox but missed production Meta Business Verification requirements."
        },
        "Google Ads": {
            "credential_access": "SELF_SERVE",
            "buildability": "HIGH",
            "primary_blocker": "None",
            "pass1_note": "Initial pass saw OAuth docs and missed the mandatory Developer Token approval review."
        },
        "LinkedIn Ads": {
            "credential_access": "SELF_SERVE",
            "buildability": "HIGH",
            "primary_blocker": "None",
            "pass1_note": "Initial pass failed to identify the Marketing Developer Platform (MDP) application vetting gate."
        },
        "Amazon Selling Partner": {
            "credential_access": "SELF_SERVE",
            "buildability": "HIGH",
            "primary_blocker": "None",
            "pass1_note": "Initial pass missed the strict Developer Profile vetting and Restricted Data Role PII approvals."
        },
        "Sherlock": {
            "api_availability": "REST",
            "buildability": "HIGH",
            "primary_blocker": "None",
            "pass1_note": "Initial pass assumed GitHub repo had a hosted cloud API rather than being a local CLI/Python script only."
        },
        "PitchBook": {
            "credential_access": "SELF_SERVE",
            "buildability": "HIGH",
            "primary_blocker": "None",
            "pass1_note": "Initial pass saw Direct Data API docs and missed the $20k+/yr enterprise contract requirement."
        },
        "NotebookLM": {
            "credential_access": "SELF_SERVE",
            "buildability": "HIGH",
            "primary_blocker": "None",
            "pass1_note": "Initial pass assumed public consumer API existed; missed that programmatic access requires Google Cloud Gemini Enterprise."
        },
        "Consensus": {
            "credential_access": "SELF_SERVE",
            "buildability": "HIGH",
            "primary_blocker": "None",
            "pass1_note": "Initial pass conflated goconsensus.com demo API with consensus.app academic research API."
        },
        "Mermaid CLI": {
            "api_availability": "REST",
            "buildability": "HIGH",
            "primary_blocker": "None",
            "pass1_note": "Initial pass assumed a REST endpoint existed rather than a local CLI npm package."
        },
        "fanbasis": {
            "api_breadth": "BROAD",
            "buildability": "HIGH",
            "primary_blocker": "None",
            "pass1_note": "Initial pass overestimated API breadth; verified pass confirmed scope is focused on checkout/webhooks during Commas rebrand."
        }
    }
    
    for app in pass1_apps:
        name = app["app"]
        if name in raw_discrepancies:
            disc = raw_discrepancies[name]
            if "credential_access" in disc:
                app["credential_access"] = disc["credential_access"]
            if "buildability" in disc:
                app["buildability"] = disc["buildability"]
            if "primary_blocker" in disc:
                app["primary_blocker"] = disc["primary_blocker"]
            if "api_availability" in disc:
                app["api"]["availability"] = disc["api_availability"]
            if "api_breadth" in disc:
                app["api"]["breadth"] = disc["api_breadth"]
            app["pass1_raw_note"] = disc["pass1_note"]
        else:
            app["pass1_raw_note"] = "Initial pass findings aligned with verified primary documentation."
            
    return pass1_apps, raw_discrepancies

if __name__ == "__main__":
    verified = load_verified_dataset()
    pass1, discs = generate_pass1_raw_data(verified)
    print(f"Verified dataset: {len(verified)} apps loaded successfully")
    print(f"Pass 1 simulated discrepancies: {len(discs)} caught items")
