import time
import sys

def print_lyrics():
    lyrics = [
        "Nigahon Mein Dekho....",
        "Meri Jo Har Bas Gaya........",
        "Woh....Hai Milta Tumse Hoo Bahu",
        "Ooo.................",
        "Jane Teri .....Aankhen Thi ya..",
        "Ya Baatein Thi Wajah.........",
        "Huye Tum Jo Dil Ki Arzooo........"
    ]

    delays = [
      0.3, 2.0, 2.5, 0.4, 0.8, 1.2, 0.4, 0.4
    ]

    print("\n Nigahon Mein Dekho :\n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)

print_lyrics()
