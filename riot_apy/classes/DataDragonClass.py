class Champion:
    def __init__(self, raw={}):
        self.__id = raw['id'] if 'id' in raw else None
        self.__key = raw['key'] if 'key' in raw else None
        self.__name = raw['name'] if 'name' in raw else None
        self.__title = raw['title'] if 'title' in raw else None
        self.__lore = raw['lore'] if 'lore' in raw else None
        self.__blurb = raw['blurb'] if 'blurb' in raw else None
        self.__tags = raw['tags'] if 'tags' in raw else None
        self.__partype = raw['partype'] if 'partype' in raw else None

    @property
    def id(self) -> str:
        return self.__id

    @property
    def key(self) -> str:
        return self.__key

    @property
    def name(self) -> str:
        return self.__name

    @property
    def title(self) -> str:
        return self.__title

    @property
    def lore(self) -> str:
        return self.__lore

    @property
    def blurb(self) -> str:
        return self.__blurb

    @property
    def tags(self) -> list:
        return self.__tags

    @property
    def partype(self) -> str:
        return self.__partype
