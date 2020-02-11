import pickle

# Read the dirList data file and dump into a dict
def readDirList():
    with open('data\\dirList.plei', 'rb') as f:
        # print(pickle.load(f))
        return pickle.load(f)   #returns dict

GAME_DIRS = readDirList()
# Storing directories of game stores

global originPath, uPlayPath, steamPath, standalonePath, egsPath

def storeDirectory(gameStore, storeDir) -> str:

    if(gameStore == "ORIGIN"):
        originPath = storeDir
        GAME_DIRS[gameStore] = originPath
        return(originPath)

    if(gameStore == "UPLAY"):
        uPlayPath = storeDir
        GAME_DIRS[gameStore] = uPlayPath
        return(uPlayPath)

    if(gameStore == "STANDALONE"):
        standalonePath = storeDir
        GAME_DIRS[gameStore] = standalonePath
        return(standalonePath)

    if(gameStore == "STEAM"):
        steamPath = storeDir
        GAME_DIRS[gameStore] = steamPath
        return(steamPath)
    
    if(gameStore == "EGS"):
        egsPath = storeDir
        GAME_DIRS[gameStore] = egsPath
        return(steamPath)

# storeDirectory('STEAM','C:\\Program Files (x86)\\Origin Games')
# print(GAME_DIRS)
def selection():
    while True:
        print("Select a game store")
        sel = int(input("\n 1: STEAM \n 2: EGS \n 3: ORIGIN \n 4: UPLAY \n 5: Standalone \n 6: Done"))
        dirLoc = str(input("Input the directory location"))

        if sel == 1: storeDirectory('STEAM', dirLoc)
        if sel == 2: storeDirectory('EGS', dirLoc)
        if sel == 3: storeDirectory('ORIGIN', dirLoc)
        if sel == 4: storeDirectory('UPLAY', dirLoc)
        if sel == 5: storeDirectory('Standalone', dirLoc)
        if sel == 6: break

    return 'We are all set!!'

# Update the dirList data file
def writeDirList(dirList: dict):
    with open('data\\dirList.plei', 'wb') as f:
       pickle.dump(dirList, f)

# readDirList()
writeDirList(GAME_DIRS)