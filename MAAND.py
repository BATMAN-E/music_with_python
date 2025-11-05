import time
import sys

def print_lyrics():
    lyrics = [
        "Jo tu nahi tou aisa main chehra",
        "Ke jis ki...." ,
        "khoobsurati maand parhi ho",
        "Aisa main darya......", 
        "jo behna na chahe",
        "Jo tu nahi to aisa main chehra",
        "Ke jis ki....", 
        "khoobsurati maand parhi ho",
        "Aisa main darya.....", 
        "jo behna na chahe....."
    ]

    delays = [
        0.5, 0.9, 0.9, 1.6, 1.0, 0.8,1.0,1.0,1.0,0.3
    ]

    print(" Maand : \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.08)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.08)

print_lyrics()
