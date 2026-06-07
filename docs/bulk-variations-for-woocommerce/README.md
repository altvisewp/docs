# Bulk Variations for WooCommerce

**Version:** 1.2.1
**Requires WordPress:** 6.4 or higher
**Requires PHP:** 8.0 or higher
**Requires WooCommerce:** 8.0 or higher
**License:** GPL-3.0+
**Download:** [WordPress.org](https://wordpress.org/plugins/bulk-variations-for-woocommerce/)

Bulk Variations for WooCommerce is a free WordPress plugin that lets you create a new variation attribute across all your existing WooCommerce variable products in a single operation. Instead of editing each product individually, you configure the variation once and the plugin applies it to every variable product in your store.

## How it works

1. You define a variation attribute name and term in the plugin settings
2. Optionally set a price adjustment percentage for the new variation
3. Click **Save & Apply** — the plugin creates the variation on every variable product automatically
4. Optionally use the `[variations]` shortcode to display a landing page of all variation terms

## Key features

**Bulk variation creation** — Create a new variation attribute for all existing WooCommerce variable products simultaneously. The plugin skips simple products and only targets variable products.

**Global price adjustment** — Set a percentage increase or decrease to apply to the price of each newly created variation. If a product has a regular price of $100 and you set +20%, the variation price is set to $120.

**Automatic attribute creation** — If the specified attribute does not yet exist in WooCommerce, the plugin creates it automatically before assigning it to products.

**Landing page shortcode** — Use `[variations attribute="your_attribute"]` on any page or post to display a grid of all terms in that attribute. Each term links to a filtered product URL and the selection is remembered via cookie for 30 days.

**HPOS compatible** — Fully compatible with WooCommerce High-Performance Order Storage (HPOS / custom order tables).

## Documentation

- [Installation](installation.md)
- [Getting Started](getting-started.md)
- [Settings](settings.md)
- [Shortcode](shortcode.md)
- [FAQ](faq.md)
- [Changelog](changelog.md)
