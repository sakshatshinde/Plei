from gameOps import storeDirectory, GAME_DIRS, GAME_LIST_MASTER

# User input for ORIGN/UPLAY/STANDALONE directories
gameStore, storeDir = input('Game Store name: '), input('Game store Dir: ')

#For Steam
if(gameStore == "STEAM"):
    storeDir = storeDir + '\\steamapps\\'
    storeDirectory(gameStore, storeDir)

#For Others
else:
    storeDir = storeDir + '\\'
    storeDirectory(gameStore, storeDir)

