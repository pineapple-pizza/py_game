from game_files.const import *
from game_files.character import Character
from game_files.items import Items
from game_files.maze import Maze

py.init()
clock = py.time.Clock()
gamedisplay = py.display.set_mode((SIDE_WINDOW, SIZE_WINDOW))
py.display.set_caption(WIN_TITLE)

book_item = py.image.load(BOOK).convert()
gold_money = py.image.load(GOLD).convert()
shoes_item = py.image.load(SHOES).convert()

win_screen = py.image.load(WIN).convert()
lost_screen = py.image.load(GAME_OVER).convert()

#load and display home screen
home = py.image.load(HOME_PAGE).convert()
gamedisplay.blit(home, (0, 0))

def main():

  #main loop
  playing = 1
#   item_count = 0
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
      my_player = Character(MY_MAZE.structure)

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

      item_1, item_2, item_3 = display_items(MY_MAZE.structure)
      item_count = 0

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
                        my_player.deplacer('right')
                    elif event.key == K_LEFT:
                        my_player.deplacer('left')
                    elif event.key == K_UP:
                        my_player.deplacer('up')
                    elif event.key == K_DOWN:
                        my_player.deplacer('down')

            if my_player.case_x == item_1.case_x and my_player.case_y == item_1.case_y:
                item_1.case_x = 0
                item_1.case_y = SPRITE_WIDTH
                item_count += 1
            if my_player.case_x == item_2.case_x and my_player.case_y == item_2.case_y:
                item_2.case_x = 1
                item_2.case_y = SPRITE_WIDTH
                item_count += 1
            if my_player.case_x == item_3.case_x and my_player.case_y == item_3.case_y:
                item_3.case_x = 2
                item_3.case_y = SPRITE_WIDTH
                item_count += 1

            #displaying new positions
            MY_MAZE.display_maze(gamedisplay)
            gamedisplay.blit(my_player.direction, (my_player._x, my_player._y))
            gamedisplay.blit(book_item, (item_1.case_x * SPRITE_SIZE, item_1.case_y * SPRITE_SIZE))
            gamedisplay.blit(gold_money, (item_2.case_x * SPRITE_SIZE, item_2.case_y * SPRITE_SIZE))
            gamedisplay.blit(shoes_item, (item_3.case_x * SPRITE_SIZE, item_3.case_y * SPRITE_SIZE))
            py.display.flip()

            if MY_MAZE.structure[my_player.case_x][my_player.case_y] == 'a' and item_count == 3:
                gamedisplay.blit(win_screen, (0, 0))
                py.display.flip()
                playing_game = 0
            elif MY_MAZE.structure[my_player.case_x][my_player.case_y] == 'a' and item_count != 3:
                gamedisplay.blit(lost_screen, (0, 0))
                playing_game = 0

if __name__ == '__main__':
    main()
