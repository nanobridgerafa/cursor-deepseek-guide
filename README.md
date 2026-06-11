# NanoBridge — Cursor & DeepSeek Integration Guide

OpenAI-compatible retry and failover gateway for Cursor, Claude Code, and AI coding agents.

Built for developers dealing with unstable upstream providers, timeouts, multi-provider routing, coding workload spikes, and cost optimization.

---

## What this repo solves

- Wrong Base URL or model name when configuring DeepSeek in Cursor
- Using the console host `platform.nanobridge.net` as the API endpoint
- Confusing OpenAI-compatible APIs with Anthropic Messages endpoints
- Not knowing which model or regional node to pick

---

## Quick Start (Cursor)

### 1. Get an API key

Sign up and create an API key in the [Nanobridge console](https://platform.nanobridge.net).

### 2. Pick a regional Base URL

**API requests go to the gateway hosts** (not the console):

| Region | OpenAI Base (use in Cursor, includes `/v1`) | Anthropic Base (Cline / Claude Code, etc.) |
|--------|---------------------------------------------|--------------------------------------------|
| Germany (default) | `https://api.nanobridge.net/v1` | `https://api.nanobridge.net/anthropic` |
| Singapore | `https://api-sg.nanobridge.net/v1` | `https://api-sg.nanobridge.net/anthropic` |
| United States | `https://api-us.nanobridge.net/v1` | `https://api-us.nanobridge.net/anthropic` |

The same API key works across regions. Pick the node closest to you for lower latency.

### 3. Cursor settings

1. Open **Cursor → Settings → Models**
2. Enable **Override OpenAI Base URL** (or a similar “OpenAI Compatible API” option)
3. Use:

```json
{
  "apiKey": "YOUR_API_KEY",
  "baseURL": "https://api.nanobridge.net/v1",
  "model": "deepseek-v4-flash"
}
```

The recommended default model is `deepseek-v4-flash` (balanced cost and latency). Use `deepseek-v4-pro` for stronger reasoning.

> Note: Some Cursor features may still use built-in channels. The OpenAI override mainly applies to Chat / Composer and other compatible paths—verify with a real request.

Generate config with: `python generate_config.py`

---

## Supported models

Use these IDs in the request `model` field (matches the console gateway catalog):

| Model ID | Notes |
|----------|-------|
| `deepseek-v4-flash` | **Recommended default** |
| `deepseek-v4-pro` | Stronger reasoning |
| `deepseek-v3.2` | DeepSeek V3.2 |
| `glm-5.1` | Alias: `glm-5-1` |
| `minimax-m2.7` | Alias: `minimax-m-2-7` |

---

## API endpoints

- **OpenAI Chat Completions**: `POST /v1/chat/completions` (or `POST /chat/completions`)
- **Model list**: `GET /v1/models`
- **Anthropic Messages**: `POST /v1/messages` (Anthropic base from the table above)
- **Streaming**: set `stream: true` in the request body; response is SSE
- **Auth**: `Authorization: Bearer <API_KEY>`

Full parameters and examples: [chat-completions.md](./chat-completions.md)

Official API docs: [platform.nanobridge.net/#/api-docs](https://platform.nanobridge.net/#/api-docs)

---

## Python (OpenAI SDK)

```bash
pip install openai
```

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.nanobridge.net/v1",
)

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Write a FastAPI middleware example"}],
)
print(response.choices[0].message.content)
```

For Singapore, change `base_url` to `https://api-sg.nanobridge.net/v1`.

---

## cURL

```bash
curl https://api.nanobridge.net/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "hello"}]
  }'
```

More examples: [api-key-example.sh](./api-key-example.sh)

---

## LiteLLM

```bash
export NANOBRIDGE_API_KEY="your-api-key"
# optional: export NANOBRIDGE_API_BASE="https://api-sg.nanobridge.net/v1"
```

```python
import litellm

response = litellm.completion(
    model="nanobridge/deepseek-v4-flash",
    messages=[{"role": "user", "content": "Hello"}],
)
print(response.choices[0].message.content)
```

---

## Compatible tools

| Tool | Protocol | Configuration |
|------|----------|---------------|
| Cursor | OpenAI | Base = `https://api*.nanobridge.net/v1` |
| Claude Code | Anthropic | `ANTHROPIC_BASE_URL` = Anthropic base |
| Cline / Roo Code / Kilo | Anthropic | Provider = Anthropic, model `deepseek-v4-flash` |
| Continue / Aider | OpenAI | Same OpenAI base as above |
| OpenAI SDK / LangChain | OpenAI | `base_url` + `api_key` |

Portal integrations: [platform.nanobridge.net](https://platform.nanobridge.net) → Integrations.

---

## FAQ

### Timeouts

Possible causes: upstream overload, long reasoning chains, network jitter. Shorten prompts, enable streaming, switch to a closer region, or retry.

### Wrong Base URL

| Correct (gateway) | Wrong |
|-------------------|-------|
| `https://api.nanobridge.net/v1` | `https://platform.nanobridge.net/v1` |
| | `https://platform.nanobridge.net/api-docs` |

`platform.nanobridge.net` is the **console and documentation**—it does not serve Chat Completions inference.

### Model not found

Do not use retired or unavailable names (e.g. `deepseek-v3`, `deepseek-reasoner`). Use the model list in the console.

---

## Repository files

| File | Description |
|------|-------------|
| [cursor-deepseek-guide.md](./cursor-deepseek-guide.md) | Cursor + DeepSeek focused guide |
| [generate_config.py](./generate_config.py) | Interactive Cursor config generator |
| [chat-completions.md](./chat-completions.md) | Chat / Messages API reference |
| [api-key-example.sh](./api-key-example.sh) | cURL examples |
| [nanobridge-overview.md](./nanobridge-overview.md) | Product overview and pricing |

---

## Links

- Website: https://www.nanobridge.ai
- Console: https://platform.nanobridge.net
- API docs: https://platform.nanobridge.net/#/api-docs
- GitHub: https://github.com/nanobridgerafa

---

## Disclaimer

Nanobridge is an independent inference gateway and is not affiliated with OpenAI or DeepSeek.
