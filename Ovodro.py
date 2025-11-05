import time
import sys

def print_lyrics():
    lyrics = [
        "Obhodro",
        "hoiyechi....... ami tomar ey prem e,....... tai",
        "Kache asho na...",
        "Aro kache asho na...",
        "Pashe bosho na...",
        "Kono kotha bolo na",
        "Obhodro",
        "hoiyechi ........ami tomar ey prem e,..... tai..."
    ]

    delays = [
        0.5,0.9, 0.3, 0.3, 0.3, 0.1, 0.5,0.5
    ]

    print("Obhodro : \n")
    time.sleep(1.0)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.07)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)

print_lyrics()
