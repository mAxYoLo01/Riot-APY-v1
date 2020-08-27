import requests
from ..classes import Champion


class DataDragonAPI:
    def __init__(self):
        self.latest = self.get_versions()[0]

    def get_versions(self):
        """
        Get a list of all versions.

        :rtype: List[str]
        """
        list = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()
        return list

    def get_languages(self):
        """
        Get a list of all languages.

        :rtype: List[str]
        """
        list = requests.get('https://ddragon.leagueoflegends.com/cdn/languages.json').json()
        return list

    def get_champions_list(self, version: str = None, language: str = 'en_US'):
        """
        Get a dictionary containing each champion's ID, key and name.

        :param str version: League version
        :param str language: League language

        The syntax for this dictionary is as follows:

        .. code-block:: python

            {champion_id (int): {'key': champion_key (str), 'name':champion_name (str)}, ...}
        """
        if not version:
            version = self.latest
        champions_dict_raw = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/champion.json').json()['data']
        champions_dict = {int(champ['key']): {"key": champ['id'], "name": champ['name']} for champ in champions_dict_raw.values()}
        return champions_dict

    def get_champion_from_id(self, id: int, version: str = None, language: str = 'en_US'):
        """
        Get the :class:`~riot_apy.classes.Champion` given its ID.

        :param int id: Champion ID
        :param str version: League version
        :param str language: League language

        :rtype: Champion
        """
        if not version:
            version = self.latest
        key = self.get_champions_list(version=version, language=language)[id]['key']
        raw = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/champion/{key}.json').json()['data'][key]
        return Champion(raw)
