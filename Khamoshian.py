import time
import sys

def print_lyrics():
    lyrics = [
        "Khamoshiyan......Ek Saaz Hai",
        "Tum Dhun Koi Laao Zaraa...",
        "Khamoshiyan.........Alfaaz Hai",
        "Kabhi Aa Gunguna Le Zaraa...",
        "Beqrar Hain.........Baat Karne Ko..",
        "Kahne Do Inko Zaraaaa.........",
        "Khamoshiyan....."
    ]

    delays = [1.2, 1.8, 1.8,2.0, 1.3,2.0,1.0]

    print("Khamoshiyan:\n")
    time.sleep(1.4)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)  
            sys.stdout.flush()          
            time.sleep(0.11)    
        print()                        
        time.sleep(delays[i])           

print_lyrics()
 
