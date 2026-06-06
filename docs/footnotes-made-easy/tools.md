---
sidebar_label: "Tools"
sidebar_position: 4
description: "Export, import, reset, and manage your plugin settings."
---

# Tools

The Tools page provides utilities for managing your Footnotes Made Easy settings — including export, import, reset, and uninstall options.

Navigate to **Footnotes → Tools** to access these utilities.

## Export settings

Exports your current Footnotes Made Easy settings as a JSON file. The exported file can be used to:

- Back up your settings before making changes
- Copy your configuration to another WordPress site
- Share a settings configuration with a colleague or client

**To export:**

1. Go to **Footnotes → Tools**
2. Under **Export / Import settings**, click **Export settings**
3. A JSON file will download to your computer

The exported file is named `footnotes-made-easy-settings-{date}.json`.

## Import settings

Imports settings from a previously exported JSON file.

**To import:**

1. Go to **Footnotes → Tools**
2. Under **Export / Import settings**, click **Choose file**
3. Select a `.json` settings file exported from Footnotes Made Easy
4. Click **Import settings**
5. A confirmation prompt will appear — click **Import** to proceed

All current settings will be replaced with the imported values. This action cannot be undone. Export your current settings first if you want to preserve them.

**Note:** Only JSON files exported from Footnotes Made Easy are supported. Importing files from other plugins or manually edited JSON may produce unexpected results.

## Reset settings

Resets all Footnotes Made Easy settings to their factory defaults. This is useful when troubleshooting or starting fresh after experimenting with settings.

**To reset:**

1. Go to **Footnotes → Tools**
2. Under **Reset settings**, click **Reset to defaults**
3. A confirmation modal will appear asking you to confirm
4. Click **Reset** to proceed

All settings will be restored to their default values. This action cannot be undone.

## Data on uninstall

Controls what happens to your settings data when the plugin is deleted from WordPress.

### Preserve settings on uninstall

When this option is **enabled**, your settings are retained in the database even after the plugin is deleted. This means your configuration will be restored if you reinstall the plugin later.

When this option is **disabled** (the default), all plugin settings are permanently deleted from the database when the plugin is removed via **Plugins → Delete**.

**Recommendation:** Enable this option before deleting the plugin if you plan to reinstall it in the future, or if you want to keep a record of your settings.

## Multisite permissions

On WordPress multisite installations, a **Multisite permissions** section appears at the bottom of the Tools page for network administrators only. See [Multisite](multisite.md) for details.
