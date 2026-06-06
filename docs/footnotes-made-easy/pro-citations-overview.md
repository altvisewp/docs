# Citations — Overview

Footnotes Made Easy Pro includes a full academic citation engine that formats footnotes as structured citations in APA, MLA, or Chicago style. Citations are generated automatically from the source information you provide — you do not need to know the formatting rules for each style.

## How citations work

When the Citations feature is enabled, the footnote entry form in the Gutenberg sidebar gains a **Citation mode** toggle. In citation mode, instead of entering free-form footnote text, you fill in a structured form — source type, author, title, year, and other relevant fields — and the plugin generates the correctly formatted citation automatically.

Citations are formatted at render time. If you change the default citation style in the settings, all citations on your site update automatically.

## Enabling citations

1. Ensure you have an active Footnotes Made Easy Pro license
2. Go to **Footnotes → Footnotes Settings → Citations**
3. Select your default citation style (APA, MLA, or Chicago)
4. Click **Save changes**

The Citations tab is available in the Gutenberg sidebar for any post once the default style is set.

## Setting a default citation style

The default citation style applies to all new citations. You can set it under **Footnotes Settings → Citations → Default citation style**.

Options are:

- **APA** (7th edition) — American Psychological Association, commonly used in social sciences, psychology, and education
- **MLA** (9th edition) — Modern Language Association, commonly used in humanities, literature, and language studies
- **Chicago** (17th edition) — Chicago Manual of Style, commonly used in history, arts, and some social sciences

The default style can be changed at any time. Changing it updates all citations on the site that do not have an individually overridden style.

## Overriding the style on a per-post basis

You can use a different citation style on an individual post without changing the site-wide default. In the Gutenberg sidebar Citations panel, select the post-level style override before adding citations to that post.

## DOI and ISBN auto-fetch

When adding a citation for a journal article or book, you can paste a DOI or ISBN into the auto-fetch field and the plugin will retrieve the source metadata automatically — title, author, year, publisher, and more.

**Using DOI auto-fetch:**

1. In the citation form, click **Fetch from DOI**
2. Paste the DOI (e.g. `10.1000/xyz123`)
3. Click **Fetch**
4. The form fields populate automatically with the retrieved metadata
5. Review and adjust any fields as needed
6. Click **Insert**

**Using ISBN auto-fetch:**

1. In the citation form, click **Fetch from ISBN**
2. Paste the ISBN-10 or ISBN-13 (e.g. `978-3-16-148410-0`)
3. Click **Fetch**
4. The form fields populate automatically
5. Review and adjust as needed
6. Click **Insert**

Auto-fetch requires an internet connection from your WordPress server. If the fetch fails, you can still enter source details manually.

## Related documentation

- [Source Types](source-types.md) — full list of supported source types and their fields
- [Citation Styles](citation-styles.md) — formatting rules and examples for APA, MLA, and Chicago
- [Gutenberg Sidebar](../gutenberg-sidebar.md) — how to use the sidebar panel to insert and manage citations
