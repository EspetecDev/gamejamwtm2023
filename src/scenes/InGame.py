import pygame
import os

class InGame:

    def __init__(self, game):
        self.name = 'ingame'
        self.game = game
        self.bg = pygame.image.load(os.getcwd()+'/assets/levels/ingame/Placeholder-big.png')

    def update(self):
        # print('entering ingame')
        for e in pygame.event.get():
            print(e.type)
            if e.type == pygame.K_RETURN:
                self.game.changeLevel('mainMenu')

    def render(self):
        pass


