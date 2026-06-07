# Getting Started

This guide covers the complete setup from a fresh installation to your first plugin being actively monitored.

## Step 1 — Enable WordPress debug logging

If you have not already done so, add the following to your `wp-config.php` file before the `/* That's all, stop editing! */` line:

```php
define( 'WP_DEBUG', true );
define( 'WP_DEBUG_LOG', true );
define( 'WP_DEBUG_DISPLAY', false );
```

This tells WordPress to write all PHP errors, warnings, and notices to `wp-content/debug.log` rather than displaying them on screen.

## Step 2 — Open the settings page

Go to **Settings → Log Inspector** in your WordPress admin dashboard.

The settings page has two main sections:

- **Monitored Plugins** — the list of plugins currently being watched, with a form to add new ones
- **General Settings** — global configuration options like scan depth and auto-detection

## Step 3 — Add your first plugin to monitor

In the **Add New Plugin to Monitor** form, fill in three fields:

**Plugin Name** — A human-readable label for your own reference. This is what appears in the admin bar when errors are found. Example: `WooCommerce`

**Plugin File Path** — The relative path to the plugin's main file from the `wp-content/plugins/` directory. Example: `woocommerce/woocommerce.php`

To find a plugin's file path: go to **Plugins → Installed Plugins** and look at the text shown beneath each plugin name in small grey text — it shows the folder and file name.

**Search Terms** — A comma-separated list of keywords the plugin will look for in log entries to identify errors from this specific plugin. Example: `woocommerce, wc-`

Use terms that appear uniquely in that plugin's error messages. The plugin's folder name, namespace, or function prefix are good starting points.

Click **Add Plugin** to save.

## Step 4 — Check the admin bar

After adding a plugin, look at the top of your admin dashboard. You will see a **LOG INSPECTOR** item in the admin bar.

- **Green** — no errors detected for any monitored plugin
- **Red** — at least one monitored plugin has errors in the log
- **Gray** — `WP_DEBUG_LOG` is not enabled

If the indicator is green and you have just set things up, everything is working correctly. See the [Testing](testing.md) guide to verify the plugin detects errors as expected.

## Step 5 — Monitor multiple plugins

Repeat Step 3 for each plugin you want to monitor. There is no limit to the number of plugins you can add to the watchlist.

For each plugin, use search terms specific enough to avoid false positives from other plugins. For example, `woo` might match messages from multiple plugins, while `woocommerce/includes` is more specific to WooCommerce core.
