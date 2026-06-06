---
sidebar_label: "Behaviour"
sidebar_position: 2
description: "Configure back link positioning, combining rules, and processing priority."
---

# Settings — Behaviour

The Behaviour tab controls how footnotes function when rendered — back link positioning, combination rules, and priority.

Navigate to **Footnotes → Footnotes Settings → Behaviour** to access these options.

## Back links

### Back link position

Controls where the back link (↩) appears relative to the footnote text:

- **After footnote text** — the back link appears at the end of the footnote reference. This is the standard placement and is recommended for most sites.
- **Before footnote text** — the back link appears at the beginning of the footnote reference.

## Combining identical footnotes

### Combine identical footnotes

When enabled, if the same footnote text appears multiple times in a post, the plugin will display only one reference in the footnotes list and link all inline markers to it.

This is useful when you reference the same source multiple times throughout a post — rather than repeating the full reference, a single footnote is created and all markers point to it.

When this option is disabled, each instance of the same footnote text creates a separate numbered reference.

## Processing priority

### Footnote process priority

WordPress processes content through a series of filters. This setting controls the priority at which the footnotes plugin processes post content relative to other plugins and theme functions.

The default value is `11`. Lower numbers run earlier; higher numbers run later.

You may need to adjust this if:

- Another plugin is interfering with footnote markers before they are processed
- Footnote markers inside shortcodes or custom blocks are not being detected
- A page builder is processing content in a non-standard order

**Recommended:** Leave this at the default value unless you are experiencing a specific conflict. If you do change it, test the output carefully.

## Footnote tag

### Footnote surround tag

The HTML element used to wrap each individual footnote in the footnotes list. Defaults to `li` (a list item within an ordered list). Changing this to `p` renders each footnote as a paragraph instead of a list item.

Most themes style ordered lists correctly, so the default `li` setting is recommended for accessibility and semantic correctness.
