from constantes import *

class Character:
    '''class for character creation'''
    def __init__(self, my_maze):
        #character sprites
        self.character = PY.image.load(ICON_MACGYVER).convert_alpha()
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