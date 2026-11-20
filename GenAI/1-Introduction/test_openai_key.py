import os
import sys
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, RateLimitError, APIConnectionError, APIStatusError

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    sys.exit("OPENAI_API_KEY not found. Check your .env file.")

client = OpenAI(api_key=api_key.strip())

try:
    # Cheap check 1: list models (validates the key without spending tokens)
    models = client.models.list()
    print(f"Key is valid. {len(models.data)} models available.")

    # Check 2: a tiny completion to confirm billing/quota works
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Reply with the single word: pong"}],
        max_tokens=5,
    )
    print("Model replied:", resp.choices[0].message.content)

except AuthenticationError:
    print("Invalid API key (401). Check the key or regenerate it.")
except RateLimitError as e:
    print("Rate limit or quota exceeded (429). Check billing/credits:", e)
except APIConnectionError as e:
    print("Network problem reaching OpenAI:", e)
except APIStatusError as e:
    print(f"API error {e.status_code}: {e.response.text}")