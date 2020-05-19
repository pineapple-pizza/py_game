from game_files.const import *

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