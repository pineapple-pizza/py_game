import pygame as PY

from pygame.locals import *
from constantes import *

PY.init()
CLOCK = PY.time.Clock()
GAMEDISPLAY = PY.display.set_mode((SIDE_WINDOW, SIDE_WINDOW))
X, Y = SIDE_SPRITE_NUM, SIDE_SPRITE_NUM

class Maze:
    def __init__(self):
        self.structure = []

    def creation(self):

      with open('map.txt') as fichier:
        structure_niveau = []
        #On parcourt les lignes du fichier
        for ligne in fichier:
          ligne_niveau = []
          #On parcourt les sprites (lettres) contenus dans le fichier
          for sprite in ligne:
            #On ignore les "\n" de fin de ligne
            if sprite != '\n':
              #On ajoute le sprite à la liste de la ligne
              ligne_niveau.append(sprite)
          #On ajoute la ligne à la liste du niveau
          structure_niveau.append(ligne_niveau)
        #On sauvegarde cette structure
        self.structure = structure_niveau

    def display_maze(self, window):
        """Méthode permettant d'afficher le niveau en fonction 
        de la liste de structure renvoyée par generer()"""

        BACKGROUND = PY.image.load(FLOOR).convert()
        FINISHLINE = PY.image.load(ICON_GUARDIAN).convert()
        WALLS = PY.image.load(WALL).convert()

        #On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
            #On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                #On calcule la position réelle en pixels
                x = num_case * SPRITE_SIZE
                y = num_ligne * SPRITE_SIZE
                if sprite == "0":
                    window.blit(BACKGROUND, (x, y))
                elif sprite == "m":
                    window.blit(WALLS, (x, y))
                elif sprite == "d":
                    window.blit(BACKGROUND, (x, y))
                elif sprite == "a":
                    window.blit(FINISHLINE, (x, y))

                num_case += 1
            num_ligne += 1

DONE = False
while not DONE:
    for event in PY.event.get():
        if event.type == PY.QUIT:
            done = True
    # GAMEDISPLAY.blit(BACKGROUND, (0, 0)) ## Blit the background onto the screen first

    MY_MAZE = Maze()
    MY_MAZE.creation()

    MY_MAZE.display_maze(GAMEDISPLAY)
    ## All other display stuff goes here
    PY.display.flip()
    CLOCK.tick(30)

PY.quit()