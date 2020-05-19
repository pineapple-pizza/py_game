import random
from constantes import *

class Maze:
    '''maze class structure'''

    def __init__(self):
        self.structure = []

    def creation(self):
        '''load map and create maze'''

        with open('game_files/map.txt') as fichier:
            content = []
            #loop through lines in file
            for ligne in fichier:
                file_sprites = []
                #loop through sprites (letters) in file
                for sprite in ligne:
                  #ignore '\n'
                    if sprite != '\n':
                        #add sprite to line list
                        file_sprites.append(sprite)
                #add line to level list
                content.append(file_sprites)
            #save structure
            self.structure = content

    def display_maze(self, window):
        '''method for displaying maze from creation()'''

        background = py.image.load(FLOOR).convert()
        finishline = py.image.load(ICON_GUARDIAN).convert()
        walls = py.image.load(WALL).convert()

        #check list level
        num_ligne = 0
        for ligne in self.structure:
            #Oloop through list of lines
            num_case = 0
            for sprite in ligne:
                #real position in pixels
                _x = num_case * SPRITE_SIZE
                _y = num_ligne * SPRITE_SIZE
                if sprite == '0':
                    window.blit(background, (_x, _y))
                elif sprite == 'm':
                    window.blit(walls, (_x, _y))
                elif sprite == 'd':
                    window.blit(background, (_x, _y))
                elif sprite == 'a':
                    window.blit(finishline, (_x, _y))

                num_case += 1
            num_ligne += 1

class Character:
    '''class for character creation'''
    def __init__(self, my_maze):
        #character sprites
        self.character = py.image.load(ICON_MACGYVER).convert_alpha()
        #character position in cases and pixels
        self.case_x = 0
        self.case_y = 0
        self._x = 0
        self._y = 0
        #default image direction
        self.direction = self.character
        self.my_maze = my_maze

    def deplacer(self, direction):
        '''method for moving character'''

        #move to the right
        if direction == 'right':
          #to not get off screen
            if self.case_x < (SIDE_SPRITE_NUM - 1):
              #to check collision with walls
                if self.my_maze[self.case_y][self.case_x + 1] != 'm':
                    #move a sprite
                    self.case_x += 1
                    #real position with pixels
                    self._x = self.case_x * SPRITE_SIZE
            #control image side
            self.direction = self.character

        #move to the left
        if direction == 'left':
            if self.case_x > 0:
                if self.my_maze[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self._x = self.case_x * SPRITE_SIZE
            self.direction = self.character

        #move up
        if direction == 'up':
            if self.case_y > 0:
                if self.my_maze[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self._y = self.case_y * SPRITE_SIZE
            self.direction = self.character

        #move down
        if direction == 'down':
            if self.case_y < (SIDE_SPRITE_NUM - 1):
                if self.my_maze[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self._y = self.case_y * SPRITE_SIZE
            self.direction = self.character

class Items:
    '''class for generating items'''

    def __init__(self, content):
        self._x = 0
        self._y = 0
        self.my_maze = content
        self.case_x = 0
        self.case_y = 0

    def generate_items(self):
        '''method for generating items'''

        while self.my_maze[self.case_y][self.case_x] != '0':
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)
        self._x = self.case_x * SPRITE_SIZE
        self._y = self.case_y * SPRITE_SIZE
