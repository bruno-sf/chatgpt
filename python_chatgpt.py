import json
import openai
import sys
import os
# Simple test using GPT-3 from terminal to generate a response to an input
# Brunof - 2023-feb-07
# Usage python3 test-chat-gpt.py "Just Say Hello!"

# Check if API key is set
if os.getenv("OPENAI_API_KEY") is None:
    print("Please set your OPENAI_API_KEY environment variable.")
    sys.exit()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Validate input
if len(sys.argv) < 2:
    _prompt="Just Say Hello!"
elif sys.argv[1] is not None:
    _prompt=sys.argv[1]
else:
    print("Usage: python3 test-chat-gpt.py \"Just Say Hello!\"")
    sys.exit()

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=_prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
response_json=json.loads(json.dumps(response))

try:
    parsed_response = response_json['choices'][0]['text']
    print(parsed_response.strip())
except KeyError:
    print("Sorry, could not parse JSON data")