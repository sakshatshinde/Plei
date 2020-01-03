import enum
class GameList:
    def __init__(self, name, gameId, gameStore):
        self.name = name 
        self.gameId = gameId
        self.gameStore = gameStore

class GameStore(enum.Enum):
    STEAM = "STEAM"
    EGS = "EGS"
    UPLAY = "UPLAY"
    ORIGIN = "ORIGIN"
    GOG = "GOG"
    PIRATED = "PIRATED"
    
