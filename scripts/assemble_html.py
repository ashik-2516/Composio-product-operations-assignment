# scripts/assemble_html.py
import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.html_header import HEADER_HTML
from scripts.html_nav_hero import get_nav_hero_html
from scripts.html_sections import get_sections_html
from scripts.html_footer_script import get_footer_script_html

def assemble():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(root, "data")
    
    with open(os.path.join(data_dir, "results_final.json"), "r", encoding="utf-8") as f:
        dataset = json.load(f)
    with open(os.path.join(data_dir, "metrics.json"), "r", encoding="utf-8") as f:
        metrics = json.load(f)
    with open(os.path.join(data_dir, "verification_queue.json"), "r", encoding="utf-8") as f:
        queue = json.load(f)

    # Priority strings aligned with compute_metrics.py
    tier1_apps = []
    tier2_apps = []
    tier3_apps = []
    tier4_apps = []

    for app in dataset:
        cred = app["credential_access"]
        build = app["buildability"]
        avail = app["api"]["availability"]
        
        if build == "HIGH" and cred == "SELF_SERVE":
            tier1_apps.append(app["app"])
        elif build == "HIGH" and cred == "SELF_SERVE_WITH_PLAN_REQUIREMENT":
            tier2_apps.append(app["app"])
        elif build in ["MEDIUM", "HIGH"] and cred in ["ADMIN_APPROVAL", "PARTNER_OR_SALES_GATED"]:
            tier3_apps.append(app["app"])
        elif build == "MEDIUM" and avail == "CLI_ONLY":
            tier2_apps.append(app["app"])
        else:
            tier4_apps.append(app["app"])

    t1_str = " • ".join([f'<span class="text-emerald-300 font-medium">{name}</span>' for name in tier1_apps])
    t2_str = " • ".join([f'<span class="text-amber-300 font-medium">{name}</span>' for name in tier2_apps])
    t3_str = " • ".join([f'<span class="text-indigo-300 font-medium">{name}</span>' for name in tier3_apps])
    t4_str = " • ".join([f'<span class="text-rose-300 font-medium">{name}</span>' for name in tier4_apps])

    verif_csv_path = os.path.join(root, "verification", "human_decisions.csv")
    queue_rows = []
    
    if os.path.exists(verif_csv_path):
        import csv
        with open(verif_csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                queue_rows.append(f'''
                  <tr class="hover:bg-surface-hover/80 transition-colors">
                    <td class="py-3 px-4 font-bold text-white text-xs">{row["app"]} <span class="text-[10px] text-slate-500 block font-normal">{row["category"]}</span></td>
                    <td class="py-3 px-4 font-mono text-indigo-300 text-xs">{row["field_tested"]}</td>
                    <td class="py-3 px-4 text-amber-300 text-xs">{row["pass1_agent_claim"]}</td>
                    <td class="py-3 px-4 text-slate-300 text-[11px] leading-relaxed max-w-xs">{row["independent_primary_evidence"]}</td>
                    <td class="py-3 px-4 text-emerald-400 font-mono text-xs font-semibold">{row["human_reviewer_decision"]}</td>
                  </tr>
                ''')
    else:
        for q in queue:
            queue_rows.append(f'''
              <tr class="hover:bg-surface-hover/80 transition-colors">
                <td class="py-3 px-4 font-bold text-white text-xs">{q["app"]} <span class="text-[10px] text-slate-500 block font-normal">{q.get("category", "")}</span></td>
                <td class="py-3 px-4 font-mono text-indigo-300 text-xs">{q["field_to_verify"]}</td>
                <td class="py-3 px-4 text-amber-300 text-xs">{q["agent_finding"]}</td>
                <td class="py-3 px-4 text-slate-300 text-[11px] leading-relaxed max-w-xs">{q["why_selected"]}</td>
                <td class="py-3 px-4 text-emerald-400 font-mono text-xs font-semibold">{q["expected_check"]}</td>
              </tr>
            ''')
    queue_items_str = "\n".join(queue_rows)

    ds_json = json.dumps(dataset).replace("</script>", "<\\/script>")
    met_json = json.dumps(metrics).replace("</script>", "<\\/script>")
    q_json = json.dumps(queue).replace("</script>", "<\\/script>")

    final_html = HEADER_HTML + get_nav_hero_html(metrics, dataset) + get_sections_html(queue_items_str, t1_str, t2_str, t3_str, t4_str, metrics, dataset) + get_footer_script_html(ds_json, met_json, q_json)

    out_path = os.path.join(root, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"index.html successfully assembled: {out_path} ({len(final_html):,} bytes)")

if __name__ == "__main__":
    assemble()

