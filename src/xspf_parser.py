import os
import xml.etree.ElementTree as ET

def xspf_parser(file_path):
    
    if not os.path.isfile(file_path):
        print(f"The file: '{file_path}' doesn't exist.")
        return
    
    try:
        ET.register_namespace('', 'http://xspf.org/ns/0/')
        
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        track_list = root.find('.//{http://xspf.org/ns/0/}trackList')
        if track_list is None:
            print("Error: The 'trackList' section was not found in the frontend.")
            return

        locations = []
        for track in track_list.findall('{http://xspf.org/ns/0/}track'):
            try:
                location = track.find('{http://xspf.org/ns/0/}location').text
                print(f'Location: {location}')
                locations.append(location)
            except AttributeError:
                print("Error: The element 'location' was not found in a track.")
                return

        print(f"The file '{file_path}' was processed successfully.")
        return locations

    except ET.ParseError:
        print("Error: The file is not a well-formed xspf file.")
        return
