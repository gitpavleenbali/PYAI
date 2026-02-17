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
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <p className={styles.heroDescription}>
          The Pandas of AI Agents - Build powerful AI applications in 3 lines or less
        </p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/quickstart">
            Get Started →
          </Link>
        </div>
        <div className={styles.installCommand}>
          <code>pip install pyai</code>
        </div>
      </div>
    </header>
  );
}

const codeExamples = {
  simple: `from pyai import ask, summarize, research

# One-liner AI calls
answer = ask("What is machine learning?")
summary = summarize("Long document text...")
report = research("Latest AI trends 2026")`,

  agent: `from pyai import Agent, Runner

# Create an AI agent
agent = Agent(
    name="Assistant",
    instructions="You are a helpful AI assistant."
)

# Run synchronously
result = Runner.run_sync(agent, "Hello!")
print(result.final_output)`,

  multiagent: `from pyai import Agent, Runner
from pyai.blueprint import ChainWorkflow

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
        <Heading as="h2" className={styles.sectionTitle}>
          Write Less, Build More
        </Heading>
        <div className={styles.codeGrid}>
          <div className={styles.codeCard}>
            <h3>⚡ Simple API</h3>
            <CodeBlock language="python">{codeExamples.simple}</CodeBlock>
          </div>
          <div className={styles.codeCard}>
            <h3>🤖 Agent API</h3>
            <CodeBlock language="python">{codeExamples.agent}</CodeBlock>
          </div>
          <div className={styles.codeCard}>
            <h3>👥 Multi-Agent</h3>
            <CodeBlock language="python">{codeExamples.multiagent}</CodeBlock>
          </div>
        </div>
      </div>
    </section>
  );
}

type FeatureItem = {
  title: string;
  emoji: string;
  description: string;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Simple by Design',
    emoji: '🎯',
    description: 'One-liner APIs like ask(), summarize(), research(). No boilerplate, just results.',
  },
  {
    title: 'Multi-Provider',
    emoji: '🔌',
    description: 'OpenAI, Azure OpenAI, Anthropic, Ollama - switch providers with one line.',
  },
  {
    title: 'Multi-Agent Ready',
    emoji: '👥',
    description: 'Chain, supervisor, and custom orchestration patterns out of the box.',
  },
  {
    title: 'Enterprise Grade',
    emoji: '🏢',
    description: 'Azure AD auth, sessions, guardrails, tracing, and evaluation built-in.',
  },
  {
    title: 'Extensible',
    emoji: '🧩',
    description: 'Plugins, custom skills, OpenAPI tools, and A2A protocol support.',
  },
  {
    title: 'RAG & Vector DBs',
    emoji: '📊',
    description: 'ChromaDB, Pinecone, Qdrant, Weaviate - connect your knowledge base.',
  },
];

function Feature({title, emoji, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4', styles.featureCard)}>
      <div className={styles.featureEmoji}>{emoji}</div>
      <Heading as="h3">{title}</Heading>
      <p>{description}</p>
    </div>
  );
}

function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <Heading as="h2" className={styles.sectionTitle}>
          Why PyAI?
        </Heading>
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
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
        <Heading as="h2">Ready to Build?</Heading>
        <p>Join developers building the next generation of AI applications.</p>
        <div className={styles.buttons}>
          <Link className="button button--primary button--lg" to="/docs/quickstart">
            Start Building →
          </Link>
          <Link
            className="button button--outline button--lg"
            style={{marginLeft: '1rem'}}
            href="https://github.com/gitpavleenbali/PYAI">
            ⭐ Star on GitHub
          </Link>
        </div>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title="Build AI Agents in Python"
      description="PyAI - The Pandas of AI Agents. Build powerful AI applications in 3 lines or less.">
      <HomepageHeader />
      <main>
        <CodeShowcase />
        <HomepageFeatures />
        <CTASection />
      </main>
    </Layout>
  );
}
