# Frequently Asked Questions

## General

### Does this plugin create separate categories for pages?

No. Page Categorizer uses the same existing category and tag taxonomies that WordPress already uses for posts. There is no separate set of categories for pages. Any category you create under **Posts → Categories** is immediately available for pages too.

### Will activating this plugin affect my existing post categories and tags?

No. The plugin only extends categories and tags to pages — it does not modify existing post categories or tags in any way. Your existing post taxonomies remain completely unaffected.

### Does it work with the block editor (Gutenberg)?

Yes. The Categories and Tags panels appear in the Gutenberg sidebar under the **Page** tab. If you do not see them, click the three-dot menu (⋮) at the top right of the editor → **Preferences → Panels** and enable them.

### Does it work with the Classic Editor?

Yes. The Categories and Tags meta boxes appear on the page editing screen. If they are not visible, click **Screen Options** at the top of the page and check the relevant checkboxes.

### Is there a settings page?

No. The plugin has no settings page and requires no configuration. Activate it and it works immediately.

## Categories and archives

### Will pages appear in my category archive pages?

Yes. Once you assign a category to a page, it will appear in that category's archive page (`/category/your-category/`) alongside any posts assigned to the same category.

### Will pages appear in my tag archive pages?

Yes. Pages assigned to a tag will appear on that tag's archive page (`/tag/your-tag/`) alongside posts.

### My category archive page is blank. What's wrong?

If the category archive page shows no results, check:

1. The page is published (not draft)
2. The category is correctly assigned and saved on the page
3. Your theme has an `archive.php` or `category.php` template that handles the archive display
4. There are no caching plugins serving a stale version of the archive page — clear your cache and try again

### Can I exclude pages from appearing in category archives?

Yes — by not assigning them to any category, or by using a custom query modification in your theme to filter page results from specific archives.

## Compatibility

### Will this work with my theme?

Yes. The plugin integrates at the WordPress core level using standard hooks and taxonomy registration. It is compatible with any theme that uses standard WordPress template hierarchy.

### Is it compatible with popular page builders like Elementor or Divi?

Yes. The plugin does not interfere with page builder functionality. Categories and tags are assigned through the standard WordPress admin interface and are independent of how the page content is built.

### Is it compatible with WooCommerce?

Yes, there are no known conflicts with WooCommerce.

### Will deactivating the plugin remove my category assignments?

No. Deactivating the plugin does not delete any data. Categories and tags previously assigned to pages remain in the database. Reactivating the plugin restores full functionality without any data loss. Deleting the plugin also does not remove taxonomy assignments.

## Support

### Where do I get support?

Support is available on the [WordPress.org support forum](https://wordpress.org/support/plugin/add-category-to-pages/).
