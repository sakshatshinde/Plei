import urllib.request

def retrieveImg(gameName, imgURL):
    location = 'data\\img\\'
    urllib.request.urlretrieve(imgURL, (location + gameName + ".png"))