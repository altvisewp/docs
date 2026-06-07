# Getting Started

Page Categorizer requires no setup. This guide covers the basic workflow for assigning categories and tags to pages.

## Assigning a category to a page

1. Go to **Pages → All Pages** in your WordPress admin
2. Click on any page to edit it
3. In the **Gutenberg block editor** — look for the **Categories** panel in the right-hand sidebar under the **Page** tab. If you do not see it, click the three-dot menu (⋮) at the top right → **Preferences → Panels** and enable Categories.
4. In the **Classic Editor** — look for the **Categories** meta box below or beside the editor. If it is not visible, click **Screen Options** at the top of the screen and check the **Categories** checkbox.
5. Check one or more categories to assign them to the page
6. Click **Update** or **Publish** to save

## Assigning a tag to a page

1. Open a page for editing
2. In the **Gutenberg editor** — find the **Tags** panel in the right-hand sidebar under the **Page** tab
3. In the **Classic Editor** — find the **Tags** meta box in the sidebar
4. Type a tag name and press Enter, or select from existing tags
5. Click **Update** or **Publish** to save

## Creating new categories for pages

Page Categorizer uses the same categories as posts — there is no separate set of page categories. To create a new category:

1. Go to **Posts → Categories**
2. Add a new category as you normally would
3. The new category is immediately available on both Posts and Pages

## Viewing pages in category archives

After assigning categories to pages, visit the category archive URL to confirm pages appear:

```
https://yoursite.com/category/your-category/
```

Pages assigned to that category will appear in the archive listing alongside any posts in the same category.

## Viewing pages in tag archives

Similarly, tag archive pages include assigned pages:

```
https://yoursite.com/tag/your-tag/
```

## Adding a Categories link to the admin menu

After activating Page Categorizer, a **Categories** link appears under **Pages** in the WordPress admin sidebar. This lets you manage categories specifically in the context of your pages, though it uses the same shared category taxonomy as posts.
