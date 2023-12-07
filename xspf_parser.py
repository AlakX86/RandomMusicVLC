import xml.etree.ElementTree as ET

def parsear_archivo_xspf(archivo):
    ET.register_namespace('', 'http://xspf.org/ns/0/')
    
    tree = ET.parse(archivo)
    root = tree.getroot()

    tracks = root.find('.//{http://xspf.org/ns/0/}trackList')

    for track in tracks.findall('{http://xspf.org/ns/0/}track'):
        location = track.find('{http://xspf.org/ns/0/}location').text
        print(f'Location: {location}')

archivo_xspf = 'music.xspf'
parsear_archivo_xspf(archivo_xspf)
