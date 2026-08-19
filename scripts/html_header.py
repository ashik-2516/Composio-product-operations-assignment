# scripts/html_header.py
HEADER_HTML = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="author" content="Shaik Ashik (smdashik2516@gmail.com)">
  <meta name="creator" content="Shaik Ashik">
  <meta name="description" content="Composio AI Product Operations Case Study: 100-App Integration-Readiness Audit across 10 SaaS categories.">
  <title>Composio AI Product Ops | 100-App Integration-Readiness Audit</title>

  <!-- Favicon (Inline SVG Data URI + standalone fallback) -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'%3E%3Crect width=\'32\' height=\'32\' rx=\'7\' fill=\'%2310111a\'/%3E%3Crect x=\'3\' y=\'3\' width=\'26\' height=\'26\' rx=\'5\' fill=\'%23506080\'/%3E%3Ctext x=\'16\' y=\'22\' font-family=\'sans-serif\' font-size=\'18\' font-weight=\'900\' fill=\'%23ffffff\' text-anchor=\'middle\'%3EC%3C/text%3E%3C/svg%3E">
  <link rel="alternate icon" href="favicon.svg" type="image/svg+xml">

  <!-- Preconnect & DNS-Prefetch for Speed -->
  <link rel="preconnect" href="https://cdn.tailwindcss.com" crossorigin>
  <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

  <!-- Fast Asynchronous Google Fonts with System Fallback -->
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" media="print" onload="this.media=\'all\'">
  <noscript>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap">
  </noscript>

  <!-- Tailwind CSS & Deferred Chart.js -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js" defer></script>

  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Inter"', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace']
          },
          colors: {
            surface: {
              DEFAULT: '#0a0b10',
              raised: '#10111a',
              card: '#141722',
              hover: '#1a1d2a',
              border: '#1f2433',
              'border-subtle': '#1a1d28'
            },
            accent: {
              DEFAULT: '#6678a0',
              hover: '#5a6a90',
              subtle: '#2d3550',
              muted: '#1e2440'
            }
          }
        }
      }
    }
  </script>

  <style>
    /* Critical Paint Styles */
    :root {
      color-scheme: dark;
    }
    html, body {
      background-color: #0a0b10;
      color: #e2e8f0;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      margin: 0;
      padding: 0;
      scroll-behavior: smooth;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    ::selection {
      background-color: #4a5a80;
      color: #ffffff;
    }
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #0a0b10;
    }
    ::-webkit-scrollbar-thumb {
      background: #1e2433;
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #2d3548;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      padding: 0.15rem 0.5rem;
      border-radius: 0.375rem;
      font-size: 0.7rem;
      font-weight: 500;
      letter-spacing: 0.01em;
    }
  </style>
</head>
<body class="min-h-screen flex flex-col antialiased text-slate-200 bg-[#0a0b10]">
'''
