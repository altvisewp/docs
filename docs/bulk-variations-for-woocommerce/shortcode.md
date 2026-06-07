# Shortcode

Bulk Variations for WooCommerce includes a shortcode that generates a landing page displaying all terms in a given WooCommerce attribute as a navigable grid.

## Usage

```
[variations attribute="your_attribute"]
```

Replace `your_attribute` with the slug of the WooCommerce attribute you want to display (without the `pa_` prefix).

**Example:**

```
[variations attribute="season"]
```

This displays all terms in the `pa_season` attribute as a grid of clickable tiles.

## How it works

When a visitor clicks a term on the landing page:

- They are sent to `/?v=term-slug` (e.g. `/?v=summer-2026`)
- The plugin automatically pre-selects that variation on any product pages the visitor views
- The selection is stored in a cookie and persists for **30 days** — so returning visitors see their previously selected variation pre-selected automatically

This is useful for stores with event, season, or category-based variations where you want customers to filter their entire shopping experience to a single variation value.

## Where to add the shortcode

Add the shortcode to any WordPress page, post, or widget that supports shortcodes:

1. Go to **Pages → Add New** (or edit an existing page)
2. Add a **Shortcode** block (Gutenberg) or paste the shortcode directly (Classic Editor)
3. Enter `[variations attribute="your_attribute"]`
4. Publish or update the page

## Output

The shortcode renders a grid of variation terms. Each tile shows the term name and links to `/?v=term-slug`. The grid uses a basic layout that can be customised with CSS — target the wrapper element with your theme's custom CSS.

## Customising the appearance

The shortcode output uses straightforward HTML that you can style via your theme's **Additional CSS** (Appearance → Customize → Additional CSS) or a custom stylesheet.

The grid does not apply any opinionated styles beyond basic layout — it inherits your theme's typography and colours by default.

## Notes

- The shortcode only displays terms for attributes that have been assigned to at least one product
- If no attribute is specified or the attribute does not exist, the shortcode outputs nothing
- The cookie-based selection works across the entire store — any variable product with the matching attribute will have the variation pre-selected
