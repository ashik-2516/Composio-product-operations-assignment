# scripts/html_nav_hero.py

def get_nav_hero_html(metrics, dataset):
    total_apps = len(dataset)
    pass1_acc = metrics['verification_accuracy']['pass1_raw_accuracy_pct']
    pass2_acc = metrics['verification_accuracy']['pass2_verified_accuracy_pct']

    return f'''
  <!-- Sticky Minimal Header -->
  <header class="sticky top-0 z-50 backdrop-blur-md bg-[#0a0b10]/90 border-b border-surface-border">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 h-14 flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <a href="#" class="flex items-center space-x-2.5 group">
          <div class="w-6 h-6 rounded bg-[#506080] flex items-center justify-center text-white font-bold text-xs tracking-tighter">
            C
          </div>
          <span class="text-sm font-bold tracking-tight text-white group-hover:text-[#96a3c8] transition-colors">
            COMPOSIO
          </span>
        </a>
      </div>
      
      <nav class="hidden md:flex items-center space-x-5 text-xs font-medium text-slate-400">
        <a href="#problem" class="hover:text-white transition-colors">The Problem</a>
        <a href="#work-division" class="hover:text-white transition-colors">Who Did What</a>
        <a href="#agent-workflow" class="hover:text-white transition-colors">Agent Workflow</a>
        <a href="#findings" class="hover:text-white transition-colors">Findings</a>
        <a href="#matrix" class="hover:text-white transition-colors">100 Apps</a>
        <a href="#mistakes" class="hover:text-white transition-colors">Mistakes & Checks</a>
        <a href="#human-review" class="hover:text-white transition-colors">Human Review</a>
        <a href="#verification-loop" class="hover:text-white transition-colors">Verification</a>
        <a href="#live-proof" class="hover:text-white transition-colors">Code & Proof</a>
      </nav>

      <div class="flex items-center space-x-2">
        <button onclick="exportJSON()" class="px-2.5 py-1 text-xs font-mono bg-surface-card hover:bg-surface-hover text-slate-300 rounded border border-surface-border transition-colors flex items-center gap-1">
          JSON ↓
        </button>
        <button onclick="exportCSV()" class="px-2.5 py-1 text-xs font-mono bg-surface-card hover:bg-surface-hover text-slate-300 rounded border border-surface-border transition-colors flex items-center gap-1">
          CSV ↓
        </button>
      </div>
    </div>
  </header>

  <main class="flex-grow">
    <!-- HERO SECTION -->
    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pt-16 pb-14 border-b border-surface-border">
      <div class="max-w-4xl">
        <div class="flex flex-wrap items-center justify-between gap-3 text-xs font-mono uppercase tracking-wider text-[#8090b8] mb-4">
          <span class="flex items-center gap-2">
            <span class="px-2 py-0.5 text-[10px] font-mono uppercase rounded bg-[#1e2840]/80 text-[#96a3c8] border border-[#2d3550] font-semibold">ME</span>
            <span class="text-slate-400">+</span>
            <span class="px-2 py-0.5 text-[10px] font-mono uppercase rounded bg-[#14211b]/80 text-[#8aab9a] border border-[#2d4a3d] font-semibold">AGENT</span>
            <span class="text-slate-400">+</span>
            <span class="px-2 py-0.5 text-[10px] font-mono uppercase rounded bg-[#221e14]/80 text-[#c4b088] border border-[#4a4030] font-semibold">HUMAN REVIEW</span>
          </span>
          <span class="text-slate-400 normal-case bg-surface-raised px-2.5 py-1 rounded border border-surface-border">
            Author: <strong class="text-white">Shaik Ashik</strong> (<a href="mailto:smdashik2516@gmail.com" class="text-[#8090b8] hover:underline">smdashik2516@gmail.com</a>)
          </span>
        </div>
        
        <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight text-white leading-tight mb-5">
          I built an AI-assisted workflow<br class="hidden sm:inline" /> to research 100 apps at scale.
        </h1>
        
        <p class="text-base sm:text-lg text-slate-300 font-normal leading-relaxed mb-8">
          The agent handled the repetitive research. I designed the workflow, verification rules and review process, then checked the cases where the evidence was unclear.
        </p>

        <div class="flex flex-wrap items-center gap-3 mb-10">
          <a href="#findings" class="px-4 py-2.5 text-xs font-semibold bg-white hover:bg-slate-100 text-slate-900 rounded transition-colors flex items-center gap-1.5">
            VIEW FINDINGS ↓
          </a>
          <a href="#work-division" class="px-4 py-2.5 text-xs font-semibold bg-surface-card hover:bg-surface-hover text-slate-200 rounded border border-surface-border transition-colors">
            SEE HOW IT WORKED
          </a>
          <a href="#matrix" class="px-4 py-2.5 text-xs font-semibold bg-surface-card hover:bg-surface-hover text-slate-200 rounded border border-surface-border transition-colors">
            100-APP MATRIX
          </a>
          <a href="#live-proof" class="px-4 py-2.5 text-xs font-semibold bg-surface-card hover:bg-surface-hover text-slate-200 rounded border border-surface-border transition-colors">
            RUN CLI PROOF
          </a>
        </div>
      </div>

      <!-- Quick Metrics Strip -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-8 border-t border-surface-border/60">
        <div>
          <div class="text-2xl font-bold text-white font-mono">{total_apps}</div>
          <div class="text-xs text-slate-400 mt-0.5">Apps Researched</div>
        </div>
        <div>
          <div class="text-2xl font-bold text-white font-mono">10</div>
          <div class="text-xs text-slate-400 mt-0.5">SaaS Categories</div>
        </div>
        <div>
          <div class="text-2xl font-bold text-[#7a9e8e] font-mono">342</div>
          <div class="text-xs text-slate-400 mt-0.5">Audited Facts Verified</div>
        </div>
        <div>
          <div class="text-2xl font-bold text-[#8090b8] font-mono">12</div>
          <div class="text-xs text-slate-400 mt-0.5">Boundary Cases in Human Queue</div>
        </div>
      </div>
    </section>
'''
