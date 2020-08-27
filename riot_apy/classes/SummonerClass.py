class Summoner:
    def __init__(self, raw):
        self.__accountId = raw['accountId'] if 'accountId' in raw else None
        self.__profileIconId = raw['profileIconId'] if 'profileIconId' in raw else None
        self.__revisionDate = raw['revisionDate'] if 'revisionDate' in raw else None
        self.__name = raw['name'] if 'name' in raw else None
        self.__id = raw['id'] if 'id' in raw else None
        self.__puuid = raw['puuid'] if 'puuid' in raw else None
        self.__summonerLevel = raw['summonerLevel'] if 'summonerLevel' in raw else None

    @property
    def accountId(self) -> str:
        return self.__accountId

    @property
    def profileIconId(self) -> int:
        return self.__profileIconId

    @property
    def revisionDate(self) -> int:
        return self.__revisionDate

    @property
    def name(self) -> str:
        return self.__name

    @property
    def id(self) -> str:
        return self.__id

    @property
    def puuid(self) -> str:
        return self.__puuid

    @property
    def summonerLevel(self) -> int:
        return self.__summonerLevel
