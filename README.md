# Nanobridge

OpenAI-compatible AI inference gateway optimized for coding workflows and AI agents.

Built for:
- Cursor
- Cline
- Continue
- Aider
- AI coding assistants
- Autonomous agents

---

# Why Nanobridge?

Modern AI coding workflows require:

- stable inference
- low latency
- OpenAI compatibility
- reliable streaming
- long-context reasoning
- affordable scaling

Nanobridge focuses specifically on practical AI coding reliability.

Built because many existing routing solutions are often:
- unstable under load
- expensive at scale
- inconsistent for coding tasks
- difficult to integrate

---

# Features

- OpenAI-compatible API
- DeepSeek V4 Pro support
- Streaming support
- Long-context reasoning
- Coding-oriented inference routing
- Retry optimization
- Crypto payment support
- AI agent compatibility

---

# Supported Models

Currently available:

- deepseek-v4-pro
- deepseek-v3
- deepseek-reasoner

More models coming soon.

---

# Supported Tools

Works with:

- Cursor
- Cline
- Continue
- Aider
- OpenAI SDK
- LangChain
- LiteLLM
- AI agents

---

# API Endpoint

Base URL:

``` id="j1k2vs"
https://platform.nanobridge.net/v1
```

API Docs:

https://platform.nanobridge.net/api-docs

---

# Quick Start

## Python

Install SDK:

```bash
pip install openai
```

Example:

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://platform.nanobridge.net/v1"
)

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {
            "role": "user",
            "content": "Write a FastAPI middleware example"
        }
    ],
    stream=False
)

print(response.choices[0].message.content)
```

---

# cURL Example

```bash
curl https://platform.nanobridge.net/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "deepseek-v4-pro",
    "messages": [
      {
        "role": "user",
        "content": "hello"
      }
    ]
  }'
```

---

# Cursor Setup

## Step 1 — Open Cursor Settings

Go to:

``` id="x4sy9l"
Cursor → Settings → Models
```

Enable:

``` id="n5z8vd"
OpenAI Compatible API
```

---

## Step 2 — Configure API

Use:

```json
{
  "apiKey": "YOUR_API_KEY",
  "baseURL": "https://platform.nanobridge.net/v1",
  "model": "deepseek-v4-pro"
}
```

---

# Recommended AI Coding Workflow

DeepSeek V4 Pro works especially well for:

- refactoring
- bug fixing
- code explanation
- multi-file edits
- long-context coding
- reasoning-heavy workflows
- autonomous coding agents

---

# Streaming Support

Streaming is fully supported.

Recommended for:
- lower perceived latency
- coding copilots
- interactive workflows
- long generations

---

# OpenAI Compatibility

Nanobridge is designed to be drop-in compatible with OpenAI-style APIs.

Supported:
- /chat/completions
- streaming
- system prompts
- multi-turn conversations

This makes integration easy with most modern AI developer tools.

---

# Why Not Just Use OpenRouter?

Some developers prefer:

- lower latency
- coding-focused routing
- simplified infrastructure
- stable long-context workflows
- direct DeepSeek optimization
- crypto payment support

Nanobridge focuses specifically on AI coding workloads and developer workflows.

---

# AI Agent Optimization

Optimized for:
- coding agents
- autonomous workflows
- multi-step reasoning
- tool-calling systems
- development automation

---

# Example Prompt Ideas

Try inside Cursor:

``` id="m4yd1g"
Refactor this codebase
```

``` id="a9x5vu"
Find concurrency issues
```

``` id="p6w1qs"
Optimize this SQL query
```

``` id="h7e4rz"
Explain this architecture
```

---

# Best Practices

For best coding performance:

- use focused prompts
- split large tasks
- restart long sessions periodically
- prefer streaming mode
- use explicit coding instructions

---

# Common Issues

## Timeout Problems

Possible causes:
- overloaded providers
- unstable routing
- long reasoning chains

Possible solutions:
- retry requests
- shorten prompts
- restart conversation sessions

---

## Invalid Base URL

Make sure the Base URL is:

``` id="x9u5pk"
https://platform.nanobridge.net/v1
```

NOT:

``` id="q2h7nf"
https://platform.nanobridge.net/api-docs
```

---

# Performance Goals

Current optimization targets:

- lower latency
- stable streaming
- reliable coding workflows
- reduced inference failures

---

# Current Status

Project status:

- Active development
- Early production usage
- API stability improvements ongoing

---

# Roadmap

Planned improvements:

- smarter routing
- fallback optimization
- additional models
- lower latency
- enhanced AI agent support
- coding workflow tuning

---

# Community

Website:
https://www.nanobridge.ai

Platform:
https://platform.nanobridge.net

API Docs:
https://platform.nanobridge.net/api-docs

GitHub:
https://github.com/nanobridgerafa

---

# Disclaimer

Nanobridge is an independent inference gateway project and is not affiliated with OpenAI or DeepSeek.
