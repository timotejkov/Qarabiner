"""Quick diagnostic to identify what's causing the 422 error."""
import os
import sys
import anthropic

API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
if not API_KEY:
    print("ERROR: Set ANTHROPIC_API_KEY env var")
    sys.exit(1)

print(f"anthropic SDK version: {anthropic.__version__}")

client = anthropic.Anthropic(api_key=API_KEY)

# Test 1: Basic call with haiku model
models_to_test = [
    "claude-haiku-4-5-20251001",
    "claude-sonnet-4-5-20250929",
    "claude-3-5-haiku-20241022",
    "claude-3-5-sonnet-20241022",
]

for model in models_to_test:
    print(f"\n--- Testing model: {model} ---")
    try:
        response = client.messages.create(
            model=model,
            max_tokens=50,
            temperature=0.1,
            system="You are a test assistant. Respond with exactly: OK",
            messages=[{"role": "user", "content": "Say OK"}],
        )
        print(f"  SUCCESS: {response.content[0].text}")
        print(f"  Usage: {response.usage.input_tokens}in / {response.usage.output_tokens}out")
    except anthropic.APIError as e:
        print(f"  FAILED: {e.status_code} - {e.message}")
    except Exception as e:
        print(f"  FAILED: {type(e).__name__}: {e}")
