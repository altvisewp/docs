# Admin Bar

The **LOG INSPECTOR** indicator appears in the WordPress admin bar at the top of every admin page once you have at least one plugin in the monitored list.

## Status colours

| Colour | Meaning |
|---|---|
| 🟢 Green | All monitored plugins are error-free |
| 🔴 Red | At least one monitored plugin has errors in the debug log |
| ⚫ Gray | `WP_DEBUG_LOG` is not enabled in `wp-config.php` |

## What the indicator shows

**Green state** — The plugin has scanned the debug log and found no entries matching the search terms of any monitored plugin. This means either no errors have occurred, or errors have occurred but do not match any configured search terms.

**Red state** — At least one search term from at least one monitored plugin was found in the debug log. Hovering over the indicator shows the most recent matching error message, so you can diagnose the issue without leaving the current page.

**Gray state** — `WP_DEBUG_LOG` is not set to `true` in `wp-config.php`. The plugin cannot scan a log that does not exist. See the [Installation](installation.md) guide to enable debug logging.

## Hover tooltip

When the indicator is red, hovering over the **LOG INSPECTOR** text in the admin bar shows a dropdown with:

- Which plugin is generating errors
- The most recent error message from the log

This gives you a quick summary without opening the full settings page or the raw log file.

## The indicator is not appearing

If the **LOG INSPECTOR** indicator is not visible in your admin bar:

1. Confirm the plugin is activated under **Plugins → Installed Plugins**
2. Confirm you have added at least one plugin to the monitored list under **Settings → Log Inspector**
3. Confirm the admin bar is enabled — go to **Users → Profile** and check that **Show Toolbar when viewing site** is enabled
4. Check that you are logged in as a user with the `manage_options` capability (Administrator role)

## The indicator is always gray

Gray means `WP_DEBUG_LOG` is not enabled. Add these lines to `wp-config.php` before the `/* That's all, stop editing! */` line:

```php
define( 'WP_DEBUG', true );
define( 'WP_DEBUG_LOG', true );
define( 'WP_DEBUG_DISPLAY', false );
```

Save the file and reload any admin page. The indicator should change to green or red depending on your log state.
