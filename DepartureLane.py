import time
import sys

def print_lyrics():
    lyrics = [
        "Tu woh jo mujhe haasil hi nahi...",
        "Main karoon tujhe kaise yeh bayaan?",
        "Meri jaan, meri jaan, tu na jaa...",
        "Abhi karz hai tujhpe woh waada...",
        "Meri jaan, mujhe kya hi pata tha...",
        "Rang badle yeh kaise aasmaan..."
    ]

    delays = [0.5, 0.2, 0.2, 0.5,0.5, 0.5]  

    print("Shikayat : \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)  
        print()
        time.sleep(delays[i])

print_lyrics()
