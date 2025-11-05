import time
import sys

def print_lyrics():

    lyrics = [
    "Eto shunyota","e mone rakhi je ami",
    "Dekhe na keu to ar,",
    "bole e shobi pagolami",
    "Kate na jamini,",
    "biroho jeno kete jay",
    "Thame na.... borsha,",
    "tomare daki je ami",
]


    delays = [1.0,1.0, 0.8, 0.8, 0.9,0.8,0.8,0.9,0.3]
    print("Long Distance Love: \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)  
            sys.stdout.flush()          
            time.sleep(0.068)    
        print()                        
        time.sleep(delays[i])           

print_lyrics()
 
