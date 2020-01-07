import enum
class Game:
    def __init__(self, name, gameId, gameStore):
        self.name = name 
        self.gameId = gameId
        self.gameStore = gameStore

class GameStore(enum.Enum):
    STEAM = "steam://rungameid/"
    EGS = "EGS"
    UPLAY = "uplay://launch/"
    ORIGIN = "origin://launchgame/"
    PIRATED = "PIRATED"
    
