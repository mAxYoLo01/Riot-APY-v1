class LeagueList:
    def __init__(self, raw={}):
        self.__leagueId = raw['leagueId'] if 'leagueId' in raw else None
        self.__entries = [LeagueItem(entry) for entry in raw['entries']] if 'entries' in raw else []
        self.__tier = raw['tier'] if 'tier' in raw else None
        self.__name = raw['name'] if 'name' in raw else None
        self.__queue = raw['queue'] if 'queue' in raw else None

    @property
    def leagueId(self) -> str:
        return self.__leagueId

    @property
    def entries(self) -> list:
        return self.__entries

    @property
    def tier(self) -> str:
        return self.__tier

    @property
    def name(self) -> str:
        return self.__name

    @property
    def queue(self) -> str:
        return self.__queue


class MiniSeries:
    def __init__(self, raw={}):
        self.__losses = raw['losses'] if 'losses' in raw else None
        self.__progress = raw['progress'] if 'progress' in raw else None
        self.__target = raw['target'] if 'target' in raw else None
        self.__wins = raw['wins'] if 'wins' in raw else None

    @property
    def losses(self) -> int:
        return self.__losses

    @property
    def progress(self) -> str:
        return self.__progress

    @property
    def target(self) -> int:
        return self.__target

    @property
    def wins(self) -> int:
        return self.__wins


class LeagueItem:
    def __init__(self, raw={}):
        self.__freshBlood = raw['freshBlood'] if 'freshBlood' in raw else None
        self.__wins = raw['wins'] if 'wins' in raw else None
        self.__summonerName = raw['summonerName'] if 'summonerName' in raw else None
        self.__miniSeries = MiniSeries(raw['miniSeries']) if 'miniSeries' in raw else MiniSeries()
        self.__inactive = raw['inactive'] if 'inactive' in raw else None
        self.__veteran = raw['veteran'] if 'veteran' in raw else None
        self.__hotStreak = raw['hotStreak'] if 'hotStreak' in raw else None
        self.__rank = raw['rank'] if 'rank' in raw else None
        self.__leaguePoints = raw['leaguePoints'] if 'leaguePoints' in raw else None
        self.__losses = raw['losses'] if 'losses' in raw else None
        self.__summonerId = raw['summonerId'] if 'summonerId' in raw else None

    @property
    def freshBlood(self) -> bool:
        return self.__freshBlood

    @property
    def wins(self) -> int:
        return self.__wins

    @property
    def summonerName(self) -> str:
        return self.__summonerName

    @property
    def miniSeries(self) -> MiniSeries:
        return self.__miniSeries

    @property
    def inactive(self) -> bool:
        return self.__inactive

    @property
    def veteran(self) -> bool:
        return self.__veteran

    @property
    def hotStreak(self) -> bool:
        return self.__hotStreak

    @property
    def rank(self) -> str:
        return self.__rank

    @property
    def leaguePoints(self) -> int:
        return self.__leaguePoints

    @property
    def losses(self) -> int:
        return self.__losses

    @property
    def summonerId(self) -> str:
        return self.__summonerId


class LeagueEntry:
    def __init__(self, raw={}):
        self.__freshBlood = raw['freshBlood'] if 'freshBlood' in raw else None
        self.__wins = raw['wins'] if 'wins' in raw else None
        self.__summonerName = raw['summonerName'] if 'summonerName' in raw else None
        self.__miniSeries = MiniSeries(raw['miniSeries']) if 'miniSeries' in raw else MiniSeries()
        self.__inactive = raw['inactive'] if 'inactive' in raw else None
        self.__veteran = raw['veteran'] if 'veteran' in raw else None
        self.__hotStreak = raw['hotStreak'] if 'hotStreak' in raw else None
        self.__rank = raw['rank'] if 'rank' in raw else None
        self.__leaguePoints = raw['leaguePoints'] if 'leaguePoints' in raw else None
        self.__losses = raw['losses'] if 'losses' in raw else None
        self.__summonerId = raw['summonerId'] if 'summonerId' in raw else None
        self.__leagueId = raw['leagueId'] if 'leagueId' in raw else None
        self.__queueType = raw['queueType'] if 'queueType' in raw else None
        self.__tier = raw['tier'] if 'tier' in raw else None

    @property
    def freshBlood(self) -> bool:
        return self.__freshBlood

    @property
    def wins(self) -> int:
        return self.__wins

    @property
    def summonerName(self) -> str:
        return self.__summonerName

    @property
    def miniSeries(self) -> MiniSeries:
        return self.__miniSeries

    @property
    def inactive(self) -> bool:
        return self.__inactive

    @property
    def veteran(self) -> bool:
        return self.__veteran

    @property
    def hotStreak(self) -> bool:
        return self.__hotStreak

    @property
    def rank(self) -> str:
        return self.__rank

    @property
    def leaguePoints(self) -> int:
        return self.__leaguePoints

    @property
    def losses(self) -> int:
        return self.__losses

    @property
    def summonerId(self) -> str:
        return self.__summonerId

    @property
    def leagueId(self) -> str:
        return self.__leagueId

    @property
    def queueType(self) -> str:
        return self.__queueType

    @property
    def tier(self) -> str:
        return self.__tier
