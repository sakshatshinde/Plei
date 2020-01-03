from gameList import GameList, GameStore
import os, fnmatch, re
from steamfiles import acf 
from collections import OrderedDict
from nested_lookup import nested_lookup

# Master game list for all the games regardless of the launcher
GAME_LIST_MASTER = {}

'''
Add steam games to the main list
Possible gameStore values = STEAM, UPLAY, PIRATED, EGS, ORIGIN, GOG
GameStore is an enum and the class has all the specified values : EGS, ORGIN etc
gameStore: GameStore makes sure that the gameStore is of type GameStore
gameStore.value is the value of the given variables in the GameStore class 
>so for example if we do gameAdd('doki doki', 123234, GameStore.EGS)
>we get the value of the EGS variable from the GameStore into -> the GAME_LIST_MASTER
'''

def gameAdd(name, gameId, gameStore: GameStore): 
    game = GameList(name, gameId, gameStore.value)
    GAME_LIST_MASTER[game.name] = [game.gameId, gameStore.value]


'''
Get the steamapps/ folder path
The steamapps/ folder contains appmanifest_STEAM-ID.acf files
find all files with .acf extension
then open the .acf files, extract the name and the appID from the files
use gameAdd to add the game
'''
def getSteamIDs(filePath):
    listOfFiles = os.listdir(filePath)
    pattern = "*.acf"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            with open(filePath + entry) as acfFile:
                STEAM_DATA = acf.load(acfFile, wrapper = OrderedDict)
                gameName = nested_lookup('name', STEAM_DATA)
                gameAppID = nested_lookup('appid', STEAM_DATA)
                gameAdd(gameName[0], gameAppID[0], GameStore.STEAM) #gameName and gameAppID are lists with 1 element only
            

# Alternative method to get the appIDs for the games
# extract the STEAM_ID from that file name
# The regex re.findall() returns ['STEAM_ID'] so it is a list with just 1 value in it at the 0th position
"""
def getSteamIDs(filePath):
    listOfFiles = os.listdir(filePath)
    pattern = "*.acf"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            extractedSteamID = re.findall(r'\d+', str(entry)) # '\d' finds any number (a digit)
            STEAM_ID.append(extractedSteamID[0])
"""
          
#path = 'D:\\SteamLibrary\\steamapps\\'
#getSteamIDs(path)
#print(STEAM_ID)
#gameAdd("Doki Doki", 698780, GameStore.EGS)
#print(GAME_LIST_MASTER)
#print(nested_lookup('Audition Online', GAME_LIST_MASTER))
#D:\SteamLibrary\steamapps
