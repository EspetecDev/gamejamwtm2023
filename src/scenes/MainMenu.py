import pygame
import os

class MainMenu:

    def __init__(self, game) -> None:
        self.name = 'mainMenu'
        self.game = game
        self.bg = pygame.image.load(os.getcwd()+'/assets/levels/mainmenu/Main_menu.png')

    def start(self):
        pass

    def update(self):
        for e in self.game.events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    self.game.changeLevel('ingame')

    def render(self):
        self.game.screen.blit(self.bg, (0,0))