import time
import sys

def print_lyrics():
    lyrics = [
    
        "Se ki amar noy?", 
        "Se jodi amar.... na-i....... hoy tobe....", 
        "charidik keno mate kolorobe", 
        "tar...... isharay.....?", 
        "Se to amar-i", 
        "ar karo noy."
    ]

    delays = [1.4, 2.3, 0.9,3.4, 1.5,0.8]
    print("Shuvro Chand: \n")
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
