---
sidebar_label: "Gutenberg Sidebar"
sidebar_position: 4
description: "Manage footnotes from the block editor sidebar."
---

# Gutenberg Sidebar Panel

The Gutenberg sidebar panel lets you manage all footnotes in a post from the block editor — without switching tabs, scrolling through content, or editing raw text markers.

## Opening the sidebar panel

1. Open a post in the block editor (Gutenberg)
2. Click the **Settings** icon (⚙) in the top-right corner of the editor to open the sidebar, if it is not already open
3. Click the **Footnotes** tab in the sidebar panel list

If you do not see the Footnotes panel, confirm that Footnotes Made Easy Pro is installed, active, and licensed.

## What the sidebar shows

The sidebar panel displays all footnotes in the current post in the order they appear in the content. Each footnote entry shows:

- The footnote number
- A preview of the footnote text or citation
- Edit and delete actions

## Adding a footnote from the sidebar

1. Place your cursor in the post content at the point where you want the footnote marker
2. In the sidebar, click **Add footnote**
3. Enter the footnote text in the text area, or switch to **Citation mode** to create a formatted citation
4. Click **Insert**

The footnote marker `(( ))` is inserted at the cursor position and the footnote appears in the sidebar list.

## Editing a footnote

1. In the sidebar, click the **Edit** icon next to the footnote you want to change
2. Edit the footnote text or citation fields
3. Click **Save**

Changes are reflected immediately in the footnote list and will be visible on the published post.

## Deleting a footnote

1. In the sidebar, click the **Delete** icon next to the footnote you want to remove
2. Confirm the deletion

Deleting a footnote from the sidebar removes both the marker from the content and the entry from the footnotes list.

## Citation mode

When citation mode is enabled in the sidebar panel, the footnote entry form expands to show structured citation fields — source type, author, title, year, and other relevant fields depending on the source type.

**To use citation mode:**

1. Click **Add footnote** in the sidebar
2. Toggle **Citation mode** on
3. Select the source type from the dropdown
4. Fill in the citation fields
5. Optionally paste a DOI or ISBN and click **Fetch** to auto-populate the fields
6. Click **Insert**

The citation is formatted according to the default citation style set in **Footnotes Settings → Citations**, unless overridden at the post level.

[Learn more about Citations →](pro-citations-overview.md)

## Inserting from the Library

1. Click **Add footnote** in the sidebar
2. Click **Insert from Library**
3. Search for your saved footnote by title or content
4. Click **Insert** next to the entry

The Library entry's content is inserted as a new footnote at the current cursor position.

[Learn more about the Footnote Library →](pro-library.md)

## Reordering footnotes

Footnote numbering is determined by the order the markers appear in the post content — not by their order in the sidebar. To change the order of footnotes, move the `(( ))` markers in the content itself.

## Post-level citation style override

You can override the site-wide default citation style for an individual post from the sidebar:

1. Open the Footnotes sidebar panel
2. In the **Post settings** section, select a citation style from the **Override style** dropdown
3. This style will be used for all citations in this post, regardless of the site-wide default

## Sidebar not appearing

If the Footnotes panel does not appear in the sidebar:

- Confirm that Footnotes Made Easy Pro is active and licensed
- Confirm that you are editing a post or page (the sidebar is not available on custom post types that have not been configured to support it)
- Check that the panel has not been hidden — click the three-dot menu (⋮) at the top of the sidebar and look for Footnotes in the panel list
- Refresh the page and try again
