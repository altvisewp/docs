# Use Cases

Page Categorizer is a flexible tool with a range of practical applications. Here are the most common ways to use it.

## Category-based page listing

Use a category to group related pages and then display them as a list using WordPress's built-in `get_posts()` or `WP_Query` with a `category_name` argument.

**Example — list all pages in the "Services" category:**

```php
$pages = get_posts([
    'post_type'      => 'page',
    'category_name'  => 'services',
    'posts_per_page' => -1,
]);

foreach ($pages as $page) {
    echo '<a href="' . get_permalink($page) . '">' . $page->post_title . '</a>';
}
```

## Category archive for pages

Once pages are assigned to a category, they automatically appear on the category archive page (`/category/your-category/`) alongside any posts in that category. This allows you to build navigation-driven sites where visitors browse by topic rather than post type.

## Hiding pages from certain sections

By assigning a specific category to pages you want to exclude, you can use conditional logic in your theme to suppress them from certain areas of the site — navigation menus, search results, or front-page queries.

**Example — exclude pages in the "draft-review" category from search:**

```php
function exclude_review_pages_from_search($query) {
    if ($query->is_search() && $query->is_main_query()) {
        $query->set('category__not_in', [get_cat_ID('draft-review')]);
    }
}
add_action('pre_get_posts', 'exclude_review_pages_from_search');
```

## Tag-based page discovery

Tagging pages makes them discoverable through tag archive pages and tag-based search. This is useful for content-heavy sites where visitors search by keyword.

For example, a government or NGO site might tag pages with topics like `housing`, `health`, or `education`, allowing visitors to find all relevant pages through a single tag archive.

## Creating a knowledge base structure

Assign pages to categories to create a structured knowledge base or documentation section. Visitors can browse by category to find related articles and pages without needing a dedicated knowledge base plugin.

## Embedding a category-based page list with a shortcode

You can create a simple shortcode in your theme's `functions.php` to embed a list of pages from a given category anywhere in your content:

```php
function pages_by_category_shortcode($atts) {
    $atts = shortcode_atts(['category' => ''], $atts);
    if (!$atts['category']) return '';

    $pages = get_posts([
        'post_type'      => 'page',
        'category_name'  => $atts['category'],
        'posts_per_page' => -1,
    ]);

    $output = '<ul>';
    foreach ($pages as $page) {
        $output .= '<li><a href="' . get_permalink($page) . '">' . $page->post_title . '</a></li>';
    }
    $output .= '</ul>';

    return $output;
}
add_shortcode('pages_by_category', 'pages_by_category_shortcode');
```

Usage: `[pages_by_category category="services"]`
