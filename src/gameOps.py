from gameList import Game, GameStore
import os, fnmatch , pickle
from steamfiles import acf 
from collections import OrderedDict
from nested_lookup import nested_lookup

# Master game list for all the games regardless of the launcher
global GAME_DIRS, GAME_LIST_MASTER
GAME_LIST_MASTER = {}
GAME_DIRS = {}

'''
Possible gameStore values = STEAM, UPLAY, PIRATED, EGS, ORIGIN, GOG
GameStore is an enum and the class has all the specified values : EGS, ORGIN etc
gameStore: GameStore makes sure that the gameStore is of type GameStore
gameStore.name is the key itself in the GameStore class 
>so for example if we do gameAdd('doki doki', 123234, GameStore.EGS)
>we get "EGS" from the GameStore into -> the GAME_LIST_MASTER
'''

def gameAdd(gameName, gameId, gameStore: GameStore): 
    game = Game(gameName, gameId, gameStore.name)
    GAME_LIST_MASTER[game.name] = [game.gameId, gameStore.name]
    #gameAdd('Apex Legends', 4444, GameStore.ORIGIN)
    #print(GAME_LIST_MASTER)

# Storing directories of game stores
def storeDirectory(gameStore , storeDir) -> str:
    if(gameStore == "ORIGIN"):
        global originPath, uPlayPath, piratedPath
        originPath = storeDir
        GAME_DIRS[gameStore] = originPath
        return(originPath)

    if(gameStore == "UPLAY"):
        uPlayPath = storeDir
        GAME_DIRS[gameStore] = uPlayPath
        return(uPlayPath)

    if(gameStore == "PIRATED"):
        piratedPath = storeDir
        GAME_DIRS[gameStore] = piratedPath
        return(piratedPath)

    if(gameStore == "STEAM"):
        steamPath = storeDir
        GAME_DIRS[gameStore] = steamPath
        return(steamPath)

    #storeDirectory('STEAM','C:\\Program Files (x86)\\Origin Games')
    #print(GAME_DIRS)

'''
Get the steamapps/ folder path
The steamapps/ folder contains appmanifest_STEAM-ID.acf files
find all files with .acf extension
then open the .acf files, extract the name and the appID from the files
use gameAdd to add the game 
'''
def getSteamIDs(filePath = 'D:\\SteamLibrary\\steamapps\\'):
    listOfFiles = os.listdir(filePath)
    pattern = "*.acf"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            with open(filePath + entry) as acfFile:
                STEAM_DATA = acf.load(acfFile, wrapper = OrderedDict)
                gameName = nested_lookup('name', STEAM_DATA)
                gameAppID = nested_lookup('appid', STEAM_DATA)
                gameAdd(gameName[0], gameAppID[0], GameStore.STEAM) #gameName and gameAppID are lists with 1 element only


'''
Origin stores info about the installed games in the C:\\ProgamData....
Inside Each game has its own folder with the same name as of the game
There we have .msft files which we can grab and strip the names and use them as gameIds
we use those gameIds with the cmd -> origin://launchgame/[gameId] to launch games later in launchGame()
'''
# LINK : https://gaming.stackexchange.com/questions/301777/find-uplay-origin-battle-net-game-id
def getOriginIDs(filePath = 'C:\\ProgramData\\Origin\\LocalContent\\'):
    pattern = "*.mfst"
    gameName, gameId  = [], []
    for root, dirs, files in os.walk("C:\\ProgramData\\Origin\\LocalContent"):
        for dir in dirs:
            gameName.append(dir)
        for fileName in files:
            if fnmatch.fnmatch(fileName, pattern):
                fileName = fileName[:-5] 
                gameId.append(fileName)

    final = dict(zip(gameName, gameId ))
    #print(final)
    for game, gameId in final.items():
        #print(game, '->' , gameId)
        gameAdd(game, gameId, GameStore.ORIGIN)
    #print(GAME_LIST_MASTER)
                            
    #getOriginIDs()
    #getSteamIDs()
    #print(GAME_LIST_MASTER)

'''
Check if the game exists
Return the gameID and game's store
'''
def gameSearch(game):
    gameFound = nested_lookup(game, GAME_LIST_MASTER)
    return gameFound


'''
gameInfo initially is a double list. Meaning gameInfo = [[gameId, gameStore]]
[gameInfo] strips down the additional listt = [gameId, gameStore]
gameObj is there to check the Game Store for the game so we can differentiate launch commands
Eg: IF STEAM THEN CMD = "steam://rungameid/"
This CMD is grabbed from the GameStore Enum by .value
'''
def launchGame(game):
    try:
        [gameInfo] = gameSearch(game)
    except:
        raise Exception('Check your game Name')
    gameId  = gameInfo[0] 
    gameStoreName = gameInfo[1]

    if(gameStoreName == 'STEAM'):
        launchStruc = GameStore.STEAM.value
        os.startfile(launchStruc + str(gameId))

    elif(gameStoreName == 'ORIGIN'):
        launchStruc = GameStore.ORIGIN.value
        os.startfile(launchStruc + str(gameId))
        
    else:
        print('Something went wrong')

    # launchGame('Apex')


# Update the gameList data file
def writeData(gameList : dict):
    with open('data\\gameList.plei', 'wb') as f:
       pickle.dump(gameList, f)

# Read the gameList data file and dump into a dict
def readData():
    with open('data\\gameList.plei', 'rb') as f:
        return pickle.load(f)   #returns dict

# getOriginIDs()
# getSteamIDs()
# print(GAME_LIST_MASTER)
# writeData(GAME_LIST_MASTER)
# readData()











#---------------------------------------------------------------------------------------------
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
          

