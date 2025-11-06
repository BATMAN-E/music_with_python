import math
import time
from turtle import *

# --- Setup ---
screen = Screen()
screen.setup(width=800, height=700)
screen.bgcolor("black")
screen.title("Broken Heart Animation")
screen.delay(0)

t = Turtle()
t.hideturtle()
t.speed(0)
t.color("red")
t.width(2)

# Heart parametric functions
def hearta(k): 
    return 16 * math.sin(k) ** 3

def heartb(k): 
    return 13 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# --- Stage 1: Heart Appears from Center ---
for i in range(0, 360, 2):
    k = math.radians(i)
    x = hearta(k) * 10
    y = heartb(k) * 10
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(x * 0.9, y * 0.9)
    time.sleep(0.001)

# --- Short Pause ---
time.sleep(0.5)

# --- Stage 2: Arrow flies across ---
arrow = Turtle()
arrow.shape("triangle")
arrow.color("white")
arrow.setheading(0)
arrow.penup()
arrow.goto(-400, 0)
arrow.showturtle()
arrow.speed(0)

for i in range(-400, 400, 25):
    arrow.goto(i, 0)
    time.sleep(0.01)

arrow.hideturtle()

# --- Stage 3: Heart breaks in half ---
left_heart = Turtle()
right_heart = Turtle()

for t_ in [left_heart, right_heart]:
    t_.hideturtle()
    t_.speed(0)
    t_.color("red")
    t_.width(2)

def draw_half(t_, start, end, shift):
    t_.penup()
    for i in range(start, end, 3):
        k = math.radians(i)
        x = hearta(k) * 10 + shift
        y = heartb(k) * 10
        if i == start:
            t_.goto(x, y)
            t_.pendown()
        else:
            t_.goto(x, y)

# --- Split Animation ---
for shift in range(0, 60, 2):
    left_heart.clear()
    right_heart.clear()
    draw_half(left_heart, 0, 180, -shift)
    draw_half(right_heart, 180, 360, shift)
    time.sleep(0.03)

# --- Final Text ---
t.penup()
t.goto(0, -250)
t.color("white")


done()
