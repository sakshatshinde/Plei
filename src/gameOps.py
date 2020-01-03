from gameList import GameList, GameStore
import os, fnmatch, re

#Master game list for all the games regardless of the launcher
GAME_LIST_MASTER = {}
STEAM_ID = []

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
extract the STEAM_ID from that file name
The regex re.findall() returns ['STEAM_ID'] so it is a list with just 1 value in it at the 0th position
'''

def getSteamIDs(filePath):
    listOfFiles = os.listdir(filePath)
    pattern = "*.acf"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            extractedSteamID = re.findall(r'\d+', str(entry)) # '\d' finds any number (a digit)
            STEAM_ID.append(extractedSteamID[0])
            
#getSteamIDs(r"D:\SteamLibrary\steamapps")
#print(STEAM_ID)
#gameAdd("Doki Doki", 698780, GameStore.EGS)
#print(GAME_LIST_MASTER)
#D:\SteamLibrary\steamapps