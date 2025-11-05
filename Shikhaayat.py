import time
import sys

def print_lyrics():
    lyrics = [
        "To aao na........",
        "mere aansu ko pochho.Aur phir se rulaao mujhe",
        "Mera sab kuch hai tere liye",
        "To aao na..... ",
        "dil ki baatein karo. Aur phir se sataao mujhe",
        "Mera sab kuch hai tere liye"
    ]

    delays = [1.5, 1.9, 0.5, 1.5, 1.5,1.2]  

    print("Shikayat : \n")
    time.sleep(1.4)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.11)  
        print()
        time.sleep(delays[i])

print_lyrics()
