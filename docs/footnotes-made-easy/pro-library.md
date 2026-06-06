---
sidebar_label: "Footnote Library"
sidebar_position: 3
description: "Save and reuse footnotes across posts with the Footnote Library."
---

# Footnote Library

The Footnote Library lets you save footnotes once and reuse them across any post on your WordPress site. This is particularly useful for sources you reference repeatedly — a frequently cited book, a recurring disclaimer, or a standard attribution note.

## Accessing the Library

Go to **Footnotes → Library** in your WordPress admin dashboard.

On multisite installations, the Library is only accessible from the network admin.

## Adding a footnote to the Library

### Method 1 — From the Library page

1. Go to **Footnotes → Library**
2. Click **Add new**
3. Enter a **Title** — this is a label for your own reference and does not appear in the published footnote
4. Enter the **Footnote content** — the text that will appear in the footnotes list when this entry is used
5. Optionally select a **Category** if you have set up Library categories
6. Click **Save**

### Method 2 — From the Gutenberg sidebar

While editing a post:

1. Open the **Footnotes** panel in the Gutenberg sidebar
2. Add or select a footnote
3. Click **Save to Library**
4. Enter a title for the Library entry
5. Click **Save**

The footnote is now saved to the Library and available for insertion in any post.

## Inserting a Library footnote into a post

### From the Gutenberg sidebar

1. Place your cursor at the point in the post where you want the footnote marker
2. Open the **Footnotes** panel in the Gutenberg sidebar
3. Click **Insert from Library**
4. Search for the footnote by title or content
5. Click **Insert** next to the entry you want to use

The footnote marker is inserted at the cursor position and the Library entry's content is used as the footnote text.

### Updating a Library entry

If you edit the content of a Library entry, posts that have already used it are **not** automatically updated. Library entries are copied into the post at the time of insertion. To update an existing usage, you would need to re-insert the updated entry or edit the footnote directly in the post.

## Searching the Library

Use the search field at the top of the Library page to find entries by title or content. The search is live — results filter as you type.

## Bulk actions

Select multiple Library entries using the checkboxes on the left side of the table to perform bulk actions:

- **Delete** — permanently remove the selected entries from the Library
- **Export** — export the selected entries as a JSON file

## Import and export

### Export

1. Go to **Footnotes → Library**
2. Click **Export Library**
3. Choose to export all entries or only selected entries
4. A JSON file downloads to your computer

### Import

1. Go to **Footnotes → Library**
2. Click **Import Library**
3. Select a previously exported JSON file
4. Choose whether to **merge** (add to existing entries) or **replace** (overwrite all existing entries)
5. Click **Import**

Import and export are useful for:

- Backing up your Library before making bulk changes
- Copying your Library to another WordPress site
- Sharing a Library of standard references with a team

## Deleting Library entries

To delete a single entry:

1. Go to **Footnotes → Library**
2. Hover over the entry
3. Click **Delete**
4. Confirm the deletion

Deleting a Library entry does not affect posts that have already used it — the footnote content was copied to the post at the time of insertion and is stored independently.

## Pagination

The Library page displays 20 entries per page by default. Use the pagination controls at the bottom of the table to navigate between pages when your Library grows large.
