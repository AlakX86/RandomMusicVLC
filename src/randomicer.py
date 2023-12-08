import random

def randomicer(playlist):

    if len(playlist) < 2:
        return playlist.copy()

    randomized_playlist = playlist.copy()
    random.shuffle(randomized_playlist)
    return randomized_playlist
