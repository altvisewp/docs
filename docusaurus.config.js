// @ts-check

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'AltviseWP Docs',
  tagline: 'Official documentation for all AltviseWP WordPress plugins and products.',
  favicon: 'img/favicon.ico',

  url: 'https://docs.altvisewp.com',
  baseUrl: '/',

  organizationName: 'altvisewp',
  projectName: 'docs',
  trailingSlash: false,

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          routeBasePath: '/',
          editUrl: 'https://github.com/altvisewp/docs/edit/main/',
          showLastUpdateTime: true,
          showLastUpdateAuthor: false,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  plugins: [
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {
        hashed: true,
        indexDocs: true,
        indexPages: false,
        docsRouteBasePath: '/',
        searchResultLimits: 8,
        searchResultContextMaxLength: 50,
        highlightSearchTermsOnTargetPage: true,
        explicitSearchResultPath: true,
      },
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },

      image: 'img/social-card.png',

      navbar: {
        title: 'AltviseWP Docs',
        logo: {
          alt: 'AltviseWP Logo',
          src: 'img/logo.svg',
          srcDark: 'img/logo-dark.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'fmeSidebar',
            position: 'left',
            label: 'Footnotes Made Easy',
          },
          {
            type: 'docSidebar',
            sidebarId: 'accountSidebar',
            position: 'left',
            label: 'Account',
          },
          {
            href: 'https://altvisewp.com',
            label: 'altvisewp.com',
            position: 'right',
          },
          {
            href: 'https://github.com/altvisewp/docs',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },

      footer: {
        style: 'dark',
        links: [
          {
            title: 'Footnotes Made Easy',
            items: [
              { label: 'Overview',        to: '/footnotes-made-easy' },
              { label: 'Installation',    to: '/footnotes-made-easy/installation' },
              { label: 'Getting Started', to: '/footnotes-made-easy/getting-started' },
              { label: 'FAQ',             to: '/footnotes-made-easy/faq' },
            ],
          },
          {
            title: 'Account',
            items: [
              { label: 'Managing Your License', to: '/account/managing-your-license' },
              { label: 'Billing and Renewals',  to: '/account/billing-and-renewals' },
              { label: 'Refunds',               to: '/account/refunds' },
            ],
          },
          {
            title: 'AltviseWP',
            items: [
              { label: 'Website',        href: 'https://altvisewp.com' },
              { label: 'Support',        href: 'https://altvisewp.com/support/' },
              { label: 'GitHub',         href: 'https://github.com/altvisewp' },
              { label: 'Privacy Policy', href: 'https://altvisewp.com/privacy/' },
              { label: 'Terms of Service', href: 'https://altvisewp.com/terms/' },
            ],
          },
        ],
        copyright: `© ${new Date().getFullYear()} AltviseWP, LLC. Built with Docusaurus.`,
      },

      prism: {
        theme: require('prism-react-renderer').themes.github,
        darkTheme: require('prism-react-renderer').themes.dracula,
        additionalLanguages: ['php', 'bash', 'json', 'yaml'],
      },
    }),
};

module.exports = config;
