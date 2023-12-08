from src.xspf_parser import xspf_parser
from src.vlc_player import vlc_player
from src.randomicer import randomicer

file_path = "music.xspf"
locations = xspf_parser(file_path)

if locations:
    randomized_locations = randomicer(locations)
    vlc_player(randomized_locations)
