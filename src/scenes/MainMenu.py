import pygame
import os

class MainMenu:

    def __init__(self, game) -> None:
        self.name = 'mainMenu'
        self.game = game
        self.bg = pygame.image.load(os.getcwd()+'/assets/levels/ingame/Placeholder-big.png')

    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.K_RETURN:
                self.game.changeLevel('ingame')

    def render(self):
        pass