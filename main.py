from constantes import *
from classes import *

py.init()
CLOCK = py.time.Clock()
GAMEDISPLAY = py.display.set_mode((SIDE_WINDOW, SIZE_WINDOW))
py.display.set_caption(WIN_TITLE)

SILVER = py.image.load(SILVER).convert()
GOLD_MONEY = py.image.load(GOLD).convert()
LOOT_MONEY = py.image.load(MONEY).convert()

WIN_SCREEN = py.image.load(WIN).convert()
LOST_SCREEN = py.image.load(GAME_OVER).convert()

#load and display home screen
HOME = py.image.load(HOME_PAGE).convert()
GAMEDISPLAY.blit(HOME, (0, 0))

#main loop
playing = 1
while playing:

    #refresh
    py.display.flip()

    #reset variables to 1 after loop is complete
    playing_game = 1
    playing_home = 1

    #home screen
    while playing_home:
        #loop speed limit
        py.time.Clock().tick(30)

        for event in py.event.get():

            #if user quits, reset var to 0 and close
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                playing_home = 0
                playing_game = 0
                playing = 0
                #var choice of level
                #choice = 0

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    playing_home = 0
                    playing_game = 1
                    py.display.flip()

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
    while playing_game:

        #loop speed limit
        py.time.Clock().tick(30)

        for event in py.event.get():

            #if user quits, reset var of playing and playing_game to 0 to close window
            if event.type == QUIT:
                playing_game = 0
                playing = 0

            elif event.type == KEYDOWN:
                #if user presses esc, go back to menu
                if event.key == K_ESCAPE:
                    playing_game = 0
                    playing = 0

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
            py.display.flip()

            if MY_MAZE.structure[MY_PLAYER.case_x][MY_PLAYER.case_y] == 'a' and ITEM_COUNT == 3:
                GAMEDISPLAY.blit(WIN_SCREEN, (0, 0))
                py.display.flip()
                playing_game = 0
            elif MY_MAZE.structure[MY_PLAYER.case_x][MY_PLAYER.case_y] == 'a' and ITEM_COUNT != 3:
                GAMEDISPLAY.blit(LOST_SCREEN, (0, 0))
                py.display.update()
                playing_game = 0
