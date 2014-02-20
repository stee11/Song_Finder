#!/usr/bin/python2

import requests, json

class LyricSearch:
    def __init__(self):
        self.api_key = "a795b44b10a2f7d8456eae9b54b434"
        self.url     = "http://api.lyricsnmusic.com/songs"

    def search_by_lyrics(self, lyrics):
        return json.loads(requests.get(self.url,
            params={"api_key": self.api_key,
            "lyrics": lyrics}).text)

def __search_test():
    lyr_search = LyricSearch()
    lyrics = raw_input('Enter some lyrics to search: ')
    try:
        track = lyr_search.search_by_lyrics(lyrics)[0]
    except IndexError:
        print "No tracks matched your search"
    else:
        print track

if __name__ == "__main__":
    __search_test()
