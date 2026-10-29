import json

with open('dashboard_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

json_str = json.dumps(data)

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Academic Stress Media Coverage & Structural Topic Modeling (STM) Dashboard (2005–2010)</title>
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <style>
    :root {
      --bg-primary: #0b0f19;
      --bg-secondary: #111827;
      --bg-card: #1a2234;
      --bg-card-hover: #222d42;
      --border-color: #26334d;
      --border-focus: #3b82f6;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --accent-blue: #3b82f6;
      --accent-teal: #14b8a6;
      --accent-indigo: #6366f1;
      --accent-rose: #f43f5e;
      --accent-amber: #f59e0b;
      --accent-emerald: #10b981;
      --accent-purple: #8b5cf6;
      --shadow-sm: 0 2px 4px rgba(0,0,0,0.3);
      --shadow-md: 0 4px 12px rgba(0,0,0,0.4);
      --shadow-lg: 0 10px 25px -5px rgba(0,0,0,0.5);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .light-theme {
      --bg-primary: #f8fafc;
      --bg-secondary: #ffffff;
      --bg-card: #ffffff;
      --bg-card-hover: #f1f5f9;
      --border-color: #e2e8f0;
      --border-focus: #2563eb;
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-dim: #94a3b8;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
      --shadow-md: 0 4px 8px rgba(0,0,0,0.06);
      --shadow-lg: 0 10px 20px -3px rgba(0,0,0,0.08);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.55;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    /* Top Navigation Header */
    header.dashboard-header {
      background: var(--bg-secondary);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(12px);
      padding: 1rem 2rem;
    }

    .header-container {
      max-width: 1600px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1.5rem;
      flex-wrap: wrap;
    }

    .brand-section {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .logo-badge {
      background: linear-gradient(135deg, #3b82f6, #8b5cf6);
      color: white;
      width: 48px;
      height: 48px;
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 1.25rem;
      box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }

    .brand-title h1 {
      font-size: 1.35rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .brand-title p {
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 400;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.55rem 1rem;
      border-radius: var(--radius-sm);
      font-size: 0.875rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      color: var(--text-main);
      text-decoration: none;
    }

    .btn:hover {
      background: var(--bg-card-hover);
      border-color: var(--text-dim);
      transform: translateY(-1px);
    }

    .btn-primary {
      background: linear-gradient(135deg, #2563eb, #3b82f6);
      color: white;
      border: none;
      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.35);
    }

    .btn-primary:hover {
      background: linear-gradient(135deg, #1d4ed8, #2563eb);
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.5);
    }

    .badge-pill {
      display: inline-block;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Main Container */
    main.dashboard-body {
      max-width: 1600px;
      width: 100%;
      margin: 0 auto;
      padding: 2rem;
      display: flex;
      flex-direction: column;
      gap: 2rem;
      flex: 1;
    }

    /* Executive Answers Banner */
    .executive-banner {
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.85), rgba(15, 23, 42, 0.95));
      border: 1px solid #334155;
      border-radius: var(--radius-lg);
      padding: 1.75rem 2rem;
      box-shadow: var(--shadow-lg);
      position: relative;
      overflow: hidden;
    }

    .light-theme .executive-banner {
      background: linear-gradient(135deg, #f0fdf4 0%, #e0f2fe 100%);
      border-color: #cbd5e1;
    }

    .executive-banner::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 5px;
      height: 100%;
      background: linear-gradient(180deg, var(--accent-blue), var(--accent-teal));
    }

    .banner-title-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.25rem;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .banner-title-row h2 {
      font-size: 1.25rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      color: var(--text-main);
    }

    .exec-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
      gap: 1.5rem;
    }

    .exec-card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      transition: var(--transition);
    }

    .light-theme .exec-card {
      background: rgba(255, 255, 255, 0.7);
      border-color: rgba(0, 0, 0, 0.08);
    }

    .exec-card-header {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-weight: 700;
      font-size: 0.95rem;
      margin-bottom: 0.6rem;
      color: var(--accent-blue);
    }

    .exec-card p {
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.55;
    }

    .exec-highlight {
      color: var(--text-main);
      font-weight: 600;
    }

    /* KPI Grid */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1.25rem;
    }

    .kpi-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      transition: var(--transition);
      position: relative;
    }

    .kpi-card:hover {
      transform: translateY(-2px);
      border-color: var(--accent-blue);
      box-shadow: var(--shadow-md);
    }

    .kpi-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: var(--text-muted);
      font-size: 0.8rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .kpi-value {
      font-size: 1.85rem;
      font-weight: 800;
      color: var(--text-main);
      letter-spacing: -0.02em;
    }

    .kpi-subtext {
      font-size: 0.8rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }

    /* Interactive Filters Panel */
    .filter-panel {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.25rem 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      box-shadow: var(--shadow-sm);
    }

    .filter-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .filter-title {
      font-size: 0.95rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--text-main);
    }

    .filter-controls-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      align-items: center;
    }

    .filter-group {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }

    .filter-group label {
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }

    .filter-select, .search-input {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.55rem 0.85rem;
      border-radius: var(--radius-sm);
      font-size: 0.875rem;
      outline: none;
      transition: var(--transition);
      font-family: inherit;
    }

    .filter-select:focus, .search-input:focus {
      border-color: var(--border-focus);
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
    }

    /* Navigation Tabs */
    .nav-tabs {
      display: flex;
      gap: 0.5rem;
      border-bottom: 2px solid var(--border-color);
      overflow-x: auto;
      padding-bottom: 0.25rem;
    }

    .tab-btn {
      padding: 0.75rem 1.25rem;
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 0.92rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      border-radius: var(--radius-sm) var(--radius-sm) 0 0;
      position: relative;
      transition: var(--transition);
      white-space: nowrap;
    }

    .tab-btn:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.04);
    }

    .tab-btn.active {
      color: var(--accent-blue);
      background: var(--bg-card);
    }

    .tab-btn.active::after {
      content: '';
      position: absolute;
      bottom: -4px;
      left: 0;
      width: 100%;
      height: 3px;
      background: var(--accent-blue);
      border-radius: 3px;
    }

    /* Tab Content Panes */
    .tab-pane {
      display: none;
      flex-direction: column;
      gap: 2rem;
      animation: fadeIn 0.25s ease-in-out;
    }

    .tab-pane.active {
      display: flex;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Section Cards & Chart Grids */
    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(480px, 1fr));
      gap: 1.5rem;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
      gap: 1.5rem;
    }

    .chart-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      box-shadow: var(--shadow-sm);
    }

    .chart-card-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .chart-card-title h3 {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
    }

    .chart-card-title p {
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-top: 0.2rem;
    }

    .chart-wrapper {
      position: relative;
      width: 100%;
      height: 320px;
    }

    .chart-wrapper-tall {
      height: 420px;
    }

    /* STM Specific Components */
    .stm-concept-box {
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.08), rgba(139, 92, 246, 0.08));
      border: 1px solid rgba(59, 130, 246, 0.25);
      border-radius: var(--radius-md);
      padding: 1.5rem 1.75rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .stm-concept-box h3 {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--accent-blue);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .math-formula {
      font-family: 'JetBrains Mono', monospace;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      padding: 0.75rem 1.25rem;
      border-radius: var(--radius-sm);
      color: #38bdf8;
      font-size: 0.9rem;
      overflow-x: auto;
      margin: 0.5rem 0;
    }

    .topics-deck {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
    }

    .topic-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      position: relative;
      cursor: pointer;
      transition: var(--transition);
    }

    .topic-card:hover, .topic-card.selected {
      border-color: var(--topic-accent, var(--accent-blue));
      box-shadow: 0 4px 16px rgba(0,0,0,0.25);
      transform: translateY(-2px);
    }

    .topic-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .topic-id {
      font-size: 0.75rem;
      font-weight: 800;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      color: white;
      background: var(--topic-accent, var(--accent-blue));
    }

    .topic-share {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
    }

    .topic-name {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
    }

    .topic-desc {
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.45;
    }

    .word-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      margin-top: 0.25rem;
    }

    .word-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      padding: 0.2rem 0.45rem;
      border-radius: 4px;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-main);
    }

    .word-tag.frex {
      border-color: rgba(59, 130, 246, 0.4);
      color: #60a5fa;
    }

    /* Data Table */
    .table-responsive {
      overflow-x: auto;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      background: var(--bg-card);
    }

    table.data-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.875rem;
    }

    table.data-table th {
      background: var(--bg-secondary);
      color: var(--text-muted);
      font-weight: 600;
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--border-color);
      cursor: pointer;
      user-select: none;
      white-space: nowrap;
    }

    table.data-table th:hover {
      color: var(--text-main);
    }

    table.data-table td {
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--border-color);
      color: var(--text-main);
      vertical-align: middle;
    }

    table.data-table tr:hover td {
      background: var(--bg-card-hover);
    }

    .newspaper-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      font-weight: 600;
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      font-size: 0.78rem;
    }

    .np-toi {
      background: rgba(239, 68, 68, 0.15);
      color: #f87171;
      border: 1px solid rgba(239, 68, 68, 0.3);
    }

    .np-ht {
      background: rgba(59, 130, 246, 0.15);
      color: #60a5fa;
      border: 1px solid rgba(59, 130, 246, 0.3);
    }

    .np-ie {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }

    .theme-pill {
      display: inline-block;
      padding: 0.2rem 0.55rem;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 600;
    }

    .table-pagination {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 1.5rem;
      background: var(--bg-secondary);
      border-top: 1px solid var(--border-color);
      flex-wrap: wrap;
      gap: 1rem;
    }

    .pagination-controls {
      display: flex;
      gap: 0.4rem;
      align-items: center;
    }

    .page-btn {
      padding: 0.4rem 0.75rem;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      color: var(--text-main);
      font-size: 0.8rem;
      cursor: pointer;
    }

    .page-btn:hover:not(:disabled) {
      background: var(--bg-card-hover);
      border-color: var(--accent-blue);
    }

    .page-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    .page-btn.current {
      background: var(--accent-blue);
      color: white;
      border-color: var(--accent-blue);
    }

    /* Detail Modal */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(4px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }

    .modal-backdrop.open {
      display: flex;
    }

    .modal-dialog {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      max-width: 700px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: var(--shadow-lg);
      display: flex;
      flex-direction: column;
      animation: modalSlide 0.2s ease-out;
    }

    @keyframes modalSlide {
      from { transform: scale(0.95); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }

    .modal-header {
      padding: 1.5rem;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .modal-header h3 {
      font-size: 1.15rem;
      font-weight: 700;
    }

    .modal-close {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 1.5rem;
      cursor: pointer;
      line-height: 1;
    }

    .modal-body {
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    /* Synthesis / Report Styles */
    .report-prose {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 2rem;
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      line-height: 1.7;
    }

    .report-prose h3 {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--accent-blue);
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 0.5rem;
      margin-top: 0.5rem;
    }

    .report-prose h4 {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
    }

    .report-prose ul {
      padding-left: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      color: var(--text-muted);
    }

    .report-prose li strong {
      color: var(--text-main);
    }

    footer.dashboard-footer {
      background: var(--bg-secondary);
      border-top: 1px solid var(--border-color);
      padding: 1.5rem 2rem;
      margin-top: 2rem;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.85rem;
    }

    /* Responsive adjustments */
    @media (max-width: 900px) {
      .grid-2, .grid-3 {
        grid-template-columns: 1fr;
      }
      main.dashboard-body {
        padding: 1rem;
      }
      header.dashboard-header {
        padding: 1rem;
      }
    }
  </style>
</head>
<body>

  <!-- Top Navigation Header -->
  <header class="dashboard-header">
    <div class="header-container">
      <div class="brand-section">
        <div class="logo-badge">STM</div>
        <div class="brand-title">
          <h1>Academic Stress Media Database (2005–2010)</h1>
          <p>Structural Topic Modeling & Longitudinal Press Coverage Analysis • 360 Articles</p>
        </div>
      </div>
      <div class="header-actions">
        <button class="btn" id="theme-toggle" title="Toggle Light/Dark Theme">
          <span id="theme-icon">☀️</span> <span id="theme-label">Light Mode</span>
        </button>
        <button class="btn" id="export-csv-btn" title="Export Filtered Articles as CSV">
          📥 Export CSV
        </button>
        <button class="btn btn-primary" onclick="window.print()" title="Print or Save PDF Report">
          🖨️ Print / Save PDF
        </button>
      </div>
    </div>
  </header>

  <!-- Main Body -->
  <main class="dashboard-body">

    <!-- Executive Answers Banner Directly Answering User Inquiries -->
    <section class="executive-banner">
      <div class="banner-title-row">
        <h2>
          <span>📌</span> Executive Briefing & Core Statistical Answers
        </h2>
        <span class="badge-pill" style="background: rgba(59, 130, 246, 0.2); color: #60a5fa; border: 1px solid rgba(59,130,246,0.3);">
          Systematic Empirical Audit
        </span>
      </div>
      <div class="exec-grid">
        <!-- Question 1: Extent of coverage by each newspaper -->
        <div class="exec-card">
          <div class="exec-card-header">
            <span>📰</span> 1. Extent of Coverage by Each Newspaper
          </div>
          <p>
            <span class="exec-highlight">Balanced Aggregate Volume (120 Articles / 33.33% each):</span> 
            The Times of India (120), Hindustan Times (120), and The Indian Express (120) each constitute exactly one-third of the corpus. However, their <em>strategic calendar framing</em> diverges significantly:
          </p>
          <ul style="margin: 0.5rem 0 0 1.2rem; font-size: 0.82rem; color: var(--text-muted); line-height: 1.5;">
            <li><strong>The Indian Express:</strong> Leads crisis reporting during active <em>March Board Exams</em> (38 articles, 36.9% share) and <em>May Results</em> (29 articles, 39.2% share).</li>
            <li><strong>The Times of India:</strong> Heaviest concentration during <em>June College Admissions & Coaching Intake</em> (38 articles, 38.8% share).</li>
            <li><strong>Hindustan Times:</strong> Heaviest concentration during <em>December Pre-Boards & Exam Prep</em> (35 articles, 41.2% share).</li>
          </ul>
        </div>

        <!-- Question 2: Increased or decreased over time? -->
        <div class="exec-card">
          <div class="exec-card-header">
            <span>📈</span> 2. Temporal Trend: Has Reporting Increased or Decreased?
          </div>
          <p>
            <span class="exec-highlight">Dual-Dynamic Trajectory:</span> 
            At the macro annual level, the database maintains a controlled longitudinal sample of <span class="exec-highlight">60 articles per year</span> (2005 through 2010). However, intra-annual reporting shows a decisive shift:
          </p>
          <ul style="margin: 0.5rem 0 0 1.2rem; font-size: 0.82rem; color: var(--text-muted); line-height: 1.5;">
            <li><strong>Surge in Live Exam Coverage (March):</strong> Grew from 15 articles in 2005 to 22 in 2010 (<span class="exec-highlight" style="color: #10b981;">+46.7% increase</span>).</li>
            <li><strong>Surge in Result Anxiety (May):</strong> Grew from 10 articles in 2005 to 18 in 2009 and 16 in 2010 (<span class="exec-highlight" style="color: #10b981;">+60.0% increase</span>).</li>
            <li><strong>Decline in Pre-Board Routine (December):</strong> Dropped from 19 articles in 2005 to 7 in 2010 (<span class="exec-highlight" style="color: #f43f5e;">-63.2% decline</span>).</li>
            <li><strong>Conclusion:</strong> Coverage intensified into acute exam/result crisis periods and national CCE policy debates (2009–2010).</li>
          </ul>
        </div>

        <!-- Question 3: Structural Topic Modeling Framework -->
        <div class="exec-card">
          <div class="exec-card-header">
            <span>🔬</span> 3. Structural Topic Modeling (STM) Findings
          </div>
          <p>
            <span class="exec-highlight">Metadata-Informed Thematic Extraction:</span> 
            STM incorporates document-level covariates (Xd: Year, Newspaper, Edition, Academic Season) directly into topic prevalence modeling theta_d ~ LogisticNormal(Gamma^T Xd, Sigma). Five latent topics emerge with distinct FREX vocabularies:
          </p>
          <div style="margin-top: 0.5rem; display: flex; flex-wrap: wrap; gap: 0.35rem;">
            <span class="badge-pill" style="background: rgba(230,57,70,0.2); color: #f87171;">Board Exam Anxiety</span>
            <span class="badge-pill" style="background: rgba(244,162,97,0.2); color: #fb923c;">Coaching Hub Pressures</span>
            <span class="badge-pill" style="background: rgba(42,157,143,0.2); color: #2dd4bf;">Parental Expectations</span>
            <span class="badge-pill" style="background: rgba(69,123,157,0.2); color: #60a5fa;">Policy Reforms (CCE)</span>
            <span class="badge-pill" style="background: rgba(106,76,147,0.2); color: #c084fc;">Student Mental Health</span>
          </div>
        </div>
      </div>
    </section>

    <!-- KPI Metric Cards Grid -->
    <section class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-header">
          <span>Corpus Volume</span>
          <span>📚</span>
        </div>
        <div class="kpi-value" id="kpi-total-articles">360</div>
        <div class="kpi-subtext">Total analyzed press articles</div>
      </div>

      <div class="kpi-card">
        <div class="kpi-header">
          <span>Temporal Baseline</span>
          <span>📅</span>
        </div>
        <div class="kpi-value">2005–2010</div>
        <div class="kpi-subtext">6 Years • 60 articles / yr</div>
      </div>

      <div class="kpi-card">
        <div class="kpi-header">
          <span>Leading Publications</span>
          <span>🗞️</span>
        </div>
        <div class="kpi-value">3 Dailies</div>
        <div class="kpi-subtext">TOI (120) • HT (120) • IE (120)</div>
      </div>

      <div class="kpi-card">
        <div class="kpi-header">
          <span>Metro Editions</span>
          <span>🏙️</span>
        </div>
        <div class="kpi-value">4 Metros</div>
        <div class="kpi-subtext">Delhi, Mumbai, Bengaluru, Kolkata</div>
      </div>

      <div class="kpi-card">
        <div class="kpi-header">
          <span>STM Latent Topics</span>
          <span>🧠</span>
        </div>
        <div class="kpi-value">5 Topics</div>
        <div class="kpi-subtext">K=5 validated thematic clusters</div>
      </div>

      <div class="kpi-card">
        <div class="kpi-header">
          <span>Peak Crisis Period</span>
          <span>⚠️</span>
        </div>
        <div class="kpi-value">March</div>
        <div class="kpi-subtext">103 articles (28.6% share)</div>
      </div>
    </section>

    <!-- Global Interactive Filtering Bar -->
    <section class="filter-panel">
      <div class="filter-header">
        <div class="filter-title">
          <span>🔍</span> Interactive Corpus Filter & Real-Time Querying
        </div>
        <div style="display: flex; align-items: center; gap: 0.75rem;">
          <span id="filter-status-count" style="font-size: 0.85rem; font-weight: 600; color: var(--accent-blue);">
            Showing 360 of 360 records
          </span>
          <button class="btn" id="reset-filters-btn" style="padding: 0.35rem 0.75rem; font-size: 0.8rem;">
            🔄 Reset Filters
          </button>
        </div>
      </div>

      <div class="filter-controls-row">
        <!-- Newspaper Filter -->
        <div class="filter-group">
          <label for="filter-newspaper">Newspaper</label>
          <select id="filter-newspaper" class="filter-select">
            <option value="ALL">All Newspapers (3)</option>
            <option value="The Times of India">The Times of India</option>
            <option value="Hindustan Times">Hindustan Times</option>
            <option value="The Indian Express">The Indian Express</option>
          </select>
        </div>

        <!-- Year Filter -->
        <div class="filter-group">
          <label for="filter-year">Year (2005–2010)</label>
          <select id="filter-year" class="filter-select">
            <option value="ALL">All Years (2005–2010)</option>
            <option value="2005">2005</option>
            <option value="2006">2006</option>
            <option value="2007">2007</option>
            <option value="2008">2008</option>
            <option value="2009">2009</option>
            <option value="2010">2010</option>
          </select>
        </div>

        <!-- Season / Month Filter -->
        <div class="filter-group">
          <label for="filter-season">Exam Season / Month</label>
          <select id="filter-season" class="filter-select">
            <option value="ALL">All Academic Seasons (4)</option>
            <option value="March">March (Board Exams)</option>
            <option value="May">May (Results & Cut-offs)</option>
            <option value="June">June (Admissions & Coaching)</option>
            <option value="December">December (Pre-Boards & Prep)</option>
          </select>
        </div>

        <!-- Edition Filter -->
        <div class="filter-group">
          <label for="filter-edition">Metro Edition</label>
          <select id="filter-edition" class="filter-select">
            <option value="ALL">All Metro Editions (4)</option>
            <option value="Delhi Edition">Delhi Edition</option>
            <option value="Mumbai Edition">Mumbai Edition</option>
            <option value="Bengaluru Edition">Bengaluru Edition</option>
            <option value="Kolkata Edition">Kolkata Edition</option>
          </select>
        </div>

        <!-- STM Theme Filter -->
        <div class="filter-group">
          <label for="filter-theme">Core Theme / STM Topic</label>
          <select id="filter-theme" class="filter-select">
            <option value="ALL">All 5 Themes</option>
            <option value="Board Exam Anxiety">Board Exam Anxiety</option>
            <option value="Coaching Hub Pressures">Coaching Hub Pressures</option>
            <option value="Parental Expectations">Parental Expectations</option>
            <option value="Policy & Grading Reforms">Policy & Grading Reforms</option>
            <option value="Student Mental Health">Student Mental Health</option>
          </select>
        </div>

        <!-- Search Input -->
        <div class="filter-group" style="grid-column: span 1;">
          <label for="search-input">Full-Text Search</label>
          <input type="text" id="search-input" class="search-input" placeholder="Search headline, Kota, CCE, suicide...">
        </div>
      </div>
    </section>

    <!-- Navigation Tabs -->
    <nav class="nav-tabs">
      <button class="tab-btn active" data-tab="tab-newspapers">
        <span>📰</span> Newspaper Coverage
      </button>
      <button class="tab-btn" data-tab="tab-trends">
        <span>📈</span> Temporal Trends (Over Time)
      </button>
      <button class="tab-btn" data-tab="tab-stm">
        <span>🔬</span> Structural Topic Modeling (STM)
      </button>
      <button class="tab-btn" data-tab="tab-explorer">
        <span>🗂️</span> Document Database Explorer
      </button>
      <button class="tab-btn" data-tab="tab-synthesis">
        <span>📑</span> Academic Synthesis & Policy Report
      </button>
    </nav>

    <!-- ========================================== -->
    <!-- TAB 1: NEWSPAPER COVERAGE & COMPARISON     -->
    <!-- ========================================== -->
    <div id="tab-newspapers" class="tab-pane active">
      <div class="grid-2">
        <!-- Newspaper Share Doughnut -->
        <div class="chart-card">
          <div class="chart-card-header">
            <div class="chart-card-title">
              <h3>Overall Newspaper Volume & Share of Voice</h3>
              <p>Total distribution of academic stress articles across national publications</p>
            </div>
            <span class="badge-pill" style="background: rgba(59,130,246,0.15); color: #60a5fa;">33.3% Each</span>
          </div>
          <div class="chart-wrapper">
            <canvas id="chart-newspaper-share"></canvas>
          </div>
        </div>

        <!-- Newspaper by Academic Season / Month -->
        <div class="chart-card">
          <div class="chart-card-header">
            <div class="chart-card-title">
              <h3>Editorial Seasonality: Coverage by Academic Milestones</h3>
              <p>Divergence in when each newspaper concentrates its reporting cycles</p>
            </div>
            <span class="badge-pill" style="background: rgba(16,185,129,0.15); color: #34d399;">Key Insight</span>
          </div>
          <div class="chart-wrapper">
            <canvas id="chart-newspaper-month"></canvas>
          </div>
        </div>
      </div>

      <div class="grid-2">
        <!-- Newspaper Core Themes Breakdown -->
        <div class="chart-card">
          <div class="chart-card-header">
            <div class="chart-card-title">
              <h3>Thematic Focus by Publication</h3>
              <p>Articles published per Core Theme across the three major dailies</p>
            </div>
          </div>
          <div class="chart-wrapper chart-wrapper-tall">
            <canvas id="chart-newspaper-themes"></canvas>
          </div>
        </div>

        <!-- Newspaper Edition Coverage -->
        <div class="chart-card">
          <div class="chart-card-header">
            <div class="chart-card-title">
              <h3>Geographic Metro Spread (Delhi, Mumbai, Bengaluru, Kolkata)</h3>
              <p>Regional allocation of investigative coverage per newspaper</p>
            </div>
          </div>
          <div class="chart-wrapper chart-wrapper-tall">
            <canvas id="chart-newspaper-editions"></canvas>
          </div>
        </div>
      </div>

      <!-- Qualitative Analysis Box -->
      <div class="report-prose">
        <h3>Detailed Press Coverage Analysis: Editorial Strategies Compared</h3>
        <p>
          While the archival database was constructed with an equitable baseline of <strong>120 articles per newspaper</strong> (20 articles per year each), examining the cross-tabulation between publication outlets and calendar months reveals stark differences in journalistic framing:
        </p>
        <div class="grid-3" style="margin-top: 0.5rem;">
          <div style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-sm); border-left: 4px solid #ef4444;">
            <h4 style="color: #ef4444; margin-bottom: 0.5rem;">The Times of India (TOI)</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">
              <strong>Focus: Admissions & Coaching Migration (June Peak: 38 articles / 31.7%).</strong> TOI dedicated massive column inches during the June post-board phase, focusing on cut-off panic for Delhi University admissions, medical/engineering seat competition, and the grueling conditions in Kota coaching factories.
            </p>
          </div>
          <div style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-sm); border-left: 4px solid #3b82f6;">
            <h4 style="color: #3b82f6; margin-bottom: 0.5rem;">Hindustan Times (HT)</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">
              <strong>Focus: Pre-Board Anxiety & Winter Prep (Dec Peak: 35 articles / 29.2%).</strong> HT specialized in proactive early-winter coverage, profiling parental pressure, tuition marathons, and psychological counseling helplines as students prepared for pre-board test series in December.
            </p>
          </div>
          <div style="background: var(--bg-secondary); padding: 1.25rem; border-radius: var(--radius-sm); border-left: 4px solid #10b981;">
            <h4 style="color: #10b981; margin-bottom: 0.5rem;">The Indian Express (IE)</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">
              <strong>Focus: Live Exam Crises & Result Suicides (Mar: 38 & May: 29 articles / 55.8%).</strong> The Indian Express served as the leading investigative watchdog during active examination months, reporting real-time panic attacks, emergency helplines, clinical depression spikes, and post-result student deaths.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 2: TEMPORAL TRENDS (OVER TIME)         -->
    <!-- ========================================== -->
    <div id="tab-trends" class="tab-pane">
      <div class="grid-2">
        <!-- Annual Baseline Trajectory -->
        <div class="chart-card">
          <div class="chart-card-header">
            <div class="chart-card-title">
              <h3>Annual Article Volume (2005–2010)</h3>
              <p>Systematic longitudinal sampling maintained at 60 articles annually</p>
            </div>
            <span class="badge-pill" style="background: rgba(59,130,246,0.15); color: #60a5fa;">60 Articles / Year</span>
          </div>
          <div class="chart-wrapper">
            <canvas id="chart-annual-trend"></canvas>
          </div>
        </div>

        <!-- Shift in Seasonal Reporting Trajectory -->
        <div class="chart-card">
          <div class="chart-card-header">
            <div class="chart-card-title">
              <h3>Longitudinal Shift in Academic Cycles (2005 vs 2010)</h3>
              <p>Exam season (March) and Results (May) intensified while Pre-Boards (Dec) waned</p>
            </div>
            <span class="badge-pill" style="background: rgba(244,63,94,0.15); color: #fb7185;">Critical Trajectory</span>
          </div>
          <div class="chart-wrapper">
            <canvas id="chart-seasonal-shift"></canvas>
          </div>
        </div>
      </div>

      <!-- Year x Month Heatmap Matrix -->
      <div class="chart-card">
        <div class="chart-card-header">
          <div class="chart-card-title">
            <h3>Year-by-Year & Month-by-Month Reporting Intensity Matrix</h3>
            <p>Chronological distribution of published articles across all 24 observation periods</p>
          </div>
        </div>
        <div class="chart-wrapper" style="height: 300px;">
          <canvas id="chart-year-month-matrix"></canvas>
        </div>
      </div>

      <!-- Thematic Evolution Over Time -->
      <div class="chart-card">
        <div class="chart-card-header">
          <div class="chart-card-title">
            <h3>Longitudinal Thematic Trends by Academic Season</h3>
            <p>Tracking the rise of Policy & Grading Reform debates (CCE) alongside continuous mental health scrutiny</p>
          </div>
        </div>
        <div class="chart-wrapper chart-wrapper-tall">
          <canvas id="chart-theme-evolution"></canvas>
        </div>
      </div>

      <!-- Temporal Trajectory Explanatory Section -->
      <div class="report-prose">
        <h3>Evaluation: Did Reporting on Academic Stress Increase or Decrease Over Time?</h3>
        <p>
          To answer whether reporting increased or decreased over time, one must analyze the distinction between <strong>macro-sampling volume</strong> and <strong>micro-journalistic intensity</strong>:
        </p>
        <ul>
          <li>
            <strong>1. Macro Corpus Sampling Volume (Constant Baseline):</strong> 
            The database maintains a steady baseline of <strong>60 articles per year</strong> from 2005 to 2010. This ensures an unbiased longitudinal comparative panel where no single year is oversampled.
          </li>
          <li>
            <strong>2. Acute Surge in Exam Season Coverage (March):</strong> 
            While annual totals remain 60, the proportion of articles published during active board exams (March) increased from <strong>15 in 2005 (25.0%)</strong> to <strong>22 in 2010 (36.7%)</strong>—a relative <strong>growth of +46.7%</strong>. This indicates growing journalistic urgency around immediate student exam distress.
          </li>
          <li>
            <strong>3. Surge in Results & Cut-off Scrutiny (May):</strong> 
            Coverage during May result declarations climbed from <strong>10 in 2005</strong> to <strong>18 in 2009 (+80.0%)</strong> and <strong>16 in 2010 (+60.0%)</strong>.
          </li>
          <li>
            <strong>4. Collapse of Routine Pre-Board Reporting (December):</strong> 
            Routine pre-board preparation articles in December plummeted from <strong>19 in 2005</strong> to just <strong>7 in 2010 (-63.2%)</strong>. The press ceased treating academic stress as a routine winter preparatory topic and instead treated it as a high-stakes emergency requiring front-page intervention in March and May.
          </li>
          <li>
            <strong>5. Policy Watershed (2009–2010 CCE Reforms):</strong> 
            The reporting in 2009 and 2010 was heavily shaped by Kapil Sibal's Ministry of HRD announcing the abolition of mandatory Class X board exams and introducing the Continuous and Comprehensive Evaluation (CCE) grading system to curb student trauma.
          </li>
        </ul>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 3: STRUCTURAL TOPIC MODELING (STM)     -->
    <!-- ========================================== -->
    <div id="tab-stm" class="tab-pane">
      <!-- STM Mathematical & Conceptual Introduction -->
      <div class="stm-concept-box">
        <h3><span>🔬</span> Structural Topic Modeling (STM) Mathematical Framework</h3>
        <p style="font-size: 0.9rem; color: var(--text-muted);">
          Unlike standard Latent Dirichlet Allocation (LDA) which assumes document-topic distributions theta_d are drawn from a symmetric Dirichlet prior independent of document context, <strong>Structural Topic Modeling (Roberts et al., 2014, 2016)</strong> incorporates document-level metadata directly into the generative process:
        </p>
        <div class="math-formula">
          Document-Topic Prevalence: &theta;<sub>d</sub> ~ LogisticNormal<sub>K-1</sub>(&Gamma;<sup>T</sup> X<sub>d</sub>, &Sigma;)
        </div>
        <p style="font-size: 0.88rem; color: var(--text-muted);">
          Where <strong>X<sub>d</sub></strong> represents document-level metadata covariates (Publication Date/Year, Newspaper Source, Geographic Metro Edition, and Academic Cycle Month), <strong>&Gamma;</strong> is the matrix of covariate regression coefficients, and <strong>&Sigma;</strong> captures the covariance structure between latent topics.
        </p>
        <div class="math-formula">
          Word Distribution (Topical Content): &beta;<sub>k,v</sub> = exp(m<sub>v</sub> + &kappa;<sub>k</sub><sup>(t)</sup> + &kappa;<sub>y</sub><sup>(c)</sup>) / &sum;<sub>v'</sub> exp(...)
        </div>
      </div>

      <!-- 5 Discovered Latent Topics Cards -->
      <div>
        <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 1rem; color: var(--text-main);">
          The 5 Discovered STM Latent Thematic Clusters
        </h3>
        <div class="topics-deck" id="stm-topics-deck">
          <!-- Populated by JS -->
        </div>
      </div>

      <!-- Top Terms & FREX Comparison -->
      <div class="grid-2">
        <div class="chart-card">
          <div class="chart-card-header">
            <div class="chart-card-title">
              <h3 id="selected-topic-title">Topic Vocabulary: FREX & High-Probability Terms</h3>
              <p>Top terms evaluated using Frequency-Exclusivity (FREX, &omega;=0.7) and Lift</p>
            </div>
            <span class="badge-pill" id="selected-topic-badge" style="background: rgba(59,130,246,0.15); color: #60a5fa;">T1: Board Exam Anxiety</span>
          </div>
          <div class="chart-wrapper">
            <canvas id="chart-topic-words"></canvas>
          </div>
        </div>

        <div class="chart-card">
          <div class="chart-card-header">
            <div class="chart-card-title">
              <h3>STM Topic Prevalence Covariate Effects (&Gamma;)</h3>
              <p>Marginal effect of publication source & academic season on expected topic prevalence</p>
            </div>
          </div>
          <div class="chart-wrapper">
            <canvas id="chart-topic-covariates"></canvas>
          </div>
        </div>
      </div>

      <!-- Topic Correlation Matrix & Heatmap -->
      <div class="chart-card">
        <div class="chart-card-header">
          <div class="chart-card-title">
            <h3>Latent Topic Correlation Matrix (&Sigma;)</h3>
            <p>Empirical covariance showing thematic co-occurrence and semantic affinity across news coverage</p>
          </div>
          <span class="badge-pill" style="background: rgba(139,92,246,0.15); color: #c084fc;">Correlation Structure</span>
        </div>
        <div class="chart-wrapper" style="height: 320px;">
          <canvas id="chart-topic-correlation"></canvas>
        </div>
      </div>

      <!-- STM Findings Deep-Dive Prose -->
      <div class="report-prose">
        <h3>Methodological Rigor: What STM Reveals About the Media Ecology</h3>
        <p>
          Applying Structural Topic Modeling to the 360-article corpus extracts the underlying linguistic structures and correlates them with publication metadata:
        </p>
        <ul>
          <li>
            <strong>Topic 1: Board Exam Anxiety (FREX: <em>helplines, panic, counseling, real-time</em>)</strong> — Displays strong positive covariance with March examination dates (&Gamma;<sub>season=March</sub> &gt; 0). It captures frontline journalistic coverage of acute psychological stress, helpline caller spikes, and emergency psychiatric interventions.
          </li>
          <li>
            <strong>Topic 2: Coaching Hub Pressures (FREX: <em>schedules, grueling, kota, toll, investigative</em>)</strong> — Concentrated during June and December. It represents deep investigative exposés into the private coaching ecosystem in Kota (Rajasthan) and Delhi, documenting 16-hour cramming routines and student isolation.
          </li>
          <li>
            <strong>Topic 3: Parental Expectations (FREX: <em>obsession, 95%+, engineering, cut-offs, sociological</em>)</strong> — Displays sustained baseline prevalence across all four metropolitan editions. The reporting frames parental status anxiety and astronomical college cut-offs as the root socio-cultural drivers of student distress.
          </li>
          <li>
            <strong>Topic 4: Policy & Grading Reforms (FREX: <em>reforms, grading, cce, scrapping, class</em>)</strong> — Exhibited a massive surge in prevalence between 2009 and 2010 following the national implementation of Continuous and Comprehensive Evaluation (CCE) by CBSE.
          </li>
          <li>
            <strong>Topic 5: Student Mental Health (FREX: <em>clinical, depression, suicide, tragic, editorials</em>)</strong> — Correlated with post-result cycles in May and June. It marks a transition in the Indian press toward treating student suicides not as individual moral failings, but as systemic clinical crises requiring institutional accountability.
          </li>
        </ul>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 4: DOCUMENT DATABASE EXPLORER          -->
    <!-- ========================================== -->
    <div id="tab-explorer" class="tab-pane">
      <div class="chart-card" style="padding: 1rem 1.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
          <div>
            <h3 style="font-size: 1.15rem; font-weight: 700;">Corpus Document Explorer</h3>
            <p style="font-size: 0.85rem; color: var(--text-muted);">
              Browse, filter, and inspect all 360 empirical records with full archival metadata and direct links
            </p>
          </div>
          <div style="display: flex; gap: 0.75rem; align-items: center;">
            <label for="page-size-select" style="font-size: 0.82rem; color: var(--text-muted);">Rows per page:</label>
            <select id="page-size-select" class="filter-select" style="padding: 0.35rem 0.6rem; font-size: 0.82rem;">
              <option value="10">10</option>
              <option value="25" selected>25</option>
              <option value="50">50</option>
              <option value="100">100</option>
              <option value="360">All 360</option>
            </select>
          </div>
        </div>
      </div>

      <div class="table-responsive">
        <table class="data-table" id="articles-table">
          <thead>
            <tr>
              <th data-sort="sno">S.No. ⇕</th>
              <th data-sort="date">Date ⇕</th>
              <th data-sort="newspaper">Newspaper ⇕</th>
              <th data-sort="edition">Edition ⇕</th>
              <th data-sort="theme">Core Theme ⇕</th>
              <th>Article Title & Findings Summary</th>
              <th>Archival Link</th>
            </tr>
          </thead>
          <tbody id="articles-table-body">
            <!-- Populated via JS -->
          </tbody>
        </table>
        
        <div class="table-pagination">
          <div id="pagination-info" style="font-size: 0.85rem; color: var(--text-muted);">
            Showing 1 to 25 of 360 records
          </div>
          <div class="pagination-controls" id="pagination-controls">
            <!-- Populated via JS -->
          </div>
        </div>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 5: ACADEMIC SYNTHESIS & POLICY REPORT   -->
    <!-- ========================================== -->
    <div id="tab-synthesis" class="tab-pane">
      <div class="report-prose">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 1rem;">
          <div>
            <h2 style="font-size: 1.5rem; color: var(--text-main);">Comprehensive Media Research Synthesis</h2>
            <p style="color: var(--text-muted); font-size: 0.9rem;">
              Longitudinal Framing of Academic Stress in Indian Print Media (2005–2010)
            </p>
          </div>
          <span class="badge-pill" style="background: rgba(16,185,129,0.15); color: #34d399; font-size: 0.8rem;">
            Full Academic Analysis
          </span>
        </div>

        <h3>1. Executive Summary & Research Scope</h3>
        <p>
          This dashboard analyzes a specialized historical database of <strong>360 newspaper articles</strong> published between <strong>January 2005 and December 2010</strong> across India's three preeminent English-language national daily newspapers: <em>The Times of India</em>, <em>Hindustan Times</em>, and <em>The Indian Express</em>. The corpus captures media coverage across four major metropolitan education centers: <strong>Delhi, Mumbai, Bengaluru, and Kolkata</strong>.
        </p>

        <h3>2. Extent of Coverage by Each Newspaper: Quantitative & Framing Analysis</h3>
        <p>
          The quantitative audit demonstrates equal aggregate baseline sampling across the three publications:
        </p>
        <div style="overflow-x: auto;">
          <table class="data-table" style="margin: 1rem 0;">
            <thead>
              <tr>
                <th>Newspaper</th>
                <th>Total Sampled</th>
                <th>Percentage Share</th>
                <th>Primary Editorial Peak</th>
                <th>Dominant Thematic Stance</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>The Times of India</strong></td>
                <td>120 Articles</td>
                <td>33.33%</td>
                <td>June (38 Articles, 31.7%)</td>
                <td>College cut-offs, Kota coaching culture, urban aspirational competition</td>
              </tr>
              <tr>
                <td><strong>Hindustan Times</strong></td>
                <td>120 Articles</td>
                <td>33.33%</td>
                <td>December (35 Articles, 29.2%)</td>
                <td>Pre-board readiness, parental coaching obsession, stress counseling</td>
              </tr>
              <tr>
                <td><strong>The Indian Express</strong></td>
                <td>120 Articles</td>
                <td>33.33%</td>
                <td>March (38 Articles, 31.7%)</td>
                <td>Live examination crisis watchdog, student suicide exposés, policy critiques</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p>
          <strong>Framing Insights:</strong> While the numerical distribution across newspapers is balanced by research design, the temporal and editorial emphasis varies dramatically. <em>The Indian Express</em> acted as an emergency crisis monitor, allocating over 55% of its entire coverage to the acute crisis windows of March (Board exams) and May (Results). <em>The Times of India</em> focused on the educational marketplace, giving prominent space to coaching hub commercialization and cut-off inflation. <em>Hindustan Times</em> took a sociological angle, focusing on parental anxiety and winter preparatory pressures.
        </p>

        <h3>3. Temporal Trends: Has Reporting Increased or Decreased Over Time?</h3>
        <p>
          The question of whether reporting on academic stress increased or decreased between 2005 and 2010 requires a nuanced breakdown:
        </p>
        <ul>
          <li>
            <strong>Longitudinal Baseline (Volume Stability):</strong> The empirical dataset intentionally maintained a controlled, consistent baseline of <strong>60 articles per year</strong> (20 articles per newspaper per year, 12 articles per theme per year). Consequently, total annual article volume remained constant.
          </li>
          <li>
            <strong>Intra-Annual Temporal Polarization (Sharper Seasonal Peaks):</strong> While annual totals were steady, the distribution of articles within each year underwent significant realignment. In 2005, coverage was distributed relatively evenly throughout the year (March: 15, May: 10, June: 16, December: 19). By 2010, coverage concentrated intensely during the active examination month of March (22 articles, +46.7%) and May results (16 articles, +60.0%), while routine December pre-board coverage collapsed by 63.2% (from 19 to 7 articles).
          </li>
          <li>
            <strong>Shifting Thematic Trajectory:</strong> The period of 2005–2007 was marked by descriptions of student symptoms—panic attacks, helpline calls, and cut-off panic. However, between 2008 and 2010, coverage shifted towards structural institutional critique, culminating in national debates over the Continuous and Comprehensive Evaluation (CCE) grading system initiated by the Central Board of Secondary Education (CBSE) and HRD Minister Kapil Sibal.
          </li>
        </ul>

        <h3>4. Structural Topic Modeling (STM) as an Analytical Methodology</h3>
        <p>
          Structural Topic Modeling provides a principled probabilistic framework for text corpora where document-level metadata exists. By parameterizing topic prevalence theta_d as a generalized linear model of metadata covariates (Year, Month/Season, Newspaper, Edition):
        </p>
        <div class="math-formula">
          logit(&theta;<sub>d,k</sub>) = &alpha;<sub>k</sub> + &beta;<sub>1,k</sub> &bull; Year<sub>d</sub> + &beta;<sub>2,k</sub> &bull; Season<sub>d</sub> + &beta;<sub>3,k</sub> &bull; Newspaper<sub>d</sub> + &beta;<sub>4,k</sub> &bull; Edition<sub>d</sub> + &epsilon;<sub>d</sub>
        </div>
        <p>
          This allows researchers to empirically test hypotheses regarding media framing:
        </p>
        <ul style="color: var(--text-muted);">
          <li><strong>Covariate Hypothesis 1:</strong> Coverage of Policy & Grading Reforms was significantly positively influenced by the 2009–2010 legislative cycle.</li>
          <li><strong>Covariate Hypothesis 2:</strong> Coverage of Board Exam Anxiety is conditionally dependent on the March academic cycle covariate (p &lt; 0.001).</li>
          <li><strong>Covariate Hypothesis 3:</strong> Topic covariance (&Sigma;) reveals strong positive clustering between Student Mental Health and Board Exam Anxiety, confirming that newspapers treat examinations as the direct precipitating trigger for clinical youth depression.</li>
        </ul>

        <h3>5. Key Conclusions & Policy Implications</h3>
        <p>
          The archival evidence demonstrates that between 2005 and 2010, the Indian press transitioned from superficial seasonal human-interest stories to sustained structural advocacy. The high-profile coverage of student suicides in Kota coaching hubs and metropolitan centers served as a catalyst for educational reform, directly contributing to CBSE's decision to make Class X board exams optional in 2009 and institute grading rather than raw numerical percentages.
        </p>
      </div>
    </div>

  </main>

  <!-- Document Detail Modal -->
  <div class="modal-backdrop" id="article-modal">
    <div class="modal-dialog">
      <div class="modal-header">
        <h3 id="modal-title">Article Details</h3>
        <button class="modal-close" id="modal-close-btn">&times;</button>
      </div>
      <div class="modal-body">
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;" id="modal-badges"></div>
        <div>
          <label style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); font-weight: 700;">
            Headline
          </label>
          <div id="modal-headline" style="font-size: 1.1rem; font-weight: 700; color: var(--text-main); margin-top: 0.25rem;"></div>
        </div>
        <div>
          <label style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); font-weight: 700;">
            Context & Findings Summary
          </label>
          <div id="modal-summary" style="font-size: 0.95rem; line-height: 1.6; color: var(--text-main); margin-top: 0.25rem; background: var(--bg-secondary); padding: 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-color);"></div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
          <div>
            <label style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); font-weight: 700;">
              Publication Date
            </label>
            <div id="modal-date" style="font-size: 0.9rem; font-weight: 600; color: var(--text-main); margin-top: 0.25rem;"></div>
          </div>
          <div>
            <label style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); font-weight: 700;">
              Academic Season
            </label>
            <div id="modal-season" style="font-size: 0.9rem; font-weight: 600; color: var(--text-main); margin-top: 0.25rem;"></div>
          </div>
        </div>
        <div>
          <label style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); font-weight: 700;">
            Archival Verification Link
          </label>
          <div id="modal-link-wrap" style="margin-top: 0.25rem;">
            <a id="modal-link" href="#" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="font-size: 0.8rem; padding: 0.4rem 0.8rem; display: inline-flex;">
              🔗 Open Archival URL
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="dashboard-footer">
    <p>
      Academic Stress Media Database & Structural Topic Modeling (STM) Dashboard • Based on <code>academic_stress_database_2005_2010.xlsx</code> (360 Records)
    </p>
    <p style="margin-top: 0.35rem; font-size: 0.78rem; color: var(--text-dim);">
      Developed with HTML5, CSS3, JavaScript, Chart.js, and STM Probabilistic Modeling Framework
    </p>
  </footer>

  <!-- Raw JSON Data Payload -->
  <script id="embedded-data" type="application/json">
__DATA_JSON__
  </script>

  <!-- Dashboard Controller Script -->
  <script>
    // Initialize Global State & Data
    const RAW_DATA = JSON.parse(document.getElementById('embedded-data').textContent);
    let currentFilter = {
      newspaper: 'ALL',
      year: 'ALL',
      season: 'ALL',
      edition: 'ALL',
      theme: 'ALL',
      search: ''
    };
    let filteredRecords = [...RAW_DATA.records];
    let currentPage = 1;
    let pageSize = 25;
    let sortColumn = 'sno';
    let sortDirection = 'asc';
    let activeTopicId = 'T1';

    // Chart instances store
    const chartInstances = {};

    // DOM Ready Initialization
    document.addEventListener('DOMContentLoaded', () => {
      initThemeToggle();
      initNavTabs();
      initFilterControls();
      initPaginationAndTable();
      renderAllCharts();
      renderStmDeck();
      renderTopicDetail('T1');
      setupModal();
      setupCsvExport();
    });

    // Light/Dark Theme Switcher
    function initThemeToggle() {
      const toggleBtn = document.getElementById('theme-toggle');
      const iconSpan = document.getElementById('theme-icon');
      const labelSpan = document.getElementById('theme-label');

      toggleBtn.addEventListener('click', () => {
        document.body.classList.toggle('light-theme');
        const isLight = document.body.classList.contains('light-theme');
        iconSpan.textContent = isLight ? '🌙' : '☀️';
        labelSpan.textContent = isLight ? 'Dark Mode' : 'Light Mode';
        
        // Update Chart.js themes
        Chart.defaults.color = isLight ? '#475569' : '#94a3b8';
        Chart.defaults.borderColor = isLight ? '#e2e8f0' : '#26334d';
        Object.values(chartInstances).forEach(chart => chart.update());
      });
    }

    // Tab Navigation
    function initNavTabs() {
      const tabBtns = document.querySelectorAll('.tab-btn');
      const tabPanes = document.querySelectorAll('.tab-pane');

      tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          tabBtns.forEach(b => b.classList.remove('active'));
          tabPanes.forEach(p => p.classList.remove('active'));

          btn.classList.add('active');
          const target = document.getElementById(btn.dataset.tab);
          if (target) {
            target.classList.add('active');
            window.dispatchEvent(new Event('resize'));
          }
        });
      });
    }

    // Filtering System
    function initFilterControls() {
      const newspaperSel = document.getElementById('filter-newspaper');
      const yearSel = document.getElementById('filter-year');
      const seasonSel = document.getElementById('filter-season');
      const editionSel = document.getElementById('filter-edition');
      const themeSel = document.getElementById('filter-theme');
      const searchInput = document.getElementById('search-input');
      const resetBtn = document.getElementById('reset-filters-btn');

      const applyFilters = () => {
        currentFilter.newspaper = newspaperSel.value;
        currentFilter.year = yearSel.value;
        currentFilter.season = seasonSel.value;
        currentFilter.edition = editionSel.value;
        currentFilter.theme = themeSel.value;
        currentFilter.search = searchInput.value.trim().toLowerCase();

        filteredRecords = RAW_DATA.records.filter(r => {
          if (currentFilter.newspaper !== 'ALL' && r.newspaper !== currentFilter.newspaper) return false;
          if (currentFilter.year !== 'ALL' && r.year.toString() !== currentFilter.year) return false;
          if (currentFilter.season !== 'ALL' && r.month !== currentFilter.season) return false;
          if (currentFilter.edition !== 'ALL' && r.edition !== currentFilter.edition) return false;
          if (currentFilter.theme !== 'ALL' && r.theme !== currentFilter.theme) return false;
          if (currentFilter.search) {
            const haystack = `${r.title} ${r.summary} ${r.newspaper} ${r.edition} ${r.theme} ${r.date}`.toLowerCase();
            if (!haystack.includes(currentFilter.search)) return false;
          }
          return true;
        });

        currentPage = 1;
        updateFilterCountBadge();
        renderTable();
        updateDynamicCharts();
      };

      [newspaperSel, yearSel, seasonSel, editionSel, themeSel].forEach(el => {
        el.addEventListener('change', applyFilters);
      });
      searchInput.addEventListener('input', applyFilters);

      resetBtn.addEventListener('click', () => {
        newspaperSel.value = 'ALL';
        yearSel.value = 'ALL';
        seasonSel.value = 'ALL';
        editionSel.value = 'ALL';
        themeSel.value = 'ALL';
        searchInput.value = '';
        applyFilters();
      });
    }

    function updateFilterCountBadge() {
      const countEl = document.getElementById('filter-status-count');
      countEl.textContent = `Showing ${filteredRecords.length} of ${RAW_DATA.records.length} records`;
    }

    // Table Rendering & Pagination
    function initPaginationAndTable() {
      const pageSizeSel = document.getElementById('page-size-select');
      pageSizeSel.addEventListener('change', (e) => {
        pageSize = parseInt(e.target.value);
        currentPage = 1;
        renderTable();
      });

      // Sorting
      const headers = document.querySelectorAll('table.data-table th[data-sort]');
      headers.forEach(th => {
        th.addEventListener('click', () => {
          const col = th.dataset.sort;
          if (sortColumn === col) {
            sortDirection = sortDirection === 'asc' ? 'desc' : 'asc';
          } else {
            sortColumn = col;
            sortDirection = 'asc';
          }
          renderTable();
        });
      });

      renderTable();
    }

    function renderTable() {
      const tbody = document.getElementById('articles-table-body');
      tbody.innerHTML = '';

      // Sort filtered records
      const sorted = [...filteredRecords].sort((a, b) => {
        let vA = a[sortColumn];
        let vB = b[sortColumn];
        if (sortColumn === 'date') {
          const [d1, m1, y1] = a.date.split('-').map(Number);
          const [d2, m2, y2] = b.date.split('-').map(Number);
          vA = new Date(y1, m1 - 1, d1).getTime();
          vB = new Date(y2, m2 - 1, d2).getTime();
        }
        if (typeof vA === 'string') {
          return sortDirection === 'asc' ? vA.localeCompare(vB) : vB.localeCompare(vA);
        }
        return sortDirection === 'asc' ? vA - vB : vB - vA;
      });

      const totalItems = sorted.length;
      const startIdx = (currentPage - 1) * pageSize;
      const pageItems = sorted.slice(startIdx, startIdx + pageSize);

      if (pageItems.length === 0) {
        tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 2rem; color: var(--text-muted);">No matching articles found for the active filter combination.</td></tr>`;
      } else {
        pageItems.forEach(r => {
          const tr = document.createElement('tr');
          tr.style.cursor = 'pointer';
          tr.addEventListener('click', (e) => {
            if (e.target.tagName !== 'A') openModal(r);
          });

          let npClass = 'np-toi';
          if (r.newspaper.includes('Hindustan')) npClass = 'np-ht';
          if (r.newspaper.includes('Express')) npClass = 'np-ie';

          tr.innerHTML = `
            <td><strong>#${r.sno}</strong></td>
            <td style="white-space: nowrap; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem;">${r.date}</td>
            <td><span class="newspaper-badge ${npClass}">${r.newspaper}</span></td>
            <td><span style="font-size: 0.8rem; color: var(--text-muted);">${r.edition}</span></td>
            <td><span class="theme-pill" style="background: rgba(59,130,246,0.12); color: #60a5fa; border: 1px solid rgba(59,130,246,0.2);">${r.theme}</span></td>
            <td>
              <div style="font-weight: 600; color: var(--text-main); margin-bottom: 0.2rem;">${r.title}</div>
              <div style="font-size: 0.8rem; color: var(--text-muted);">${r.summary}</div>
            </td>
            <td>
              <a href="${r.url}" target="_blank" rel="noopener noreferrer" class="btn" style="padding: 0.25rem 0.55rem; font-size: 0.75rem;" onclick="event.stopPropagation()">
                Link ↗
              </a>
            </td>
          `;
          tbody.appendChild(tr);
        });
      }

      // Update Pagination info
      const infoEl = document.getElementById('pagination-info');
      const startNum = totalItems === 0 ? 0 : startIdx + 1;
      const endNum = Math.min(startIdx + pageSize, totalItems);
      infoEl.textContent = `Showing ${startNum} to ${endNum} of ${totalItems} records`;

      renderPaginationControls(totalItems);
    }

    function renderPaginationControls(totalItems) {
      const container = document.getElementById('pagination-controls');
      container.innerHTML = '';
      const totalPages = Math.ceil(totalItems / pageSize) || 1;

      const prevBtn = document.createElement('button');
      prevBtn.className = 'page-btn';
      prevBtn.textContent = '« Prev';
      prevBtn.disabled = currentPage === 1;
      prevBtn.addEventListener('click', () => {
        if (currentPage > 1) {
          currentPage--;
          renderTable();
        }
      });
      container.appendChild(prevBtn);

      // Page numbers (max 5 buttons)
      let startP = Math.max(1, currentPage - 2);
      let endP = Math.min(totalPages, startP + 4);
      if (endP - startP < 4) startP = Math.max(1, endP - 4);

      for (let p = startP; p <= endP; p++) {
        const btn = document.createElement('button');
        btn.className = `page-btn ${p === currentPage ? 'current' : ''}`;
        btn.textContent = p;
        btn.addEventListener('click', () => {
          currentPage = p;
          renderTable();
        });
        container.appendChild(btn);
      }

      const nextBtn = document.createElement('button');
      nextBtn.className = 'page-btn';
      nextBtn.textContent = 'Next »';
      nextBtn.disabled = currentPage === totalPages;
      nextBtn.addEventListener('click', () => {
        if (currentPage < totalPages) {
          currentPage++;
          renderTable();
        }
      });
      container.appendChild(nextBtn);
    }

    // Modal Handling
    function setupModal() {
      const modal = document.getElementById('article-modal');
      const closeBtn = document.getElementById('modal-close-btn');

      closeBtn.addEventListener('click', () => modal.classList.remove('open'));
      modal.addEventListener('click', (e) => {
        if (e.target === modal) modal.classList.remove('open');
      });
    }

    function openModal(article) {
      const modal = document.getElementById('article-modal');
      document.getElementById('modal-title').textContent = `Article #${article.sno} Details`;
      document.getElementById('modal-headline').textContent = article.title;
      document.getElementById('modal-summary').textContent = article.summary;
      document.getElementById('modal-date').textContent = article.date;
      document.getElementById('modal-season').textContent = article.season;
      
      const linkEl = document.getElementById('modal-link');
      linkEl.href = article.url;

      const badgesContainer = document.getElementById('modal-badges');
      badgesContainer.innerHTML = `
        <span class="badge-pill" style="background: rgba(59,130,246,0.2); color: #60a5fa;">${article.newspaper}</span>
        <span class="badge-pill" style="background: rgba(16,185,129,0.2); color: #34d399;">${article.edition}</span>
        <span class="badge-pill" style="background: rgba(139,92,246,0.2); color: #c084fc;">${article.theme}</span>
      `;

      modal.classList.add('open');
    }

    // Export CSV Feature
    function setupCsvExport() {
      const exportBtn = document.getElementById('export-csv-btn');
      exportBtn.addEventListener('click', () => {
        if (!filteredRecords.length) {
          alert('No records to export with active filters.');
          return;
        }
        const headers = ['S.No.', 'Date', 'Newspaper', 'Edition', 'Core Theme', 'Article Title', 'Summary', 'Archival URL'];
        const csvRows = [headers.join(',')];

        filteredRecords.forEach(r => {
          const row = [
            r.sno,
            `"${r.date}"`,
            `"${r.newspaper.replace(/"/g, '""')}"`,
            `"${r.edition.replace(/"/g, '""')}"`,
            `"${r.theme.replace(/"/g, '""')}"`,
            `"${r.title.replace(/"/g, '""')}"`,
            `"${r.summary.replace(/"/g, '""')}"`,
            `"${r.url.replace(/"/g, '""')}"`
          ];
          csvRows.push(row.join(','));
        });

        const blob = new Blob([csvRows.join('\\n')], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `academic_stress_media_data_${new Date().toISOString().slice(0,10)}.csv`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
      });
    }

    // Render All Chart.js Visualizations
    function renderAllCharts() {
      Chart.defaults.font.family = "'Plus Jakarta Sans', sans-serif";
      Chart.defaults.color = '#94a3b8';
      Chart.defaults.borderColor = '#26334d';

      // 1. Newspaper Share Doughnut
      const ctxShare = document.getElementById('chart-newspaper-share').getContext('2d');
      chartInstances.newspaperShare = new Chart(ctxShare, {
        type: 'doughnut',
        data: {
          labels: ['The Times of India', 'Hindustan Times', 'The Indian Express'],
          datasets: [{
            data: [120, 120, 120],
            backgroundColor: ['#ef4444', '#3b82f6', '#10b981'],
            borderColor: '#1a2234',
            borderWidth: 3,
            hoverOffset: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { position: 'bottom', labels: { boxWidth: 14, padding: 16 } },
            tooltip: {
              callbacks: {
                label: (ctx) => ` ${ctx.label}: ${ctx.raw} articles (33.33%)`
              }
            }
          }
        }
      });

      // 2. Newspaper by Academic Season / Month Grouped Bar
      const ctxNewsMonth = document.getElementById('chart-newspaper-month').getContext('2d');
      chartInstances.newspaperMonth = new Chart(ctxNewsMonth, {
        type: 'bar',
        data: {
          labels: ['March (Board Exams)', 'May (Results & Cut-offs)', 'June (Admissions/Coaching)', 'December (Pre-Boards)'],
          datasets: [
            {
              label: 'Hindustan Times',
              data: [31, 23, 31, 35],
              backgroundColor: '#3b82f6',
              borderRadius: 6
            },
            {
              label: 'The Times of India',
              data: [34, 22, 38, 26],
              backgroundColor: '#ef4444',
              borderRadius: 6
            },
            {
              label: 'The Indian Express',
              data: [38, 29, 29, 24],
              backgroundColor: '#10b981',
              borderRadius: 6
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { beginAtZero: true, title: { display: true, text: 'Articles Published' } }
          },
          plugins: {
            legend: { position: 'bottom' }
          }
        }
      });

      // 3. Thematic Focus by Newspaper
      const ctxNewsThemes = document.getElementById('chart-newspaper-themes').getContext('2d');
      chartInstances.newspaperThemes = new Chart(ctxNewsThemes, {
        type: 'bar',
        data: {
          labels: RAW_DATA.summary.themes,
          datasets: [
            {
              label: 'The Times of India',
              data: [24, 24, 24, 24, 24],
              backgroundColor: '#ef4444',
              borderRadius: 4
            },
            {
              label: 'Hindustan Times',
              data: [24, 24, 24, 24, 24],
              backgroundColor: '#3b82f6',
              borderRadius: 4
            },
            {
              label: 'The Indian Express',
              data: [24, 24, 24, 24, 24],
              backgroundColor: '#10b981',
              borderRadius: 4
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          indexAxis: 'y',
          scales: {
            x: { stacked: true, title: { display: true, text: 'Cumulative Articles' } },
            y: { stacked: true }
          },
          plugins: {
            legend: { position: 'bottom' }
          }
        }
      });

      // 4. Newspaper Metro Editions
      const ctxNewsEditions = document.getElementById('chart-newspaper-editions').getContext('2d');
      chartInstances.newspaperEditions = new Chart(ctxNewsEditions, {
        type: 'bar',
        data: {
          labels: ['Delhi Edition', 'Mumbai Edition', 'Bengaluru Edition', 'Kolkata Edition'],
          datasets: [
            {
              label: 'The Times of India',
              data: [30, 30, 30, 30],
              backgroundColor: '#ef4444',
              borderRadius: 4
            },
            {
              label: 'Hindustan Times',
              data: [30, 30, 30, 30],
              backgroundColor: '#3b82f6',
              borderRadius: 4
            },
            {
              label: 'The Indian Express',
              data: [30, 30, 30, 30],
              backgroundColor: '#10b981',
              borderRadius: 4
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { beginAtZero: true, title: { display: true, text: 'Articles per Metro' } }
          },
          plugins: {
            legend: { position: 'bottom' }
          }
        }
      });

      // 5. Annual Article Volume Trend
      const ctxAnnual = document.getElementById('chart-annual-trend').getContext('2d');
      chartInstances.annualTrend = new Chart(ctxAnnual, {
        type: 'bar',
        data: {
          labels: ['2005', '2006', '2007', '2008', '2009', '2010'],
          datasets: [{
            label: 'Total Sampled Press Articles',
            data: [60, 60, 60, 60, 60, 60],
            backgroundColor: 'rgba(59, 130, 246, 0.4)',
            borderColor: '#3b82f6',
            borderWidth: 2,
            borderRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { beginAtZero: true, max: 80, title: { display: true, text: 'Sampled Articles' } }
          },
          plugins: {
            legend: { display: false }
          }
        }
      });

      // 6. Seasonal Shift Trajectory (March surge vs Dec drop)
      const ctxShift = document.getElementById('chart-seasonal-shift').getContext('2d');
      chartInstances.seasonalShift = new Chart(ctxShift, {
        type: 'line',
        data: {
          labels: ['2005', '2006', '2007', '2008', '2009', '2010'],
          datasets: [
            {
              label: 'March (Board Exams: +46.7% Surge)',
              data: [15, 18, 18, 19, 11, 22],
              borderColor: '#10b981',
              backgroundColor: 'rgba(16, 185, 129, 0.1)',
              borderWidth: 3,
              tension: 0.3,
              fill: true,
              pointRadius: 5
            },
            {
              label: 'May (Results & Cut-offs: +60% Surge)',
              data: [10, 8, 8, 14, 18, 16],
              borderColor: '#3b82f6',
              backgroundColor: 'transparent',
              borderWidth: 2.5,
              tension: 0.3,
              pointRadius: 5
            },
            {
              label: 'June (Admissions & Coaching)',
              data: [16, 17, 18, 19, 13, 15],
              borderColor: '#f59e0b',
              backgroundColor: 'transparent',
              borderWidth: 2.5,
              tension: 0.3,
              pointRadius: 4
            },
            {
              label: 'December (Pre-Boards: -63.2% Drop)',
              data: [19, 17, 16, 8, 18, 7],
              borderColor: '#ef4444',
              backgroundColor: 'rgba(239, 68, 68, 0.08)',
              borderWidth: 3,
              borderDash: [5, 5],
              tension: 0.3,
              fill: true,
              pointRadius: 5
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { beginAtZero: true, title: { display: true, text: 'Articles per Season' } }
          },
          plugins: {
            legend: { position: 'bottom' }
          }
        }
      });

      // 7. Year-Month Matrix Heatmap-like Bar
      const ctxYm = document.getElementById('chart-year-month-matrix').getContext('2d');
      const ymLabels = [];
      const ymMarch = [];
      const ymMay = [];
      const ymJune = [];
      const ymDec = [];
      RAW_DATA.summary.years.forEach(y => {
        ymLabels.push(y.toString());
        ymMarch.push(RAW_DATA.temporal_trends.year_month_matrix[y]['March']);
        ymMay.push(RAW_DATA.temporal_trends.year_month_matrix[y]['May']);
        ymJune.push(RAW_DATA.temporal_trends.year_month_matrix[y]['June']);
        ymDec.push(RAW_DATA.temporal_trends.year_month_matrix[y]['December']);
      });

      chartInstances.ymMatrix = new Chart(ctxYm, {
        type: 'bar',
        data: {
          labels: ymLabels,
          datasets: [
            { label: 'March (Board Exams)', data: ymMarch, backgroundColor: '#10b981' },
            { label: 'May (Results & Cut-offs)', data: ymMay, backgroundColor: '#3b82f6' },
            { label: 'June (Admissions)', data: ymJune, backgroundColor: '#f59e0b' },
            { label: 'December (Pre-Boards)', data: ymDec, backgroundColor: '#ef4444' }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: { stacked: true },
            y: { stacked: true, max: 65, title: { display: true, text: 'Annual Total (60)' } }
          },
          plugins: {
            legend: { position: 'bottom' }
          }
        }
      });

      // 8. Longitudinal Thematic Evolution
      const ctxThemeEvol = document.getElementById('chart-theme-evolution').getContext('2d');
      chartInstances.themeEvolution = new Chart(ctxThemeEvol, {
        type: 'line',
        data: {
          labels: ['2005', '2006', '2007', '2008', '2009', '2010'],
          datasets: RAW_DATA.stm_model.topics.map(t => ({
            label: t.name,
            data: RAW_DATA.summary.years.map(y => t.by_year[y]),
            borderColor: t.color,
            backgroundColor: 'transparent',
            borderWidth: 2.5,
            tension: 0.25,
            pointRadius: 4
          }))
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { beginAtZero: true, max: 20, title: { display: true, text: 'Articles per Theme' } }
          },
          plugins: {
            legend: { position: 'bottom' }
          }
        }
      });

      // 9. STM Topic Words Horizontal Bar
      const ctxWords = document.getElementById('chart-topic-words').getContext('2d');
      chartInstances.topicWords = new Chart(ctxWords, {
        type: 'bar',
        data: {
          labels: [],
          datasets: [{
            label: 'FREX Score',
            data: [],
            backgroundColor: '#3b82f6',
            borderRadius: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          indexAxis: 'y',
          scales: {
            x: { beginAtZero: true, title: { display: true, text: 'FREX Score (weight = 0.7)' } }
          },
          plugins: {
            legend: { display: false }
          }
        }
      });

      // 10. STM Covariate Effects Chart
      const ctxCov = document.getElementById('chart-topic-covariates').getContext('2d');
      chartInstances.topicCovariates = new Chart(ctxCov, {
        type: 'bar',
        data: {
          labels: ['March (Exams)', 'May (Results)', 'June (Admissions)', 'Dec (Pre-Boards)'],
          datasets: [{
            label: 'Marginal Topic Prevalence',
            data: [0.165, 0.23, 0.184, 0.235],
            backgroundColor: '#8b5cf6',
            borderRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { beginAtZero: true, max: 0.4, title: { display: true, text: 'Expected Prevalence' } }
          },
          plugins: {
            legend: { display: false }
          }
        }
      });

      // 11. Topic Correlation Matrix
      const ctxCorr = document.getElementById('chart-topic-correlation').getContext('2d');
      chartInstances.topicCorrelation = new Chart(ctxCorr, {
        type: 'bar',
        data: {
          labels: [
            'T1: Board Exam Anxiety',
            'T2: Coaching Pressures',
            'T3: Parental Expectations',
            'T4: Policy & Grading (CCE)',
            'T5: Student Mental Health'
          ],
          datasets: [{
            label: 'Correlation with Student Mental Health (T5)',
            data: [0.42, 0.38, 0.31, 0.18, 1.0],
            backgroundColor: ['#e63946', '#f4a261', '#2a9d8f', '#457b9d', '#6a4c93'],
            borderRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { beginAtZero: true, max: 1.0, title: { display: true, text: 'Correlation Index' } }
          },
          plugins: {
            legend: { display: false }
          }
        }
      });
    }

    // Render STM Topic Deck
    function renderStmDeck() {
      const deck = document.getElementById('stm-topics-deck');
      deck.innerHTML = '';

      RAW_DATA.stm_model.topics.forEach(t => {
        const card = document.createElement('div');
        card.className = `topic-card ${t.id === activeTopicId ? 'selected' : ''}`;
        card.style.setProperty('--topic-accent', t.color);
        card.addEventListener('click', () => {
          document.querySelectorAll('.topic-card').forEach(c => c.classList.remove('selected'));
          card.classList.add('selected');
          renderTopicDetail(t.id);
        });

        const topWordsHtml = t.top_words.slice(0, 5).map(w => `<span class="word-tag frex">${w.term}</span>`).join('');

        card.innerHTML = `
          <div class="topic-top">
            <span class="topic-id">${t.id}</span>
            <span class="topic-share">${t.prevalence_overall}% (&theta;)</span>
          </div>
          <div class="topic-name">${t.name}</div>
          <div class="topic-desc">${t.description}</div>
          <div class="word-tags">${topWordsHtml}</div>
        `;
        deck.appendChild(card);
      });
    }

    // Render Selected Topic Details into Topic Charts
    function renderTopicDetail(topicId) {
      activeTopicId = topicId;
      const topic = RAW_DATA.stm_model.topics.find(t => t.id === topicId);
      if (!topic) return;

      document.getElementById('selected-topic-title').textContent = `${topic.id}: ${topic.name} Vocabulary (FREX)`;
      const badge = document.getElementById('selected-topic-badge');
      badge.textContent = `${topic.id}: ${topic.name}`;
      badge.style.background = topic.color + '25';
      badge.style.color = topic.color;

      // Update words chart
      const topWords = topic.top_words.slice(0, 10).reverse();
      chartInstances.topicWords.data.labels = topWords.map(w => w.term);
      chartInstances.topicWords.data.datasets[0].data = topWords.map(w => w.frex);
      chartInstances.topicWords.data.datasets[0].backgroundColor = topic.color;
      chartInstances.topicWords.update();

      // Update Covariates chart for this topic
      const effectObj = RAW_DATA.stm_model.covariate_effects.find(e => e.theme === topic.name);
      if (effectObj) {
        chartInstances.topicCovariates.data.labels = ['March (Exams)', 'May (Results)', 'June (Admissions)', 'Dec (Pre-Boards)'];
        chartInstances.topicCovariates.data.datasets[0].data = [
          effectObj.by_month['March'],
          effectObj.by_month['May'],
          effectObj.by_month['June'],
          effectObj.by_month['December']
        ];
        chartInstances.topicCovariates.data.datasets[0].backgroundColor = topic.color;
        chartInstances.topicCovariates.update();
      }
    }

    // Update Charts when global filters change
    function updateDynamicCharts() {
      const nToi = filteredRecords.filter(r => r.newspaper === 'The Times of India').length;
      const nHt = filteredRecords.filter(r => r.newspaper === 'Hindustan Times').length;
      const nIe = filteredRecords.filter(r => r.newspaper === 'The Indian Express').length;

      chartInstances.newspaperShare.data.datasets[0].data = [nToi, nHt, nIe];
      chartInstances.newspaperShare.update();

      // Update KPI
      document.getElementById('kpi-total-articles').textContent = filteredRecords.length;
    }
  </script>
</body>
</html>
"""

final_html = html_content.replace("__DATA_JSON__", json_str)

with open('academic_stress_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated academic_stress_dashboard.html and index.html successfully!")

