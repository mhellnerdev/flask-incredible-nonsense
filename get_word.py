import os
from random import random

import requests
import json
from dotenv import load_dotenv
import traceback

load_dotenv()
WORDS_API_KEY = os.getenv('WORDS_API_KEY')
base_uri = os.getenv('BASE_URI')
WORDS_URI = os.getenv('WORDS_URI')

headers = {
  'x-rapidapi-key': WORDS_API_KEY,
  'x-rapidapi-host': WORDS_URI
}

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



def get_random_word_json():
  response = requests.get(f'{base_uri}/words/?random=true', headers=headers)
  json_response = response.json()
  return json_response



def word_and_definition():
    while True:
      try:
        random_json = get_random_word_json()
        random_word = random_json['word']
        random_results = random_json['results']
        random_definition = random_json['results'][0]['definition']
        print(random_word)
        # print(random_results)
        print(random_definition)
      except Exception as e:
        print(e)
        continue
      else:
        break



def create_random_word_list():
  word_list=[]
  for word in range(5):
    # get_random_word_json()
    response = requests.get(f'{base_uri}/words/?random=true', headers=headers)
    json_response = response.json()
    word = json_response['word']
    word_list.append(word)
  return word_list



def list_random_words():
  word_list = create_random_word_list()
  for word in word_list:
    print(word)  



def json_output():
  response = requests.get(f'{base_uri}/words/?random=true', headers=headers)
  json_response = response.json()
  json_dumps = json.dumps(json_response, indent=0)
  return json_dumps




if __name__ == '__main__':
  # get_random_word_json()
  # create_random_word_list()
  list_random_words()
  