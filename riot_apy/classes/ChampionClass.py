class ChampionInfo:
    def __init__(self, raw={}):
        self.__maxNewPlayerLevel = raw['maxNewPlayerLevel'] if 'maxNewPlayerLevel' in raw else None
        self.__freeChampionIdsForNewPlayers = raw['freeChampionIdsForNewPlayers'] if 'freeChampionIdsForNewPlayers' in raw else []
        self.__freeChampionIds = raw['freeChampionIds'] if 'freeChampionIds' in raw else []

    @property
    def maxNewPlayerLevel(self) -> int:
        return self.__maxNewPlayerLevel

    @property
    def freeChampionIdsForNewPlayers(self) -> list:
        return self.__freeChampionIdsForNewPlayers

    @property
    def freeChampionIds(self) -> list:
        return self.__freeChampionIds
