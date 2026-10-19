#!/usr/bin/env python3
"""Minimal smoke test for the DeutschlandGPT Platform API."""
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

api_key = os.getenv("DGPT_API_KEY")
model = os.getenv("DGPT_MODEL")
if not api_key or not model:
    sys.exit("Set DGPT_API_KEY and DGPT_MODEL before running this script.")

base_url = os.getenv("DGPT_BASE_URL", "https://api.deutschlandgpt.de/v2").rstrip("/")
payload = {
    "model": model,
    "messages": [{
        "role": "user",
        "content": " ".join(sys.argv[1:]) or "Reply with a short API connectivity check.",
    }],
}
request = Request(
    f"{base_url}/chat/completions",
    data=json.dumps(payload).encode(),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
)

try:
    with urlopen(request, timeout=30) as response:
        result = json.load(response)
    print(result["choices"][0]["message"]["content"])
except HTTPError as error:
    print(f"HTTP {error.code}: {error.read().decode(errors='replace')}", file=sys.stderr)
    sys.exit(1)
except URLError as error:
    print(f"Request failed: {error.reason}", file=sys.stderr)
    sys.exit(1)
