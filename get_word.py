import os
from unittest import result
from flask import render_template
import requests
import json
from dotenv import load_dotenv
import traceback

load_dotenv()
WORDS_API_KEY = os.getenv('WORDS_API_KEY')
base_uri = os.getenv('BASE_URI')

headers = {
  'x-rapidapi-key': WORDS_API_KEY,
  'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
}

# func to return name of current file to import
def get_filename():
  return __name__

# func to print and return word, definition, and typeof word. this also outputs a list
def get_random_word():
  response = requests.get(f'{base_uri}/words/persian', headers=headers)
  json_response = response.json()

  try:
    # store word key in json_response to word var
    word = json_response["word"]
    
    # store results list. can be indexed by results[0]['{key}']
    results = json_response["results"]
    
    print("Word: " + word)
    
    # # store pronunciation
    # pronunciation =  json_response["pronunciation"]
    # print("Pronunciation: " + pronunciation['all'])

    # store type of words into a list
    for typeof_list in results:
      type_list = (typeof_list['typeOf'])
          
    for types in type_list:
      typelisted = types


    for result_list in results:
      print("Definition: " + result_list['definition'])
      print("Type of word:")
      print(typelisted)


    # # debug code  
    print(type(types)) # used for debugging
  
  except Exception as e:
    print('There was an exception error!')
    traceback.print_exc() # debugging
    print(str(e))
    # print("Word missing definition or type.")

def json_output():
  response = requests.get(f'{base_uri}/words/?random=true', headers=headers)
  json_response = response.json()
  json_dumps = json.dumps(json_response, indent=0)
  return json_dumps




if __name__ == '__main__':
  get_random_word()

