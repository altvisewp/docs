# Frequently Asked Questions — Pro

## Installation and licensing

### Do I need the free plugin to use Pro?

Yes. Footnotes Made Easy Pro is an add-on that requires the free Footnotes Made Easy plugin to be installed and active. Installing Pro without the free plugin will trigger an error notice and the Pro plugin will deactivate itself automatically.

### How many sites can I use Pro on?

- **Personal license** — 1 site
- **Professional license** — 3 sites

Each site is one WordPress installation. A WordPress multisite network counts as one site regardless of the number of subsites.

### Can I use my license on a staging site?

Staging and development sites count toward your activation limit. If you need an additional activation for a staging environment, contact us at [altvisewp.com/support](https://altvisewp.com/support/) and we can accommodate reasonable requests.

### My license key is not working. What should I check?

- Confirm the key is entered without extra spaces before or after
- Confirm your license has not expired in your [account dashboard](https://altvisewp.com/my-account/)
- Confirm you have not exceeded your activation limit
- Confirm the free plugin is installed and active
- If the issue persists, contact [altvisewp.com/support](https://altvisewp.com/support/)

### What happens when my license expires?

When an annual license expires, Pro features continue to work — your published footnotes and citations are not affected. However, you will no longer receive automatic plugin updates or have access to support. Renew your license at [altvisewp.com/my-account/](https://altvisewp.com/my-account/).

---

## Citations

### Which citation styles are supported?

APA 7th edition, MLA 9th edition, and Chicago 17th edition (Notes-Bibliography system).

### Can I use different citation styles on different posts?

Yes. You can set a site-wide default style under **Footnotes Settings → Citations** and override it on individual posts from the Gutenberg sidebar.

### How accurate is the auto-generated citation formatting?

The plugin follows current edition guidelines for each style. For formal academic submission (journals, theses, dissertations), we recommend verifying citations against the official style manual, as edge cases and discipline-specific conventions may apply.

### DOI auto-fetch is not working. What should I check?

- Confirm the DOI is entered correctly — DOIs typically start with `10.` followed by a registrant code
- Confirm your WordPress server has outbound internet access (some hosting environments restrict this)
- Try the ISBN auto-fetch if you have the book's ISBN as an alternative

### Can I mix citations and plain footnotes in the same post?

Yes. Some footnotes in a post can be formatted as citations while others are plain text. Each footnote is handled independently.

### The citation style changed site-wide and now some citations look wrong. Why?

Different citation styles have different field requirements. If you switch from APA to Chicago, for example, some fields may be formatted differently or additional fields (like place of publication) may now be included or excluded. Review the affected citations and update any missing fields for the new style.

---

## Footnote Library

### Is the Library shared across all posts?

Yes. The Library is site-wide. Any footnote saved to the Library is available for insertion in any post or page on the site.

### If I edit a Library entry, does it update in posts where I already used it?

No. When you insert a Library footnote into a post, the content is copied to that post at the time of insertion. Subsequent changes to the Library entry do not affect posts that already used it.

### Can I import my Library from another site?

Yes. Export the Library from the source site (**Footnotes → Library → Export**) and import the JSON file on the destination site (**Footnotes → Library → Import**).

---

## Gutenberg sidebar

### The Footnotes panel is not showing in the sidebar. What should I do?

- Confirm your Pro license is active under **Footnotes → License**
- Refresh the editor page
- Check that the panel has not been manually hidden — click the three-dot menu at the top of the sidebar and look for Footnotes in the panel options
- If the issue persists, deactivate and reactivate the Pro plugin

### Does the sidebar work with the Classic Editor?

No. The Gutenberg sidebar is only available in the block editor. If you use the Classic Editor, footnotes can still be added manually using the `(( ))` syntax.

### Does the sidebar work with full-site editing (FSE)?

The sidebar is available for post and page editing. Full-site editing templates are not currently supported.

---

## Support

### How do I get support?

Submit a support request at [altvisewp.com/support](https://altvisewp.com/support/). Support is available to all users with an active Pro license. We aim to respond within 2 business days.

### Is support available for the free plugin?

Support for the free plugin is provided on a best-effort basis through the [WordPress.org support forum](https://wordpress.org/support/plugin/footnotes-made-easy/). It is not covered by the Pro support terms.
