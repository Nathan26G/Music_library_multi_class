from lib.track import *

class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def search_by_title(self, keyword):
        results = []
        for track in self.tracks:
            if keyword.lower() in track.lower():
                results.append(track)
        return results
