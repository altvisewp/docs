/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {

  fmeSidebar: [
    {
      type: 'doc',
      id: 'footnotes-made-easy/index',
      label: 'Overview',
    },
    {
      type: 'doc',
      id: 'footnotes-made-easy/installation',
      label: 'Installation',
    },
    {
      type: 'doc',
      id: 'footnotes-made-easy/getting-started',
      label: 'Getting Started',
    },
    {
      type: 'category',
      label: 'Settings',
      collapsed: false,
      items: [
        'footnotes-made-easy/settings/display',
        'footnotes-made-easy/settings/behaviour',
        'footnotes-made-easy/settings/suppress',
        'footnotes-made-easy/settings/advanced',
      ],
    },
    {
      type: 'doc',
      id: 'footnotes-made-easy/tools',
      label: 'Tools',
    },
    {
      type: 'doc',
      id: 'footnotes-made-easy/multisite',
      label: 'Multisite',
    },
    {
      type: 'doc',
      id: 'footnotes-made-easy/faq',
      label: 'FAQ',
    },
    {
      type: 'doc',
      id: 'footnotes-made-easy/changelog',
      label: 'Changelog',
    },
    {
      type: 'category',
      label: '⚡ Pro',
      collapsed: false,
      items: [
        'footnotes-made-easy/pro-installation',
        'footnotes-made-easy/pro-license-activation',
        {
          type: 'category',
          label: 'Citations',
          collapsed: false,
          items: [
            'footnotes-made-easy/pro-citations-overview',
            'footnotes-made-easy/pro-citations-source-types',
            'footnotes-made-easy/pro-citations-styles',
          ],
        },
        'footnotes-made-easy/pro-library',
        'footnotes-made-easy/pro-gutenberg-sidebar',
        'footnotes-made-easy/pro-faq',
      ],
    },
  ],

  accountSidebar: [
    {
      type: 'doc',
      id: 'account/managing-your-license',
      label: 'Managing Your License',
    },
    {
      type: 'doc',
      id: 'account/billing-and-renewals',
      label: 'Billing and Renewals',
    },
    {
      type: 'doc',
      id: 'account/refunds',
      label: 'Refunds',
    },
  ],

};

module.exports = sidebars;
