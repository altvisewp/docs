# Installation

## Requirements

- WordPress 5.0 or higher
- PHP 7.0 or higher
- `WP_DEBUG` and `WP_DEBUG_LOG` enabled in `wp-config.php` (required for the plugin to function — see below)

## Method 1 — Install from WordPress dashboard (recommended)

1. Log in to your WordPress admin dashboard
2. Go to **Plugins → Add New**
3. Search for **Lumiblog Debug Log Inspector**
4. Click **Install Now** on the plugin by Patrick Lumumba
5. Click **Activate**

## Method 2 — Upload via WordPress dashboard

1. Download the plugin ZIP file from [WordPress.org](https://wordpress.org/plugins/lumiblog-debug-log-inspector/)
2. Go to **Plugins → Add New**
3. Click **Upload Plugin**
4. Select the ZIP file and click **Install Now**
5. Click **Activate Plugin**

## Method 3 — Manual FTP installation

1. Download and extract the plugin ZIP
2. Upload the `lumiblog-debug-log-inspector` folder to `/wp-content/plugins/`
3. Go to **Plugins → Installed Plugins** and click **Activate**

## Enable WordPress debug logging

The plugin requires WordPress debug logging to be active. Without it, there is no log to scan and the admin bar indicator will show gray.

Add these lines to your `wp-config.php` file **before** the line that says `/* That's all, stop editing! */`:

```php
define( 'WP_DEBUG', true );
define( 'WP_DEBUG_LOG', true );
define( 'WP_DEBUG_DISPLAY', false );
```

Setting `WP_DEBUG_DISPLAY` to `false` prevents raw error messages from appearing on the frontend — important on any site that real users visit.

After adding these lines, WordPress will begin writing errors to `wp-content/debug.log`.

**Note:** Only enable `WP_DEBUG` on development, staging, or testing environments. Avoid enabling it on live production sites unless you are actively debugging a specific issue.

## After activation

1. Go to **Settings → Log Inspector**
2. Add one or more plugins to monitor
3. Look for the **LOG INSPECTOR** indicator in the WordPress admin bar

See the [Getting Started](getting-started.md) guide for full setup instructions.

## Uninstalling

1. Go to **Plugins → Installed Plugins**
2. Click **Deactivate** under Lumiblog Debug Log Inspector
3. Click **Delete**

All plugin settings and monitored plugin configurations are removed from the database on deletion.
