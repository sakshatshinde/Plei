import enum

class Game:
    def __init__(self, name, gameId, gameStore):
        self.name = name 
        self.gameId = gameId
        self.gameStore = gameStore

class GameStore(enum.Enum):
    STEAM = "steam://rungameid/"
    EGS = "com.epicgames.launcher://apps/" # + ?action=launch&silent=true"
    UPLAY = "uplay://launch/"   # launch/ID/0
    ORIGIN = "origin://launchgame/"
    PIRATED = "PIRATED"
    
