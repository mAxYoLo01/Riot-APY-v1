import requests
from ..classes import Match, Matchlist, MatchTimeline


class MatchAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_match(self, id: int, region: str):
        """
        Get the :class:`~riot_apy.classes.Match` given its ID.

        :param int id: Match ID
        :param str region: League region

        :rtype: Match
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/match/v4/matches/{id}?api_key={self.api_key}').json()
        match = Match(raw)
        return match

    def get_matchlist(self, accountId: str, region: str, champion: list = None,
                      queue: list = None, season: list = None,
                      end_time: int = None, begin_time: int = None,
                      end_index: int = None, begin_index: int = None):
        """
        Get the :class:`~riot_apy.classes.Matchlist` for a certain player.

        Additional filters can be set.

        :param str accountId: Account ID
        :param str region: League region
        :param List[int] champion: List of champion IDs
        :param List[int] queue: List of queue IDs
        :param List[int] season: List of season IDs
        :param int end_time: End time in epoch milliseconds
        :param int begin_time: Begin time in epoch milliseconds
        :param int end_index: End index
        :param int begin_index: Begin index

        :rtype: Matchlist
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{accountId}?api_key={self.api_key}',
                           params={'champion': champion, 'queue': queue, 'season': season, 'endTime': end_time,
                                   'beginTime': begin_time, 'endIndex': end_index, 'beginIndex': begin_index}).json()
        matchlist = Matchlist(raw)
        return matchlist

    def get_timeline(self, id: int, region: str):
        """
        Get the :class:`~riot_apy.classes.MatchTimeline` of a :class:`~riot_apy.classes.Match` given its ID.

        :param int id: Match ID
        :param str region: League region

        :rtype: MatchTimeline
        """
        raw = requests.get(f'https://{region}.api.riotgames.com/lol/match/v4/timelines/by-match/{id}?api_key={self.api_key}').json()
        timeline = MatchTimeline(raw)
        return timeline
