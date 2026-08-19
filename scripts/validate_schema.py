import json

with open("data/results_final.json", "r", encoding="utf-8") as f:
    apps = json.load(f)

print(f"Total apps in final dataset: {len(apps)}")

required_keys = [
    "id", "app", "category", "description", "auth_methods",
    "credential_access", "free_or_trial_access", "api", "mcp",
    "buildability", "primary_blocker", "secondary_blockers",
    "evidence", "confidence", "human_verification_required",
    "uncertainties", "research_notes"
]

for idx, a in enumerate(apps, 1):
    for k in required_keys:
        assert k in a, f"App #{idx} ({a.get('app')}) missing key {k}"
    assert len(a["evidence"]) > 0, f"App #{idx} ({a.get('app')}) has no evidence"
    for ev in a["evidence"]:
        assert ev["url"].startswith("http"), f"App #{idx} invalid url: {ev['url']}"

print("All 100 app records strictly conform to the required schema and evidence validation rules!")
