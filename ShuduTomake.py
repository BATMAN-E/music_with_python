import time
import sys

def print_lyrics():
    lyrics = [
        "Megher dhaka din gulo’r..",
        "Brishtir haashi...",
        "Keno shei batasher majhe...",
        "Tomay khunji",
        
        "Moner majhe genthe rekhechi",
        "Tomay ami...",
        "Shudhu ek isharar",
        "Ashai royechhi...."
    ]

    delays = [1.6, 1.6,1.6, 1.6, 1.5, 1.6, 1.6, 1.5,1.5]

    print("Shudu Tomake : \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        time.sleep(delays[i])

print_lyrics()
