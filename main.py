import pygame as PY

from pygame.locals import *
from constantes import *

PY.init()
CLOCK = PY.time.Clock()
GAMEDISPLAY = PY.display.set_mode((SIDE_WINDOW, SIDE_WINDOW))
PY.display.set_caption('MacGyver : The Maze Runner')
X, Y = SIDE_SPRITE_NUM, SIDE_SPRITE_NUM

PLAYER = PY.image.load('ressource/MacGyver.png').convert_alpha()

LOOP = True
while LOOP:
    # this adds the sprite at every frame rate
    GAMEDISPLAY.fill((0, 0, 0))
    GAMEDISPLAY.blit(PLAYER, (X, Y))

    for event in PY.event.get():
        # this is to close the window
        if event.type == QUIT:
            LOOP = False
            #sys.exit() # this will close the kernel too
            # in development mode leave the comment above
    # this is the list with the KEYS being pressed
    KEYS = PY.key.get_pressed()
    if KEYS[PY.K_LEFT]:
        X -= 1
    if KEYS[PY.K_RIGHT]:
        X += 1
    if KEYS[PY.K_UP]:
        Y -= 1
    if KEYS[PY.K_DOWN]:
        Y += 1
    # we update the screen at every frame

    PY.display.flip()
    # if we put the frame rate at 60 the sprite will move slower
    CLOCK.tick(120)

PY.quit()