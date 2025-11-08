import time
import sys

def print_lyrics():
    lyrics = [
      
        "Oh, I used to say",
        "… I would never fall in love again until I found her",
        "I said, 'I would never fall unless it's you I fall into'",
        "I was lost within the darkness, but then I found her",
        "I found you"
        ]

    delays = [
        1.2,1.5, 1.5, 1.5, 2.0,
    ]

    print(" Untill I Found Her : \n")
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
            time.sleep(0.9)

print_lyrics()