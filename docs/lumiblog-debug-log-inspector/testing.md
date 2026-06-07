# Testing the Plugin

This guide walks you through verifying that Lumiblog Debug Log Inspector is correctly detecting errors. Useful after initial setup or after any configuration changes.

## Prerequisites

- `WP_DEBUG` and `WP_DEBUG_LOG` are enabled in `wp-config.php`
- At least one plugin is added to the monitored list
- The admin bar indicator is visible (not gray)

## Step 1 — Confirm debug logging is active

Check that `wp-content/debug.log` exists on your server. If it does not, either no errors have occurred yet or `WP_DEBUG_LOG` is not enabled.

You can trigger a harmless log entry by temporarily adding this to your theme's `functions.php`:

```php
error_log( 'Debug logging test — ' . date('Y-m-d H:i:s') );
```

Reload any admin page, then check `wp-content/debug.log` via your file manager or FTP. You should see the test message. Remove the line from `functions.php` once confirmed.

## Step 2 — Add a plugin to monitor

If you have not already done so:

1. Go to **Settings → Log Inspector**
2. Click **Add New Plugin to Monitor**
3. Fill in a plugin you have installed, for example:
   - **Plugin Name:** `WooCommerce`
   - **Plugin File Path:** `woocommerce/woocommerce.php`
   - **Search Terms:** `woocommerce, wc-`
4. Click **Add Plugin**

## Step 3 — Generate a test error

To confirm error detection is working, temporarily add a code snippet to any active plugin's main PHP file that triggers a PHP warning.

**Note:** This test requires PHP 8.4 or higher on your server.

Add this to any active plugin's main file (remove it immediately after testing):

```php
/**
 * DEBUG LOG INSPECTOR TEST — REMOVE AFTER TESTING
 */
add_action( 'load-index.php', function() {
    if ( version_compare( PHP_VERSION, '8.4.0', '>=' ) ) {
        $test_array = array( 'name' => 'Debug Log Inspector' );
        $undefined_value = $test_array['email']; // Triggers undefined key warning
        error_log( '[DLI-TEST] PHP 8.4 warning triggered for testing purposes!' );
    }
} );
```

Make sure the search terms for the plugin you are monitoring would match this log entry. If you are using this to test the inspector itself, add `DLI-TEST` as a search term to the plugin you configured in Step 2.

## Step 4 — Trigger the error

1. Save the modified plugin file
2. Reload the WordPress admin dashboard (`/wp-admin/`)
3. The error is triggered and written to `debug.log`
4. The admin bar indicator should turn **red**

## Step 5 — Verify the result

- The admin bar shows a red **LOG INSPECTOR** indicator
- Hovering over it shows the most recent error message

## Step 6 — Clean up

1. Remove the test code snippet from the plugin file
2. Delete or clear the contents of `wp-content/debug.log`
3. Reload any admin page — the indicator should return to green

## Troubleshooting test failures

**Admin bar still green after adding test code:**
- Confirm the search terms you set for the monitored plugin match text in the log entry. The test code above logs `[DLI-TEST]` — make sure your search terms include something from that string
- Confirm the error was actually written — check `wp-content/debug.log` directly
- Confirm the plugin's monitoring is enabled (not toggled off)

**Admin bar is gray:**
- `WP_DEBUG_LOG` is not enabled — see [Installation](installation.md)

**Error log is empty:**
- The PHP version on your server may be below 8.4. Try using `trigger_error('Test error', E_USER_WARNING);` instead of the array access approach
