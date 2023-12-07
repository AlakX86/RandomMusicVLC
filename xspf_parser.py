import xml.etree.ElementTree as ET

def parsear_archivo_xspf(archivo):
    tree = ET.parse(archivo)
    root = tree.getroot()
    print(root)

archivo_xspf = 'music.xspf'
parsear_archivo_xspf(archivo_xspf)