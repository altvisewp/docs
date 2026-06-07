# Frequently Asked Questions

## Setup

### Do I need to enable WP_DEBUG to use this plugin?

Yes. The plugin monitors `wp-content/debug.log`, which WordPress only creates when `WP_DEBUG_LOG` is set to `true` in `wp-config.php`. Without it, there is no log to scan and the admin bar indicator will show gray.

Add these lines to `wp-config.php` before the `/* That's all, stop editing! */` line:

```php
define( 'WP_DEBUG', true );
define( 'WP_DEBUG_LOG', true );
define( 'WP_DEBUG_DISPLAY', false );
```

### Should I use this on a live production site?

This plugin is primarily designed for development, staging, and QA environments. Enabling `WP_DEBUG` on a production site can expose sensitive error information and may impact performance. If you need to debug a production issue, enable it temporarily and disable it immediately after.

### Can I monitor any plugin — not just ones from WordPress.org?

Yes. Any plugin that generates PHP errors or writes to the debug log can be monitored. This includes custom plugins, proprietary plugins, and client plugins.

## Monitoring

### What are Search Terms and how do I choose them?

Search terms are keywords the plugin looks for in each line of the debug log to determine whether an error belongs to the plugin you are monitoring. Use terms unique to that plugin such as its folder name, function prefix, class namespace, or file path.

For example, for WooCommerce: `woocommerce, wc-`

Avoid very short or common terms that might match entries from other plugins.

### How much of the debug.log file is scanned?

By default, the last 300KB. You can adjust this under **Settings → Log Inspector → General Settings → Log scan depth**. The plugin reads from the end of the file (newest entries first) up to the configured limit.

### What does "Only monitor active plugins" do?

When enabled under General Settings, plugins in your watchlist that are currently deactivated in WordPress are automatically excluded from monitoring. This prevents false alerts from plugins you have temporarily disabled.

### Can I monitor the same plugin on multiple sites?

Yes, but you need to configure the plugin separately on each WordPress installation. There is no central dashboard.

### Will this slow down my site?

No. The plugin only runs in the WordPress admin area and uses efficient file reading (scanning only the end of the log file). There is no frontend impact.

## Admin bar

### The LOG INSPECTOR indicator is not showing in my admin bar

- Confirm the plugin is active
- Confirm you have added at least one plugin to the monitored list
- Confirm your user role is Administrator (the indicator is only shown to users with `manage_options` capability)
- Go to **Users → Profile** and confirm **Show Toolbar when viewing site** is enabled

### The indicator is always gray

Gray means `WP_DEBUG_LOG` is not enabled. Enable it in `wp-config.php` as shown above.

### The indicator is green but I know there are errors

Check that your search terms match the text actually appearing in the log. Open `wp-content/debug.log` and look at a real error from the plugin you are monitoring, then make sure your search terms appear in that log entry.

Also check that the plugin's monitoring toggle is enabled (not disabled) in the settings list.

## Compatibility

### Does it work with WordPress Multisite?

Yes.

### Does it work with PHP 8.x?

Yes. The plugin has been tested with PHP 8.4 and 8.5.

### Does the plugin modify the debug.log file?

No. The plugin reads the log file but never writes to or modifies it. WordPress and PHP are responsible for writing to `debug.log`.

## Support

### Where do I report bugs or request features?

- **GitHub:** [lumumbapl/lumiblog-debug-log-inspector](https://github.com/lumumbapl/lumiblog-debug-log-inspector)
- **WordPress.org:** [Support forum](https://wordpress.org/support/plugin/lumiblog-debug-log-inspector/)
