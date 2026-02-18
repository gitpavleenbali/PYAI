import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'openstackai',
  tagline: 'Build AI Agents in Python with Elegant Simplicity',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  // GitHub Pages deployment
  url: 'https://gitpavleenbali.github.io',
  baseUrl: '/PYAI/',
  organizationName: 'gitpavleenbali',
  projectName: 'PYAI',
  trailingSlash: false,

  onBrokenLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  // Enable Mermaid diagrams
  markdown: {
    mermaid: true,
    parseFrontMatter: async (params) => {
      const result = await params.defaultParseFrontMatter(params);
      return result;
    },
  },
  themes: ['@docusaurus/theme-mermaid'],

  // Client modules for mobile enhancements
  clientModules: [
    require.resolve('./src/theme/MobileDocsMenu.js'),
  ],

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/gitpavleenbali/PYAI/tree/master/website/',
          routeBasePath: 'docs',
        },
        blog: false, // Disable blog for now
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/openstackai-social-card.png',
    colorMode: {
      defaultMode: 'dark',
      respectPrefersColorScheme: true,
    },
    docs: {
      sidebar: {
        hideable: true,
        autoCollapseCategories: true,
      },
    },
    announcementBar: {
      id: 'v0.6.0',
      content: '🚀 openstackai v0.6.0 is out! <a href="/PYAI/docs/Changelog">See what\'s new</a>',
      backgroundColor: '#6366f1',
      textColor: '#ffffff',
      isCloseable: true,
    },
    navbar: {
      title: 'openstackai',
      hideOnScroll: true,
      logo: {
        alt: 'openstackai Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'docsSidebar',
          position: 'left',
          label: 'Documentation',
        },
        {
          to: '/docs/API-Reference',
          label: 'API',
          position: 'left',
        },
        {
          to: '/docs/examples',
          label: 'Examples',
          position: 'left',
        },
        {
          href: 'https://pypi.org/project/openstackai/',
          label: 'PyPI',
          position: 'right',
        },
        {
          href: 'https://github.com/gitpavleenbali/PYAI',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Learn',
          items: [
            { label: 'Quick Start', to: '/docs/quickstart' },
            { label: 'Installation', to: '/docs/Installation' },
            { label: 'Configuration', to: '/docs/Configuration' },
          ],
        },
        {
          title: 'API',
          items: [
            { label: 'Easy API', to: '/docs/Easy-Module' },
            { label: 'Agent API', to: '/docs/Agent' },
            { label: 'Runner', to: '/docs/Runner' },
          ],
        },
        {
          title: 'Community',
          items: [
            { label: 'GitHub', href: 'https://github.com/gitpavleenbali/PYAI' },
            { label: 'Issues', href: 'https://github.com/gitpavleenbali/PYAI/issues' },
            { label: 'Discussions', href: 'https://github.com/gitpavleenbali/PYAI/discussions' },
          ],
        },
        {
          title: 'More',
          items: [
            { label: 'Changelog', to: '/docs/Changelog' },
            { label: 'Contributing', to: '/docs/Contributing' },
            { label: 'License', href: 'https://github.com/gitpavleenbali/PYAI/blob/master/LICENSE' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} openstackai Contributors. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['python', 'bash', 'yaml', 'json', 'toml'],
    },
    mermaid: {
      theme: { light: 'neutral', dark: 'dark' },
    },
    algolia: undefined, // Can add Algolia search later
  } satisfies Preset.ThemeConfig,
};

export default config;
