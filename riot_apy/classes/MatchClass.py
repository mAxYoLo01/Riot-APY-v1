class Match:
    def __init__(self, raw={}):
        self.__gameId = raw['gameId'] if 'gameId' in raw else None
        self.__queueId = raw['queueId'] if 'queueId' in raw else None
        self.__gameType = raw['gameType'] if 'gameType' in raw else None
        self.__mapId = raw['mapId'] if 'mapId' in raw else None
        self.__platformId = raw['platformId'] if 'platformId' in raw else None
        self.__seasonId = raw['seasonId'] if 'seasonId' in raw else None
        self.__gameVersion = raw['gameVersion'] if 'gameVersion' in raw else None
        self.__gameMode = raw['gameMode'] if 'gameMode' in raw else None
        self.__gameCreation = raw['gameCreation'] if 'gameCreation' in raw else None
        self.__gameDuration = raw['gameDuration'] if 'gameDuration' in raw else None
        self.__teams = [TeamStat(stat) for stat in raw['teams']] if 'teams' in raw else []
        self.__participantIdentities = [ParticipantIdentity(identity) for identity in raw['participantIdentities']] if 'participantIdentities' in raw else []
        self.__participants = [Participant(participant) for participant in raw['participants']] if 'participants' in raw else []

    @property
    def gameId(self) -> int:
        return self.__gameId

    @property
    def queueId(self) -> int:
        return self.__queueId

    @property
    def gameType(self) -> str:
        return self.__gameType

    @property
    def mapId(self) -> int:
        return self.__mapId

    @property
    def platformId(self) -> str:
        return self.__platformId

    @property
    def seasonId(self) -> int:
        return self.__seasonId

    @property
    def gameVersion(self) -> str:
        return self.__gameVersion

    @property
    def gameMode(self) -> str:
        return self.__gameMode

    @property
    def gameCreation(self) -> int:
        return self.__gameCreation

    @property
    def gameDuration(self) -> int:
        return self.__gameDuration

    @property
    def teams(self) -> list:
        return self.__teams

    @property
    def participantIdentities(self) -> list:
        return self.__participantIdentities

    @property
    def participants(self) -> list:
        return self.__participants


class TeamStat:
    def __init__(self, raw={}):
        self.__teamId = raw['teamId'] if 'teamId' in raw else None
        self.__win = raw['win'] if 'win' in raw else None
        self.__towerKills = raw['towerKills'] if 'towerKills' in raw else None
        self.__inhibitorKills = raw['inhibitorKills'] if 'inhibitorKills' in raw else None
        self.__riftHeraldKills = raw['riftHeraldKills'] if 'riftHeraldKills' in raw else None
        self.__dragonKills = raw['dragonKills'] if 'dragonKills' in raw else None
        self.__baronKills = raw['baronKills'] if 'baronKills' in raw else None
        self.__firstBlood = raw['firstBlood'] if 'firstBlood' in raw else None
        self.__firstTower = raw['firstTower'] if 'firstTower' in raw else None
        self.__firstInhibitor = raw['firstInhibitor'] if 'firstInhibitor' in raw else None
        self.__firstRiftHerald = raw['firstRiftHerald'] if 'firstRiftHerald' in raw else None
        self.__firstDragon = raw['firstDragon'] if 'firstDragon' in raw else None
        self.__firstBaron = raw['firstBaron'] if 'firstBaron' in raw else None
        self.__bans = [TeamBan(ban) for ban in raw['bans']] if 'bans' in raw else []

    @property
    def teamId(self) -> int:
        return self.__teamId

    @property
    def win(self) -> str:
        return self.__win

    @property
    def towerKills(self) -> int:
        return self.__towerKills

    @property
    def inhibitorKills(self) -> int:
        return self.__inhibitorKills

    @property
    def riftHeraldKills(self) -> int:
        return self.__riftHeraldKills

    @property
    def dragonKills(self) -> int:
        return self.__dragonKills

    @property
    def baronKills(self) -> int:
        return self.__baronKills

    @property
    def firstBlood(self) -> bool:
        return self.__firstBlood

    @property
    def firstTower(self) -> bool:
        return self.__firstTower

    @property
    def firstInhibitor(self) -> bool:
        return self.__firstInhibitor

    @property
    def firstRiftHerald(self) -> bool:
        return self.__firstRiftHerald

    @property
    def firstDragon(self) -> bool:
        return self.__firstDragon

    @property
    def firstBaron(self) -> bool:
        return self.__firstBaron

    @property
    def bans(self) -> list:
        return self.__bans


class TeamBan:
    def __init__(self, raw={}):
        self.__championId = raw['championId'] if 'championId' in raw else None
        self.__pickTurn = raw['pickTurn'] if 'pickTurn' in raw else None

    @property
    def championId(self) -> int:
        return self.__championId

    @property
    def pickTurn(self) -> int:
        return self.__pickTurn


class Player:
    def __init__(self, raw={}):
        self.__profileIcon = raw['profileIcon'] if 'profileIcon' in raw else None
        self.__accountId = raw['accountId'] if 'accountId' in raw else None
        self.__matchHistoryUri = raw['matchHistoryUri'] if 'matchHistoryUri' in raw else None
        self.__currentAccountId = raw['currentAccountId'] if 'currentAccountId' in raw else None
        self.__currentPlatformId = raw['currentPlatformId'] if 'currentPlatformId' in raw else None
        self.__summonerName = raw['summonerName'] if 'summonerName' in raw else None
        self.__summonerId = raw['summonerId'] if 'summonerId' in raw else None
        self.__platformId = raw['platformId'] if 'platformId' in raw else None

    @property
    def profileIcon(self) -> int:
        return self.__profileIcon

    @property
    def accountId(self) -> str:
        return self.__accountId

    @property
    def matchHistoryUri(self) -> str:
        return self.__matchHistoryUri

    @property
    def currentAccountId(self) -> str:
        return self.__currentAccountId

    @property
    def currentPlatformId(self) -> str:
        return self.__currentPlatformId

    @property
    def summonerName(self) -> str:
        return self.__summonerName

    @property
    def summonerId(self) -> str:
        return self.__summonerId

    @property
    def platformId(self) -> str:
        return self.__platformId


class ParticipantIdentity:
    def __init__(self, raw={}):
        self.__participantId = raw['participantId'] if 'participantId' in raw else None
        self.__player = Player(raw['player']) if 'player' in raw else Player()

    @property
    def participantId(self) -> int:
        return self.__participantId

    @property
    def player(self) -> Player:
        return self.__player


class ParticipantTimeline:
    def __init__(self, raw={}):
        self.__participantId = raw['participantId'] if 'participantId' in raw else None
        self.__role = raw['role'] if 'role' in raw else None
        self.__lane = raw['lane'] if 'lane' in raw else None
        self.__csDiffPerMinDeltas = raw['csDiffPerMinDeltas'] if 'csDiffPerMinDeltas' in raw else {}
        self.__damageTakenPerMinDeltas = raw['damageTakenPerMinDeltas'] if 'damageTakenPerMinDeltas' in raw else {}
        self.__damageTakenDiffPerMinDeltas = raw['damageTakenDiffPerMinDeltas'] if 'damageTakenDiffPerMinDeltas' in raw else {}
        self.__xpPerMinDeltas = raw['xpPerMinDeltas'] if 'xpPerMinDeltas' in raw else {}
        self.__xpDiffPerMinDeltas = raw['xpDiffPerMinDeltas'] if 'xpDiffPerMinDeltas' in raw else {}
        self.__creepsPerMinDeltas = raw['creepsPerMinDeltas'] if 'creepsPerMinDeltas' in raw else {}
        self.__goldPerMinDeltas = raw['goldPerMinDeltas'] if 'goldPerMinDeltas' in raw else {}

    @property
    def participantId(self) -> int:
        return self.__participantId

    @property
    def role(self) -> str:
        return self.__role

    @property
    def lane(self) -> str:
        return self.__lane

    @property
    def csDiffPerMinDeltas(self) -> dict:
        return self.__csDiffPerMinDeltas

    @property
    def damageTakenPerMinDeltas(self) -> dict:
        return self.__damageTakenPerMinDeltas

    @property
    def damageTakenDiffPerMinDeltas(self) -> dict:
        return self.__damageTakenDiffPerMinDeltas

    @property
    def xpPerMinDeltas(self) -> dict:
        return self.__xpPerMinDeltas

    @property
    def xpDiffPerMinDeltas(self) -> dict:
        return self.__xpDiffPerMinDeltas

    @property
    def creepsPerMinDeltas(self) -> dict:
        return self.__creepsPerMinDeltas

    @property
    def goldPerMinDeltas(self) -> dict:
        return self.__goldPerMinDeltas


class Participant:
    def __init__(self, raw={}):
        self.__participantId = raw['participantId'] if 'participantId' in raw else None
        self.__championId = raw['championId'] if 'championId' in raw else None
        self.__teamId = raw['teamId'] if 'teamId' in raw else None
        self.__spell1Id = raw['spell1Id'] if 'spell1Id' in raw else None
        self.__spell2Id = raw['spell2Id'] if 'spell2Id' in raw else None
        self.__highestAchievedSeasonTier = raw['highestAchievedSeasonTier'] if 'highestAchievedSeasonTier' in raw else None
        self.__timeline = ParticipantTimeline(raw['timeline']) if 'timeline' in raw else ParticipantTimeline()
        # self.stats = ParticipantStat(raw['stats']) TODO

    @property
    def participantId(self) -> int:
        return self.__participantId

    @property
    def championId(self) -> int:
        return self.__championId

    @property
    def teamId(self) -> int:
        return self.__teamId

    @property
    def spell1Id(self) -> int:
        return self.__spell1Id

    @property
    def spell2Id(self) -> int:
        return self.__spell2Id

    @property
    def highestAchievedSeasonTier(self) -> str:
        return self.__highestAchievedSeasonTier

    @property
    def timeline(self) -> ParticipantTimeline:
        return self.__timeline


class Matchlist:
    def __init__(self, raw={}):
        self.__startIndex = raw['startIndex'] if 'startIndex' in raw else None
        self.__endIndex = raw['endIndex'] if 'endIndex' in raw else None
        self.__totalGames = raw['totalGames'] if 'totalGames' in raw else None
        self.__matches = [MatchReference(ref) for ref in raw['matches']] if 'matches' in raw else []

    @property
    def startIndex(self) -> int:
        return self.__startIndex

    @property
    def endIndex(self) -> int:
        return self.__endIndex

    @property
    def totalGames(self) -> int:
        return self.__totalGames

    @property
    def matches(self) -> list:
        return self.__matches


class MatchReference:
    def __init__(self, raw={}):
        self.__gameId = raw['gameId'] if 'gameId' in raw else None
        self.__role = raw['role'] if 'role' in raw else None
        self.__lane = raw['lane'] if 'lane' in raw else None
        self.__season = raw['season'] if 'season' in raw else None
        self.__platformId = raw['platformId'] if 'platformId' in raw else None
        self.__champion = raw['champion'] if 'champion' in raw else None
        self.__queue = raw['queue'] if 'queue' in raw else None
        self.__timestamp = raw['timestamp'] if 'timestamp' in raw else None

    @property
    def gameId(self) -> int:
        return self.__gameId

    @property
    def role(self) -> str:
        return self.__role

    @property
    def lane(self) -> str:
        return self.__lane

    @property
    def season(self) -> int:
        return self.__season

    @property
    def platformId(self) -> str:
        return self.__platformId

    @property
    def champion(self) -> int:
        return self.__champion

    @property
    def queue(self) -> int:
        return self.__queue

    @property
    def timestamp(self) -> int:
        return self.__timestamp


class MatchTimeline:
    def __init__(self, raw={}):
        self.__frames = [MatchFrame(frame) for frame in raw['frames']] if 'frames' in raw else []
        self.__frameInterval = raw['frameInterval'] if 'frameInterval' in raw else None

    @property
    def frames(self) -> list:
        return self.__frames

    @property
    def frameInterval(self) -> int:
        return self.__frameInterval


class MatchFrame:
    def __init__(self, raw={}):
        self.__participantFrames = {key: MatchParticipantFrame(value) for key, value in raw['participantFrames'].items()} if 'participantFrames' in raw else {}
        self.__events = [MatchEvent(event) for event in raw['events']] if 'events' in raw else []
        self.__timestamp = raw['timestamp'] if 'timestamp' in raw else None

    @property
    def participantFrames(self) -> dict:
        return self.__participantFrames

    @property
    def events(self) -> list:
        return self.__events

    @property
    def timestamp(self) -> int:
        return self.__timestamp


class MatchPosition:
    def __init__(self, raw={}):
        self.__x = raw['x'] if 'x' in raw else None
        self.__y = raw['y'] if 'y' in raw else None

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y


class MatchParticipantFrame:
    def __init__(self, raw={}):
        self.__participantId = raw['participantId'] if 'participantId' in raw else None
        self.__minionsKilled = raw['minionsKilled'] if 'minionsKilled' in raw else None
        self.__teamScore = raw['teamScore'] if 'teamScore' in raw else None
        self.__dominionScore = raw['dominionScore'] if 'dominionScore' in raw else None
        self.__totalGold = raw['totalGold'] if 'totalGold' in raw else None
        self.__level = raw['level'] if 'level' in raw else None
        self.__xp = raw['xp'] if 'xp' in raw else None
        self.__currentGold = raw['currentGold'] if 'currentGold' in raw else None
        self.__position = MatchPosition(raw['position']) if 'position' in raw else MatchPosition()
        self.__jungleMinionsKilled = raw['jungleMinionsKilled'] if 'jungleMinionsKilled' in raw else None

    @property
    def participantId(self) -> int:
        return self.__participantId

    @property
    def minionsKilled(self) -> int:
        return self.__minionsKilled

    @property
    def teamScore(self) -> int:
        return self.__teamScore

    @property
    def dominionScore(self) -> int:
        return self.__dominionScore

    @property
    def totalGold(self) -> int:
        return self.__totalGold

    @property
    def level(self) -> int:
        return self.__level

    @property
    def xp(self) -> int:
        return self.__xp

    @property
    def currentGold(self) -> int:
        return self.__currentGold

    @property
    def position(self) -> MatchPosition:
        return self.__position

    @property
    def jungleMinionsKilled(self) -> int:
        return self.__jungleMinionsKilled


class MatchEvent:
    def __init__(self, raw={}):
        self.__type = raw['type'] if 'type' in raw else None
        self.__eventType = raw['eventType'] if 'eventType' in raw else None
        self.__position = MatchPosition(raw['position']) if 'position' in raw else MatchPosition()
        self.__laneType = raw['laneType'] if 'laneType' in raw else None
        self.__teamId = raw['teamId'] if 'teamId' in raw else None
        self.__skillSlot = raw['skillSlot'] if 'skillSlot' in raw else None
        self.__creatorId = raw['creatorId'] if 'creatorId' in raw else None
        self.__afterId = raw['afterId'] if 'afterId' in raw else None
        self.__beforeId = raw['beforeId'] if 'beforeId' in raw else None
        self.__levelUpType = raw['levelUpType'] if 'levelUpType' in raw else None
        self.__wardType = raw['wardType'] if 'wardType' in raw else None
        self.__participantId = raw['participantId'] if 'participantId' in raw else None
        self.__towerType = raw['towerType'] if 'towerType' in raw else None
        self.__itemId = raw['itemId'] if 'itemId' in raw else None
        self.__pointCaptured = raw['pointCaptured'] if 'pointCaptured' in raw else None
        self.__killedId = raw['killedId'] if 'killedId' in raw else None
        self.__victimId = raw['victimId'] if 'victimId' in raw else None
        self.__timestamp = raw['timestamp'] if 'timestamp' in raw else None
        self.__assistingParticipantIds = raw['assistingParticipantIds'] if 'assistingParticipantIds' in raw else []
        self.__buildingType = raw['buildingType'] if 'buildingType' in raw else None
        self.__ascendedType = raw['ascendedType'] if 'ascendedType' in raw else None
        self.__monsterType = raw['monsterType'] if 'monsterType' in raw else None
        self.__monsterSubType = raw['monsterSubType'] if 'monsterSubType' in raw else None

    @property
    def type(self) -> str:
        return self.__type

    @property
    def eventType(self) -> str:
        return self.__eventType

    @property
    def position(self) -> MatchPosition:
        return self.__position

    @property
    def laneType(self) -> str:
        return self.__laneType

    @property
    def teamId(self) -> int:
        return self.__teamId

    @property
    def skillSlot(self) -> int:
        return self.__skillSlot

    @property
    def creatorId(self) -> int:
        return self.__creatorId

    @property
    def afterId(self) -> int:
        return self.__afterId

    @property
    def beforeId(self) -> int:
        return self.__beforeId

    @property
    def levelUpType(self) -> str:
        return self.__levelUpType

    @property
    def wardType(self) -> str:
        return self.__wardType

    @property
    def participantId(self) -> int:
        return self.__participantId

    @property
    def towerType(self) -> str:
        return self.__towerType

    @property
    def itemId(self) -> int:
        return self.__itemId

    @property
    def pointCaptured(self) -> str:
        return self.__pointCaptured

    @property
    def killerId(self) -> int:
        return self.__killerId

    @property
    def victimId(self) -> int:
        return self.__victimId

    @property
    def timestamp(self) -> int:
        return self.__timestamp

    @property
    def assistingParticipantIds(self) -> list:
        return self.__assistingParticipantIds

    @property
    def buildingType(self) -> str:
        return self.__buildingType

    @property
    def ascendedType(self) -> str:
        return self.__ascendedType

    @property
    def monsterType(self) -> str:
        return self.__monsterType

    @property
    def monsterSubType(self) -> str:
        return self.__monsterSubType
