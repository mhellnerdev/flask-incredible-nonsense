# get_word.py

import os
from random import random

import requests
import json
from dotenv import load_dotenv
from datetime import datetime
import traceback


from prepositions import random_preposition

now = datetime.now() # get current datetime
dt = now.strftime("%Y-%m-%d_%H.%M.%S")


load_dotenv()
WORDS_API_KEY = os.getenv('WORDS_API_KEY')
base_uri = os.getenv('BASE_URI')
WORDS_URI = os.getenv('WORDS_URI')

headers = {
  'x-rapidapi-key': WORDS_API_KEY,
  'x-rapidapi-host': WORDS_URI
}



# take in number for amount of words to output
def input_values():
  word_number = int(input("How much incredible nonsense? "))
  return word_number



# function to connect to api and store a json response
def get_random_word_json():
  response = requests.get(f'{base_uri}/words/?random=true', headers=headers)
  json_response = response.json()
  return  json_response



# function to loop through words until word with definiton is found
def word_and_definition():
  while True:
    try:
      random_json = get_random_word_json()
      random_word = random_json['word']
      random_results = random_json['results']
      random_definition = random_json['results'][0]['definition']
      print()
      print("Random Word: " + random_word)
      # print(random_results)
      print("Definition: " + random_definition)
    except Exception as e:
      # print(traceback.print_exc()) # throws debug if cant find 'results' key 
      # print(e)
      continue
    else:
      break



def create_random_word_list():
  word_list = []
  word_number = input_values()
  # i = 0 # debug variable for code in loop
  for word in range(word_number):
    json_response = get_random_word_json()
    word = json_response['word']
    word_list.append(word)

    # i += 1 # used to check api calls in loop
    # print(f"API Call {i}") # debug use to check api calls in loop
    # print(word) # debug use for if you want word printed on each loop
  
  with open("wordlist_" + dt + ".json", "w") as outfile:
    json.dump(word_list, outfile)

  return word_list



def create_random_word_dict():
  # word_list = []
  word_dict = {}    # define a dict
  word_key = 0      # key for dict. used to iterate key as an int
  word_number = input_values()
  for word in range(word_number):
    json_response = get_random_word_json()
    word = json_response['word']
    word_key += 1    # iterate key value
    word_dict[word_key] = word    # add word to dict
  print(word_dict)    # prints the dict

  #output file
  with open("worddict_" + dt + ".json", "w") as outfile:
    json.dump(word_dict, outfile)

  return word_dict




def list_random_words():
  word_list = create_random_word_list()
  print()
  print("========= WORD LIST =========")
  for word in word_list:
    print(word)



def list_sentence():
  word_list = create_random_word_list()
  for word in word_list:
    preposition = random_preposition()
    print(word, end=" ")
    print(preposition, end=" ")
  print()

    



if __name__ == '__main__':
  # get_random_word_json()
  # create_random_word_list()
  # word_and_definition()
  # list_random_words()
  create_random_word_dict()
  # list_sentence()






















### TEST / Deprecated code
# # func to print and return word, definition, and typeof word. this also outputs a list
# def get_random_word_full():
#   response = requests.get(f'{base_uri}/words/persian', headers=headers)
#   json_response = response.json()

#   try:
#     # store word key in json_response to word var
#     word = json_response["word"]
    
#     # store results list. can be indexed by results[0]['{key}']
#     results = json_response["results"]
    
#     print("Word: " + word)
    
#     # # store pronunciation
#     # pronunciation =  json_response["pronunciation"]
#     # print("Pronunciation: " + pronunciation['all'])

#     # store type of words into a list
#     for typeof_list in results:
#       type_list = (typeof_list['typeOf'])
          
#     for types in type_list:
#       typelisted = types


#     for result_list in results:
#       print("Definition: " + result_list['definition'])
#       print("Type of word:")
#       print(typelisted)


#     # # debug code  
#     print(type(types)) # used for debugging
  
#   except Exception as e:
#     print('There was an exception error!')
#     traceback.print_exc() # debugging
#     print(str(e))
#     # print("Word missing definition or type.")
