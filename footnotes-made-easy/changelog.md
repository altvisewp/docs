# Changelog

All notable changes to Footnotes Made Easy are documented here. Dates are in YYYY-MM-DD format.

## 3.2.0 — 2026-07-30

### Added
- Complete admin UI redesign — new tabbed settings interface, Dashboard, Tools, and Get Help pages
- Export and import settings as JSON
- Factory reset — restore all settings to defaults from the Tools page
- Suppress footnotes on specific URLs via the Suppress tab
- Suppress footnotes by post type
- Custom header and footer text for the footnotes list
- Preserve settings on uninstall option
- Welcome modal — shown once on fresh install or plugin update
- Deactivation survey — optional feedback when deactivating the plugin
- Multisite support — network-managed mode and subsite override mode
- Pro Coming Soon page — in-plugin preview of upcoming Pro features
- Upgrade to Pro menu item with direct link to coming soon page

### Changed
- Settings page moved from WordPress Settings to a dedicated top-level Footnotes menu
- All admin pages now use a consistent layout with a topbar, content area, sidebar, and footer
- Minimum WordPress version raised to 6.0
- Minimum PHP version raised to 7.4

### Fixed
- Replaced `parse_url()` with `wp_parse_url()` for cross-version PHP compatibility
- All function names and variable names PHPCS-compliant

## 3.1.0

### Added
- Basic settings page under WordPress Settings
- Configurable identifier style (decimal, alpha, roman)
- Tooltip support
- Back link configuration

### Fixed
- Various compatibility fixes for WordPress 6.x

## 3.0.0

- Initial public release on WordPress.org
