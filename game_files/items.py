import random
from game_files.const import *

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