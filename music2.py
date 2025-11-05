import time
import sys

def print_lyrics():
    lyrics = [
        "Tumi..", 
        "Shamne nei,", 
        "Tao Tumi...", 
        "Vasho",
        "Moner...........",
        "Majhe",
        "Lukiye",
        "Ektu Khani Hasho....",
        "Shopne Amar Tomar Chobi........Chupti Kore Ashe...",
        "Shokal Theke Rater Shehe",
        "Thako Amar Pashe.....eeeee...",
        "Ta.Taaa.Taaaaaaa......"
    ]

    delays = [2.0, 2.5, 2.9, 3.5, 2.5, 2.0, 2.8, 3.0, 2.0, 0.9,0.9,0.5]

    print("LEVEL FIVE :\n")
    time.sleep(1.4)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)  
            sys.stdout.flush()          
            time.sleep(0.1)    
        print()                        
        time.sleep(delays[i])           

print_lyrics()
 
