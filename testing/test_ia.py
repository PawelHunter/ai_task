import os
import openai
from functions.functions import load_data_from_file


load_data_from_file(r"data/key.json")
openai.api_key = os.environ["AI_API_KEY"]

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Correct this to standard English:\n\nShe no went to the market.",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response)