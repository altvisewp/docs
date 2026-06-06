---
sidebar_label: "Getting Started"
sidebar_position: 3
description: "Learn the basic syntax and write your first footnote."
---

# Getting Started

This guide covers everything you need to know to start adding footnotes to your WordPress posts and pages.

## The basic syntax

Footnotes Made Easy uses a simple inline marker syntax. To add a footnote, wrap the footnote text in double parentheses anywhere in your content:

```
This is your post content.((This is the footnote text.))
```

When the post is published or previewed, the plugin:

- Replaces the `(( ))` marker with a numbered superscript — `¹`
- Appends a numbered footnotes list at the bottom of the post
- Links the superscript to the reference and back

You do not need to track numbers manually. The plugin numbers all footnotes sequentially in the order they appear in the post.

## Adding your first footnote

1. Open a post or page in the WordPress editor
2. Place your cursor at the point in the text where you want the footnote marker to appear
3. Type your footnote content wrapped in `(( ))`:

```
WordPress was first released in 2003.((Matt Mullenweg and Mike Little, May 27, 2003.))
```

4. Click **Preview** or **Publish**
5. The footnote appears as a superscript in the text, with the reference listed at the bottom of the post

## Adding multiple footnotes

Add as many footnotes as you need — just keep using the `(( ))` syntax:

```
The population reached 4.2 million in 2022.((World Bank Development Indicators, 2022.))
Growth has accelerated since 2015,((UN Urbanisation Report, 2023.)) particularly in coastal regions.
```

This produces two numbered footnotes in sequential order. If you add a new footnote between two existing ones later, the numbering updates automatically.

## Adding footnotes in the block editor (Gutenberg)

In the block editor, you can add footnotes inside any text block — paragraphs, headings, list items, and more. Simply type the `(( ))` syntax directly in the block content.

The plugin processes the syntax when the post is saved and rendered — it does not display as a visual block in the editor.

## Adding footnotes in the Classic Editor

In the Classic Editor, add the `(( ))` syntax directly in the text editor (Text or Visual mode). In Visual mode, the markers remain visible as plain text until the post is previewed or published.

## Viewing the output

Click **Preview** on any post to see the rendered output. You will see:

- Superscript numbers at each footnote insertion point
- A **Footnotes** section at the bottom of the post (the heading text is configurable)
- Clickable ↩ arrows next to each reference that return the reader to the inline marker

## Changing the delimiter

By default, the plugin uses `((` and `))` as delimiters. If these conflict with another plugin or your content, you can change them under **Footnotes → Footnotes Settings → Advanced**.

For example, to use `{fn` and `}` instead:

```
This is your content.{fnThis is the footnote text.}
```

## Next steps

- [Settings — Display](settings/display.md) — change identifier style, header text, and tooltip behaviour
- [Settings — Behaviour](settings/behaviour.md) — configure back links and combining options
- [Settings — Suppress](settings/suppress.md) — hide footnotes on specific page types or URLs
- [Settings — Advanced](settings/advanced.md) — change delimiters and other advanced options
