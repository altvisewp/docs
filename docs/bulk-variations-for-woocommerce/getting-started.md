# Getting Started

This guide walks you through creating your first bulk variation from start to finish.

## Before you begin

Bulk Variations for WooCommerce works with **variable products** only. Simple products are skipped automatically. Make sure you have at least one variable product in your WooCommerce store before running the operation.

## Step 1 — Open the plugin settings

Go to **WooCommerce → Bulk Variations** in your WordPress admin dashboard.

## Step 2 — Set the attribute name

In the **Attribute** field, enter the slug of the WooCommerce attribute you want to create variations for. The field is pre-filled with the `pa_` prefix — enter only the slug part after it.

For example, if your attribute is called **Season**, enter `season`. The full attribute key will be `pa_season`.

If the attribute does not yet exist in WooCommerce, the plugin will create it automatically when you run the operation.

**Note:** The attribute slug must match an existing attribute in **Products → Attributes**, or be a new slug you want the plugin to create. If you enter a slug that partially matches an existing attribute, the plugin uses the existing one.

## Step 3 — Set the variation term name

In the **Variation** field, enter the term name for the new variation. This is the value customers will see — for example, `Summer 2026`, `Large`, or `Red`.

## Step 4 — Set a price adjustment (optional)

In the **Price adjustment** field, enter a percentage value to adjust the price of the newly created variations:

- Enter a **positive number** (e.g. `20`) to increase variation prices by 20%
- Enter a **negative number** (e.g. `-10`) to decrease variation prices by 10%
- Leave at **0** to set no price adjustment — the variation inherits the parent product price

## Step 5 — Run the operation

Click **Save & Apply**. The plugin will:

1. Create the attribute if it does not already exist
2. Loop through every variable product in your store
3. Add the new variation term to each product
4. Apply the price adjustment to the newly created variation
5. Display a confirmation when complete

Depending on the number of products in your store, this may take a few seconds.

## Step 6 — Verify the results

After the operation completes, open any variable product in **Products → All Products** and check its **Variations** tab to confirm the new variation was added correctly.

## Next steps

- [Settings](settings.md) — full reference for all configuration options
- [Shortcode](shortcode.md) — display a landing page of variation terms on the frontend
