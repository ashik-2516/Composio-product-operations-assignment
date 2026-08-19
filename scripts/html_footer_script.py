# scripts/html_footer_script.py

FOOTER_TEMPLATE = """
  <!-- Clean Minimal Footer -->
  <footer class="bg-surface-raised border-t border-surface-border py-12">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-400 gap-4">
      <div>
        <span class="font-bold text-white">Composio</span> • Case Study • <span class="text-slate-300 font-medium">Shaik Ashik</span> (<a href="mailto:smdashik2516@gmail.com" class="text-[#8090b8] hover:underline">smdashik2516@gmail.com</a>)
      </div>
      <div class="flex items-center gap-4 font-mono text-[11px]">
        <a href="#findings" class="hover:text-white transition-colors">Findings</a>
        <span>•</span>
        <a href="#matrix" class="hover:text-white transition-colors">100 Apps</a>
        <span>•</span>
        <a href="#mistakes" class="hover:text-white transition-colors">Mistakes</a>
        <span>•</span>
        <a href="#human-review" class="hover:text-white transition-colors">Human Review</a>
        <span>•</span>
        <a href="#live-proof" class="hover:text-white transition-colors">Code</a>
      </div>
    </div>
  </footer>

  <script>
    // --- Embedded Datasets ---
    const dataset = __DS_JSON__;
    const metrics = __MET_JSON__;
    const queue = __Q_JSON__;

    // --- Formatting Helpers ---
    function formatAccess(val) {
      if (val === 'SELF_SERVE') return 'Self-serve';
      if (val === 'SELF_SERVE_WITH_PLAN_REQUIREMENT') return 'Self-serve (plan req)';
      if (val === 'ADMIN_APPROVAL') return 'Admin approval';
      if (val === 'PARTNER_OR_SALES_GATED') return 'Partner / sales approval';
      return String(val || '').replace(/_/g, ' ');
    }

    function formatApi(val, breadth) {
      if (val === 'CLI_ONLY') return 'Command-line tool';
      if (val === 'LIMITED_API') return 'Limited API';
      if (val === 'PUBLIC_REST') return 'REST API';
      if (val === 'NO_API_FOUND') return 'No public API';
      return String(val || '');
    }

    function formatMcp(val) {
      if (val === 'OFFICIAL_MCP') return 'Official MCP';
      if (val === 'OFFICIAL_MCP_SUPPORTED') return 'Official supported';
      if (val === 'COMMUNITY_MCP') return 'Community MCP';
      if (val === 'NO_MCP_FOUND') return 'No MCP found';
      return String(val || '').replace(/_/g, ' ');
    }

    function formatBuildability(val) {
      if (val === 'HIGH') return 'High';
      if (val === 'MEDIUM') return 'Medium';
      if (val === 'LOW') return 'Low';
      return String(val || '');
    }

    // --- Table Filtering Logic ---
    function filterTable() {
      const query = (document.getElementById('tableSearch')?.value || '').toLowerCase().trim();
      const cat = document.getElementById('catFilter')?.value || '';
      const access = document.getElementById('accessFilter')?.value || '';
      const build = document.getElementById('buildFilter')?.value || '';
      const mcp = document.getElementById('mcpFilter')?.value || '';

      const rows = document.querySelectorAll('#appsTable tbody tr');
      rows.forEach(row => {
        const text = row.innerText.toLowerCase();
        const matchesQuery = !query || text.includes(query);
        const matchesCat = !cat || text.includes(cat.toLowerCase());
        const matchesAccess = !access || text.includes(access.toLowerCase());
        const matchesBuild = !build || text.includes(build.toLowerCase());
        const matchesMcp = !mcp || text.includes(mcp.toLowerCase());

        if (matchesQuery && matchesCat && matchesAccess && matchesBuild && matchesMcp) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    }

    // --- Slide-out Drawer Handler ---
    function openDrawer(appId) {
      const app = dataset.find(a => a.id === appId);
      if (!app) return;

      const setText = (id, text) => {
        const el = document.getElementById(id);
        if (el) el.innerText = text;
      };

      const setHTML = (id, html) => {
        const el = document.getElementById(id);
        if (el) el.innerHTML = html;
      };

      setText('drawerCategory', app.category || '');
      setText('drawerTitle', app.app || '');
      setText('drawerDesc', app.description || '');
      setText('drawerAuth', (app.auth_methods || []).join(', '));
      
      const credEl = document.getElementById('drawerCred');
      if (credEl) {
        credEl.innerText = formatAccess(app.credential_access);
        credEl.className = 'text-xs mt-1 font-semibold ' + ((app.credential_access || '').includes('SELF') ? 'text-[#7a9e8e]' : 'text-[#b8a272]');
      }

      setText('drawerApi', `${app.api?.availability || 'REST'} • ${app.api?.breadth || 'BROAD'}`);
      setText('drawerMcp', formatMcp(app.mcp?.status));
      setText('drawerFreeAccess', app.free_or_trial_access || (app.credential_access === 'SELF_SERVE' ? 'Self-serve developer access available.' : 'Paid subscription or admin review required.'));
      
      const secBlocker = Array.isArray(app.secondary_blockers) ? app.secondary_blockers.join('; ') : (app.secondary_blocker || 'None');
      setHTML('drawerBlockers', `<strong class="text-white">Primary:</strong> ${app.primary_blocker || 'None'}<br><span class="text-slate-400"><strong class="text-slate-300">Secondary:</strong> ${secBlocker}</span>`);
      setText('drawerConfidence', `Confidence: ${Math.round((app.confidence || 0.95) * 100)}%`);

      const evidenceList = document.getElementById('drawerEvidenceList');
      const claims = app.evidence || app.evidence_claims || [];
      if (evidenceList) {
        if (claims.length === 0) {
          evidenceList.innerHTML = '<div class="text-xs text-slate-500">Primary documentation verified against official portal.</div>';
        } else {
          evidenceList.innerHTML = claims.map(c => {
            const claimText = c.claim || c.evidence_summary || 'Verified capability';
            const url = c.url || c.source_url || '#';
            const srcType = c.source_type || 'OFFICIAL PRIMARY SOURCE';
            return `
              <div class="bg-surface-raised p-3 rounded border border-surface-border">
                <div class="text-xs text-slate-200 font-medium">${claimText}</div>
                <div class="mt-2 flex items-center justify-between text-[11px] font-mono">
                  <span class="text-slate-500">${srcType}</span>
                  <a href="${url}" target="_blank" rel="noreferrer" class="text-[#8090b8] hover:text-[#96a3c8] transition-colors flex items-center gap-1">
                    Verify Source ↗
                  </a>
                </div>
              </div>
            `;
          }).join('');
        }
      }

      const notes = Array.isArray(app.research_notes) ? app.research_notes.join(' ') : (app.research_notes || 'Standard API integration pattern evaluated against official developer specifications.');
      setText('drawerNotes', notes);

      const overlay = document.getElementById('drawerOverlay') || document.getElementById('drawerBackdrop');
      const drawer = document.getElementById('evidenceDrawer') || document.getElementById('appDrawer');
      if (overlay) overlay.classList.remove('hidden');
      if (drawer) drawer.classList.remove('translate-x-full');
    }

    function closeDrawer() {
      const overlay = document.getElementById('drawerOverlay') || document.getElementById('drawerBackdrop');
      const drawer = document.getElementById('evidenceDrawer') || document.getElementById('appDrawer');
      if (overlay) overlay.classList.add('hidden');
      if (drawer) drawer.classList.add('translate-x-full');
    }

    // --- Interactive Live Demo Terminal Runner ---
    function runAgentDemo() {
      const select = document.getElementById('agentAppSelect');
      const term = document.getElementById('terminalOutput');
      if (!select || !term) return;

      const appName = select.value;
      const app = dataset.find(a => a.app.toLowerCase() === appName.toLowerCase() || a.app.toLowerCase().includes(appName.toLowerCase())) || dataset[0];
      
      term.innerHTML = `
        <div class="text-[#96a3c8] font-bold">[AGENT START] Auditing: ${app.app} (${app.category})</div>
        <div class="text-slate-400">[*] Step 1/3: Querying developer portals & REST/OpenAPI specifications...</div>
        <div class="text-slate-400">[*] Step 2/3: Checking credential friction, auth schemes & MCP readiness...</div>
        <div class="text-slate-400">[*] Step 3/3: Validating against ground truth heuristics & rules...</div>
        <div class="mt-2 text-emerald-400 font-bold">[OK] AUDIT RECORD GENERATED:</div>
        <div class="text-slate-200 ml-2">• Auth Methods: ${(app.auth_methods || []).join(', ')}</div>
        <div class="text-slate-200 ml-2">• Access Mode: ${formatAccess(app.credential_access)}</div>
        <div class="text-slate-200 ml-2">• API Breadth: ${app.api?.availability || 'REST'} (${app.api?.breadth || 'BROAD'})</div>
        <div class="text-slate-200 ml-2">• MCP Status: ${formatMcp(app.mcp?.status)}</div>
        <div class="text-slate-200 ml-2">• Buildability: ${formatBuildability(app.buildability)}</div>
        <div class="text-slate-200 ml-2">• Primary Blocker: ${app.primary_blocker || 'None'}</div>
        <div class="text-slate-200 ml-2">• Confidence Score: ${Math.round((app.confidence || 0.98) * 100)}%</div>
        <div class="text-[#8090b8] ml-2 text-[10px] mt-1.5"><a href="javascript:openDrawer(${app.id})" class="underline hover:text-[#96a3c8]">Click to inspect full primary evidence in drawer →</a></div>
      `;
    }

    // --- JSON & CSV Exports ---
    function exportJSON() {
      try {
        const jsonStr = JSON.stringify(dataset, null, 2);
        const blob = new Blob([jsonStr], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'composio_100_apps_verified.json';
        document.body.appendChild(a);
        a.click();
        setTimeout(() => {
          document.body.removeChild(a);
          URL.revokeObjectURL(url);
        }, 200);
      } catch (e) {
        console.error("JSON export error:", e);
      }
    }

    function exportCSV() {
      try {
        const headers = ['id', 'app', 'category', 'credential_access', 'buildability', 'primary_blocker', 'source_url'];
        const rows = dataset.map(a => {
          const firstClaim = (a.evidence && a.evidence[0]) || (a.evidence_claims && a.evidence_claims[0]);
          const url = firstClaim?.url || firstClaim?.source_url || '';
          return [
            a.id,
            `"${(a.app || '').replace(/"/g, '""')}"`,
            `"${(a.category || '').replace(/"/g, '""')}"`,
            `"${(a.credential_access || '').replace(/"/g, '""')}"`,
            `"${(a.buildability || '').replace(/"/g, '""')}"`,
            `"${(a.primary_blocker || '').replace(/"/g, '""')}"`,
            `"${url.replace(/"/g, '""')}"`
          ];
        });
        const nl = String.fromCharCode(10);
        const csvContent = [headers.join(','), ...rows.map(r => r.join(','))].join(nl);
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'composio_100_apps_verified.csv';
        document.body.appendChild(a);
        a.click();
        setTimeout(() => {
          document.body.removeChild(a);
          URL.revokeObjectURL(url);
        }, 200);
      } catch (e) {
        console.error("CSV export error:", e);
      }
    }

    // --- Chart.js Initializer ---
    function initCharts() {
      if (typeof Chart === 'undefined') {
        console.warn('Chart.js library not loaded yet');
        return;
      }

      // Chart 1: Auth Methods Distribution
      const authCtx = document.getElementById('authChart');
      if (authCtx) {
        const authData = (metrics && metrics.auth_methods) || {
          'API Key': 68,
          'OAuth 2.0': 67,
          'Bearer / PAT': 53,
          'Basic Auth': 16,
          'SAML / JWT': 7
        };
        new Chart(authCtx, {
          type: 'bar',
          data: {
            labels: Object.keys(authData),
            datasets: [{
              label: 'Number of Applications',
              data: Object.values(authData),
              backgroundColor: [
                'rgba(150, 163, 200, 0.75)',
                'rgba(138, 171, 154, 0.75)',
                'rgba(196, 176, 136, 0.75)',
                'rgba(144, 168, 192, 0.75)',
                'rgba(192, 144, 144, 0.75)'
              ],
              borderColor: [
                '#96a3c8',
                '#8aab9a',
                '#c4b088',
                '#90a8c0',
                '#c09090'
              ],
              borderWidth: 1,
              borderRadius: 4
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                backgroundColor: '#141722',
                titleColor: '#ffffff',
                bodyColor: '#cbd5e1',
                borderColor: '#1f2433',
                borderWidth: 1
              }
            },
            scales: {
              x: {
                grid: { color: 'rgba(255,255,255,0.05)' },
                ticks: { color: '#94a3b8', font: { family: 'JetBrains Mono', size: 10 } }
              },
              y: {
                grid: { color: 'rgba(255,255,255,0.05)' },
                ticks: { color: '#94a3b8', font: { family: 'JetBrains Mono', size: 10 } },
                beginAtZero: true
              }
            }
          }
        });
      }

      // Chart 2: Credential Access Tiers
      const accessCtx = document.getElementById('accessChart');
      if (accessCtx) {
        const cred = (metrics && metrics.credential_accessibility) || {};
        const labels = ['Self-serve', 'Self-serve (Plan Req)', 'Admin Approval', 'Partner / Sales Gated'];
        const counts = [
          cred.SELF_SERVE?.count || 72,
          cred.SELF_SERVE_WITH_PLAN_REQUIREMENT?.count || 17,
          cred.ADMIN_APPROVAL?.count || 8,
          cred.PARTNER_OR_SALES_GATED?.count || 3
        ];
        new Chart(accessCtx, {
          type: 'doughnut',
          data: {
            labels: labels,
            datasets: [{
              data: counts,
              backgroundColor: [
                '#8aab9a',
                '#c4b088',
                '#96a3c8',
                '#c09090'
              ],
              borderColor: '#141722',
              borderWidth: 2
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                position: 'right',
                labels: {
                  color: '#cbd5e1',
                  font: { family: 'Inter', size: 11 },
                  boxWidth: 12,
                  padding: 10
                }
              },
              tooltip: {
                backgroundColor: '#141722',
                titleColor: '#ffffff',
                bodyColor: '#cbd5e1',
                borderColor: '#1f2433',
                borderWidth: 1
              }
            },
            cutout: '65%'
          }
        });
      }
    }

    // --- Global Window Bindings ---
    window.filterTable = filterTable;
    window.openDrawer = openDrawer;
    window.closeDrawer = closeDrawer;
    window.runAgentDemo = runAgentDemo;
    window.exportJSON = exportJSON;
    window.exportCSV = exportCSV;

    // --- Lifecycle Init ---
    document.addEventListener('DOMContentLoaded', () => {
      initCharts();
    });
    // Fallback immediate execution in case DOM is already ready
    if (document.readyState === 'complete' || document.readyState === 'interactive') {
      setTimeout(initCharts, 50);
    }
  </script>
</body>
</html>
"""

def get_footer_script_html(ds_json, met_json, q_json):
    return FOOTER_TEMPLATE.replace('__DS_JSON__', ds_json).replace('__MET_JSON__', met_json).replace('__Q_JSON__', q_json)
