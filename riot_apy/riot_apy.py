from .apis import DataDragonAPI, ChampionAPI, ChampionMasteryAPI, LeagueAPI, MatchAPI, SpectatorAPI, SummonerAPI


class RiotAPY:
    """
    Initiate a RiotAPY class, from which all API calls will be made.

    :param str api_key: API key

    .. note:: Your API key can be found over `here <https://developer.riotgames.com/>`_ by creating a Riot Games Developer account.
    """
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.__datadragon = DataDragonAPI()
        self.__summoner = SummonerAPI(self.api_key)
        self.__match = MatchAPI(self.api_key)
        self.__champion_mastery = ChampionMasteryAPI(self.api_key)
        self.__spectator = SpectatorAPI(self.api_key)
        self.__champion = ChampionAPI(self.api_key)
        self.__league = LeagueAPI(self.api_key)

    @property
    def datadragon(self):
        """
        Interface to the DataDragonAPI.

        :rtype: DataDragonAPI
        """
        return self.__datadragon

    @property
    def summoner(self):
        """
        Interface to the SummonerAPI.

        :rtype: SummonerAPI
        """
        return self.__summoner

    @property
    def match(self):
        """
        Interface to the MatchAPI.

        :rtype: MatchAPI
        """
        return self.__match

    @property
    def champion_mastery(self):
        """
        Interface to the ChampionMasteryAPI.

        :rtype: ChampionMasteryAPI
        """
        return self.__champion_mastery

    @property
    def spectator(self):
        """
        Interface to the SpectatorAPI.

        :rtype: SpectatorAPI
        """
        return self.__spectator

    @property
    def champion(self):
        """
        Interface to the ChampionAPI.

        :rtype: ChampionAPI
        """
        return self.__champion

    @property
    def league(self):
        """
        Interface to the LeagueAPI.

        :rtype: LeagueAPI
        """
        return self.__league
