from constantes import *
from classes import *

def displayItems(my_maze):
    ITEM_1 = Items(my_maze)
    ITEM_1.generateItems()
    ITEM_2 = Items(my_maze)
    ITEM_2.generateItems()

    while ITEM_1.y_rand == ITEM_2.y_rand and ITEM_1.x_rand == ITEM_2.x_rand:
        ITEM_2.generateItems()
    ITEM_3 = Items(my_maze)
    ITEM_3.generateItems()
    while (ITEM_1.y_rand == ITEM_3.y_rand and ITEM_1.x_rand == ITEM_3.x_rand) \
    or (ITEM_2.y_rand == ITEM_3.y_rand and ITEM_2.x_rand == ITEM_3.x_rand):
        ITEM_3.generateItems()
    return(ITEM_1, ITEM_2, ITEM_3)

PY.init()
# CLOCK = PY.time.Clock()
GAMEDISPLAY = PY.display.set_mode((SIDE_WINDOW, SIDE_WINDOW))
PY.display.set_caption(WIN_TITLE)

# x_rand = random.randint(0, 14)
# y_rand = random.randint(0, 14)
# transparent = (0, 0, 0, 0)

# SILVER_MONEY = PY.image.load(SILVER).convert()
# GOLD_MONEY = PY.image.load(GOLD).convert()
# LOOT_MONEY = PY.image.load(MONEY).convert()

#BOUCLE PRINCIPALE
PLAYING = 1
while PLAYING:
      #Chargement et affichage de l'écran d'accueil
      HOME = PY.image.load(HOME_PAGE).convert()
      GAMEDISPLAY.blit(HOME, (0, 0))

      #Rafraichissement
      PY.display.flip()

      #On remet ces variables à 1 à chaque tour de boucle
      PLAYING_GAME = 1
      PLAYING_HOME = 1

      #BOUCLE D'ACCUEIL
      while PLAYING_HOME:
      
            #Limitation de vitesse de la boucle
            # PY.time.Clock().tick(30)
        
            for event in PY.event.get():
            
              #Si l'utilisateur quitte, on met les variables
              #de boucle à 0 pour n'en parcourir aucune et fermer
              if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                PLAYING_HOME = 0
                PLAYING_GAME = 0
                PLAYING = 0
                #Variable de choix du niveau
                # choix = 0

              elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    PLAYING_HOME = 0
                    PLAYING_GAME = 1
                    PY.display.flip()

      MY_MAZE = Maze()
      MY_MAZE.creation()
      MY_PLAYER = Character(MY_MAZE.structure)
      ITEM_1, ITEM_2, ITEM_3 = displayItems(MY_MAZE.structure)
      item_count = 0

      #BOUCLE DE JEU
      while PLAYING_GAME:

        #Limitation de vitesse de la boucle
        # PY.time.Clock().tick(30)

        for event in PY.event.get():

          #Si l'utilisateur quitte, on met la variable qui continue le jeu
          #ET la variable générale à 0 pour fermer la fenêtre
          if event.type == QUIT:
            PLAYING_GAME = 0
            PLAYING = 0

          elif event.type == KEYDOWN:
            #Si l'utilisateur presse Echap ici, on revient seulement au menu
            if event.key == K_ESCAPE:
              PLAYING_GAME = 0
              PLAYING = 0

            #Touches de déplacement de Donkey Kong
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
              item_count += 1
          if MY_PLAYER.case_x == ITEM_2.case_x and MY_PLAYER.case_y == ITEM_2.case_y:
              ITEM_2.case_x = 1
              ITEM_2.case_y = 15
              item_count += 1
          if MY_PLAYER.case_x == ITEM_3.case_x and MY_PLAYER.case_y == ITEM_3.case_y:
              ITEM_3.case_x = 2
              ITEM_3.case_y = 15
              item_count += 1

          #Affichages aux nouvelles positions
          # GAMEDISPLAY.blit(fond, (0,0))
          MY_MAZE.display_maze(GAMEDISPLAY)
          GAMEDISPLAY.blit(MY_PLAYER.direction, (MY_PLAYER.x, MY_PLAYER.y)) #MY_PLAYER.direction = l'image dans la bonne direction
          # GAMEDISPLAY.blit(SILVER_MONEY, (x_rand * SPRITE_SIZE, y_rand * SPRITE_SIZE)) 
          GAMEDISPLAY.blit(ITEM_1, (ITEM_1.x * SPRITE_SIZE, ITEM_1.y * SPRITE_SIZE))
          GAMEDISPLAY.blit(ITEM_2, (ITEM_2.x * SPRITE_SIZE, ITEM_2.y * SPRITE_SIZE))
          GAMEDISPLAY.blit(ITEM_3, (ITEM_3.x * SPRITE_SIZE, ITEM_3.y * SPRITE_SIZE))
          PY.display.flip()

        if MY_MAZE.structure[MY_PLAYER.case_x][MY_PLAYER.case_y] == "F" and item_count == 3:
            GAMEDISPLAY.blit(WIN, (0, 0))
            PY.display.flip()
            PLAYING_GAME = 0
            PLAYING_HOME = 1
        elif MY_MAZE.structure[MY_PLAYER.case_x][MY_PLAYER.case_y] == "F" and item_count != 3:
            GAMEDISPLAY.blit(GAME_OVER, (0, 0))
            PLAYING_GAME = 0
            PLAYING_HOME = 1


      #Victoire -> Retour à l'accueil
      # if niveau.structure[MY_PLAYER.case_y][MY_PLAYER.case_x] == 'a':
      #   PLAYING_GAME = 0




# DONE = False
# while not DONE:
#     for event in PY.event.get():
#         if event.type == PY.QUIT:
#             done = True
#     # GAMEDISPLAY.blit(BACKGROUND, (0, 0)) ## Blit the background onto the screen first

#     MY_MAZE = Maze()
#     MY_MAZE.creation()

#     MY_MAZE.display_maze(GAMEDISPLAY)
#     ## All other display stuff goes here
#     PY.display.flip()
#     CLOCK.tick(30)

# PY.quit()