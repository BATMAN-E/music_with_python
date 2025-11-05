import time
import sys

def print_lyrics():
    lyrics = [
        "Jano na tumi 10 e 10",
        "Ma kasam tumi 10 e 10",
        "Jano na tumi 10 e 10",
        "Tomar ei rup-e scale o behush",
        "Jano na tumi 10 e 10",
        "Ma kasam tumi 10 e 10",
        "Jano na tumi 10 e 10",
        "Tomar ei rup-e scale o behush"
    ]

    delays = [
        0.8, 0.8, 0.8, 0.9, 0.8, 0.8, 0.8, 0.8
    ]

    print(" 10 e 10 : \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.07)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.08)

print_lyrics()
