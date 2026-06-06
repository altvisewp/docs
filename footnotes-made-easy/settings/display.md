# Settings — Display

The Display tab controls how footnote markers and the footnotes list appear to your readers.

Navigate to **Footnotes → Footnotes Settings → Display** to access these options.

## Footnote identifier

The identifier is the marker that appears inline in your content to indicate a footnote.

### Pre-identifier and post-identifier

These fields wrap the identifier character. By default the pre-identifier is empty and the post-identifier is empty, producing a plain number like `1`. You can wrap the number in brackets by setting:

- **Pre-identifier:** `[`
- **Post-identifier:** `]`

This produces `[1]` in your content.

### Identifier start

Sets the starting number for footnotes. Defaults to `1`. Change this if you need footnotes on a page to begin at a different number — for example, if you are manually continuing a sequence from a previous page.

### List style type

Controls the style of the identifier. Options include:

- **Decimal** (1, 2, 3) — default
- **Lower alpha** (a, b, c)
- **Upper alpha** (A, B, C)
- **Lower roman** (i, ii, iii)
- **Upper roman** (I, II, III)

### List style symbol

When **List style type** is set to a symbol style, this field sets the symbol character to use.

### Superscript

When enabled, the inline footnote identifier is displayed as a superscript — raised slightly above the text baseline. Enabled by default. Disable this if your theme's typography handles superscript styling differently and you want to control the positioning via CSS.

## Back links

Back links are the ↩ arrows that appear next to each footnote reference, allowing readers to return to the inline marker after reading a footnote.

### Back link style

Sets the character or string displayed for the back link. Default is `↩`. You can change this to any character, word, or HTML entity.

### Pre back link and post back link

Wrap the back link character with optional text or HTML. For example, setting pre back link to `[` and post back link to `]` produces `[↩]`.

## Footnotes header and footer

### Header text

Text displayed immediately above the footnotes list. Defaults to `Footnotes`. Set this to `References`, `Sources`, `Notes`, or any heading text that fits your content style.

To display no heading at all, clear this field.

### Footer text

Text displayed immediately below the footnotes list. Empty by default. Use this for a disclaimer, attribution note, or any supplementary text you want to appear after all footnotes.

## Tooltips

### Pretty tooltips

When enabled, hovering over a footnote identifier displays the footnote content in a small tooltip popup. This allows readers to read footnotes without scrolling to the bottom of the post.

Tooltips are rendered using a lightweight JavaScript library included with the plugin. They are styled to match common WordPress themes but can be customised via CSS.

**Note:** Tooltips add a small amount of JavaScript to your front end. If page performance is a priority and your audience is predominantly mobile, consider leaving tooltips disabled.
