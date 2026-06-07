# Adding Plugins to Monitor

## The monitored plugins list

The main area of **Settings → Log Inspector** shows all plugins currently being monitored. Each entry displays:

- Plugin name
- File path
- Search terms
- Current status (enabled or disabled)
- Action buttons — Edit, Delete, and toggle Enable/Disable

## Adding a new plugin

Click **Add New Plugin to Monitor** or scroll to the add form at the bottom of the settings page. Fill in the three required fields:

### Plugin Name

A label for your reference. This appears in the admin bar tooltip when errors are found. Use a name that clearly identifies the plugin.

Examples: `WooCommerce`, `Contact Form 7`, `My Custom Plugin`

### Plugin File Path

The path to the plugin's main PHP file, relative to the `wp-content/plugins/` directory. Format: `folder-name/main-file.php`

**How to find it:**
1. Go to **Plugins → Installed Plugins**
2. Look at the grey text below each plugin name — it shows the file path
3. Copy the folder and filename portion

Common examples:

| Plugin | File Path |
|---|---|
| WooCommerce | `woocommerce/woocommerce.php` |
| Contact Form 7 | `contact-form-7/wp-contact-form-7.php` |
| Yoast SEO | `wordpress-seo/wp-seo.php` |
| Elementor | `elementor/elementor.php` |

### Search Terms

A comma-separated list of keywords the plugin searches for in the debug log to identify errors originating from this plugin. The more specific your terms, the fewer false positives.

**Good search term strategies:**

- Use the plugin's folder name: `woocommerce`
- Use a unique function or class prefix: `wc_`, `cf7_`
- Use the plugin's namespace: `WC\\`, `ContactForm7`
- Use file path fragments that appear in stack traces: `woocommerce/includes`

**Example:** For WooCommerce, use `woocommerce, wc-` to catch both the plugin name and WooCommerce-prefixed function calls.

**Avoid:**
- Very short or common terms like `wp`, `admin`, `error` — these will match unrelated log entries
- Terms that appear in other active plugins

## Editing a monitored plugin

1. Find the plugin in the list on the settings page
2. Click the **Edit** button
3. Update any of the three fields
4. Click **Update Plugin** to save, or **Cancel** to discard changes

## Enabling and disabling monitoring

Each plugin in the list has an **Enable/Disable** toggle. Disabling a plugin removes it from active monitoring without deleting it from the list — useful when you want to temporarily stop watching a plugin without losing its configuration.

## Deleting a monitored plugin

Click **Delete** next to any plugin in the list to remove it permanently. This only removes it from the monitoring list — it does not affect the actual WordPress plugin in any way.

## Duplicate prevention

The plugin prevents you from adding the same plugin file path twice. If you attempt to add a plugin that is already in the list, you will see a warning and the duplicate will not be saved.

## Auto-detection mode

In **General Settings**, you can enable **Only monitor active plugins**. When this is on, plugins that are disabled in the WordPress plugins list are automatically hidden from monitoring, even if they are in your watchlist. This keeps the admin bar clean and prevents stale entries from showing false statuses.
