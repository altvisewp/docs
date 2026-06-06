# AltviseWP Docs

Official documentation for all AltviseWP WordPress plugins and products.

Live at: **https://docs.altvisewp.com**

## How it works

- All documentation is written in **Markdown** inside the `docs/` folder
- On every push to `main`, GitHub Actions runs `build.py` which converts the Markdown to HTML
- The built HTML files are automatically deployed to the server via FTP
- Changes are live within 1–2 minutes of pushing

## Editing docs

1. Find the Markdown file you want to edit in `docs/`
2. Edit it directly on GitHub or clone the repo and edit locally
3. Commit and push to `main`
4. GitHub Actions handles the rest

## Repo structure

```
docs/                        ← Markdown source files
  footnotes-made-easy/       ← Free plugin docs
    settings/
    pro-*.md                 ← Pro plugin docs (prefixed with pro-)
  account/                   ← Account, billing, refunds
assets/
  css/style.css              ← Site stylesheet
  js/app.js                  ← Search, theme toggle
  .htaccess                  ← Clean URLs
build.py                     ← Build script (Markdown → HTML)
.github/workflows/deploy.yml ← Auto-deploy workflow
```

## Adding a new page

1. Create a new `.md` file in the appropriate `docs/` folder
2. Add the page to `build.py` — add an entry to the `PAGES` list and `PAGE_SEQUENCE` list
3. Add the page to the sidebar in `build.py` — update the `SIDEBAR` definition
4. Push — the page will be built and deployed automatically

## GitHub Secrets required

| Secret | Value |
|---|---|
| `FTP_SERVER` | `ftp.gb.stackcp.com` |
| `FTP_USERNAME` | Your FTP username |
| `FTP_PASSWORD` | Your FTP password |

Add these under **Settings → Secrets and variables → Actions** in the GitHub repo.
