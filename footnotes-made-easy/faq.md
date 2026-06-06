# Frequently Asked Questions

## General

### Does the plugin work with the Gutenberg block editor?

Yes. The `(( ))` syntax works inside any text block in the Gutenberg editor — paragraphs, headings, list items, and more. The footnote markers are processed when the post is saved and rendered on the front end.

### Does it work with the Classic Editor?

Yes. Add the `(( ))` syntax directly in the text editor in either Visual or Text mode.

### Does it work with page builders like Elementor, Beaver Builder, or Divi?

Compatibility varies by page builder. Most page builders that render standard WordPress post content will process footnote markers correctly. Page builders that use their own rendering pipeline outside of the standard WordPress content filters may not. Test on your specific setup before publishing.

### Will footnotes appear in my RSS feed?

By default, yes. You can disable this under **Footnotes Settings → Suppress → No footnotes on feeds**, which is recommended for most sites.

### Can I add HTML inside a footnote?

Yes. Basic HTML is supported inside footnote markers. For example:

```
This is content.((<em>Emphasis</em> and <a href="https://example.com">links</a> work inside footnotes.))
```

### Does the plugin slow down my site?

The plugin adds minimal overhead. Tooltip functionality loads a small JavaScript file on the front end, which can be disabled if not needed under **Footnotes Settings → Display → Pretty tooltips**.

### How do I change the "Footnotes" heading above the references list?

Go to **Footnotes → Footnotes Settings → Display → Footnotes header / footer** and change the **Header text** field to your preferred heading.

### Can I suppress footnotes on a single post without changing global settings?

Yes. Open the post in the editor, find the **Footnotes** panel in the block editor sidebar or the **Footnotes Made Easy** meta box in the Classic Editor, and enable the **Suppress footnotes** option for that post.

### The footnote numbers reset to 1 on every post. Is that correct?

Yes. Footnote numbering is per-post. Each post or page starts its own sequential count from 1 (or the value set in **Identifier start** under Display settings).

### My footnotes are not rendering. What should I check?

1. Confirm the plugin is active under **Plugins → Installed Plugins**
2. Check that you are using the correct delimiter — `((` and `))` by default
3. Check **Footnotes Settings → Suppress** to confirm footnotes are not suppressed on the relevant page type
4. If you have changed the delimiter, confirm your content uses the new delimiter
5. Check if another plugin might be processing the content before the footnotes plugin. Try adjusting the **Footnote process priority** under **Settings → Behaviour**

### Can I use footnotes inside widgets or shortcodes?

The plugin processes the standard `the_content` filter. Widgets and some shortcodes may use different filters. Enable **Allow shortcodes in footnotes** under **Settings → Advanced** and test your specific use case.

## Settings and configuration

### I changed a setting and now footnotes look different across my site. How do I revert?

Go to **Footnotes → Tools → Reset settings** and click **Reset to defaults**. This restores all settings to their original values.

Alternatively, export your settings before making changes so you can import them back if needed.

### Can I copy my settings to another site?

Yes. Go to **Footnotes → Tools → Export settings** to download a JSON file, then import it on the other site using **Import settings**.

### What is the minimum WordPress version required?

WordPress 6.0 or higher.

### What is the minimum PHP version required?

PHP 7.4 or higher.

## Pro version

### What additional features does the Pro version include?

Footnotes Made Easy Pro adds:

- Academic citations in APA, MLA, and Chicago style
- 10 source types (book, journal, website, newspaper, film, thesis, and more)
- DOI and ISBN auto-fetch
- A reusable Footnote Library
- A Gutenberg sidebar panel for managing footnotes without leaving the editor

[Learn more about the Pro version](README.md).

### Do I need the free plugin to use the Pro version?

Yes. Footnotes Made Easy Pro is an add-on that requires the free plugin to be installed and active.
