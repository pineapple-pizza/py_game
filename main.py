from constantes import *
from classes import *

PY.init()
CLOCK = PY.time.Clock()
GAMEDISPLAY = PY.display.set_mode((SIDE_WINDOW, SIZE_WINDOW))
PY.display.set_caption(WIN_TITLE)

SILVER = PY.image.load(SILVER).convert()
GOLD_MONEY = PY.image.load(GOLD).convert()
LOOT_MONEY = PY.image.load(MONEY).convert()

WIN_SCREEN = PY.image.load(WIN).convert()
LOST_SCREEN = PY.image.load(GAME_OVER).convert()

#main loop
PLAYING = 1
while PLAYING:
    #load and display home screen
    HOME = PY.image.load(HOME_PAGE).convert()
    GAMEDISPLAY.blit(HOME, (0, 0))

    #refresh
    PY.display.flip()

    #reset variables to 1 after loop is complete
    PLAYING_GAME = 1
    PLAYING_HOME = 1

    #home screen
    while PLAYING_HOME:
        #loop speed limit
        PY.time.Clock().tick(30)

        for event in PY.event.get():

            #if user quits, reset var to 0 and close
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                PLAYING_HOME = 0
                PLAYING_GAME = 0
                PLAYING = 0
                #var choice of level
                #choice = 0

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    PLAYING_HOME = 0
                    PLAYING_GAME = 1
                    PY.display.flip()

    MY_MAZE = Maze()
    MY_MAZE.creation()
    MY_PLAYER = Character(MY_MAZE.structure)

    def display_items(my_maze):
        '''method for displaying items'''

        item_1 = Items(my_maze)
        item_1.generate_items()
        item_2 = Items(my_maze)
        item_2.generate_items()

        while item_1.case_y == item_2.case_y and item_1.case_x == item_2.case_x:
            item_2.generate_items()
        item_3 = Items(my_maze)
        item_3.generate_items()
        while (item_1.case_y == item_3.case_y and item_1.case_x == item_3.case_x) \
        or (item_2.case_y == item_3.case_y and item_2.case_x == item_3.case_x):
            item_3.generate_items()
        return(item_1, item_2, item_3)

    ITEM_1, ITEM_2, ITEM_3 = display_items(MY_MAZE.structure)
    ITEM_COUNT = 0

    #GAME LOOP
    while PLAYING_GAME:

        #loop speed limit
        PY.time.Clock().tick(30)

        for event in PY.event.get():

            #if user quits, reset var of PLAYING and PLAYING_GAME to 0 to close window
            if event.type == QUIT:
                PLAYING_GAME = 0
                PLAYING = 0

            elif event.type == KEYDOWN:
                #if user presses esc, go back to menu
                if event.key == K_ESCAPE:
                    PLAYING_GAME = 0
                    PLAYING = 0

                #movements of the character
                elif event.key == K_RIGHT:
                    MY_PLAYER.deplacer('right')
                elif event.key == K_LEFT:
                    MY_PLAYER.deplacer('left')
                elif event.key == K_UP:
                    MY_PLAYER.deplacer('up')
                elif event.key == K_DOWN:
                    MY_PLAYER.deplacer('down')

            if MY_PLAYER.case_x == ITEM_1.case_x and MY_PLAYER.case_y == ITEM_1.case_y:
                ITEM_1.case_x = 0
                ITEM_1.case_y = 15
                ITEM_COUNT += 1
            if MY_PLAYER.case_x == ITEM_2.case_x and MY_PLAYER.case_y == ITEM_2.case_y:
                ITEM_2.case_x = 1
                ITEM_2.case_y = 15
                ITEM_COUNT += 1
            if MY_PLAYER.case_x == ITEM_3.case_x and MY_PLAYER.case_y == ITEM_3.case_y:
                ITEM_3.case_x = 2
                ITEM_3.case_y = 15
                ITEM_COUNT += 1

            #displaying new positions
            MY_MAZE.display_maze(GAMEDISPLAY)
            GAMEDISPLAY.blit(MY_PLAYER.direction, (MY_PLAYER._x, MY_PLAYER._y))
            GAMEDISPLAY.blit(SILVER, (ITEM_1.case_x * SPRITE_SIZE, ITEM_1.case_y * SPRITE_SIZE))
            GAMEDISPLAY.blit(GOLD_MONEY, (ITEM_2.case_x * SPRITE_SIZE, ITEM_2.case_y * SPRITE_SIZE))
            GAMEDISPLAY.blit(LOOT_MONEY, (ITEM_3.case_x * SPRITE_SIZE, ITEM_3.case_y * SPRITE_SIZE))
            PY.display.flip()

        if MY_MAZE.structure[MY_PLAYER.case_x][MY_PLAYER.case_y] == 'a' and ITEM_COUNT == 3:
            #loop speed limit
            PY.time.Clock().tick(1000)
            GAMEDISPLAY.blit(WIN_SCREEN, (0, 0))
            PY.display.flip()
            PLAYING_GAME = 0
        elif MY_MAZE.structure[MY_PLAYER.case_x][MY_PLAYER.case_y] == 'a' and ITEM_COUNT != 3:
            GAMEDISPLAY.blit(LOST_SCREEN, (0, 0))
            PY.display.update()
            PLAYING_GAME = 0
            #loop speed limit
            # PY.time.Clock().tick(1000)
