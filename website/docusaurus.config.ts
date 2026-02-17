import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'PyAI',
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
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  // Enable Mermaid diagrams
  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],

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
    image: 'img/pyai-social-card.png',
    colorMode: {
      defaultMode: 'dark',
      respectPrefersColorScheme: true,
    },
    announcementBar: {
      id: 'v0.5.1',
      content: '🚀 PyAI v0.5.1 is out! <a href="/PYAI/docs/changelog">See what\'s new</a>',
      backgroundColor: '#6366f1',
      textColor: '#ffffff',
      isCloseable: true,
    },
    navbar: {
      title: 'PyAI',
      logo: {
        alt: 'PyAI Logo',
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
          to: '/docs/api-reference',
          label: 'API',
          position: 'left',
        },
        {
          to: '/docs/examples',
          label: 'Examples',
          position: 'left',
        },
        {
          href: 'https://pypi.org/project/pyai/',
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
            { label: 'Installation', to: '/docs/installation' },
            { label: 'Configuration', to: '/docs/configuration' },
          ],
        },
        {
          title: 'API',
          items: [
            { label: 'Easy API', to: '/docs/easy-api' },
            { label: 'Agent API', to: '/docs/agent' },
            { label: 'Runner', to: '/docs/runner' },
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
            { label: 'Changelog', to: '/docs/changelog' },
            { label: 'Contributing', to: '/docs/contributing' },
            { label: 'License', href: 'https://github.com/gitpavleenbali/PYAI/blob/master/LICENSE' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} PyAI Contributors. Built with Docusaurus.`,
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
