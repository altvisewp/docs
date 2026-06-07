# Frequently Asked Questions

## General

### Does this plugin work with simple products?

No. Bulk Variations for WooCommerce only creates variations on **variable products**. Simple products are automatically skipped during the operation.

### Will running the operation affect existing variations?

The plugin adds new variations to existing products. If a product already has variations, the new variation is added alongside them — existing variations are not modified or removed.

### Can I create multiple variation attributes at once?

No. The plugin creates one variation attribute at a time. You can run the operation multiple times with different attribute and term configurations to add additional variations.

### What happens if the attribute already exists?

If the attribute slug you enter already exists in WooCommerce, the plugin uses the existing attribute rather than creating a new one.

### What happens if the variation term already exists on a product?

If a product already has the specified variation term assigned to it, the plugin skips that product and moves on to the next one.

### Can I undo the operation?

There is no undo function built into the plugin. To remove variations added by the plugin, you would need to edit each product individually via **Products → All Products → Edit** and remove the variation from the Variations tab.

For large stores, consider using WooCommerce's bulk edit feature or a dedicated product management plugin to remove variations in bulk.

### Does it work with WooCommerce HPOS?

Yes. The plugin is fully compatible with WooCommerce High-Performance Order Storage (HPOS / custom order tables).

## Settings

### What does the price adjustment do exactly?

The price adjustment field takes a percentage value and applies it to each product's **regular price** when creating the new variation. For example, if a product has a regular price of $50 and you set the adjustment to `+20`, the new variation is priced at $60.

If a product has no regular price set, the variation is created with no price.

### Does the price adjustment apply to existing variations?

No. The price adjustment only applies to the newly created variations. Existing product prices and existing variation prices are not changed.

### What format should the attribute slug be in?

Enter only the slug part — lowercase letters, numbers, and hyphens. Do not include the `pa_` prefix — the plugin adds it automatically.

Correct: `season`
Incorrect: `pa_season`, `Season`, `SEASON`

## Shortcode

### How do I display my variation terms on the frontend?

Use the shortcode `[variations attribute="your_attribute"]` on any page or post, replacing `your_attribute` with your attribute slug.

### How long does the cookie-based selection persist?

The visitor's variation selection is stored in a browser cookie for 30 days. After 30 days, the cookie expires and the selection is cleared.

### Can I display terms from multiple attributes on the same page?

Yes — add multiple shortcodes to the same page, one for each attribute:

```
[variations attribute="season"]
[variations attribute="show-type"]
```

Each shortcode renders its own grid independently.

## Support

### Where do I get support?

Support is available on the [WordPress.org support forum](https://wordpress.org/support/plugin/bulk-variations-for-woocommerce/) for the free plugin.
