import pgzrun
import random


WIDTH = 1200
HEIGHT = 800
R = 50
def draw():
    screen.fill("white")
    for x in range(1, WIDTH, R):
        for y in range(1, HEIGHT, R):
            screen.draw.circle((x, y), R, \
            (random.randint(0, 255), random.randint(0, 255), \
            random.randint(0, 255)))

def on_mouse_down():
    draw()

pgzrun.go()