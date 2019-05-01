import subprocess

def main():
    output = subprocess.check_output("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:org.mpris.MediaPlayer2.Player string:Metadata",
                          shell=True)
    output = str(output).split("\\n")

    # Find song name
    for i,x in enumerate(output):
        if "xesam:title" in x:
            # Bit dirty
            song_name = output[i+1].split('"')[1]
            break

    # Find album name
    for i, x in enumerate(output):
        if "xesam:album" in x:
            # Bit dirty
            album_name = output[i + 1].split('"')[1]
            break

    print(album_name)
    print(song_name)


if __name__ == "__main__":
    main()
