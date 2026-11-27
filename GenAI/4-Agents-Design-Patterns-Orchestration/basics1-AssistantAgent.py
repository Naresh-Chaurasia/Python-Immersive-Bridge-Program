# Demonstrates a basic AutoGen AssistantAgent (using an OpenAI GPT-4o model client) answering a simple math question via a streamed Console conversation.
import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from openai import OpenAI

import os
from dotenv import load_dotenv

# load_dotenv("/Users/nareshchaurasia/nc/PYTHON-ARCHITECT/Python-Immersive-AI-MAC/.env")

# api_key = os.getenv("OPENAI_API_KEY")
# # print(api_key)

# os.environ["OPENAI_API_KEY"] = api_key


# 1. Load environment variables from your .env file
# (Note: standard filename is ".env", not ".evn" — adjust the path if your file is elsewhere)
env_path = "/Users/nareshchaurasia/nc/PYTHON-ARCHITECT/Python-Immersive-AI-MAC/.env"
loaded = load_dotenv(dotenv_path=env_path, override=True)

# Optional fallback if running from a subdirectory and not using the hardcoded path above:
# if not loaded:
#     load_dotenv(dotenv_path=os.path.join("..", ".env"), override=True)

# 2. Verify OPENAI_API_KEY was loaded
assert os.environ.get("OPENAI_API_KEY"), (
    f"OPENAI_API_KEY not found. Check that it is set in {env_path}"
)

# The OpenAI client reads OPENAI_API_KEY from the environment automatically
client = OpenAI()

# Use a valid OpenAI model identifier (e.g., "gpt-4o-mini", "gpt-4.1-mini", or whichever model your account supports)
MODEL = "gpt-4o-mini"
print(f"Client ready. Using model: {MODEL}")

async def main1():
    print( "I am inside function" )

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o" )
    assistant = AssistantAgent( name="assistant", model_client=model_client )
    await Console( assistant.run_stream( task="What is 25 * 8?" ) )
    await model_client.close()


asyncio.run( main1() )
