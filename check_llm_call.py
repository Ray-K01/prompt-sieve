"""Hour 1 sanity check: confirm your API key and model work."""
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
key, model = os.getenv("GEMINI_API_KEY"), os.getenv("GEMINI_MODEL")
if not key or not model:
    raise SystemExit("Set GEMINI_API_KEY and GEMINI_MODEL in your .env file first.")

client = genai.Client(api_key=key)
resp = client.models.generate_content(model=model, contents="Reply with exactly: API OK")
print(resp.text)
