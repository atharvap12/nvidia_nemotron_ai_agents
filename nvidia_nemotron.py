import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

# First API call with reasoning
response = client.chat.completions.create(
  model="nvidia/nemotron-3-super-120b-a12b:free",
  messages=[
          {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?"
          }
        ],
  extra_body={"reasoning": {"enabled": True}}
)

if not response.choices:
    raise RuntimeError(f"No choices returned from OpenRouter.")

# Extract the assistant message with reasoning_details
message = response.choices[0].message

print("=" * 60)
print("REASONING")
print("=" * 60)
print(message.reasoning)

print()
print("=" * 60)
print("FINAL ANSWER")
print("=" * 60)
print(message.content)
# Preserve the assistant message with reasoning_details
messages = [
  {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
  {
    "role": "assistant",
    "content": message.content,
    "reasoning_details": message.reasoning_details  # Pass back unmodified
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# Second API call - model continues reasoning from where it left off
response2 = client.chat.completions.create(
  model="nvidia/nemotron-3-super-120b-a12b:free",
  messages=messages,
  extra_body={"reasoning": {"enabled": True}}
)

if not response2.choices:
    raise RuntimeError("No choices returned from OpenRouter on second call.")

message2 = response2.choices[0].message

print()
print("=" * 60)
print("FOLLOW-UP: REASONING")
print("=" * 60)
print(message2.reasoning)

print()
print("=" * 60)
print("FOLLOW-UP: FINAL ANSWER")
print("=" * 60)
print(message2.content)