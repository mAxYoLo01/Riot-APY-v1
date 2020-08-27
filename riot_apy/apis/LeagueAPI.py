import requests
from ..classes import LeagueList, LeagueEntry


class LeagueAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_challenger_queue(self, queue: str, region: str):
        """
        Get information about the Challenger queue in the given region and queue type.

        :param str queue: Queue type (RANKED_SOLO_5x5 or RANKED_FLEX_SR)
        :param str region: League region

        :rtype: LeagueList
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{queue}?api_key={self.api_key}').json()
        queue = LeagueList(raw)
        return queue

    def get_grandmaster_queue(self, queue: str, region: str):
        """
        Get information about the Grandmaster queue in the given region and queue type.

        :param str queue: Queue type (RANKED_SOLO_5x5 or RANKED_FLEX_SR)
        :param str region: League region

        :rtype: LeagueList
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{queue}?api_key={self.api_key}').json()
        queue = LeagueList(raw)
        return queue

    def get_master_queue(self, queue: str, region: str):
        """
        Get information about the Master queue in the given region and queue type.

        :param str queue: Queue type (RANKED_SOLO_5x5 or RANKED_FLEX_SR)
        :param str region: League region

        :rtype: LeagueList
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/league/v4/masterleagues/by-queue/{queue}?api_key={self.api_key}').json()
        queue = LeagueList(raw)
        return queue

    def get_league_entries(self, id: str, region: str):
        """
        Get information about the ranked positions from the given summoner ID.

        :param str id: Summoner ID
        :param str region: League region

        :rtype: List[LeagueEntry]
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}?api_key={self.api_key}').json()
        entries = [LeagueEntry(entry) for entry in raw]
        return entries

    def get_league(self, id: str, region: str):
        """
        Get the :class:`~riot_apy.classes.LeagueList` given its ID.

        :param str id: League ID
        :param str region: League region

        :rtype: LeagueList
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/league/v4/leagues/{id}?api_key={self.api_key}').json()
        list = LeagueList(raw)
        return list
