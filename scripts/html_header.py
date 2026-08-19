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

  <!-- Universal Favicon Suite (Base64 PNG + Root ICO + SVG Fallback) -->
  <link rel="icon" type="image/png" sizes="64x64" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAEcElEQVR4nOWba0wcVRTH/3PZXZZll+7yXh7dQqFUWkHbSGsfhsZUTdtU1EajQRJfGI01JmrSTzYm+EUTtSZNtDFp7AejTYxgUq1USCkpVbRgX7SlQguFugW3QF32vWDmYi5ot7CzdLLcub9kknNn5p695z9n7syc2ZGstpxJCAyB4BAIDoHg6ObTufLRWiwUjjbsi6mfpHQSXEhB3wkxiNaCVzpOKZoM4CXwWLKBaDn4aMZP5tOZF2aLg0BwiNaP/lzxECU7806kuAgEh0BwiCjpf7v4CASHQHAIBEcXjx81JxtRsjQfNqsZiyzJCAZDcHt86B8cwuV+J8LhCW0KUHFvCbZtXoPSEgcSSOTk8/mDOHbiNBp+PIFrTpc2BEizWbDzhSqUryi8ZZvXF4DBoGOCGBP1eKhyNTatL8f+rxrxQ/OvfAtgz0rFu2/XICNtEW2HQmEcaenAsZ/P0HT3B4J0fXamDavuLsb2h9ciK8MGvV6H2me3INGgR/3hNj4FSLGY8N6u5+i5LjPodOGDvQfRNzB0y77OoRF839SOptZOvPb8dmxYs5Kur3lyM7p7B9DV3c/fVeD1F6tY8MOuMex+/0DE4GciZ8TH+77F+UtTAUsS8FL1FtXGSNRyvL5iBVaXFbP2J5/XwzVyM6q+4YkJfHbgEGsvyc/CsqV5fAlQ9cg6Zh9vP4ezF64o6i9nyrmLfax93z3LwI0ARUtyUFSQw9qxzuQdpy8xu3CxHdxMgmWlBcweHXP/50gqofn4KTpxyni8PnAjQGmJg9ndvYMx+5HF+6XjAtSEqOHUnpnK7P45Zv14Q9RwajGbmO32eCGcACZTIrN9vgCEE8Dvn7q9lTEaDRBOAPf4dNqbTUkQTgDXjDu+/NwMLGR0aji92DOAu4oXU7uoIDdmP7n2dOTZ06l9fXgEV65eBxcZcH7Gk5tcC1helB+Tn2ce34RdO5+iS8Wq5VADoobTjjN/YPTmOGvLBQ6l6HUJKC+dLqBc7vsT3AgQCoXRePQka1euK6PPB0p44P4yJJuM1PZ4/TjV1QuungYbDrfhrxtTk6EkSXij9jFYzNFdEVLMJlTveJC1G1tOIhAI8SWAx+vH3v3fYXJyekJ7581qZKZbZ+2XarVg91vVsKYks0LK1/Utag0TqlaEfj/b868IUyrIp8Geulfo0XXkZSIhgbAMkYseT1dVYk/dqyh02Nn9RN1HX8LnD/BbFG1q7YTX68fLNVtpjdCYaMATWzfQRdbF6/MjyWigIsxEvuR9+Ok3uHptmP+yeNtvXXQS27FtIzauXYk0WwpdL8dsSpp+bpCRAz70UzuaWzsRDIW182Jk3OPDFweP0KXQkY2c7HR6nssZIW8bGXOju2cAN0b/huZfjfX2OemyECAQHALBIRAccqf+dc0L/4+PQHAIBIdEWqnV0yBSXETJzjxzu3gIBIfMtlErWTBbHGQ+nXlgrvFLSj6a4ulvtNEeOKKG03ijZJzSfL4dFvK7Qa1BIDgk3gOIN/8ACpp3QvajoqoAAAAASUVORK5CYII=">
  <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="apple-touch-icon" href="favicon.png">

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
