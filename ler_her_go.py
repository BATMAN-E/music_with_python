import time
import sys

def print_lyrics():
   
    lyrics = [
    "Staring at the bottom of your glass",
    "Hoping one day you'll make a dream last",
    "But dreams come slow and they go so fast",
    "You see her when you close your eyes",
    "Maybe one day you'll understand why",
    "Everything you touch surely dies",
    "But you only need the light when it's burning low",
    "Only miss the sun when it starts to snow",
    "Only know you love her when you let her go"
    ]


    delays = [0.6, 0.5, 5.0, 0.5, 1.0, 5.0, 0.9,0.9,0.5,0.5]

    print("Let Her Go Lyrics:\n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  # faster typing effect
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.9)

print_lyrics()
