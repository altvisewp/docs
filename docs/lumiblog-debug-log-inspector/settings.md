# Settings

Navigate to **Settings → Log Inspector** to access all plugin configuration options.

## General Settings

### Log scan depth

**Default:** 300KB

Controls how much of the `debug.log` file is read on each admin page load. The plugin reads from the end of the file (the most recent entries) up to this limit.

Increasing this value lets you catch errors that happened further back in time but uses slightly more memory per page load. Decreasing it reduces memory usage but may miss older errors.

For most sites, the default 300KB covers several hours to days of log history depending on how active your site is.

### Only monitor active plugins

**Default:** Off

When enabled, the plugin automatically ignores any plugin in your watchlist that is currently deactivated in WordPress. This prevents deactivated plugins from triggering false positives or cluttering the admin bar tooltip.

Useful for sites where you frequently activate and deactivate plugins during development or testing.

## Monitored plugins

The monitored plugins section lists all plugins currently in your watchlist. Each row shows:

| Column | Description |
|---|---|
| Plugin Name | The label you set when adding the plugin |
| File Path | The plugin's main file path |
| Search Terms | Keywords used to match log entries |
| Status | Whether monitoring is currently enabled for this plugin |
| Actions | Edit, Delete, Enable/Disable |

## Add New Plugin to Monitor

The form at the bottom of the settings page (or via the **Add New Plugin** button) adds a plugin to the watchlist. See [Adding Plugins to Monitor](adding-plugins.md) for full details on each field.

## Edit Plugin

Clicking **Edit** on any monitored plugin opens an edit form pre-filled with the plugin's current values. Make your changes and click **Update Plugin**. Click **Cancel** to discard changes and return to the list.

## Accessing the settings page

The settings page is available at **Settings → Log Inspector** in the WordPress admin. It is only accessible to users with the `manage_options` capability (Administrator role by default).
