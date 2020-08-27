class ChampionMastery:
    def __init__(self, raw={}):
        self.__championId = raw['championId'] if 'championId' in raw else None
        self.__championPointsUntilNextLevel = raw['championPointsUntilNextLevel'] if 'championPointsUntilNextLevel' in raw else None
        self.__championPointsSinceLastLevel = raw['championPointsSinceLastLevel'] if 'championPointsSinceLastLevel' in raw else None
        self.__chestGranted = raw['chestGranted'] if 'chestGranted' in raw else None
        self.__lastPlayTime = raw['lastPlayTime'] if 'lastPlayTime' in raw else None
        self.__championLevel = raw['championLevel'] if 'championLevel' in raw else None
        self.__summonerId = raw['summonerId'] if 'summonerId' in raw else None
        self.__championPoints = raw['championPoints'] if 'championPoints' in raw else None
        self.__tokensEarned = raw['tokensEarned'] if 'tokensEarned' in raw else None

    @property
    def championId(self) -> int:
        return self.__championId

    @property
    def championPointsUntilNextLevel(self) -> int:
        return self.__championPointsUntilNextLevel

    @property
    def championPointsSinceLastLevel(self) -> int:
        return self.__championPointsSinceLastLevel

    @property
    def chestGranted(self) -> bool:
        return self.__chestGranted

    @property
    def lastPlayTime(self) -> int:
        return self.__lastPlayTime

    @property
    def championLevel(self) -> int:
        return self.__championLevel

    @property
    def summonerId(self) -> str:
        return self.__summonerId

    @property
    def championPoints(self) -> int:
        return self.__championPoints

    @property
    def tokensEarned(self) -> int:
        return self.__tokensEarned
