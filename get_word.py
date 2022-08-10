# get_word.py

import os
import requests
import json
from dotenv import load_dotenv
import traceback

from pprint import pprint

from prepositions import random_preposition

from datetime import datetime


load_dotenv()
WORDS_API_KEY = os.getenv('WORDS_API_KEY')
base_uri = os.getenv('BASE_URI')
WORDS_URI = os.getenv('WORDS_URI')
SAVE_PATH = os.getenv('SAVE_PATH')

headers = {
  'x-rapidapi-key': WORDS_API_KEY,
  'x-rapidapi-host': WORDS_URI
}



# take in number for amount of words to output
def input_values():
  number_of_words = int(input("How much incredible nonsense? "))
  return number_of_words


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
  # number_of_words = input_values()
  # i = 0 # debug variable for code in loop
  for word in range(20):
    json_response = get_random_word_json()
    word = json_response['word']
    word_list.append(word)
    # # debug use to check api calls in loop
    # i += 1 
    # print(f"API Call {i}")
    # print(word)
  output_file(word_list)
  return word_list


def create_random_word_dict():
  word_dict = {}    # define a dict
  word_key = 0      # key for dict. used to iterate key as an int
  for word in range(10):
    json_response = get_random_word_json()
    word = json_response['word']
    word_key += 1    # iterate key value
    word_dict[word_key] = word    # add word to dict
  return word_dict


def list_random_words():
  word_list = create_random_word_list()
  for word in word_list:
    return(word)


def list_sentence():
  word_list = create_random_word_list()
  sentence = ""
  for word in word_list:
    preposition = random_preposition()
    sentence += word + " "
    sentence += preposition + " "
  return sentence
  

def format_sentence():
  sentence = list_sentence()
  return sentence.capitalize()


def output_file(f):
  now = datetime.now() # get current datetime
  dt = now.strftime("%Y-%m-%d_%H.%M.%S")
  with open(SAVE_PATH + "wordlist_" + dt + ".json", "w") as outfile:
    json.dump(f, outfile)



if __name__ == '__main__':
  # get_random_word_json()
  # create_random_word_list()
  # word_and_definition()
  # list_random_words()
  # create_random_word_dict()
  # list_sentence()
  format_sentence()






















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