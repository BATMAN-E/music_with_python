import time
import sys

def print_lyrics():
    lyrics = [
        "Yaad hai mujhe.....", "teri har adaa",
        "Muskuraahatein......teri",
        "Tera mujh se", "chup ke se yoon",
        "Kahna ki tu hai meri",
        "Jaane ye kya ho gaya", "ho gaye juda"
    ]
   
    delays = [
        0.9, 2.3, 4.1, 2.9, 2.0, 3.5,2.5, 2.0
    ]

    print("\n Nigahon Mein Dekho :\n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.12)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.9)

print_lyrics()
