import urllib.request
import re 

def retrieveImg(gameName, imgURL):
    gameName = legalFileName(gameName)     # Windows doesn't like weird stuff in filenames
    location = 'data\\img\\'
    urllib.request.urlretrieve(imgURL, (location + gameName + ".png"))

# Making sure windows doesn't cry if : or similar characters appear in the game name
def legalFileName(inString):
    checkList = ['<', '>', ':', '"', '/', '\\', '|', '?', '?', '*', '.', ',']
    for i in checkList:
        if i in inString:
            inString = inString.replace(i, '')
    return inString

