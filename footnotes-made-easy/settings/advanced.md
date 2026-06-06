# Settings — Advanced

The Advanced tab contains delimiter configuration and other low-level settings. Most users will not need to change these defaults.

Navigate to **Footnotes → Footnotes Settings → Advanced** to access these options.

## Delimiters

Delimiters are the opening and closing characters that the plugin uses to detect footnote markers in your content. The default delimiter pair is `((` and `))`.

### Opening delimiter

The character or string that marks the beginning of a footnote. Default: `((`

### Closing delimiter

The character or string that marks the end of a footnote. Default: `))`

### When to change delimiters

You may need to change the delimiters if:

- Another plugin uses `(( ))` syntax for its own purposes
- Your content regularly contains double parentheses for non-footnote reasons
- You are migrating from another footnotes plugin that uses a different syntax

### Choosing custom delimiters

When choosing custom delimiters, pick a character combination that:

- Does not appear in your regular content
- Does not conflict with HTML, Markdown, or any other syntax your editor processes
- Is easy to type when writing

**Common alternatives:**

| Opening | Closing | Example |
|---|---|---|
| `[fn]` | `[/fn]` | `[fn]Footnote text.[/fn]` |
| `{fn` | `}` | `{fnFootnote text.}` |
| `[[` | `]]` | `[[Footnote text.]]` |

### Changing delimiters on an existing site

If you change your delimiters after already publishing content with the old syntax, existing footnotes will stop rendering until you update the content to use the new delimiters. Use the **Delimiter Migration Tool** in the Tools page (coming soon) to automatically convert existing content to the new delimiter format.

## Short codes

### Allow shortcodes in footnotes

When enabled, WordPress shortcodes within footnote text are processed and rendered. Disable this if you do not use shortcodes inside footnotes and want to improve performance slightly.
