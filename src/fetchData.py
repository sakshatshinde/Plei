# This DATA is grabbed from GIANT BOMB 
# Vist them at : https://www.giantbomb.com/
# import json

import pybomb, os
from nested_lookup import  nested_lookup
from dotenv import load_dotenv
from gui.imgServe import retrieveImg

# Client 
load_dotenv()   # secure way to access API keys
API_KEY = os.getenv('API_KEY')
client = pybomb.GamesClient(API_KEY)

# Funcs 
def gameSearch(gameName: str):
    response = client.quick_search(
        name = gameName,
        platform = pybomb.PC,
        sort_by = 'original_release_date',
        desc = False
    )
    return response.results

def gameImgSearch(gameName: str):
    query = gameSearch(gameName)
    try :
        result = nested_lookup("medium_url", query)[0] # returns a list 
        return result
    except :
        raise Exception('Game not found')
# print(gameImgSearch('Star Wars Jedi: fallen order'))

def gameRating(gameName: str):
    query = gameSearch(gameName)
    try :
        result = nested_lookup("original_game_rating", query)[0][0] # returns a dict 
        rating = nested_lookup("name", result)[0]   # extracting data
        return rating
    except :
        raise Exception('Rating not found')
# print(gameRating('Heave Ho'))
   
def imageCache(gameName: str):
    imgURL = gameImgSearch(gameName)
    retrieveImg(gameName, imgURL)
# imageCache('Star Wars Jedi: fallen order') #// look in gui/imgServe