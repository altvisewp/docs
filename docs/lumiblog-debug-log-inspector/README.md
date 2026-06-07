# Lumiblog Debug Log Inspector

**Version:** 1.1.0
**Requires WordPress:** 5.0 or higher
**Requires PHP:** 7.0 or higher
**License:** GPL-2.0+
**GitHub:** [lumumbapl/lumiblog-debug-log-inspector](https://github.com/lumumbapl/lumiblog-debug-log-inspector)
**Download:** [WordPress.org](https://wordpress.org/plugins/lumiblog-debug-log-inspector/)

Lumiblog Debug Log Inspector is a WordPress plugin that monitors your `debug.log` file for plugin-specific errors and displays real-time status indicators in the WordPress admin bar. Add any plugin you want to watch through the settings interface — no code editing required.

## How it works

1. WordPress writes errors to `wp-content/debug.log` when `WP_DEBUG_LOG` is enabled
2. The plugin scans the last 300KB of that log file on every admin page load
3. It checks each monitored plugin's search terms against the log entries
4. The admin bar indicator updates in real time — green means clean, red means errors found

## Admin bar indicator

The **LOG INSPECTOR** item in the admin bar shows the current status at a glance:

- **Green** — all monitored plugins are error-free
- **Red** — at least one monitored plugin has errors in the debug log
- **Gray** — `WP_DEBUG_LOG` is not enabled

Hovering over the indicator shows the most recent error message for quick diagnosis without leaving the page you are on.

## Key features

**Monitor any plugin** — Add any WordPress plugin to the watchlist through the settings UI. Not limited to a predefined list.

**No code editing required** — Add, edit, enable, disable, and delete monitored plugins entirely through the admin interface.

**Real-time status** — The admin bar updates on every page load, giving you an always-current view of plugin health.

**Plugin-specific tracking** — Each monitored plugin has its own status. You can see at a glance which specific plugin is generating errors.

**Auto-detection** — Optional setting to only monitor plugins that are currently active, keeping the watchlist clean.

**Configurable scan depth** — By default scans the last 300KB of the log. Adjustable in General Settings.

**Toggle monitoring** — Enable or disable monitoring per plugin without deleting it from the list.

**Multisite compatible** — Works on WordPress multisite networks.

**Lightweight** — Only runs in the admin area. No frontend impact.

## Documentation

- [Installation](installation.md)
- [Getting Started](getting-started.md)
- [Adding Plugins to Monitor](adding-plugins.md)
- [Admin Bar](admin-bar.md)
- [Settings](settings.md)
- [Testing the Plugin](testing.md)
- [FAQ](faq.md)
- [Changelog](changelog.md)
