import subprocess

def vlc_player(locations):

    try:
        vlc_path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"

        vlc_args = [vlc_path] + locations

        subprocess.run(vlc_args, check=True)
        print("VLC has been executed.")
    
    except FileNotFoundError:
        print(f"Error: {FileNotFoundError}")
