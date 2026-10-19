# dgpt

Minimal smoke test for the DeutschlandGPT Platform API. Requires Python 3.8+ and no third-party packages.

## Run

1. Create a DeutschlandGPT Platform API key and choose a model available to your workspace.
2. In a shell, set the key and model, then run the script:

~~~sh
export DGPT_API_KEY="your-api-key"
export DGPT_MODEL="your-model-id"
python3 test_api.py
~~~

You can pass a custom prompt:

~~~sh
python3 test_api.py "Say hello in one sentence"
~~~

The script uses https://api.deutschlandgpt.de/v2 by default. For a self-hosted deployment, set DGPT_BASE_URL to its OpenAI-compatible /v2 base URL. Keep your API key secret; do not commit it to this repository.
