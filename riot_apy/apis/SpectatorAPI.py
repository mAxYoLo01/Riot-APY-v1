import requests
from ..classes import CurrentGameInfo, FeaturedGames


class SpectatorAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_current_game(self, summonerId: str, region: str):
        """
        Get the :class:`~riot_apy.classes.CurrentGameInfo` of the live game of a summoner.

        :param int id: Match ID
        :param str region: League region

        :rtype: CurrentGameInfo
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summonerId}?api_key={self.api_key}').json()
        current_game = CurrentGameInfo(raw)
        return current_game

    def get_featured_games(self, region: str):
        """
        Get the :class:`~riot_apy.classes.FeaturedGames` of League.

        :param str region: League region

        :rtype: FeaturedGames
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/spectator/v4/featured-games?api_key={self.api_key}').json()
        featured_games = FeaturedGames(raw)
        return featured_games
