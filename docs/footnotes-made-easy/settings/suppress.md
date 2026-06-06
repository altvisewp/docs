---
sidebar_label: "Suppress"
sidebar_position: 3
description: "Hide footnotes on specific page types, post types, or URLs."
---

# Settings — Suppress

The Suppress tab controls where footnotes are displayed across your WordPress site. You can hide footnotes on specific page types, post types, or individual URLs.

Navigate to **Footnotes → Footnotes Settings → Suppress** to access these options.

## Page type suppression

These toggles let you disable footnote rendering on specific types of WordPress pages. When footnotes are suppressed on a page type, the inline markers are removed from the content and the footnotes list is not appended.

### No footnotes on the homepage

When enabled, footnotes are not displayed on your site's main homepage (the page set as your front page in **Settings → Reading**).

### No footnotes on archive pages

When enabled, footnotes are not displayed on category, tag, date, author, or custom taxonomy archive pages.

### No footnotes on search results

When enabled, footnotes are not displayed on search results pages.

### No footnotes on feeds

When enabled, footnotes are not included in your site's RSS and Atom feeds. This is recommended for most sites — footnote markers and references can look out of place in feed readers and email newsletter tools that consume your RSS feed.

## Post type suppression

### Suppress on post types

Select which post types should never display footnotes. This is useful if you have custom post types — such as products, portfolio items, or events — where footnote rendering is not appropriate.

All registered public post types are listed here. By default, no post types are suppressed.

## URL suppression

### Exclude URLs

Enter a list of specific URLs or URL paths where footnotes should be suppressed, one per line. This gives you precise control over individual pages or sections of your site.

You can enter:

- **Full URLs** — `https://yoursite.com/specific-page/`
- **Relative paths** — `/specific-page/`
- **Partial paths** — `/category/news/` (suppresses footnotes on all URLs containing this path)

**Example:**

```
/about/
/contact/
https://yoursite.com/landing-page/
```

Footnotes will be hidden on any page whose URL matches or contains one of the listed values.

## Suppress on specific posts and pages

In addition to the global suppress settings above, you can suppress footnotes on individual posts or pages directly from the post editor. A **Suppress footnotes** option is available in the post settings sidebar.

This is useful when you want to disable footnotes on a single post without changing your global settings.
