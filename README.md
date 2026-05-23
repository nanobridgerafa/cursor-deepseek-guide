# DeepSeek V4 Pro & V3 API Access (USDT/Crypto Supported)

Fast, reliable, and privacy-focused API gateway for the latest DeepSeek models. Designed for developers who need stable access without credit card restrictions.

## 🚀 Why Nanobridge?

* **No Credit Card Required**: We solve the "Stripe decline" headache. 
* **Crypto Native**: Native support for **USDT (BSC/BEP20)** and other cryptocurrencies.
* **High Performance**: Optimized for low latency (TTFT) with dedicated clusters for DeepSeek V4 Pro.
* **OpenAI Compatible**: Seamless integration with your existing apps. Just change the `base_url`.

## 💰 Transparent Pricing

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
| :--- | :--- | :--- |
| **DeepSeek V3** | $0.20 | $0.36 |
| **DeepSeek V4 Pro** | $1.28 | $3.00 |

## 🛠️ Quick Start (Python)

```python
import openai

client = openai.OpenAI(
    api_key="YOUR_NANOBRIDGE_KEY",
    base_url="[https://api.nanobridge.net/v1](https://api.nanobridge.net/v1)"
)

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
