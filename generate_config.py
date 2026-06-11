#!/usr/bin/env python3
"""Generate Cursor-compatible OpenAI API settings for Nanobridge."""

import json

REGIONS = {
    "de": {
        "label": "Germany (default)",
        "baseURL": "https://api.nanobridge.net/v1",
    },
    "sg": {
        "label": "Singapore",
        "baseURL": "https://api-sg.nanobridge.net/v1",
    },
    "us": {
        "label": "United States",
        "baseURL": "https://api-us.nanobridge.net/v1",
    },
}

MODELS = [
    "deepseek-v4-flash",
    "deepseek-v4-pro",
    "deepseek-v3.2",
    "glm-5.1",
    "minimax-m2.7",
]


def prompt_region() -> str:
    print("Select region:")
    keys = list(REGIONS.keys())
    for i, key in enumerate(keys, 1):
        print(f"  {i}. {REGIONS[key]['label']} — {REGIONS[key]['baseURL']}")
    choice = input("Region [1]: ").strip() or "1"
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(keys):
            return keys[idx]
    except ValueError:
        pass
    return "de"


def prompt_model() -> str:
    print("Select model:")
    for i, model in enumerate(MODELS, 1):
        default = " (recommended)" if model == "deepseek-v4-flash" else ""
        print(f"  {i}. {model}{default}")
    choice = input("Model [1]: ").strip() or "1"
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(MODELS):
            return MODELS[idx]
    except ValueError:
        pass
    return "deepseek-v4-flash"


def main() -> None:
    print("=== Nanobridge Cursor Config Generator ===\n")
    api_key = input("Enter your Nanobridge API key: ").strip()
    if not api_key:
        raise SystemExit("API key is required.")

    region = prompt_region()
    model = prompt_model()

    config = {
        "apiKey": api_key,
        "baseURL": REGIONS[region]["baseURL"],
        "model": model,
    }

    print("\nGenerated Cursor config (paste into Settings → Models):\n")
    print(json.dumps(config, indent=2))
    print("\nAPI docs: https://platform.nanobridge.net/#/api-docs")


if __name__ == "__main__":
    main()
