class Site():

    def __init__(self, fun, book, episodes, english):
        self.fun = fun
        self.book = book
        self.episodes = episodes
        self.english = english

    def get_fun(self):
        fun = {}
        pikabu = "https://pikabu.ru/"
        fun.update(pikabu)
        reddit = "https://www.reddit.com/"
        fun.update(reddit)
        return fun

    def get_book(self):
        book = {}
        livelib = ""
        book.update(livelib)
        briefly = ""
        book.update(briefly)
        return book

    def get_episodes(self):
        episodes = {}
        netflix = ""
        episodes.update(netflix)
        kinopoisk = ""
        episodes.update(kinopoisk)
        return episodes

    def get_english(self):
        english = {}
        bbc = ""
        english.update(bbc)
        council = ""
        english.update(council)
        return english
