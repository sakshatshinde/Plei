from gameList import Game, GameStore
from steamfiles import acf 
from collections import OrderedDict
from nested_lookup import nested_lookup
import os, fnmatch , pickle, re, json
import winreg #for Uplay

# Master game list for all the games regardless of the launcher
GAME_LIST_MASTER = {}

'''
Possible gameStore values = STEAM, UPLAY, STANDALONE, EGS, ORIGIN, GOG
GameStore is an enum and the class has all the specified values : EGS, ORIGIN etc
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
Finding binaries for games 
Eliminating other types of binaries, eg: uninstall.exe etc
''' 
def getStandalone(filePath = 'D:\\Games\\'):
    pattern = "*.exe"
    pattern2 = "unin*"
    for  root, dir, files in os.walk(filePath):
        for file in files:
            if(
                fnmatch.fnmatch(file, pattern) and 
                fnmatch.fnmatch(file, pattern) != 
                fnmatch.fnmatch(file, pattern2)
            ):
                print(file)
                
# print(getStandalone())

'''
Origin stores info about the installed games in the C:\ProgamData....
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
    
    for game, gameId in final.items():
        gameAdd(game, gameId, GameStore.ORIGIN)
                        
# getOriginIDs()
# getSteamIDs()
# print(GAME_LIST_MASTER)


''' Finding Uplay IDs Old Method -> Depricated '''

# def getUplayIDs(filePath = 'C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\data'):
#     listOfFiles = os.listdir(filePath)

#     def findIDs():
#         result = re.findall(r'\d+', str(entry))
#         try : return result[0]
#         except : pass

#     for entry in listOfFiles:
#         uPlayID = findIDs() # '\d' finds any number (a digit)
#         if uPlayID != None : print(uPlayID)       
# # getUplayIDs()

''' 
Finding Uplay IDs via registry 
------------------------------
Uplay afaik doesn't have user accessible data files. So had to go WinRegistry route
Even their game icons have "encrypted" names. 
The Uplay IDs have key values stored in them which contain their install directory.
'''
def getUplayIDs():
    # WOW6432Node -> Represents you are on a 64 bit machines 
    # If someone can port this to work for 32 bit machines as well Thanks!
    baseReg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    subKey = winreg.OpenKey(baseReg, "SOFTWARE\\WOW6432Node\\Ubisoft\\Launcher\\Installs\\")

    for _ in range(50) :
        try :
            gameId = winreg.EnumKey(subKey, _)

            gameNameKey = winreg.OpenKey(baseReg, "SOFTWARE\\WOW6432Node\\Ubisoft\\Launcher\\Installs\\" + gameId + "\\")
            name = winreg.EnumValue(gameNameKey, 1)     # Name is a list of keys returned by the func
            path = name[1]                              # The pos 1 contains Game Directory
            path = os.path.dirname(path)
            gameName = os.path.basename(path)           # The path name is actually the ID for the game

            # print('\nThe Game name is: ' + gameName + ' \nThe Game ID is: ' + gameId)
            # GAME_LIST_MASTER[gameName] = gameId
            gameAdd(gameName, gameId, GameStore.UPLAY)

        except :
            pass

    winreg.CloseKey(baseReg)
    

''' 
Finding Epic Games Launcher codenames 
-------------------------------------
Epic Games Launcher uses "special" codenames for each of their games.
I don't know why? Seems extra work
They follow a specific naming theme : All are either flowers / animals
'''
def getEpicIDs(filePath = 'C:\\ProgramData\\Epic\\UnrealEngineLauncher\\LauncherInstalled.dat'):
    with open(filePath) as datFile:
        
        data = json.load(datFile)
        codeName = nested_lookup('AppName', data) # returns a list of codeNames
        
        gameName = []
        dirPath = nested_lookup('InstallLocation', data) # returns a directory path
        for name in dirPath:
            name = re.search(r"(\\)(\w+)($)", name) # Regex for finding the game's name from the directory path
            gameName.append(name.group().strip('\\'))
    
    final = dict(zip(gameName, codeName)) # combining the game's actual name with the codename
    
    for game, codeName in final.items():        # Adding game details to the master list
        gameAdd(game, codeName, GameStore.EGS)
    
    
#getEpicIDs()
#print(GAME_LIST_MASTER)


'''
Check if the game exists
Return the gameID and game's store
'''
def gameSearch(game: str):
    gameFound = nested_lookup(game, GAME_LIST_MASTER)
    return gameFound


'''
gameInfo initially is a double list. Meaning gameInfo = [[gameId, gameStore]]
[gameInfo] strips down the additional listt = [gameId, gameStore]
gameObj is there to check the Game Store for the game so we can differentiate launch commands
Eg: IF STEAM THEN CMD = "steam://rungameid/"
This CMD is grabbed from the GameStore Enum by .value
'''
def launchGame(game: str):
    try:
        [gameInfo] = gameSearch(game)
    except:
        raise Exception('Check your game Name')
    gameId  = gameInfo[0] 
    gameStoreName = gameInfo[1]

    if(gameStoreName == 'STEAM'):
        launchStruc = GameStore.STEAM.value
        os.startfile(launchStruc + str(gameId))     # Search for an optional -silent flag if possible

    elif(gameStoreName == 'ORIGIN'):
        launchStruc = GameStore.ORIGIN.value
        os.startfile(launchStruc + str(gameId))
    
    elif(gameStoreName ==  'EGS'):
        launchStruc = GameStore.EGS.value
        os.startfile(launchStruc + gameId + '?action=launch&silent=true')
        
    elif(gameStoreName ==  'UPLAY'):
        launchStruc = GameStore.UPLAY.value
        os.startfile(launchStruc + gameId + '/0')

    else:
        print('Something went wrong')

# launchGame('Apex')

# Read the gameList data file and dump into a dict
def readData():
    with open('data\\gameList.plei', 'rb') as f:
        # print(pickle.load(f))
        return pickle.load(f)   #returns dict

# Update the gameList data file
def writeData(gameList: dict):
    with open('data\\gameList.plei', 'wb') as f:
       pickle.dump(gameList, f)

# Syncs the master list to all the installed games
def sync(GAME_LIST_MASTER = GAME_LIST_MASTER):
    getOriginIDs()
    getSteamIDs()
    getEpicIDs()
    getUplayIDs()
    writeData(GAME_LIST_MASTER)

# sync()    
# print(GAME_LIST_MASTER)








#---------------------------------------------------------------------------------------------
# Alternative method to get the appIDs for the games
# extract the STEAM_ID from that file name
# The regex re.findall() returns ['STEAM_ID'] so it is a list with just 1 value in it at the 0th position


# def getSteamIDs(filePath):
#     listOfFiles = os.listdir(filePath)
#     pattern = "*.acf"
#     for entry in listOfFiles:
#         if fnmatch.fnmatch(entry, pattern):
#             extractedSteamID = re.findall(r'\d+', str(entry)) # '\d' finds any number (a digit)
#             STEAM_ID.append(extractedSteamID[0])

          

