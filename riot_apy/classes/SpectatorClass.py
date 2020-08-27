class Observer:
    def __init__(self, raw={}):
        self.__encryptionKey = raw['encryptionKey'] if 'encryptionKey' in raw else None

    @property
    def encryptionKey(self) -> str:
        return self.__encryptionKey


class CurrentGameInfo:
    def __init__(self, raw={}):
        self.__gameId = raw['gameId'] if 'gameId' in raw else None
        self.__gameType = raw['gameType'] if 'gameType' in raw else None
        self.__gameStartTime = raw['gameStartTime'] if 'gameStartTime' in raw else None
        self.__mapId = raw['mapId'] if 'mapId' in raw else None
        self.__gameLength = raw['gameLength'] if 'gameLength' in raw else None
        self.__platformId = raw['platformId'] if 'platformId' in raw else None
        self.__gameMode = raw['gameMode'] if 'gameMode' in raw else None
        self.__bannedChampions = [BannedChampion(champ) for champ in raw['bannedChampions']] if 'bannedChampions' in raw else []
        self.__gameQueueConfigId = raw['gameQueueConfigId'] if 'gameQueueConfigId' in raw else None
        self.__observers = Observer(raw['observers']) if 'observers' in raw else Observer()
        self.__participants = [CurrentGameParticipant(part) for part in raw['participants']] if 'participants' in raw else []

    @property
    def gameId(self) -> int:
        return self.__gameId

    @property
    def gameType(self) -> str:
        return self.__gameType

    @property
    def gameStartTime(self) -> int:
        return self.__gameStartTime

    @property
    def mapId(self) -> int:
        return self.__mapId

    @property
    def gameLength(self) -> int:
        return self.__gameLength

    @property
    def platformId(self) -> str:
        return self.__platformId

    @property
    def gameMode(self) -> str:
        return self.__gameMode

    @property
    def bannedChampions(self) -> list:
        return self.__bannedChampions

    @property
    def gameQueueConfigId(self) -> int:
        return self.__gameQueueConfigId

    @property
    def observers(self) -> Observer:
        return self.__observers

    @property
    def participants(self) -> list:
        return self.__participants


class BannedChampion:
    def __init__(self, raw={}):
        self.__pickTurn = raw['pickTurn'] if 'pickTurn' in raw else None
        self.__championId = raw['championId'] if 'championId' in raw else None
        self.__teamId = raw['teamId'] if 'teamId' in raw else None

    @property
    def pickTurn(self) -> int:
        return self.__pickTurn

    @property
    def championId(self) -> int:
        return self.__championId

    @property
    def teamId(self) -> int:
        return self.__teamId


class Perks:
    def __init__(self, raw={}):
        self.__perkIds = raw['perkIds'] if 'perkIds' in raw else []
        self.__perkStyle = raw['perkStyle'] if 'perkStyle' in raw else None
        self.__perkSubStyle = raw['perkSubStyle'] if 'perkSubStyle' in raw else None

    @property
    def perkIds(self) -> list:
        return self.__perkIds

    @property
    def perkStyle(self) -> int:
        return self.__perkStyle

    @property
    def perkSubStyle(self) -> int:
        return self.__perkSubStyle


class CurrentGameParticipant:
    def __init__(self, raw={}):
        self.__championId = raw['championId'] if 'championId' in raw else None
        self.__perks = Perks(raw['perks']) if 'perks' in raw else Perks()
        self.__profileIconId = raw['profileIconId'] if 'profileIconId' in raw else None
        self.__bot = raw['bot'] if 'bot' in raw else None
        self.__teamId = raw['teamId'] if 'teamId' in raw else None
        self.__summonerName = raw['summonerName'] if 'summonerName' in raw else None
        self.__summonerId = raw['summonerId'] if 'summonerId' in raw else None
        self.__spell1Id = raw['spell1Id'] if 'spell1Id' in raw else None
        self.__spell2Id = raw['spell2Id'] if 'spell2Id' in raw else None
        self.__gameCustomizationObjects = [GameCustomizationObject(obj) for obj in raw['gameCustomizationObjects']] if 'gameCustomizationObjects' in raw else []

    @property
    def championId(self) -> int:
        return self.__championId

    @property
    def perks(self) -> Perks:
        return self.__perks

    @property
    def profileIconId(self) -> int:
        return self.__profileIconId

    @property
    def bot(self) -> bool:
        return self.__bot

    @property
    def teamId(self) -> int:
        return self.__teamId

    @property
    def summonerName(self) -> str:
        return self.__summonerName

    @property
    def summonerId(self) -> str:
        return self.__summonerId

    @property
    def spell1Id(self) -> int:
        return self.__spell1Id

    @property
    def spell2Id(self) -> int:
        return self.__spell2Id

    @property
    def gameCustomizationObjects(self) -> list:
        return self.__gameCustomizationObjects


class GameCustomizationObject:
    def __init__(self, raw={}):
        self.__category = raw['category'] if 'category' in raw else None
        self.__content = raw['content'] if 'content' in raw else None

    @property
    def category(self) -> str:
        return self.__category

    @property
    def content(self) -> str:
        return self.__content


class FeaturedGames:
    def __init__(self, raw={}):
        self.__gameList = [FeaturedGameInfo(game) for game in raw['gameList']] if 'gameList' in raw else []
        self.__clientRefreshInterval = raw['clientRefreshInterval'] if 'clientRefreshInterval' in raw else None

    @property
    def gameList(self) -> list:
        return self.__gameList

    @property
    def clientRefreshInterval(self) -> int:
        return self.__clientRefreshInterval


class FeaturedGameInfo:
    def __init__(self, raw={}):
        self.__gameId = raw['gameId'] if 'gameId' in raw else None
        self.__gameType = raw['gameType'] if 'gameType' in raw else None
        self.__gameStartTime = raw['gameStartTime'] if 'gameStartTime' in raw else None
        self.__mapId = raw['mapId'] if 'mapId' in raw else None
        self.__gameLength = raw['gameLength'] if 'gameLength' in raw else None
        self.__platformId = raw['platformId'] if 'platformId' in raw else None
        self.__gameMode = raw['gameMode'] if 'gameMode' in raw else None
        self.__bannedChampions = [BannedChampion(champ) for champ in raw['bannedChampions']] if 'bannedChampions' in raw else []
        self.__gameQueueConfigId = raw['gameQueueConfigId'] if 'gameQueueConfigId' in raw else None
        self.__observers = Observer(raw['observers']) if 'observers' in raw else Observer()
        self.__participants = [SpecParticipant(part) for part in raw['participants']] if 'participants' in raw else []

    @property
    def gameId(self) -> int:
        return self.__gameId

    @property
    def gameType(self) -> str:
        return self.__gameType

    @property
    def gameStartTime(self) -> int:
        return self.__gameStartTime

    @property
    def mapId(self) -> int:
        return self.__mapId

    @property
    def gameLength(self) -> int:
        return self.__gameLength

    @property
    def platformId(self) -> str:
        return self.__platformId

    @property
    def gameMode(self) -> str:
        return self.__gameMode

    @property
    def bannedChampions(self) -> list:
        return self.__bannedChampions

    @property
    def gameQueueConfigId(self) -> int:
        return self.__gameQueueConfigId

    @property
    def observers(self) -> Observer:
        return self.__observers

    @property
    def participants(self) -> list:
        return self.__participants


class SpecParticipant:
    def __init__(self, raw={}):
        self.__championId = raw['championId'] if 'championId' in raw else None
        self.__profileIconId = raw['profileIconId'] if 'profileIconId' in raw else None
        self.__bot = raw['bot'] if 'bot' in raw else None
        self.__teamId = raw['teamId'] if 'teamId' in raw else None
        self.__summonerName = raw['summonerName'] if 'summonerName' in raw else None
        self.__spell1Id = raw['spell1Id'] if 'spell1Id' in raw else None
        self.__spell2Id = raw['spell2Id'] if 'spell2Id' in raw else None

    @property
    def championId(self) -> int:
        return self.__championId

    @property
    def profileIconId(self) -> int:
        return self.__profileIconId

    @property
    def bot(self) -> bool:
        return self.__bot

    @property
    def teamId(self) -> int:
        return self.__teamId

    @property
    def summonerName(self) -> str:
        return self.__summonerName

    @property
    def spell1Id(self) -> int:
        return self.__spell1Id

    @property
    def spell2Id(self) -> int:
        return self.__spell2Id
