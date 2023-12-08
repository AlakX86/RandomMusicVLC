from src.xspf_parser import xspf_parser

def test_successful_processing():
    result = xspf_parser("music.xspf")
    assert result == ['file:///C:/Users/alaki/Downloads/VLC%20music/dab.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dak.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dam.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dap.mp3', 
                      'file:///C:/Users/alaki/Downloads/VLC%20music/deb.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dek.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dem.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dep.mp3',
                      'file:///C:/Users/alaki/Downloads/VLC%20music/dib.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dik.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dim.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dip.mp3',
                      'file:///C:/Users/alaki/Downloads/VLC%20music/dob.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dok.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dom.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dop.mp3',
                      'file:///C:/Users/alaki/Downloads/VLC%20music/dub.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/duk.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dum.mp3', 'file:///C:/Users/alaki/Downloads/VLC%20music/dup.mp3']

def test_nonexistent_file():
    result = xspf_parser('nonexistent_file.xspf')
    assert result is None

def test_missing_tracklist():
    result = xspf_parser('tests\\no_track_list.xspf')
    assert result is None

def test_missing_location():
    result = xspf_parser('tests\\no_location.xspf')
    assert result is None

def test_well_formed_xspf():
    result = xspf_parser("tests\\well_formed_xspf.xspf")
    assert result is None
