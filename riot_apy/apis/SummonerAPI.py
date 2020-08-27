import requests
from ..classes import Summoner


class SummonerAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def from_name(self, name: str, region: str):
        """
        Get the :class:`~riot_apy.classes.Summoner` given its name.

        :param str name: Summoner name
        :param str region: League region

        :rtype: Summoner
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={self.api_key}').json()
        summoner = Summoner(raw)
        return summoner

    def from_id(self, id: str, region: str):
        """
        Get the :class:`~riot_apy.classes.Summoner` given its ID.

        :param str id: Summoner ID
        :param str region: League region

        :rtype: Summoner
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/{id}?api_key={self.api_key}').json()
        summoner = Summoner(raw)
        return summoner

    def from_puuid(self, puuid: str, region: str):
        """
        Get the :class:`~riot_apy.classes.Summoner` given its PUUID.

        :param str puuid: Summoner PUUID
        :param str region: League region

        :rtype: Summoner
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={self.api_key}').json()
        summoner = Summoner(raw)
        return summoner

    def from_account_id(self, id: str, region: str):
        """
        Get the :class:`~riot_apy.classes.Summoner` given its account ID.

        :param str id: Account ID
        :param str region: League region

        :rtype: Summoner
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{id}?api_key={self.api_key}').json()
        summoner = Summoner(raw)
        return summoner
