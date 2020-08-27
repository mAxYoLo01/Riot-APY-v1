import requests
from ..classes import ChampionInfo


class ChampionAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_champion_rotation(self, region: str):
        """
        Get a :class:`~riot_apy.classes.ChampionInfo` containing the list of champions in free rotation.

        :param str region: League region

        :rtype: ChampionInfo
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={self.api_key}').json()
        current_game = ChampionInfo(raw)
        return current_game
