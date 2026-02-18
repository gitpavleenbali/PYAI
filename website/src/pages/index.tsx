import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import CodeBlock from '@theme/CodeBlock';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className={styles.heroBackground}></div>
      <div className="container">
        <div className={styles.heroContent}>
          <span className={styles.heroLabel}>🐍 Python SDK for AI Agents</span>
          <Heading as="h1" className={styles.heroTitle}>
            Build AI Agents<br />
            <span className={styles.heroGradient}>That Actually Work</span>
          </Heading>
          <p className={styles.heroSubtitle}>
            Three lines of code. Any LLM provider. Production-ready multi-agent workflows.
          </p>
          <div className={styles.heroButtons}>
            <Link className={clsx('button button--lg', styles.primaryButton)} to="/docs/quickstart">
              Get Started
            </Link>
            <Link className={clsx('button button--lg', styles.secondaryButton)} href="https://github.com/gitpavleenbali/PYAI">
              <span className={styles.githubIcon}>⭐</span> Star on GitHub
            </Link>
          </div>
          <div className={styles.installBox}>
            <code className={styles.installCode}>pip install openstackai</code>
            <button className={styles.copyButton} title="Copy to clipboard">📋</button>
          </div>
        </div>
      </div>
    </header>
  );
}

const codeExamples = {
  simple: `from openstackai import ask, summarize, research

# One-liner AI calls
answer = ask("What is machine learning?")
summary = summarize("Long document text...")
report = research("Latest AI trends 2026")`,

  agent: `from openstackai import Agent, Runner

# Create an AI agent
agent = Agent(
    name="Assistant",
    instructions="You are a helpful AI assistant."
)

# Run synchronously  
result = Runner.run_sync(agent, "Hello!")
print(result.final_output)`,

  multiagent: `from openstackai import Agent, Runner
from openstackai.blueprint import ChainWorkflow

# Multi-agent workflow
researcher = Agent(name="Researcher", instructions="Research topics")
writer = Agent(name="Writer", instructions="Write articles")

workflow = ChainWorkflow([researcher, writer])
result = Runner.run_sync(workflow, "AI in healthcare")`,
};

function CodeShowcase() {
  return (
    <section className={styles.codeShowcase}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <span className={styles.sectionLabel}>Write Less, Build More</span>
          <Heading as="h2" className={styles.sectionTitle}>
            From Zero to AI Agent in <span className={styles.highlight}>3 Lines</span>
          </Heading>
        </div>
        <div className={styles.codeGrid}>
          <div className={styles.codeCard}>
            <div className={styles.codeCardHeader}>
              <span className={styles.codeCardIcon}>⚡</span>
              <h3>Simple API</h3>
            </div>
            <CodeBlock language="python">{codeExamples.simple}</CodeBlock>
          </div>
          <div className={styles.codeCard}>
            <div className={styles.codeCardHeader}>
              <span className={styles.codeCardIcon}>🤖</span>
              <h3>Agent API</h3>
            </div>
            <CodeBlock language="python">{codeExamples.agent}</CodeBlock>
          </div>
          <div className={styles.codeCard}>
            <div className={styles.codeCardHeader}>
              <span className={styles.codeCardIcon}>👥</span>
              <h3>Multi-Agent</h3>
            </div>
            <CodeBlock language="python">{codeExamples.multiagent}</CodeBlock>
          </div>
        </div>
      </div>
    </section>
  );
}

type FeatureItem = {
  title: string;
  icon: string;
  description: string;
  color: string;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Simple by Design',
    icon: '🎯',
    description: 'One-liner APIs like ask(), summarize(), research(). No boilerplate, just results.',
    color: '#6366f1',
  },
  {
    title: 'Multi-Provider',
    icon: '🔌',
    description: 'OpenAI, Azure OpenAI, Anthropic, Ollama, Gemini - switch with one line.',
    color: '#8b5cf6',
  },
  {
    title: 'Multi-Agent',
    icon: '👥',
    description: 'Chain, supervisor, and custom orchestration patterns out of the box.',
    color: '#a855f7',
  },
  {
    title: 'Enterprise Ready',
    icon: '🏢',
    description: 'Azure AD auth, sessions, guardrails, tracing, and evaluation built-in.',
    color: '#ec4899',
  },
  {
    title: 'Extensible',
    icon: '🧩',
    description: 'Custom skills, OpenAPI tools, A2A protocol, and plugin architecture.',
    color: '#f43f5e',
  },
  {
    title: 'RAG & Vector DBs',
    icon: '📊',
    description: 'ChromaDB, Pinecone, Qdrant, Weaviate - connect your knowledge base.',
    color: '#f97316',
  },
];

function Feature({title, icon, description, color}: FeatureItem) {
  return (
    <div className={styles.featureCard}>
      <div className={styles.featureIcon} style={{background: `${color}20`, color}}>{icon}</div>
      <h3 className={styles.featureTitle}>{title}</h3>
      <p className={styles.featureDescription}>{description}</p>
    </div>
  );
}

function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <span className={styles.sectionLabel}>What It Does</span>
          <Heading as="h2" className={styles.sectionTitle}>
            Everything You Need to Build <span className={styles.highlight}>AI Agents</span>
          </Heading>
        </div>
        <div className={styles.featureGrid}>
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}

const integrations = [
  { name: 'OpenAI', emoji: '🤖' },
  { name: 'Azure', emoji: '☁️' },
  { name: 'Anthropic', emoji: '🧠' },
  { name: 'Ollama', emoji: '🦙' },
  { name: 'ChromaDB', emoji: '🔮' },
  { name: 'Pinecone', emoji: '🌲' },
  { name: 'Qdrant', emoji: '🎯' },
  { name: 'Weaviate', emoji: '🕸️' },
];

function IntegrationsSection() {
  return (
    <section className={styles.integrations}>
      <div className="container">
        <div className={styles.sectionHeader}>
          <span className={styles.sectionLabel}>Works With Everything</span>
          <Heading as="h2" className={styles.sectionTitle}>
            <span className={styles.highlight}>Any Provider.</span> Your Choice.
          </Heading>
        </div>
        <div className={styles.integrationsGrid}>
          {integrations.map((item, idx) => (
            <div key={idx} className={styles.integrationItem}>
              <span className={styles.integrationEmoji}>{item.emoji}</span>
              <span className={styles.integrationName}>{item.name}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function CTASection() {
  return (
    <section className={styles.ctaSection}>
      <div className="container">
        <div className={styles.ctaContent}>
          <Heading as="h2" className={styles.ctaTitle}>
            Ready to Build <span className={styles.highlight}>AI Agents</span>?
          </Heading>
          <p className={styles.ctaDescription}>
            Join developers building the next generation of AI applications.
          </p>
          <div className={styles.ctaButtons}>
            <Link className={clsx('button button--lg', styles.primaryButton)} to="/docs/quickstart">
              Start Building →
            </Link>
            <Link className={clsx('button button--lg', styles.secondaryButton)} to="/docs/API-Reference">
              View API Docs
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  return (
    <Layout
      title="Build AI Agents in Python"
      description="openstackai - The SDK for building AI agents in Python. Build powerful multi-agent AI applications in 3 lines or less.">
      <HomepageHeader />
      <main>
        <CodeShowcase />
        <HomepageFeatures />
        <IntegrationsSection />
        <CTASection />
      </main>
    </Layout>
  );
}
