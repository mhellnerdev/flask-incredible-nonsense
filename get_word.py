import os
from unittest import result
import requests
import json
from dotenv import load_dotenv

load_dotenv()
WORDS_API_KEY = os.getenv('WORDS_API_KEY')
base_uri = os.getenv('BASE_URI')

headers = {
  'x-rapidapi-key': WORDS_API_KEY,
  'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
}

def get_random_word():
  response = requests.get(f'{base_uri}/words/?random=true', headers=headers)
  json_response = response.json()

  try:
    word = json_response["word"]
    results = json_response["results"]
    # definition = json_response["results"][0]
    print("Word: " + word)
    print("Definition: " + results[0]['definition'])
    print("Type of word:")
    for typeof in results[0]['typeOf']:
      print(typeof)
  except:
    print("Word missing definition or type.")


if __name__ == '__main__':
  get_random_word()

