import pygame
import sys
import time
import random

pygame.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Faasle")

FONT = pygame.font.SysFont("Georgia", 40, bold=True)
colors = [
    (82, 8, 23),     # deep wine red
    (120, 30, 60),   # romantic plum
    (176, 60, 92),   # rose mauve
    (250, 195, 210), # blush pink
    
    (60, 25, 70)     # deep purple dusk
]



lyrics = [
        "Baatein Zaroori Hain,",
        "Tera Milna Bhi Zaroori...",
        "Maine Mita Deni,",
        "Yeh Jo Teri Meri Doori.",
        
        "Jhoothi Hain Woh Raahein Saari, Duniya Ki,",
        "Ishq Jahaan Naa Chale...",
       
        "Tera Hona, Mera Hona, Kya Hona,",
        "Agar Naa Dono Mile...",
        "Tu Pehla Pehla Pyaar Hai Mera"
    ]

def typewriter_text(text, color, bg_color, char_delay=0.1, duration=1.2):
    current_text = ""
    for char in text:
        current_text += char
        text_surface = FONT.render(current_text, True, color)
        text_surface = text_surface.convert_alpha()
        rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        
        screen.fill(bg_color)           # clear screen to bg
        screen.blit(text_surface, rect) # draw current text
        pygame.display.flip()           # update screen
        time.sleep(char_delay)          # wait for next char
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    # Hold the full line
    time.sleep(duration)


    for alpha in range(255, -1, -5):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(bg_color)
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, rect)
        pygame.display.flip()
        time.sleep(0.02)

durations = [0.6, 1.4, 1.5, 1.0,  0.3, 1.4, 0.2, 0.4, 1.0, 0.9]  

for i, line in enumerate(lyrics):
    bg = random.choice(colors)
    typewriter_text(line, (255, 255, 255), bg, char_delay=0.07, duration=durations[i])

pygame.quit()
