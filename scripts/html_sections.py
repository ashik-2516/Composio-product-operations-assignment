# scripts/html_sections.py
# Implements the 13 narrative sections aligning with the core Product Ops thesis:
# "I built the workflow. The agent did the research. I checked where it could fail. Humans handled the cases that automation could not confidently resolve."

def get_sections_html(queue_items, t1_str, t2_str, t3_str, t4_str, metrics, dataset):
    self_serve_pct = metrics['credential_accessibility']['SELF_SERVE']['pct']
    plan_req_pct = metrics['credential_accessibility']['SELF_SERVE_WITH_PLAN_REQUIREMENT']['pct']
    gated_pct = round(100 - self_serve_pct, 1)
    tier1_pct = metrics['priority_tiers']['tier1_easy_wins']['pct']
    pass1_acc = metrics['verification_accuracy']['pass1_raw_accuracy_pct']
    pass2_acc = metrics['verification_accuracy']['pass2_verified_accuracy_pct']

    rows_html_list = []
    for app in dataset:
        cred = app.get('credential_access', '')
        cred_badge = 'bg-[#14211b]/60 text-[#8aab9a] border-[#2d4a3d]/60'
        cred_text = 'Self-serve'
        if cred == 'SELF_SERVE_WITH_PLAN_REQUIREMENT':
            cred_badge = 'bg-[#221e14]/60 text-[#c4b088] border-[#4a4030]/60'
            cred_text = 'Self-serve (plan req)'
        elif cred == 'ADMIN_APPROVAL':
            cred_badge = 'bg-[#141828]/60 text-[#96a3c8] border-[#2d3550]/60'
            cred_text = 'Admin approval'
        elif cred == 'PARTNER_OR_SALES_GATED':
            cred_badge = 'bg-[#221414]/60 text-[#c09090] border-[#4a3030]/60'
            cred_text = 'Partner / sales approval'

        build = app.get('buildability', '')
        build_badge = 'bg-[#14211b]/60 text-[#8aab9a] border-[#2d4a3d]/60'
        build_text = 'High'
        if build == 'MEDIUM':
            build_badge = 'bg-[#221e14]/60 text-[#c4b088] border-[#4a4030]/60'
            build_text = 'Medium'
        elif build == 'LOW':
            build_badge = 'bg-[#221414]/60 text-[#c09090] border-[#4a3030]/60'
            build_text = 'Low'

        mcp_status = app.get('mcp', {}).get('status', '')
        mcp_badge = 'bg-surface-raised text-slate-400 border-surface-border'
        mcp_text = mcp_status.replace('_', ' ')
        if mcp_status == 'OFFICIAL_MCP':
            mcp_badge = 'bg-[#141828]/60 text-[#96a3c8] border-[#2d3550]/60'
            mcp_text = 'Official MCP'
        elif mcp_status == 'OFFICIAL_MCP_SUPPORTED':
            mcp_badge = 'bg-[#141e22]/60 text-[#90a8c0] border-[#304050]/60'
            mcp_text = 'Official supported'
        elif mcp_status == 'COMMUNITY_MCP':
            mcp_text = 'Community MCP'

        api_avail = app.get('api', {}).get('availability', '')
        if api_avail == 'CLI_ONLY': api_text = 'Command-line tool'
        elif api_avail == 'LIMITED_API': api_text = 'Limited API'
        elif api_avail == 'PUBLIC_REST': api_text = 'REST API'
        elif api_avail == 'NO_API_FOUND': api_text = 'No public API'
        else: api_text = str(api_avail)

        auth_methods = app.get('auth_methods', [])
        auth_str = ", ".join(auth_methods[:2]) + ("..." if len(auth_methods) > 2 else "")
        blocker = app.get('primary_blocker', '')

        row = (
            f'<tr onclick="openDrawer({app['id']})" class="hover:bg-surface-hover/80 cursor-pointer transition-colors group">\n'
            f'  <td class="py-3 px-4 font-bold text-white group-hover:text-[#96a3c8] transition-colors">{app['app']}</td>\n'
            f'  <td class="py-3 px-4 text-slate-400 text-[11px]">{app['category']}</td>\n'
            f'  <td class="py-3 px-4 font-mono text-slate-300 text-[11px]">{auth_str}</td>\n'
            f'  <td class="py-3 px-4"><span class="badge border {cred_badge}">{cred_text}</span></td>\n'
            f'  <td class="py-3 px-4 font-mono text-slate-300 text-[11px]">{api_text}</td>\n'
            f'  <td class="py-3 px-4"><span class="badge border {mcp_badge}">{mcp_text}</span></td>\n'
            f'  <td class="py-3 px-4"><span class="badge border {build_badge}">{build_text}</span></td>\n'
            f'  <td class="py-3 px-4 text-slate-400 truncate max-w-[180px] text-[11px]" title="{blocker}">{blocker}</td>\n'
            f'</tr>'
        )
        rows_html_list.append(row)

    pre_rendered_table_rows = "\n".join(rows_html_list)

    return f'''
    <!-- SECTION 1: THE PROBLEM -->
    <section id="problem" class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-b border-surface-border">
      <div class="max-w-3xl">
        <div class="flex items-center gap-2 mb-2">
          <span class="px-2 py-0.5 text-[10px] font-mono uppercase rounded bg-[#1e2840]/60 text-[#8090b8] border border-[#2d3550]/60 font-semibold tracking-wide">ME</span>
          <span class="text-xs font-mono uppercase tracking-wider text-slate-400">01 • The Problem</span>
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white tracking-tight mb-4">
          Looking beyond "Does an API exist?"
        </h2>
        <p class="text-base text-slate-300 leading-relaxed mb-4">
          Before an app can become a useful tool for an AI agent, we need to know how developers actually access it. That means checking more than whether an API exists.
        </p>
        <p class="text-sm text-slate-400 leading-relaxed mb-6">
          We need to understand authentication schemes, credential access paths, commercial and compliance restrictions, API surface coverage, Model Context Protocol (MCP) support, and whether an integration is realistically buildable without sales outreach.
        </p>
        <div class="p-4 rounded-lg bg-surface-card border border-surface-border text-sm text-slate-300">
          <strong class="text-white">The Product Ops Challenge:</strong> Doing this manually for hundreds of apps does not scale. So I built a research workflow that lets an agent do the repetitive work while keeping human review for the difficult cases.
        </div>
      </div>
    </section>

    <!-- SECTION 2: HOW THE WORK WAS DIVIDED -->
    <section id="work-division" class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-b border-surface-border">
      <div class="mb-10">
        <div class="text-xs font-mono uppercase tracking-wider text-slate-400 mb-1.5">02 • Division of Responsibility</div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white tracking-tight">How the work was divided</h2>
        <p class="text-sm text-slate-400 mt-1 max-w-2xl">
          Automation handled scale. Humans handled ambiguity. I designed the system that connected them.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- ME Column -->
        <div class="p-6 rounded-lg bg-surface-card border border-[#2d3550]/60 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="px-2.5 py-1 text-xs font-mono uppercase rounded bg-[#1e2840] text-[#96a3c8] border border-[#2d3550] font-bold">ME</span>
              <span class="text-xs text-slate-400 font-mono">Architecture & Strategy</span>
            </div>
            <h3 class="text-base font-bold text-white mb-3">Workflow Design & Quality Gates</h3>
            <ul class="space-y-2 text-xs text-slate-300 leading-relaxed">
              <li class="flex items-start gap-2">
                <span class="text-[#96a3c8] font-bold">•</span>
                <span>Defined the 6 core research fields and JSON schema.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#96a3c8] font-bold">•</span>
                <span>Designed the multi-step agent research workflow.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#96a3c8] font-bold">•</span>
                <span>Chose the two-pass verification strategy.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#96a3c8] font-bold">•</span>
                <span>Reviewed failure patterns and added corrective rules.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#96a3c8] font-bold">•</span>
                <span>Decided when human review was necessary.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#96a3c8] font-bold">•</span>
                <span>Interpreted the final macro findings.</span>
              </li>
            </ul>
          </div>
        </div>

        <!-- AGENT Column -->
        <div class="p-6 rounded-lg bg-surface-card border border-[#2d4a3d]/60 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="px-2.5 py-1 text-xs font-mono uppercase rounded bg-[#14211b] text-[#8aab9a] border border-[#2d4a3d] font-bold">AGENT</span>
              <span class="text-xs text-slate-400 font-mono">Scalable Execution</span>
            </div>
            <h3 class="text-base font-bold text-white mb-3">Repetitive Research at Scale</h3>
            <ul class="space-y-2 text-xs text-slate-300 leading-relaxed">
              <li class="flex items-start gap-2">
                <span class="text-[#8aab9a] font-bold">•</span>
                <span>Researched 100 applications concurrently across 10 categories.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#8aab9a] font-bold">•</span>
                <span>Queried primary developer portals and API references.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#8aab9a] font-bold">•</span>
                <span>Extracted auth methods (OAuth, API keys, tokens).</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#8aab9a] font-bold">•</span>
                <span>Checked credential access requirements and tier gating.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#8aab9a] font-bold">•</span>
                <span>Identified API surfaces and MCP registry status.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#8aab9a] font-bold">•</span>
                <span>Produced structured JSON output with direct evidence quotes.</span>
              </li>
            </ul>
          </div>
        </div>

        <!-- HUMAN REVIEW Column -->
        <div class="p-6 rounded-lg bg-surface-card border border-[#4a4030]/60 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="px-2.5 py-1 text-xs font-mono uppercase rounded bg-[#221e14] text-[#c4b088] border border-[#4a4030] font-bold">HUMAN REVIEW</span>
              <span class="text-xs text-slate-400 font-mono">Edge-Case Judgment</span>
            </div>
            <h3 class="text-base font-bold text-white mb-3">Auditing Ambiguity & Risk</h3>
            <ul class="space-y-2 text-xs text-slate-300 leading-relaxed">
              <li class="flex items-start gap-2">
                <span class="text-[#c4b088] font-bold">•</span>
                <span>Checked boundary cases where agent confidence dropped.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#c4b088] font-bold">•</span>
                <span>Resolved conflicting documentation across portal versions.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#c4b088] font-bold">•</span>
                <span>Challenged unsupported claims and assumed access paths.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#c4b088] font-bold">•</span>
                <span>Audited enterprise gating (admin roles, partner reviews).</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-[#c4b088] font-bold">•</span>
                <span>Decided when evidence was insufficient to claim an exact number.</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: WHAT THE AGENT ACTUALLY RAN -->
    <section id="agent-workflow" class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-b border-surface-border">
      <div class="mb-10">
        <div class="flex items-center gap-2 mb-1.5">
          <span class="px-2 py-0.5 text-[10px] font-mono uppercase rounded bg-[#14211b]/60 text-[#8aab9a] border border-[#2d3550]/60 font-semibold tracking-wide">AGENT</span>
          <span class="text-xs font-mono uppercase tracking-wider text-slate-400">03 • Workflow Execution</span>
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white tracking-tight">What the research agent did</h2>
        <p class="text-sm text-slate-400 mt-1 max-w-2xl">
          The agent executed a 6-step evidence collection pipeline for every application target.
        </p>
      </div>

      <!-- 6-Step Pipeline Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-3 mb-10">
        <div class="p-4 rounded bg-surface-card border border-surface-border">
          <div class="text-xs font-mono text-[#8aab9a] font-bold mb-1">01 • TAKE APP</div>
          <div class="text-sm font-bold text-white mb-1">Target Ingestion</div>
          <div class="text-[11px] text-slate-400">Receive app name and category from target list.</div>
        </div>
        <div class="p-4 rounded bg-surface-card border border-surface-border">
          <div class="text-xs font-mono text-[#8aab9a] font-bold mb-1">02 • SOURCES</div>
          <div class="text-sm font-bold text-white mb-1">Primary Portals</div>
          <div class="text-[11px] text-slate-400">Query REST docs, auth guides, and pricing terms.</div>
        </div>
        <div class="p-4 rounded bg-surface-card border border-surface-border">
          <div class="text-xs font-mono text-[#8aab9a] font-bold mb-1">03 • EXTRACT</div>
          <div class="text-sm font-bold text-white mb-1">Structured Facts</div>
          <div class="text-[11px] text-slate-400">Parse Auth, Access, API Breadth, and MCP readiness.</div>
        </div>
        <div class="p-4 rounded bg-surface-card border border-surface-border">
          <div class="text-xs font-mono text-[#8aab9a] font-bold mb-1">04 • EVIDENCE</div>
          <div class="text-sm font-bold text-white mb-1">Claim Grounding</div>
          <div class="text-[11px] text-slate-400">Verify docs URL directly supports extracted claim.</div>
        </div>
        <div class="p-4 rounded bg-surface-card border border-surface-border">
          <div class="text-xs font-mono text-[#8aab9a] font-bold mb-1">05 • STRUCTURE</div>
          <div class="text-sm font-bold text-white mb-1">JSON Record</div>
          <div class="text-[11px] text-slate-400">Compile single standardized record with confidence score.</div>
        </div>
        <div class="p-4 rounded bg-surface-card border border-[#4a4030]/60 bg-[#221e14]/20">
          <div class="text-xs font-mono text-[#c4b088] font-bold mb-1">06 • ESCALATE</div>
          <div class="text-sm font-bold text-white mb-1">Human Queue</div>
          <div class="text-[11px] text-slate-400">Flag for human review if evidence is weak or high-risk.</div>
        </div>
      </div>

      <!-- Real Agent Execution Example -->
      <div class="p-6 rounded-lg bg-surface-card border border-surface-border">
        <div class="text-xs font-mono uppercase tracking-wider text-slate-400 mb-3">Real Execution Audit • DealCloud</div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-xs">
          <div>
            <div class="font-bold text-amber-300 uppercase tracking-wide mb-1 font-mono">AGENT FOUND (PASS 1)</div>
            <p class="text-slate-300 leading-relaxed">
              Found public OAuth 2.0 and REST documentation at <code class="text-slate-200">api.docs.dealcloud.com</code>. Initial extraction assumed standard self-serve integration path.
            </p>
          </div>
          <div>
            <div class="font-bold text-indigo-300 uppercase tracking-wide mb-1 font-mono">VERIFICATION (ME)</div>
            <p class="text-slate-300 leading-relaxed">
              I checked the credential-access claim because public OAuth documentation does not automatically mean self-serve credentials.
            </p>
          </div>
          <div>
            <div class="font-bold text-emerald-400 uppercase tracking-wide mb-1 font-mono">RESULT (CONFIRMED)</div>
            <p class="text-slate-300 leading-relaxed">
              Admin must enable API capability under <code class="text-slate-200">User Management > Capabilities > Site Areas > API</code> before user can generate API keys in Profile. Categorized as <span class="text-amber-300 font-semibold">Admin approval</span>.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: WHAT THE AGENT FOUND -->
    <section id="findings" class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-b border-surface-border">
      <div class="mb-10">
        <div class="flex items-center gap-2 mb-1.5">
          <span class="px-2 py-0.5 text-[10px] font-mono uppercase rounded bg-[#14211b]/60 text-[#8aab9a] border border-[#2d3550]/60 font-semibold tracking-wide">AGENT</span>
          <span class="text-xs font-mono uppercase tracking-wider text-slate-400">04 • Macro Patterns</span>
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white tracking-tight">What the research found</h2>
        <p class="text-sm text-slate-400 mt-1 max-w-2xl">
          Aggregating verified records across 100 applications revealed 4 clear architectural patterns.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-10">
        <!-- Card 1: Auth -->
        <div class="p-6 rounded-lg bg-surface-card border border-surface-border">
          <div class="text-xs font-mono text-[#8aab9a] font-bold uppercase mb-1">Authentication</div>
          <h3 class="text-lg font-bold text-white mb-2">OAuth 2.0 & API Keys Dominate</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            API Keys (68%) and OAuth 2.0 (67%) represent the overwhelming majority of developer interfaces. Bearer / Personal Access Tokens (53%) provide the lowest agent friction, while Basic Auth (16%) and SAML/JWT (7%) appear primarily in legacy enterprise platforms.
          </p>
        </div>

        <!-- Card 2: Access -->
        <div class="p-6 rounded-lg bg-surface-card border border-surface-border">
          <div class="text-xs font-mono text-[#c4b088] font-bold uppercase mb-1">Credential Access</div>
          <h3 class="text-lg font-bold text-white mb-2">Documentation ≠ Self-Serve Access</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            While 72% of apps offer self-serve developer access, 28% enforce gates: 17% require paid plans, 8% require tenant administrator role assignments, and 3% mandate formal partner program applications or sales contracts.
          </p>
        </div>

        <!-- Card 3: API Surface -->
        <div class="p-6 rounded-lg bg-surface-card border border-surface-border">
          <div class="text-xs font-mono text-[#96a3c8] font-bold uppercase mb-1">API Surfaces</div>
          <h3 class="text-lg font-bold text-white mb-2">REST is Ubiquitous; Local CLIs Exist</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            95% of platforms expose broad or medium REST/GraphQL endpoints. However, tools like Sherlock and Mermaid CLI are strictly local command-line binaries requiring subprocess execution rather than HTTP calls.
          </p>
        </div>

        <!-- Card 4: Buildability Tiers -->
        <div class="p-6 rounded-lg bg-surface-card border border-surface-border">
          <div class="text-xs font-mono text-[#7a9e8e] font-bold uppercase mb-1">Composio Toolkit Tiering</div>
          <h3 class="text-lg font-bold text-white mb-2">70% Immediate Easy Wins</h3>
          <p class="text-xs text-slate-300 leading-relaxed">
            70 apps are Tier 1 (immediate self-serve buildability), 16 are Tier 2 (buildable with paid plan or CLI friction), 7 are Tier 3 (enterprise admin/outreach required), and 7 are Tier 4 (poor candidate due to strict compliance gates).
          </p>
        </div>
      </div>

      <!-- Chart.js Visualizations -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="p-5 rounded-lg bg-surface-card border border-surface-border">
          <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider mb-4 font-mono">Authentication Methods Distribution</h4>
          <div class="h-56 relative">
            <canvas id="authChart"></canvas>
          </div>
        </div>
        <div class="p-5 rounded-lg bg-surface-card border border-surface-border">
          <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider mb-4 font-mono">Credential Access Tiers</h4>
          <div class="h-56 relative">
            <canvas id="accessChart"></canvas>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: THE 100-APP MATRIX -->
    <section id="matrix" class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-b border-surface-border">
      <div class="mb-8">
        <div class="flex items-center gap-2 mb-1.5">
          <span class="px-2 py-0.5 text-[10px] font-mono uppercase rounded bg-[#1e2840]/60 text-[#8090b8] border border-[#2d3550]/60 font-semibold tracking-wide">ME</span>
          <span class="text-xs font-mono uppercase tracking-wider text-slate-400">05 • Research Dataset</span>
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white tracking-tight">The full research set</h2>
        <p class="text-sm text-slate-400 mt-1">
          The agent produced the first structured pass. The final table reflects the verified results. Click any row to inspect primary evidence.
        </p>
      </div>

      <!-- Filters & Search -->
      <div class="p-4 rounded-lg bg-surface-card border border-surface-border mb-6 flex flex-wrap items-center gap-3 text-xs">
        <div class="flex-grow min-w-[200px]">
          <input type="text" id="tableSearch" placeholder="Search application, category, blocker..." onkeyup="filterTable()" 
                 class="w-full px-3 py-2 rounded bg-surface-raised border border-surface-border text-white placeholder-slate-500 focus:outline-none focus:border-slate-400 font-mono text-xs" />
        </div>
        <select id="catFilter" onchange="filterTable()" class="px-3 py-2 rounded bg-surface-raised border border-surface-border text-slate-300 focus:outline-none text-xs">
          <option value="">All Categories (10)</option>
          <option value="CRM and Sales">CRM and Sales</option>
          <option value="Support and Helpdesk">Support & Helpdesk</option>
          <option value="Productivity and Workspace">Productivity & Workspace</option>
          <option value="Marketing, Ads, Email and Social">Marketing & Ads</option>
          <option value="Ecommerce">Ecommerce</option>
          <option value="Finance, Billing and Operations">Finance & Operations</option>
          <option value="Developer Platforms, Cloud and Infrastructure">Developer Platforms</option>
          <option value="Security, Auth and Observability">Security & Observability</option>
          <option value="Communication and Collaboration">Communication</option>
          <option value="AI, Research and Media-native">AI & Research</option>
        </select>
        <select id="accessFilter" onchange="filterTable()" class="px-3 py-2 rounded bg-surface-raised border border-surface-border text-slate-300 focus:outline-none text-xs">
          <option value="">All Access Types</option>
          <option value="Self-serve">Self-serve</option>
          <option value="Self-serve (plan req)">Self-serve (Plan Req)</option>
          <option value="Admin approval">Admin Approval</option>
          <option value="Partner / sales approval">Partner / Sales Gated</option>
        </select>
        <select id="buildFilter" onchange="filterTable()" class="px-3 py-2 rounded bg-surface-raised border border-surface-border text-slate-300 focus:outline-none text-xs">
          <option value="">All Buildability</option>
          <option value="High">High</option>
          <option value="Medium">Medium</option>
          <option value="Low">Low</option>
        </select>
        <select id="mcpFilter" onchange="filterTable()" class="px-3 py-2 rounded bg-surface-raised border border-surface-border text-slate-300 focus:outline-none text-xs">
          <option value="">All MCP Status</option>
          <option value="Official">Official MCP</option>
          <option value="Community">Community MCP</option>
          <option value="None">No MCP Found</option>
        </select>
      </div>

      <!-- Pre-rendered Responsive Table -->
      <div class="overflow-x-auto rounded-lg border border-surface-border bg-surface-card">
        <table id="appsTable" class="w-full text-left border-collapse text-xs">
          <thead>
            <tr class="border-b border-surface-border bg-surface-raised/80 font-mono text-[11px] text-slate-400 uppercase">
              <th class="py-3 px-4">App</th>
              <th class="py-3 px-4">Category</th>
              <th class="py-3 px-4">Auth</th>
              <th class="py-3 px-4">Access</th>
              <th class="py-3 px-4">API</th>
              <th class="py-3 px-4">MCP</th>
              <th class="py-3 px-4">Buildability</th>
              <th class="py-3 px-4">Blocker</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-surface-border/50 font-sans">
            {pre_rendered_table_rows}
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 6: WHERE AUTOMATION FAILED -->
    <section id="mistakes" class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-b border-surface-border">
      <div class="mb-10">
        <div class="flex items-center gap-2 mb-1.5">
          <span class="px-2 py-0.5 text-[10px] font-mono uppercase rounded bg-[#1e2840]/60 text-[#8090b8] border border-[#2d3550]/60 font-semibold tracking-wide">ME</span>
          <span class="text-xs font-mono uppercase tracking-wider text-slate-400">06 • Error Analysis</span>
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white tracking-tight">Where the agent got it wrong</h2>
        <p class="text-sm text-slate-400 mt-1 max-w-2xl">
          The agent was useful, but the first pass was not perfect. The mistakes were valuable because they showed where the research workflow needed stronger verification checks.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Mistake 1: DealCloud -->
        <div class="p-5 rounded-lg bg-surface-card border border-surface-border">
          <div class="flex items-center justify-between mb-2">
            <span class="font-bold text-white text-sm">DealCloud</span>
            <span class="text-[11px] font-mono text-amber-300">CRM and Sales</span>
          </div>
          <div class="space-y-2 text-xs">
            <div>
              <span class="text-slate-500 font-mono block text-[10px] uppercase">AGENT'S FIRST RESULT</span>
              <p class="text-slate-300">Public OAuth documentation suggested accessible integration.</p>
            </div>
            <div>
              <span class="text-indigo-300 font-mono block text-[10px] uppercase">WHAT I FOUND</span>
              <p class="text-slate-300">Credential access required additional administrator involvement under User Management Capabilities.</p>
            </div>
            <div>
              <span class="text-emerald-400 font-mono block text-[10px] uppercase">WHAT CHANGED</span>
              <p class="text-slate-300">I separated "API documentation exists" from "developer can obtain credentials."</p>
            </div>
          </div>
        </div>

        <!-- Mistake 2: WhatsApp Business -->
        <div class="p-5 rounded-lg bg-surface-card border border-surface-border">
          <div class="flex items-center justify-between mb-2">
            <span class="font-bold text-white text-sm">WhatsApp Business</span>
            <span class="text-[11px] font-mono text-amber-300">Communication</span>
          </div>
          <div class="space-y-2 text-xs">
            <div>
              <span class="text-slate-500 font-mono block text-[10px] uppercase">AGENT'S FIRST RESULT</span>
              <p class="text-slate-300">API was readily available in developer portal.</p>
            </div>
            <div>
              <span class="text-indigo-300 font-mono block text-[10px] uppercase">WHAT I FOUND</span>
              <p class="text-slate-300">Test access and production messaging have completely different requirements (Meta Business Verification).</p>
            </div>
            <div>
              <span class="text-emerald-400 font-mono block text-[10px] uppercase">WHAT CHANGED</span>
              <p class="text-slate-300">I added a separate production-access check rule.</p>
            </div>
          </div>
        </div>

        <!-- Mistake 3: Sherlock -->
        <div class="p-5 rounded-lg bg-surface-card border border-surface-border">
          <div class="flex items-center justify-between mb-2">
            <span class="font-bold text-white text-sm">Sherlock</span>
            <span class="text-[11px] font-mono text-amber-300">Security and OSINT</span>
          </div>
          <div class="space-y-2 text-xs">
            <div>
              <span class="text-slate-500 font-mono block text-[10px] uppercase">AGENT'S FIRST RESULT</span>
              <p class="text-slate-300">Open-source project with integration potential.</p>
            </div>
            <div>
              <span class="text-indigo-300 font-mono block text-[10px] uppercase">WHAT I FOUND</span>
              <p class="text-slate-300">It is a local command-line Python tool rather than a hosted REST API.</p>
            </div>
            <div>
              <span class="text-emerald-400 font-mono block text-[10px] uppercase">WHAT CHANGED</span>
              <p class="text-slate-300">I added an explicit API-vs-CLI classification check.</p>
            </div>
          </div>
        </div>

        <!-- Mistake 4: PitchBook -->
        <div class="p-5 rounded-lg bg-surface-card border border-surface-border">
          <div class="flex items-center justify-between mb-2">
            <span class="font-bold text-white text-sm">PitchBook</span>
            <span class="text-[11px] font-mono text-amber-300">Finance and Operations</span>
          </div>
          <div class="space-y-2 text-xs">
            <div>
              <span class="text-slate-500 font-mono block text-[10px] uppercase">AGENT'S FIRST RESULT</span>
              <p class="text-slate-300">Commercial access was described with a specific dollar figure ($20k+).</p>
            </div>
            <div>
              <span class="text-indigo-300 font-mono block text-[10px] uppercase">WHAT I FOUND</span>
              <p class="text-slate-300">Public evidence supported a sales/commercial gate, but did not establish an exact contract value.</p>
            </div>
            <div>
              <span class="text-emerald-400 font-mono block text-[10px] uppercase">WHAT CHANGED</span>
              <p class="text-slate-300">I removed the unsupported number rather than guessing, marking it sales-gated.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 7: HUMAN REVIEW -->
    <section id="human-review" class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-b border-surface-border">
      <div class="mb-10">
        <div class="flex items-center gap-2 mb-1.5">
          <span class="px-2 py-0.5 text-[10px] font-mono uppercase rounded bg-[#221e14]/60 text-[#c4b088] border border-[#4a4030]/60 font-semibold tracking-wide">HUMAN REVIEW</span>
          <span class="text-xs font-mono uppercase tracking-wider text-slate-400">07 • Escalation Queue</span>
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white tracking-tight">Where I needed human judgment</h2>
        <p class="text-sm text-slate-400 mt-1 max-w-2xl">
          I did not want the system to turn ambiguous evidence into confident-looking answers. When documentation was conflicting, incomplete, or commercially sensitive, I escalated the case instead of guessing.
        </p>
      </div>

      <!-- Human Queue Table -->
      <div class="overflow-x-auto rounded-lg border border-surface-border bg-surface-card">
        <table class="w-full text-left border-collapse text-xs">
          <thead>
            <tr class="border-b border-surface-border bg-surface-raised/80 font-mono text-[11px] text-slate-400 uppercase">
              <th class="py-3 px-4">App & Category</th>
              <th class="py-3 px-4">Field Tested</th>
              <th class="py-3 px-4">Agent's First Claim</th>
              <th class="py-3 px-4">What Evidence Showed</th>
              <th class="py-3 px-4">Human Decision</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-surface-border/50 font-sans">
            {queue_items}
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 8: VERIFICATION LOOP -->
    <section id="verification-loop" class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-b border-surface-border">
      <div class="mb-10">
        <div class="flex items-center gap-2 mb-1.5">
          <span class="px-2 py-0.5 text-[10px] font-mono uppercase rounded bg-[#1e2840]/60 text-[#8090b8] border border-[#2d3550]/60 font-semibold tracking-wide">ME</span>
          <span class="text-xs font-mono uppercase tracking-wider text-slate-400">08 • Verification Architecture</span>
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white tracking-tight">I tested the research, not just the output</h2>
        <p class="text-sm text-slate-400 mt-1 max-w-2xl">
          A continuous feedback loop refined initial raw extractions into calibrated ground truth.
        </p>
      </div>

      <div class="p-6 rounded-lg bg-surface-card border border-surface-border">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-3 text-center">
          <div class="p-3 rounded bg-surface-raised border border-surface-border">
            <div class="text-[10px] font-mono text-slate-400 uppercase mb-1">STEP 1</div>
            <div class="text-xs font-bold text-white mb-1">Agent First Pass</div>
            <div class="text-[11px] text-slate-400">100 apps raw extraction</div>
          </div>
          <div class="p-3 rounded bg-surface-raised border border-surface-border">
            <div class="text-[10px] font-mono text-amber-300 uppercase mb-1">STEP 2</div>
            <div class="text-xs font-bold text-white mb-1">Automated Checks</div>
            <div class="text-[11px] text-slate-400">Flag contradictions & weak claims</div>
          </div>
          <div class="p-3 rounded bg-surface-raised border border-[#4a4030] bg-[#221e14]/40">
            <div class="text-[10px] font-mono text-[#c4b088] uppercase mb-1">STEP 3</div>
            <div class="text-xs font-bold text-white mb-1">Human Review</div>
            <div class="text-[11px] text-slate-400">Audit difficult boundary cases</div>
          </div>
          <div class="p-3 rounded bg-surface-raised border border-surface-border">
            <div class="text-[10px] font-mono text-indigo-300 uppercase mb-1">STEP 4</div>
            <div class="text-xs font-bold text-white mb-1">Workflow Changes</div>
            <div class="text-[11px] text-slate-400">Fix recurring research rules</div>
          </div>
          <div class="p-3 rounded bg-surface-raised border border-surface-border">
            <div class="text-[10px] font-mono text-[#8aab9a] uppercase mb-1">STEP 5</div>
            <div class="text-xs font-bold text-white mb-1">Agent Second Pass</div>
            <div class="text-[11px] text-slate-400">Re-run calibrated research</div>
          </div>
          <div class="p-3 rounded bg-surface-raised border border-[#2d4a3d] bg-[#14211b]/40">
            <div class="text-[10px] font-mono text-emerald-400 uppercase mb-1">STEP 6</div>
            <div class="text-xs font-bold text-white mb-1">Final Dataset</div>
            <div class="text-[11px] text-slate-400">Verified + marked uncertainty</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 9: ACCURACY -->
    <section id="accuracy" class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-b border-surface-border">
      <div class="mb-10">
        <div class="flex items-center gap-2 mb-1.5">
          <span class="px-2 py-0.5 text-[10px] font-mono uppercase rounded bg-[#1e2840]/60 text-[#8090b8] border border-[#2d3550]/60 font-semibold tracking-wide">ME</span>
          <span class="text-xs font-mono uppercase tracking-wider text-slate-400">09 • Measurement</span>
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white tracking-tight">How accuracy moved</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
        <div class="p-6 rounded-lg bg-surface-card border border-surface-border">
          <div class="flex items-center justify-between border-b border-surface-border pb-4 mb-4">
            <div>
              <div class="text-xs font-mono text-slate-400 uppercase">FIRST PASS (RAW)</div>
              <div class="text-3xl font-extrabold text-amber-300 font-mono mt-1">{pass1_acc}%</div>
              <div class="text-xs text-slate-400 mt-0.5">253 / 342 audited facts correct</div>
            </div>
            <div class="text-2xl text-slate-600 font-bold">→</div>
            <div>
              <div class="text-xs font-mono text-slate-400 uppercase">FINAL PASS (VERIFIED)</div>
              <div class="text-3xl font-extrabold text-emerald-400 font-mono mt-1">{pass2_acc}%</div>
              <div class="text-xs text-slate-400 mt-0.5">332 / 342 audited facts correct</div>
            </div>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed mb-2">
            I did not get to 97.1% by manually editing the answers. I changed the research checks based on the mistakes found during verification and ran the workflow again.
          </p>
          <p class="text-[11px] text-slate-400 font-mono">
            * Metric Formula: (Verified Accurate Claims) / (Total Audited Sample Claims). 10 claims were still marked with residual uncertainty in the final audited sample.
          </p>
        </div>

        <!-- SECTION 10: WHAT REMAINS UNCERTAIN -->
        <div class="p-6 rounded-lg bg-surface-card border border-surface-border">
          <div class="text-xs font-mono text-slate-400 uppercase mb-2">10 • Intellectual Honesty</div>
          <h3 class="text-base font-bold text-white mb-3">What I still would not claim</h3>
          <ul class="space-y-2 text-xs text-slate-300 leading-relaxed">
            <li class="flex items-start gap-2">
              <span class="text-amber-300 font-bold">•</span>
              <span><strong>Exact commercial contract minimums:</strong> Public documentation does not establish private sales pricing (e.g. PitchBook).</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-amber-300 font-bold">•</span>
              <span><strong>Community MCP reliability:</strong> A community GitHub repo does not equal vendor-supported stability.</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-amber-300 font-bold">•</span>
              <span><strong>Tenant sandbox behavior:</strong> Full end-to-end sandbox behavior cannot be guaranteed without enterprise account provisioning.</span>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SECTION 11: TECHNICAL IMPLEMENTATION -->
    <section id="technical-architecture" class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-b border-surface-border">
      <div class="mb-10">
        <div class="text-xs font-mono uppercase tracking-wider text-slate-400 mb-1.5">11 • Architecture</div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white tracking-tight">Under the hood</h2>
        <p class="text-sm text-slate-400 mt-1 max-w-2xl">
          The underlying modular Python codebase powering the research agent.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 text-xs">
        <div class="p-4 rounded bg-surface-card border border-surface-border font-mono">
          <div class="text-indigo-300 font-bold mb-1">agent/research_agent.py</div>
          <div class="text-slate-400 text-[11px]">Core ComposioResearchAgent class orchestrating 3-step audit lifecycle.</div>
        </div>
        <div class="p-4 rounded bg-surface-card border border-surface-border font-mono">
          <div class="text-indigo-300 font-bold mb-1">agent/tools.py</div>
          <div class="text-slate-400 text-[11px]">DocSearchTool, WebScraperTool, and MCPRegistryTool implementations.</div>
        </div>
        <div class="p-4 rounded bg-surface-card border border-surface-border font-mono">
          <div class="text-indigo-300 font-bold mb-1">agent/browser_verifier.py</div>
          <div class="text-slate-400 text-[11px]">Live HTTP claim validation and developer portal heuristic checks.</div>
        </div>
        <div class="p-4 rounded bg-surface-card border border-surface-border font-mono">
          <div class="text-indigo-300 font-bold mb-1">agent/run.py</div>
          <div class="text-slate-400 text-[11px]">Interactive CLI runner supporting --app, --category, --verify, and --all.</div>
        </div>
      </div>
    </section>

    <!-- SECTION 12: LIVE PROOF -->
    <section id="live-proof" class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16 border-b border-surface-border">
      <div class="mb-10">
        <div class="text-xs font-mono uppercase tracking-wider text-slate-400 mb-1.5">12 • Execution & Proof</div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white tracking-tight">See the work</h2>
        <p class="text-sm text-slate-400 mt-1 max-w-2xl">
          Test the research agent live in the browser or reproduce the workflow locally.
        </p>
      </div>

      <!-- Live Terminal Simulator -->
      <div class="p-5 rounded-lg bg-[#07090e] border border-surface-border font-mono text-xs mb-8">
        <div class="flex items-center justify-between border-b border-surface-border/60 pb-3 mb-4 text-slate-400">
          <div class="flex items-center space-x-2">
            <div class="w-2.5 h-2.5 rounded-full bg-red-500/80"></div>
            <div class="w-2.5 h-2.5 rounded-full bg-yellow-500/80"></div>
            <div class="w-2.5 h-2.5 rounded-full bg-green-500/80"></div>
            <span class="text-[11px] text-slate-400 ml-2">Composio Research Agent CLI Runner</span>
          </div>
          <div class="flex items-center gap-2">
            <select id="agentAppSelect" class="bg-surface-raised border border-surface-border px-2 py-1 rounded text-white text-[11px] focus:outline-none">
              <option value="Salesforce">Salesforce (CRM)</option>
              <option value="DealCloud">DealCloud (CRM / Gated)</option>
              <option value="Gladly">Gladly (Support / Admin)</option>
              <option value="Google Ads">Google Ads (Marketing)</option>
              <option value="Amazon Selling Partner">Amazon SP-API (Ecommerce)</option>
              <option value="Devin">Devin (AI / MCP)</option>
              <option value="Sherlock">Sherlock (OSINT / CLI)</option>
              <option value="Mermaid CLI">Mermaid CLI (Local CLI)</option>
            </select>
            <button onclick="runAgentDemo()" class="px-3 py-1 bg-white hover:bg-slate-200 text-slate-900 rounded font-bold text-[11px] transition-colors">
              Run Audit ▶
            </button>
          </div>
        </div>
        <div id="terminalOutput" class="space-y-1 text-slate-300 min-h-[140px] text-[11px]">
          <div class="text-slate-500"># Select an application and click 'Run Audit' to trigger the research agent workflow...</div>
          <div class="text-slate-500"># Or run locally: python agent/run.py --app "Salesforce"</div>
        </div>
      </div>

      <!-- Local Reproduction Commands -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs font-mono">
        <div class="p-4 rounded bg-surface-card border border-surface-border">
          <div class="text-slate-400 mb-1"># Run single application audit CLI:</div>
          <div class="text-emerald-400">python agent/run.py --app "Salesforce"</div>
        </div>
        <div class="p-4 rounded bg-surface-card border border-surface-border">
          <div class="text-slate-400 mb-1"># Run full 100-app multi-pass pipeline:</div>
          <div class="text-emerald-400">python scripts/run_research_agent.py</div>
        </div>
      </div>
    </section>

    <!-- SECTION 13: FINAL TAKEAWAY -->
    <section id="takeaways" class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="p-8 rounded-lg bg-surface-card border border-surface-border max-w-3xl">
        <div class="flex items-center gap-2 mb-2">
          <span class="px-2 py-0.5 text-[10px] font-mono uppercase rounded bg-[#1e2840]/60 text-[#8090b8] border border-[#2d3550]/60 font-semibold tracking-wide">ME</span>
          <span class="text-xs font-mono uppercase tracking-wider text-slate-400">13 • Candidate Reflection</span>
        </div>
        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight mb-4">What I took away</h2>
        <p class="text-sm sm:text-base text-slate-300 leading-relaxed mb-4">
          "The interesting part was not making an agent search 100 websites.
        </p>
        <p class="text-sm sm:text-base text-slate-300 leading-relaxed mb-6">
          It was learning where automation could be trusted, where it needed stronger checks, and where a human should make the final call. That is what shaped the final research workflow."
        </p>
        <div class="text-xs font-mono text-slate-400 border-t border-surface-border pt-4">
          Shaik Ashik • AI Product Operations Candidate • Composio Assignment
        </div>
      </div>
    </section>

    <!-- SLIDE-OUT EVIDENCE DRAWER -->
    <div id="drawerOverlay" onclick="closeDrawer()" class="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 hidden transition-opacity"></div>
    <div id="evidenceDrawer" class="fixed right-0 top-0 bottom-0 w-full max-w-xl bg-surface-card border-l border-surface-border z-50 transform translate-x-full transition-transform duration-300 ease-in-out overflow-y-auto p-6 shadow-2xl">
      <div class="flex items-center justify-between border-b border-surface-border pb-4 mb-6">
        <div>
          <span id="drawerCategory" class="text-xs font-mono text-[#8090b8] uppercase tracking-wider"></span>
          <h3 id="drawerTitle" class="text-2xl font-bold text-white mt-0.5"></h3>
        </div>
        <button onclick="closeDrawer()" class="p-1.5 text-slate-400 hover:text-white rounded hover:bg-surface-raised transition-colors">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>

      <div class="space-y-6">
        <div>
          <label class="text-[11px] font-mono uppercase text-slate-400 tracking-wider">Application Description</label>
          <p id="drawerDesc" class="text-xs text-slate-200 mt-1 font-medium leading-relaxed"></p>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div class="bg-surface-raised p-3 rounded border border-surface-border">
            <label class="text-[10px] font-mono uppercase text-slate-400 tracking-wider">Auth Methods</label>
            <div id="drawerAuth" class="text-xs text-slate-200 mt-1 font-semibold"></div>
          </div>
          <div class="bg-surface-raised p-3 rounded border border-surface-border">
            <label class="text-[10px] font-mono uppercase text-slate-400 tracking-wider">Getting Access</label>
            <div id="drawerCred" class="text-xs mt-1 font-semibold"></div>
          </div>
          <div class="bg-surface-raised p-3 rounded border border-surface-border">
            <label class="text-[10px] font-mono uppercase text-slate-400 tracking-wider">API Surface</label>
            <div id="drawerApi" class="text-xs text-slate-200 mt-1 font-semibold"></div>
          </div>
          <div class="bg-surface-raised p-3 rounded border border-surface-border">
            <label class="text-[10px] font-mono uppercase text-slate-400 tracking-wider">MCP Status</label>
            <div id="drawerMcp" class="text-xs text-slate-200 mt-1 font-semibold"></div>
          </div>
        </div>

        <div class="bg-surface-raised p-3.5 rounded border border-surface-border">
          <label class="text-[11px] font-mono uppercase text-slate-400 tracking-wider">Free / Trial Developer Access</label>
          <p id="drawerFreeAccess" class="text-xs text-slate-300 mt-1 leading-relaxed"></p>
        </div>

        <div class="bg-surface-raised p-3.5 rounded border border-surface-border">
          <label class="text-[11px] font-mono uppercase text-slate-400 tracking-wider">Buildability & Primary Blocker</label>
          <div id="drawerBlockers" class="text-xs text-slate-300 mt-1 leading-relaxed"></div>
        </div>

        <div>
          <label class="text-[11px] font-mono uppercase text-slate-400 tracking-wider flex items-center justify-between">
            <span>Primary Evidence Claims</span>
            <span id="drawerConfidence" class="text-[#8090b8] text-xs font-mono"></span>
          </label>
          <div id="drawerEvidenceList" class="mt-2 space-y-2.5"></div>
        </div>

        <div class="bg-surface-raised p-3.5 rounded border border-surface-border">
          <label class="text-[11px] font-mono uppercase text-slate-400 tracking-wider">Research Notes</label>
          <p id="drawerNotes" class="text-xs text-slate-300 mt-1 leading-relaxed"></p>
        </div>
      </div>
    </div>
  </main>
    '''
