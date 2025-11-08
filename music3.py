import time
import sys

def print_lyrics():
    lyrics = [
        " Maybe it's 6:45",
        "Maybe I'm barely alive",
        "Maybe you've taken my shit for the last time, yeah",
        "Maybe I know that I'm drunk",
        "Maybe I know you're the one",
        "Maybe you thinking it's better if you drive",
        "…......Oh, 'cause girls like you run 'round with guys like me"
        "Til sun down when I come through",
        "I need a girl like you, yeah"
    ]

    delays = [0.7, 0.2, 0.5, 0.5, 0.5,1.1,0.5,0.5,0.3]

    print("Girls Like you: \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)  
            sys.stdout.flush()          
            time.sleep(0.06)    
        print()                        
        time.sleep(delays[i])           

print_lyrics()
 
