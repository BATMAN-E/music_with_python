import time
import sys

def print_lyrics():
    lyrics = [
        "Baatein Zaroori Hain,",
        "Tera Milna Bhi Zaroori...",
        "Maine Mita Deni,",
        "Yeh Jo Teri Meri Doori.",
        "",
        "Jhoothi Hain Woh Raahein Saari, Duniya Ki,",
        "Ishq Jahaan Naa Chale...",
        "",
        "Tera Hona, Mera Hona,",
        "Kya Hona,",
        "Agar Naa Dono Mile...",
        "Tu Pehla Pehla Pyaar Hai Mera"
    ]

    delays = [0.6, 1.4, 2.0, 1.7, 0.2, 0.3, 1.5, 0.4, 0.2, 0.4, 0.8, 0.9]  

    print("Baatein Zaroori Hain :\n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.09)  
        print()
        time.sleep(delays[i])

print_lyrics()
