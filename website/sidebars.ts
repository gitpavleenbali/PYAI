import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  docsSidebar: [
    // ==================== GETTING STARTED ====================
    {
      type: 'category',
      label: '🚀 Getting Started',
      collapsed: false,
      items: [
        'index',
        'quickstart',
        'Installation',
        'Configuration',
        'Design-Philosophy',
        'Three-Dimensions',
      ],
    },

    // ==================== EASY API (One-Liners) ====================
    {
      type: 'category',
      label: '⚡ Easy API',
      collapsed: false,
      items: [
        'Easy-Module',
        'ask',
        'chat',
        'summarize',
        'analyze',
        'extract',
        'translate',
        'code',
        'generate',
        'fetch',
        'research',
        'rag',
      ],
    },

    // ==================== CORE CONCEPTS ====================
    {
      type: 'category',
      label: '🤖 Core Concepts',
      items: [
        'Core-Module',
        'Agent',
        'Runner',
        'Runner-Module',
        'Memory',
        'Sessions',
        'Sessions-Module',
        'LLM-Providers',
      ],
    },

    // ==================== TOOLS & SKILLS ====================
    {
      type: 'category',
      label: '🔧 Tools & Skills',
      items: [
        'Skills-Module',
        'Creating-Tools',
        'Built-in-Skills',
        {
          type: 'category',
          label: 'OpenAPI Integration',
          items: [
            'OpenAPI-Tools',
            'OpenAPI-Module',
            'OpenAPIParser',
            'OpenAPIClient',
          ],
        },
      ],
    },

    // ==================== MULTI-AGENT ====================
    {
      type: 'category',
      label: '👥 Multi-Agent',
      items: [
        'Blueprint-Module',
        'Workflows',
        'Orchestration-Patterns',
        'Handoffs',
        'Software-Factories',
        'Synthesis',
      ],
    },

    // ==================== A2A PROTOCOL ====================
    {
      type: 'category',
      label: '🔗 A2A Protocol',
      items: [
        'A2A-Protocol',
        'A2A-Module',
        'A2AServer',
        'A2AClient',
      ],
    },

    // ==================== PLUGINS ====================
    {
      type: 'category',
      label: '🔌 Plugins',
      items: [
        'Plugins-Module',
        'PluginBase',
        'PluginRegistry',
      ],
    },

    // ==================== KERNEL & REGISTRY ====================
    {
      type: 'category',
      label: '⚙️ Kernel & Registry',
      items: [
        'Kernel-Module',
        'Kernel-Registry',
      ],
    },

    // ==================== VECTOR DATABASES ====================
    {
      type: 'category',
      label: '📊 Vector Databases',
      items: [
        'Vector-Database',
        'VectorDB-Module',
        'ChromaDB',
        'Pinecone',
        'Qdrant',
        'Weaviate',
      ],
    },

    // ==================== MULTIMODAL ====================
    {
      type: 'category',
      label: '🎨 Multimodal',
      items: [
        'Multimodal',
        'Multimodal-Module',
        'ImageContent',
        'AudioContent',
        'VideoContent',
        'Transcription',
      ],
    },

    // ==================== VOICE ====================
    {
      type: 'category',
      label: '🎤 Voice',
      items: [
        'Voice',
        'Voice-Module',
        'VoiceSession',
      ],
    },

    // ==================== EVALUATION ====================
    {
      type: 'category',
      label: '📈 Evaluation',
      items: [
        'Evaluation',
        'Evaluation-Module',
        'Evaluator',
        'EvalSet',
        'TestCase',
      ],
    },

    // ==================== SAFETY & OBSERVABILITY ====================
    {
      type: 'category',
      label: '🛡️ Safety & Observability',
      items: [
        'Guardrails',
        'Tracing',
      ],
    },

    // ==================== AZURE ====================
    {
      type: 'category',
      label: '☁️ Azure',
      items: [
        'azure-setup',
        'Azure-AD-Auth',
      ],
    },

    // ==================== REFERENCE ====================
    {
      type: 'category',
      label: '📚 Reference',
      items: [
        'API-Reference',
        'Architecture',
        'examples',
      ],
    },

    // ==================== DEVELOPMENT ====================
    {
      type: 'category',
      label: '🛠️ Development',
      items: [
        'Contributing',
        'Changelog',
      ],
    },
  ],
};

export default sidebars;
