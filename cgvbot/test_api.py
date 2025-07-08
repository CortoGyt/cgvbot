from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-nano-2025-04-14",
    input=""
)
print(response.output_text)