#!/usr/bin/env python3
"""
AltviseWP Docs Build Script
Converts Markdown files in docs/ to HTML files in build/
Run: python build.py
"""

import os
import re
import shutil

# ── Config ────────────────────────────────────────────────
BUILD_DIR   = 'build'
DOCS_DIR    = 'docs'
ASSETS_DIR  = 'assets'

FONT_URL    = "https://fonts.googleapis.com/css2?family=Jost:wght@300;400;600;700&family=Bungee+Inline&family=DM+Mono:wght@400;500&display=swap"

# Sidebar navigation definition — order matters
SIDEBAR = [
    {
        'label': 'Footnotes Made Easy',
        'items': [
            ('Overview',            'footnotes-made-easy/index.html',             False),
            ('Installation',        'footnotes-made-easy/installation.html',      False),
            ('Getting Started',     'footnotes-made-easy/getting-started.html',   False),
        ],
        'groups': [
            {
                'label': 'Settings',
                'items': [
                    ('Display',     'footnotes-made-easy/settings/display.html',    False),
                    ('Behaviour',   'footnotes-made-easy/settings/behaviour.html',  False),
                    ('Suppress',    'footnotes-made-easy/settings/suppress.html',   False),
                    ('Advanced',    'footnotes-made-easy/settings/advanced.html',   False),
                ]
            }
        ],
        'items2': [
            ('Tools',               'footnotes-made-easy/tools.html',             False),
            ('Multisite',           'footnotes-made-easy/multisite.html',         False),
            ('FAQ',                 'footnotes-made-easy/faq.html',               False),
            ('Changelog',           'footnotes-made-easy/changelog.html',         False),
        ]
    },
    {
        'label': 'Footnotes Made Easy Pro',
        'pro': True,
        'items': [
            ('Installation',        'footnotes-made-easy/pro-installation.html',          True),
            ('License Activation',  'footnotes-made-easy/pro-license-activation.html',    True),
        ],
        'groups': [
            {
                'label': 'Citations',
                'items': [
                    ('Overview',        'footnotes-made-easy/pro-citations-overview.html',      True),
                    ('Source Types',    'footnotes-made-easy/pro-citations-source-types.html',  True),
                    ('Citation Styles', 'footnotes-made-easy/pro-citations-styles.html',        True),
                ]
            }
        ],
        'items2': [
            ('Footnote Library',    'footnotes-made-easy/pro-library.html',               True),
            ('Gutenberg Sidebar',   'footnotes-made-easy/pro-gutenberg-sidebar.html',     True),
            ('FAQ',                 'footnotes-made-easy/pro-faq.html',                   True),
        ]
    },
    {
        'label': 'Account',
        'items': [
            ('Managing Your License',   'account/managing-your-license.html',  False),
            ('Billing and Renewals',    'account/billing-and-renewals.html',   False),
            ('Refunds',                 'account/refunds.html',                False),
        ]
    }
]

# Page sequence for prev/next navigation
PAGE_SEQUENCE = [
    ('Overview',            '/footnotes-made-easy/'),
    ('Installation',        '/footnotes-made-easy/installation'),
    ('Getting Started',     '/footnotes-made-easy/getting-started'),
    ('Display',             '/footnotes-made-easy/settings/display'),
    ('Behaviour',           '/footnotes-made-easy/settings/behaviour'),
    ('Suppress',            '/footnotes-made-easy/settings/suppress'),
    ('Advanced',            '/footnotes-made-easy/settings/advanced'),
    ('Tools',               '/footnotes-made-easy/tools'),
    ('Multisite',           '/footnotes-made-easy/multisite'),
    ('FAQ',                 '/footnotes-made-easy/faq'),
    ('Changelog',           '/footnotes-made-easy/changelog'),
    ('Pro Installation',    '/footnotes-made-easy/pro-installation'),
    ('License Activation',  '/footnotes-made-easy/pro-license-activation'),
    ('Citations Overview',  '/footnotes-made-easy/pro-citations-overview'),
    ('Source Types',        '/footnotes-made-easy/pro-citations-source-types'),
    ('Citation Styles',     '/footnotes-made-easy/pro-citations-styles'),
    ('Footnote Library',    '/footnotes-made-easy/pro-library'),
    ('Gutenberg Sidebar',   '/footnotes-made-easy/pro-gutenberg-sidebar'),
    ('Pro FAQ',             '/footnotes-made-easy/pro-faq'),
    ('Managing License',    '/account/managing-your-license'),
    ('Billing & Renewals',  '/account/billing-and-renewals'),
    ('Refunds',             '/account/refunds'),
]

# ── Markdown to HTML ──────────────────────────────────────
def fmt(text):
    # Images first (before links, to avoid conflict)
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" class="doc-img">', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*',     r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`',       r'<code>\1</code>', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\.md\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\)',      r'<a href="\2">\1</a>', text)
    return text

def md_to_html(md):
    # Strip frontmatter
    md = re.sub(r'^---\n.*?\n---\n', '', md, flags=re.DOTALL)
    # Remove H1 (used as page title)
    md = re.sub(r'^# .+\n', '', md, count=1)

    lines = md.split('\n')
    html = []
    in_code = False
    in_list = False
    list_type = None
    in_table = False
    table_rows = []

    def close_list():
        nonlocal in_list, list_type
        if in_list:
            html.append(f'</{list_type}>')
            in_list = False
            list_type = None

    def flush_table():
        nonlocal in_table, table_rows
        if not table_rows:
            return
        h = '<table>'
        for i, row in enumerate(table_rows):
            cells = [c.strip() for c in row.strip('|').split('|')]
            if i == 0:
                h += '<thead><tr>' + ''.join(f'<th>{fmt(c)}</th>' for c in cells) + '</tr></thead><tbody>'
            elif i == 1 and all(re.match(r'[-:]+', c.strip()) for c in cells):
                continue
            else:
                h += '<tr>' + ''.join(f'<td>{fmt(c)}</td>' for c in cells) + '</tr>'
        h += '</tbody></table>'
        html.append(h)
        table_rows = []
        in_table = False

    for line in lines:
        # Table detection
        if '|' in line and line.strip().startswith('|'):
            close_list()
            in_table = True
            table_rows.append(line)
            continue
        else:
            if in_table:
                flush_table()

        # Code block
        if line.startswith('```'):
            close_list()
            if in_code:
                html.append('</code></pre>')
                in_code = False
            else:
                lang = line[3:].strip() or ''
                html.append(f'<pre><code class="language-{lang}">')
                in_code = True
            continue
        if in_code:
            html.append(line.replace('<', '&lt;').replace('>', '&gt;'))
            continue

        # Close list if needed
        if in_list and not (line.startswith('- ') or line.startswith('* ') or re.match(r'^\d+\. ', line)):
            close_list()

        if line.startswith('## '):
            html.append(f'<h2>{fmt(line[3:])}</h2>')
        elif line.startswith('### '):
            html.append(f'<h3>{fmt(line[4:])}</h3>')
        elif line.startswith('#### '):
            html.append(f'<h4>{fmt(line[5:])}</h4>')
        elif line.startswith('> '):
            html.append(f'<blockquote><p>{fmt(line[2:])}</p></blockquote>')
        elif line.startswith('- ') or line.startswith('* '):
            if not in_list:
                html.append('<ul>')
                in_list = True
                list_type = 'ul'
            html.append(f'<li>{fmt(line[2:])}</li>')
        elif re.match(r'^\d+\. ', line):
            if not in_list:
                html.append('<ol>')
                in_list = True
                list_type = 'ol'
            clean_line = re.sub(r'^\d+\. ', '', line)
            html.append(f'<li>{fmt(clean_line)}</li>')
        elif line.startswith('---'):
            html.append('<hr>')
        elif re.match(r'^!\[', line):
            # Standalone image line
            html.append(f'<figure class="doc-figure">{fmt(line)}</figure>')
        elif line.strip() == '':
            html.append('')
        else:
            html.append(f'<p>{fmt(line)}</p>')

    close_list()
    if in_code:
        html.append('</code></pre>')
    if in_table:
        flush_table()

    result = '\n'.join(html)
    result = re.sub(r'(<p></p>\n?)+', '', result)
    return result

# ── Sidebar HTML ──────────────────────────────────────────
def build_sidebar():
    html = ''
    for group in SIDEBAR:
        pro_label = '<span class="badge-pro">Pro</span>' if group.get('pro') else ''
        html += f'<div class="sidenav__group">'
        html += f'<div class="sidenav__label">{group["label"]} {pro_label}</div>'

        for label, url, is_pro in group.get('items', []):
            clean_url = '/' + url.replace('.html', '').replace('index', '')
            clean_url = clean_url.rstrip('/') + '/' if url.endswith('index.html') else clean_url.rstrip('/')
            pro_badge = '<span class="badge-pro">Pro</span>' if is_pro else ''
            html += f'<a href="{clean_url}" class="sidenav__link">{label} {pro_badge}</a>'

        for sub in group.get('groups', []):
            html += f'<div class="sidenav__sublabel">{sub["label"]}</div>'
            for label, url, is_pro in sub['items']:
                clean_url = '/' + url.replace('.html', '')
                pro_badge = '<span class="badge-pro">Pro</span>' if is_pro else ''
                html += f'<a href="{clean_url}" class="sidenav__link sidenav__link--sub">{label} {pro_badge}</a>'

        for label, url, is_pro in group.get('items2', []):
            clean_url = '/' + url.replace('.html', '')
            pro_badge = '<span class="badge-pro">Pro</span>' if is_pro else ''
            html += f'<a href="{clean_url}" class="sidenav__link">{label} {pro_badge}</a>'

        html += '</div>'
    return html

# ── Page template ─────────────────────────────────────────
def page_template(title, section, breadcrumb_html, content_html, nav_html, is_pro=False):
    pro_badge = '<span class="badge-pro">Pro</span>' if is_pro else ''
    sidebar_html = build_sidebar()

    return f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — AltviseWP Docs</title>
<meta name="description" content="{title} — AltviseWP documentation.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="{FONT_URL}" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
</head>
<body>

<header class="topbar">
  <div class="topbar__inner">
    <a href="/" class="topbar__logo">
      <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor"><path d="M3 4h14v2H3zm0 5h9v2H3zm0 5h11v2H3z"/></svg>
      <span>AltviseWP <strong>Docs</strong></span>
    </a>
    <div class="topbar__search">
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><circle cx="6" cy="6" r="4.5" stroke="currentColor" stroke-width="1.4"/><path d="M10 10l2.5 2.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      <input type="text" id="search-input" placeholder="Search docs..." autocomplete="off" spellcheck="false">
      <kbd>⌘K</kbd>
    </div>
    <nav class="topbar__nav">
      <a href="https://altvisewp.com" target="_blank" rel="noopener">altvisewp.com</a>
      <a href="https://altvisewp.com/support/" target="_blank" rel="noopener">Support</a>
      <button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">
        <svg class="icon-sun" width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 11a3 3 0 100-6 3 3 0 000 6zm0 1a4 4 0 100-8 4 4 0 000 8zM8 0a.5.5 0 01.5.5v1a.5.5 0 01-1 0v-1A.5.5 0 018 0zm0 13a.5.5 0 01.5.5v1a.5.5 0 01-1 0v-1A.5.5 0 018 13zM2.343 2.343a.5.5 0 01.707 0l.707.707a.5.5 0 11-.707.707l-.707-.707a.5.5 0 010-.707zm9.9 9.9a.5.5 0 01.707 0l.707.707a.5.5 0 01-.707.707l-.707-.707a.5.5 0 010-.707zM0 8a.5.5 0 01.5-.5h1a.5.5 0 010 1h-1A.5.5 0 010 8zm13 0a.5.5 0 01.5-.5h1a.5.5 0 010 1h-1A.5.5 0 0113 8zM2.343 13.657a.5.5 0 010-.707l.707-.707a.5.5 0 11.707.707l-.707.707a.5.5 0 01-.707 0zm9.9-9.9a.5.5 0 010-.707l.707-.707a.5.5 0 11.707.707l-.707-.707a.5.5 0 01-.707 0z"/></svg>
        <svg class="icon-moon" width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M6 .278a.768.768 0 01.08.858 7.208 7.208 0 00-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 01.81.316.733.733 0 01-.031.893A8.349 8.349 0 018.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 016 .278z"/></svg>
      </button>
    </nav>
  </div>
</header>

<div class="search-overlay" id="search-overlay">
  <div class="search-modal">
    <div class="search-modal__input-wrap">
      <svg width="16" height="16" viewBox="0 0 14 14" fill="none"><circle cx="6" cy="6" r="4.5" stroke="currentColor" stroke-width="1.4"/><path d="M10 10l2.5 2.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      <input type="text" id="search-modal-input" placeholder="Search documentation..." autocomplete="off">
      <button id="search-close">ESC</button>
    </div>
    <div class="search-results" id="search-results"></div>
    <div class="search-footer"><span>↑↓ navigate</span><span>↵ select</span><span>ESC close</span></div>
  </div>
</div>

<div class="layout">
  <aside class="sidebar" id="sidebar">
    <div class="sidebar__inner">
      <nav class="sidenav">
        {sidebar_html}
      </nav>
    </div>
  </aside>

  <main class="main">
    <div class="page-content">
      <div class="doc-content">
        <nav class="breadcrumb">{breadcrumb_html}</nav>
        <h1>{title} {pro_badge}</h1>
        <div class="doc-meta">
          <span>{section}</span>
        </div>
        {content_html}
        {nav_html}
      </div>
    </div>
    <footer class="footer">
      <div class="footer__inner">
        <span>© 2026 AltviseWP, LLC</span>
        <div class="footer__links">
          <a href="https://altvisewp.com" target="_blank" rel="noopener">Website</a>
          <a href="https://altvisewp.com/support/" target="_blank" rel="noopener">Support</a>
          <a href="https://altvisewp.com/privacy/" target="_blank" rel="noopener">Privacy</a>
          <a href="https://altvisewp.com/terms/" target="_blank" rel="noopener">Terms</a>
        </div>
      </div>
    </footer>
  </main>
</div>

<script src="/js/app.js"></script>
</body>
</html>'''

# ── Build breadcrumb ──────────────────────────────────────
def build_breadcrumb(items):
    parts = []
    for i, (label, url) in enumerate(items):
        if i > 0:
            parts.append('<span class="breadcrumb__sep">/</span>')
        if url:
            parts.append(f'<a href="{url}">{label}</a>')
        else:
            parts.append(f'<span>{label}</span>')
    return ''.join(parts)

# ── Build prev/next nav ───────────────────────────────────
def build_nav(current_url):
    for i, (label, url) in enumerate(PAGE_SEQUENCE):
        if url == current_url or url == current_url.rstrip('/'):
            prev_link = f'<a href="{PAGE_SEQUENCE[i-1][1]}" class="doc-nav__link"><span class="doc-nav__label">← Previous</span><span class="doc-nav__title">{PAGE_SEQUENCE[i-1][0]}</span></a>' if i > 0 else '<div></div>'
            next_link = f'<a href="{PAGE_SEQUENCE[i+1][1]}" class="doc-nav__link doc-nav__link--next"><span class="doc-nav__label">Next →</span><span class="doc-nav__title">{PAGE_SEQUENCE[i+1][0]}</span></a>' if i < len(PAGE_SEQUENCE)-1 else '<div></div>'
            return f'<div class="doc-nav">{prev_link}{next_link}</div>'
    return ''

# ── Page definitions ──────────────────────────────────────
PAGES = [
    {
        'src':       'docs/footnotes-made-easy/README.md',
        'dst':       'footnotes-made-easy/index.html',
        'title':     'Footnotes Made Easy',
        'section':   'Footnotes Made Easy',
        'url':       '/footnotes-made-easy/',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', None)],
        'is_pro':    False,
    },
    {
        'src':       'docs/footnotes-made-easy/installation.md',
        'dst':       'footnotes-made-easy/installation.html',
        'title':     'Installation',
        'section':   'Footnotes Made Easy',
        'url':       '/footnotes-made-easy/installation',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Installation', None)],
        'is_pro':    False,
    },
    {
        'src':       'docs/footnotes-made-easy/getting-started.md',
        'dst':       'footnotes-made-easy/getting-started.html',
        'title':     'Getting Started',
        'section':   'Footnotes Made Easy',
        'url':       '/footnotes-made-easy/getting-started',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Getting Started', None)],
        'is_pro':    False,
    },
    {
        'src':       'docs/footnotes-made-easy/settings/display.md',
        'dst':       'footnotes-made-easy/settings/display.html',
        'title':     'Settings — Display',
        'section':   'Footnotes Made Easy › Settings',
        'url':       '/footnotes-made-easy/settings/display',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Settings', None), ('Display', None)],
        'is_pro':    False,
    },
    {
        'src':       'docs/footnotes-made-easy/settings/behaviour.md',
        'dst':       'footnotes-made-easy/settings/behaviour.html',
        'title':     'Settings — Behaviour',
        'section':   'Footnotes Made Easy › Settings',
        'url':       '/footnotes-made-easy/settings/behaviour',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Settings', None), ('Behaviour', None)],
        'is_pro':    False,
    },
    {
        'src':       'docs/footnotes-made-easy/settings/suppress.md',
        'dst':       'footnotes-made-easy/settings/suppress.html',
        'title':     'Settings — Suppress',
        'section':   'Footnotes Made Easy › Settings',
        'url':       '/footnotes-made-easy/settings/suppress',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Settings', None), ('Suppress', None)],
        'is_pro':    False,
    },
    {
        'src':       'docs/footnotes-made-easy/settings/advanced.md',
        'dst':       'footnotes-made-easy/settings/advanced.html',
        'title':     'Settings — Advanced',
        'section':   'Footnotes Made Easy › Settings',
        'url':       '/footnotes-made-easy/settings/advanced',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Settings', None), ('Advanced', None)],
        'is_pro':    False,
    },
    {
        'src':       'docs/footnotes-made-easy/tools.md',
        'dst':       'footnotes-made-easy/tools.html',
        'title':     'Tools',
        'section':   'Footnotes Made Easy',
        'url':       '/footnotes-made-easy/tools',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Tools', None)],
        'is_pro':    False,
    },
    {
        'src':       'docs/footnotes-made-easy/multisite.md',
        'dst':       'footnotes-made-easy/multisite.html',
        'title':     'Multisite',
        'section':   'Footnotes Made Easy',
        'url':       '/footnotes-made-easy/multisite',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Multisite', None)],
        'is_pro':    False,
    },
    {
        'src':       'docs/footnotes-made-easy/faq.md',
        'dst':       'footnotes-made-easy/faq.html',
        'title':     'FAQ',
        'section':   'Footnotes Made Easy',
        'url':       '/footnotes-made-easy/faq',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('FAQ', None)],
        'is_pro':    False,
    },
    {
        'src':       'docs/footnotes-made-easy/changelog.md',
        'dst':       'footnotes-made-easy/changelog.html',
        'title':     'Changelog',
        'section':   'Footnotes Made Easy',
        'url':       '/footnotes-made-easy/changelog',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Changelog', None)],
        'is_pro':    False,
    },
    # Pro pages
    {
        'src':       'docs/footnotes-made-easy/pro-installation.md',
        'dst':       'footnotes-made-easy/pro-installation.html',
        'title':     'Installation',
        'section':   'Footnotes Made Easy Pro',
        'url':       '/footnotes-made-easy/pro-installation',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Pro', None), ('Installation', None)],
        'is_pro':    True,
    },
    {
        'src':       'docs/footnotes-made-easy/pro-license-activation.md',
        'dst':       'footnotes-made-easy/pro-license-activation.html',
        'title':     'License Activation',
        'section':   'Footnotes Made Easy Pro',
        'url':       '/footnotes-made-easy/pro-license-activation',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Pro', None), ('License Activation', None)],
        'is_pro':    True,
    },
    {
        'src':       'docs/footnotes-made-easy/pro-citations-overview.md',
        'dst':       'footnotes-made-easy/pro-citations-overview.html',
        'title':     'Citations — Overview',
        'section':   'Footnotes Made Easy Pro › Citations',
        'url':       '/footnotes-made-easy/pro-citations-overview',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Pro', None), ('Citations', None), ('Overview', None)],
        'is_pro':    True,
    },
    {
        'src':       'docs/footnotes-made-easy/pro-citations-source-types.md',
        'dst':       'footnotes-made-easy/pro-citations-source-types.html',
        'title':     'Citations — Source Types',
        'section':   'Footnotes Made Easy Pro › Citations',
        'url':       '/footnotes-made-easy/pro-citations-source-types',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Pro', None), ('Citations', None), ('Source Types', None)],
        'is_pro':    True,
    },
    {
        'src':       'docs/footnotes-made-easy/pro-citations-styles.md',
        'dst':       'footnotes-made-easy/pro-citations-styles.html',
        'title':     'Citation Styles',
        'section':   'Footnotes Made Easy Pro › Citations',
        'url':       '/footnotes-made-easy/pro-citations-styles',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Pro', None), ('Citations', None), ('Styles', None)],
        'is_pro':    True,
    },
    {
        'src':       'docs/footnotes-made-easy/pro-library.md',
        'dst':       'footnotes-made-easy/pro-library.html',
        'title':     'Footnote Library',
        'section':   'Footnotes Made Easy Pro',
        'url':       '/footnotes-made-easy/pro-library',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Pro', None), ('Library', None)],
        'is_pro':    True,
    },
    {
        'src':       'docs/footnotes-made-easy/pro-gutenberg-sidebar.md',
        'dst':       'footnotes-made-easy/pro-gutenberg-sidebar.html',
        'title':     'Gutenberg Sidebar',
        'section':   'Footnotes Made Easy Pro',
        'url':       '/footnotes-made-easy/pro-gutenberg-sidebar',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Pro', None), ('Gutenberg Sidebar', None)],
        'is_pro':    True,
    },
    {
        'src':       'docs/footnotes-made-easy/pro-faq.md',
        'dst':       'footnotes-made-easy/pro-faq.html',
        'title':     'FAQ',
        'section':   'Footnotes Made Easy Pro',
        'url':       '/footnotes-made-easy/pro-faq',
        'breadcrumb': [('Home', '/'), ('Footnotes Made Easy', '/footnotes-made-easy/'), ('Pro', None), ('FAQ', None)],
        'is_pro':    True,
    },
    # Account
    {
        'src':       'docs/account/managing-your-license.md',
        'dst':       'account/managing-your-license.html',
        'title':     'Managing Your License',
        'section':   'Account',
        'url':       '/account/managing-your-license',
        'breadcrumb': [('Home', '/'), ('Account', None), ('Managing Your License', None)],
        'is_pro':    False,
    },
    {
        'src':       'docs/account/billing-and-renewals.md',
        'dst':       'account/billing-and-renewals.html',
        'title':     'Billing and Renewals',
        'section':   'Account',
        'url':       '/account/billing-and-renewals',
        'breadcrumb': [('Home', '/'), ('Account', None), ('Billing and Renewals', None)],
        'is_pro':    False,
    },
    {
        'src':       'docs/account/refunds.md',
        'dst':       'account/refunds.html',
        'title':     'Refunds',
        'section':   'Account',
        'url':       '/account/refunds',
        'breadcrumb': [('Home', '/'), ('Account', None), ('Refunds', None)],
        'is_pro':    False,
    },
]

# ── Homepage ──────────────────────────────────────────────
HOMEPAGE = '''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AltviseWP Documentation</title>
<meta name="description" content="Official documentation for all AltviseWP WordPress plugins and products.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="{font_url}" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
</head>
<body>

<header class="topbar">
  <div class="topbar__inner">
    <a href="/" class="topbar__logo">
      <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor"><path d="M3 4h14v2H3zm0 5h9v2H3zm0 5h11v2H3z"/></svg>
      <span>AltviseWP <strong>Docs</strong></span>
    </a>
    <div class="topbar__search">
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><circle cx="6" cy="6" r="4.5" stroke="currentColor" stroke-width="1.4"/><path d="M10 10l2.5 2.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      <input type="text" id="search-input" placeholder="Search docs..." autocomplete="off" spellcheck="false">
      <kbd>⌘K</kbd>
    </div>
    <nav class="topbar__nav">
      <a href="https://altvisewp.com" target="_blank" rel="noopener">altvisewp.com</a>
      <a href="https://altvisewp.com/support/" target="_blank" rel="noopener">Support</a>
      <button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">
        <svg class="icon-sun" width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 11a3 3 0 100-6 3 3 0 000 6zm0 1a4 4 0 100-8 4 4 0 000 8zM8 0a.5.5 0 01.5.5v1a.5.5 0 01-1 0v-1A.5.5 0 018 0zm0 13a.5.5 0 01.5.5v1a.5.5 0 01-1 0v-1A.5.5 0 018 13zM2.343 2.343a.5.5 0 01.707 0l.707.707a.5.5 0 11-.707.707l-.707-.707a.5.5 0 010-.707zm9.9 9.9a.5.5 0 01.707 0l.707.707a.5.5 0 01-.707.707l-.707-.707a.5.5 0 010-.707zM0 8a.5.5 0 01.5-.5h1a.5.5 0 010 1h-1A.5.5 0 010 8zm13 0a.5.5 0 01.5-.5h1a.5.5 0 010 1h-1A.5.5 0 0113 8zM2.343 13.657a.5.5 0 010-.707l.707-.707a.5.5 0 11.707.707l-.707.707a.5.5 0 01-.707 0zm9.9-9.9a.5.5 0 010-.707l.707-.707a.5.5 0 11.707.707l-.707-.707a.5.5 0 01-.707 0z"/></svg>
        <svg class="icon-moon" width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M6 .278a.768.768 0 01.08.858 7.208 7.208 0 00-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 01.81.316.733.733 0 01-.031.893A8.349 8.349 0 018.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 016 .278z"/></svg>
      </button>
    </nav>
  </div>
</header>

<div class="search-overlay" id="search-overlay">
  <div class="search-modal">
    <div class="search-modal__input-wrap">
      <svg width="16" height="16" viewBox="0 0 14 14" fill="none"><circle cx="6" cy="6" r="4.5" stroke="currentColor" stroke-width="1.4"/><path d="M10 10l2.5 2.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      <input type="text" id="search-modal-input" placeholder="Search documentation..." autocomplete="off">
      <button id="search-close">ESC</button>
    </div>
    <div class="search-results" id="search-results"></div>
    <div class="search-footer"><span>↑↓ navigate</span><span>↵ select</span><span>ESC close</span></div>
  </div>
</div>

<div class="layout">
  <aside class="sidebar" id="sidebar">
    <div class="sidebar__inner">
      <nav class="sidenav">
        {sidebar}
      </nav>
    </div>
  </aside>

  <main class="main">
    <div class="page-content">

      <div class="home-hero">
        <div class="home-hero__eyebrow">Documentation</div>
        <h1 class="home-hero__title">AltviseWP Docs</h1>
        <p class="home-hero__sub">Official documentation for all AltviseWP WordPress plugins and products. Choose a product below to get started.</p>
      </div>

      <div class="product-grid">
        <a href="/footnotes-made-easy/" class="product-card">
          <div class="product-card__icon">
            <svg viewBox="0 0 24 24" fill="none"><path d="M4 6h16M4 11h16M4 16h10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
          </div>
          <div class="product-card__body">
            <h3 class="product-card__name">Footnotes Made Easy</h3>
            <p class="product-card__desc">Add professional footnotes to WordPress posts and pages. Free plugin + Pro add-on with citations, Library, and Gutenberg sidebar.</p>
            <div style="margin-top:8px;display:flex;gap:6px;flex-wrap:wrap;">
              <span style="font-size:11px;background:var(--brand-xl);color:var(--brand);padding:2px 8px;border-radius:10px;font-weight:600;">Free</span>
              <span style="font-size:11px;background:#fff8ee;color:var(--btn-bg);padding:2px 8px;border-radius:10px;font-weight:600;">Pro</span>
            </div>
          </div>
          <div class="product-card__arrow">→</div>
        </a>

        <a href="/account/managing-your-license" class="product-card">
          <div class="product-card__icon">
            <svg viewBox="0 0 24 24" fill="none"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2z" stroke="currentColor" stroke-width="1.6"/><path d="M12 8v4l3 3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
          </div>
          <div class="product-card__body">
            <h3 class="product-card__name">Account</h3>
            <p class="product-card__desc">Manage your license, billing, renewals, and refund requests.</p>
          </div>
          <div class="product-card__arrow">→</div>
        </a>
      </div>

      <div class="quick-links">
        <h2 class="quick-links__title">Popular pages</h2>
        <div class="quick-links__grid">
          <a href="/footnotes-made-easy/getting-started" class="quick-link">Getting Started</a>
          <a href="/footnotes-made-easy/installation" class="quick-link">Installation</a>
          <a href="/footnotes-made-easy/faq" class="quick-link">FAQ</a>
          <a href="/footnotes-made-easy/pro-license-activation" class="quick-link">License Activation</a>
          <a href="/footnotes-made-easy/pro-citations-overview" class="quick-link">Citations Overview</a>
          <a href="/account/refunds" class="quick-link">Refund Policy</a>
        </div>
      </div>

    </div>
    <footer class="footer">
      <div class="footer__inner">
        <span>© 2026 AltviseWP, LLC</span>
        <div class="footer__links">
          <a href="https://altvisewp.com" target="_blank" rel="noopener">Website</a>
          <a href="https://altvisewp.com/support/" target="_blank" rel="noopener">Support</a>
          <a href="https://altvisewp.com/privacy/" target="_blank" rel="noopener">Privacy</a>
          <a href="https://altvisewp.com/terms/" target="_blank" rel="noopener">Terms</a>
        </div>
      </div>
    </footer>
  </main>
</div>

<script src="/js/app.js"></script>
</body>
</html>'''

# ── Main build function ───────────────────────────────────
def build():
    # Clean and create build dir
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(BUILD_DIR)

    # Copy static assets
    shutil.copytree('assets/css', f'{BUILD_DIR}/css')
    shutil.copytree('assets/js',  f'{BUILD_DIR}/js')
    shutil.copy('assets/.htaccess', f'{BUILD_DIR}/.htaccess')

    # Build homepage
    with open(f'{BUILD_DIR}/index.html', 'w') as f:
        f.write(HOMEPAGE.format(font_url=FONT_URL, sidebar=build_sidebar()))
    print('  ✅ index.html')

    # Build all doc pages
    for page in PAGES:
        src = page['src']
        if not os.path.exists(src):
            print(f'  ⚠  MISSING: {src}')
            continue

        with open(src) as f:
            md = f.read()

        content_html    = md_to_html(md)
        breadcrumb_html = build_breadcrumb(page['breadcrumb'])
        nav_html        = build_nav(page['url'])

        html = page_template(
            title           = page['title'],
            section         = page['section'],
            breadcrumb_html = breadcrumb_html,
            content_html    = content_html,
            nav_html        = nav_html,
            is_pro          = page.get('is_pro', False),
        )

        dst = os.path.join(BUILD_DIR, page['dst'])
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'w') as f:
            f.write(html)
        print(f'  ✅ {page["dst"]}')

    print(f'\n✅ Build complete — {len(PAGES) + 1} pages in {BUILD_DIR}/')

if __name__ == '__main__':
    build()
