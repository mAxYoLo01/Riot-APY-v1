#!/usr/bin/env python

from riot_apy import RiotAPY

api_key = 'RGAPI-380a6d92-ccaa-4ddd-87ef-c5a4fc424210'

apy = RiotAPY(api_key)
summoner = apy.summoner.from_name('mAxYoLo01', 'euw1')
champ_list = apy.datadragon.get_champions_list()
