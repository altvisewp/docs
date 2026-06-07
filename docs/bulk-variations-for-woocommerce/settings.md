# Settings

Navigate to **WooCommerce → Bulk Variations** to access the plugin settings. The settings page consists of a single configuration form and a shortcode reference card.

## Attribute

**Field:** `Attribute`
**Input:** Text field, pre-filled with `pa_` prefix

The WooCommerce attribute slug to use when creating variations. Enter only the slug after the `pa_` prefix — the plugin prepends it automatically.

The slug must be lowercase and may contain letters, numbers, and hyphens. It should match an existing attribute in **Products → Attributes**, or you can enter a new slug and the plugin will create the attribute automatically.

**Examples:**
- `season` → creates or uses the `pa_season` attribute
- `show-type` → creates or uses the `pa_show-type` attribute

## Variation

**Field:** `Variation`
**Input:** Text field

The term name for the new variation. This is the human-readable label that customers see on the product page and that appears in variation dropdowns.

**Examples:** `Summer 2026`, `Exhibition`, `Large`, `Red`

## Price adjustment

**Field:** `Price adjustment (%)`
**Input:** Number field (accepts positive and negative values)

A percentage value applied to the regular price of each variable product when creating the new variation.

| Value | Effect |
|---|---|
| `0` | No adjustment — variation uses parent product price |
| `20` | Increases variation price by 20% |
| `-15` | Decreases variation price by 15% |

The adjustment is calculated from the product's regular price at the time the operation is run. If a product has no regular price set, the variation price is left empty.

## Save & Apply button

Clicking **Save & Apply** saves the current settings and immediately runs the bulk variation creation across all variable products in the store.

The operation cannot be undone from within the plugin. To remove variations added by the plugin, you would need to edit each product individually or use a bulk edit tool.

## Quick links

The settings page includes a **Quick Links** card with shortcuts to:

- **Manage Attributes** — opens the WooCommerce product attributes screen
- **All Products** — opens the product list to verify results

## Shortcode reference

The settings page also includes a **Shortcode** card showing the correct usage of the `[variations]` shortcode. See the [Shortcode](shortcode.md) page for full details.
