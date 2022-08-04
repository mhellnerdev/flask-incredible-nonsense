import os
from unittest import result
from flask import render_template
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

def index_page():
  return "index_page function"

def get_random_word():
  response = requests.get(f'{base_uri}/words/?random=true', headers=headers)
  json_response = response.json()

  try:
    word = json_response["word"]
    results = json_response["results"]
    definition = json_response["results"][0]
    print("Word: " + word)
    print("Definition: " + results[0]['definition'])
    print("Type of word:")
    for typeof in results[0]['typeOf']:
      print(typeof)
  except:
    print("Word missing definition or type.")

def json_output():
  response = requests.get(f'{base_uri}/words/?random=true', headers=headers)
  json_response = response.json()
  json_dumps = json.dumps(json_response, indent=0)
  return json_dumps




if __name__ == '__main__':
  get_random_word()

