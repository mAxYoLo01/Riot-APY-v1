import requests
from ..classes import ChampionMastery


class ChampionMasteryAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_all_masteries(self, summonerId: str, region: str):
        """
        Get a list of :class:`~riot_apy.classes.ChampionMastery` for all champions.

        :param str summonerId: Summoner ID
        :param str region: League region

        :rtype: List[ChampionMastery]
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summonerId}?api_key={self.api_key}').json()
        masteries_list = [ChampionMastery(champ) for champ in raw]
        return masteries_list

    def get_champion_mastery(self, summonerId: str, championId: int, region: str):
        """
        Get the :class:`~riot_apy.classes.ChampionMastery` for a specific champion, given its ID.

        :param str summonerId: Summoner ID
        :param int championId: Champion ID
        :param str region: League region

        :rtype: ChampionMastery
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summonerId}/by-champion/{championId}?api_key={self.api_key}').json()
        mastery = ChampionMastery(raw)
        return mastery

    def get_mastery_score(self, summonerId: str, region: str):
        """
        Get the total mastery score for a given summoner.

        :param str summonerId: Summoner ID
        :param str region: League region

        :rtype: int
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{summonerId}?api_key={self.api_key}').json()
        return raw
