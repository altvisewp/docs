---
sidebar_label: "Multisite"
sidebar_position: 5
description: "Configure Footnotes Made Easy on WordPress multisite networks."
---

# Multisite

Footnotes Made Easy supports WordPress multisite installations. Network administrators can control whether subsite admins can manage their own footnote settings or whether settings are managed centrally from the network admin.

## Overview

On a multisite installation, the plugin can operate in two modes:

- **Allow subsite override** — each subsite admin can manage their own Footnotes Made Easy settings independently. Network defaults apply as starting values but can be changed per subsite.
- **Network managed** — all settings are controlled from the network admin. The Footnotes menu is hidden from subsite admins entirely.

## Configuring multisite mode

1. Log in to your **Network Admin** dashboard (`/wp-admin/network/`)
2. Go to **Footnotes → Tools**
3. Scroll to the **Multisite permissions** section
4. Select your preferred mode
5. Click **Save**

The Multisite permissions section is only visible to super admins and only appears in the network admin — not on individual subsites.

## Allow subsite override mode

In this mode:

- Subsite admins see the full Footnotes menu on their own site
- Each subsite can have its own display, behaviour, suppress, and advanced settings
- Network defaults serve as the starting configuration for new subsites
- The License page is hidden from subsite admins

This mode is recommended for multisite networks where each subsite operates independently and has its own content style.

## Network managed mode

In this mode:

- The Footnotes menu is hidden from all regular admin screens — including the main site and all subsites — for all users, including super admins
- All footnote settings are managed exclusively from the network admin
- Subsite admins have no access to footnote configuration
- All subsites use the same settings

This mode is recommended for networks where a central administrator manages all sites, such as an agency managing client sites or a university managing department sites.

## Upgrade to Pro visibility

The **Upgrade to Pro** card and related upsell elements are only shown in the network admin to super admins. Subsite admins never see upgrade prompts regardless of the multisite mode.

## Pro plugin on multisite

When Footnotes Made Easy Pro is installed on a multisite network:

- The Library and License menu items are only accessible from the network admin
- Subsite admins see the Citations lock screen with a message directing them to contact the network administrator to activate the license
- The Gutenberg sidebar is available on all subsites once the license is activated at the network level

## Per-subsite settings (override mode)

When operating in override mode, each subsite's settings are stored independently. Changing settings on one subsite does not affect any other subsite or the network defaults.

To reset a subsite to the network defaults, use the **Factory reset** option under **Footnotes → Tools** on that subsite.
