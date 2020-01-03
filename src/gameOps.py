from gameList import GameList
import os, fnmatch, re

#Master game list for all the games regardless of the launcher
GAME_LIST_MASTER = {}
STEAM_ID = []

#Add steam games to the main list
def gameAddSteam(name, gameId, gameStore):
    game = GameList(name, gameId, gameStore)
    GAME_LIST_MASTER[game.name] = [game.gameId, gameStore]

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
            extractedSteamID = re.findall(r'\d+', str(entry)) 
            STEAM_ID.append(extractedSteamID[0])
            




#getSteamIDs(r"D:\SteamLibrary\steamapps")
#print(STEAM_ID)
#gameAddSteam("Doki Doki", 698780, "Steam")
#print(GAME_LIST_MASTER)
#D:\SteamLibrary\steamapps