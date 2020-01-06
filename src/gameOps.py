from gameList import Game, GameStore
import os, fnmatch
from steamfiles import acf 
from collections import OrderedDict
from nested_lookup import nested_lookup

# Master game list for all the games regardless of the launcher
GAME_LIST_MASTER = {}
GAME_DIRS = {}

'''
Add steam games to the main list
Possible gameStore values = STEAM, UPLAY, PIRATED, EGS, ORIGIN, GOG
GameStore is an enum and the class has all the specified values : EGS, ORGIN etc
gameStore: GameStore makes sure that the gameStore is of type GameStore
gameStore.value is the value of the given variables in the GameStore class 
>so for example if we do gameAdd('doki doki', 123234, GameStore.EGS)
>we get the value of the EGS variable from the GameStore into -> the GAME_LIST_MASTER
'''

def gameAdd(gameName, gameId, gameStore: GameStore): 
    game = Game(gameName, gameId, gameStore.name)
    GAME_LIST_MASTER[game.name] = [game.gameId, gameStore.name]

#For handling other stores than STEAM
def storeDirectory(gameStore , storeDir) -> str:
    if(gameStore == "ORIGIN"):
        global originPath, uPlayPath, piratedPath
        originPath = storeDir
        #originPath = input('Input the PATH to origin directory: ')
        GAME_DIRS[gameStore] = originPath
        return(originPath)
    if(gameStore == "UPLAY"):
        uPlayPath = storeDir
        #uPlayPath = input('Input the PATH to uPlay directory: ')
        GAME_DIRS[gameStore] = uPlayPath
        return(uPlayPath)
    if(gameStore == "PIRATED"):
        piratedPath = storeDir
        #piratedPath = input('Input the PATH to Pirated Games directory')
        GAME_DIRS[gameStore] = piratedPath
        return(piratedPath)

#storeDirectory('STEAM','C:\\Program Files (x86)\\Origin Games')
#print(GAME_DIRS)

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

'''
Check if the game exists
Return the gameID and game's store
'''
def gameSearch(game):
    gameFound = nested_lookup(game, GAME_LIST_MASTER)
    return gameFound

#Temp solution
'''
def getPath(gameStoreName):
    if(gameStoreName == 'ORIGIN'):
        originPath = input('Please enter your Origin librarie\'s path here')
        return originPath
    if(gameStoreName == 'UPLAY'):
        uPlayPath = input('Please enter your UPLAY librarie\'s path here')
        return uPlayPath
    if(gameStoreName == 'PIRATED'):
        pathToExe = input('Please input the PATH of your game\'s .exe file')
        return pathToExe
    else:
        pass
'''


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
    gameObj = GameStore

    if(gameStoreName == 'STEAM'):
        launchStruc = gameObj.STEAM.value
        os.startfile(launchStruc + str(gameId))
    else:
        print('Something went wrong')
    '''
    elif(gameStoreName == 'PIRATED'):
        path = getPiratedPath('PIRATED')
        os.startfile(path)
    
    elif(gameStoreName == 'ORIGIN'):
        path = getPath('ORIGIN')
        os.startfile(path)

    elif(gameStoreName == 'UPLAY'):
        path = getPath('UPLAY')
        os.startfile(path)
    '''
    
       
       
#path = 'D:\\SteamLibrary\\steamapps\\'
#getSteamIDs(path)
#gameAdd("Apex Legends", 0, GameStore.ORIGIN)
#print(GAME_LIST_MASTER)
#print(nested_lookup('Audition Online', GAME_LIST_MASTER))
#D:\SteamLibrary\steamapps
#launchGame('Apex Legends') 

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
          

