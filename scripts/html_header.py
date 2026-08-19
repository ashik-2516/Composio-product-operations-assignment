# scripts/html_header.py
HEADER_HTML = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="author" content="Shaik Ashik (smdashik2516@gmail.com)">
  <meta name="creator" content="Shaik Ashik">
  <title>Composio AI Product Ops | 100-App Integration-Readiness Audit & Case Study</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Inter"', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace']
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
    body {
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      background-color: #0a0b10;
      color: #e2e8f0;
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

