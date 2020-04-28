import random
from constantes import *

class Maze:
    def __init__(self):
        self.structure = []

    def creation(self):

      with open('map.txt') as fichier:
        content = []
        #On parcourt les lignes du fichier
        for ligne in fichier:
          file_sprites = []
          #On parcourt les sprites (lettres) contenus dans le fichier
          for sprite in ligne:
            #On ignore les "\n" de fin de ligne
            if sprite != '\n':
              #On ajoute le sprite à la liste de la ligne
              file_sprites.append(sprite)
          #On ajoute la ligne à la liste du niveau
          content.append(file_sprites)
        #On sauvegarde cette structure
        self.structure = content

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

class Character:
    """Classe permettant de créer un personnage"""
    def __init__(self, my_maze):
        #Sprites du personnage
        self.character = PY.image.load(ICON_MACGYVER).convert_alpha()
        #Position du personnage en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        #Direction par défaut
        self.direction = self.character
        self.my_maze = my_maze

    def deplacer(self, direction):
        """Methode permettant de déplacer le personnage"""
        
        #Déplacement vers la right
        if direction == 'right':
          #Pour ne pas dépasser l'écran
          if self.case_x < (SIDE_SPRITE_NUM - 1):
            #On vérifie que la case de destination n'est pas un mur
            if self.my_maze[self.case_y][self.case_x+1] != 'm':
              #Déplacement d'une case
              self.case_x += 1
              #Calcul de la position "réelle" en pixel
              self.x = self.case_x * SPRITE_SIZE
          #Image dans la bonne direction
          self.direction = self.character
        
        #Déplacement vers la left
        if direction == 'left':
          if self.case_x > 0:
            if self.my_maze[self.case_y][self.case_x-1] != 'm':
              self.case_x -= 1
              self.x = self.case_x * SPRITE_SIZE
          self.direction = self.character
        
        #Déplacement vers le up
        if direction == 'up':
          if self.case_y > 0:
            if self.my_maze[self.case_y-1][self.case_x] != 'm':
              self.case_y -= 1
              self.y = self.case_y * SPRITE_SIZE
          self.direction = self.character
        
        #Déplacement vers le down
        if direction == 'down':
          if self.case_y < (SIDE_SPRITE_NUM - 1):
            if self.my_maze[self.case_y+1][self.case_x] != 'm':
              self.case_y += 1
              self.y = self.case_y * SPRITE_SIZE
          self.direction = self.character

class Items:
    """Classe générer les items"""
    def __init__(self, content):
      # self.items = []
      self.x = 0
      self.y = 0
      # self.position = 0
      self.my_maze = content
      self.case_x = 0
      self.case_y = 0

    def generateItems(self):
      while self.my_maze[self.case_y][self.case_x] != 'm':
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)
      self.x = self.case_x * SPRITE_SIZE
      self.y = self.case_y * SPRITE_SIZE


# PLACER LES OBJETS DE FACON FIXE D'ABORD ET CHANGER / COMPLEXIFIER LES FONCTIONS ENSUITE