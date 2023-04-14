import pygame
from src.scenes.MainMenu import MainMenu
from src.scenes.InGame import InGame

global config

config = {
    "title": "GameJam WTM 2023",
    "res": (1280, 720),
    "minigame_res": ((0,0))
}

class Game():

    def __init__(self) -> None:
        pass

    def init(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(config["title"])
        self.screen = pygame.display.set_mode(config["res"])
        self.running = True
        self.clock = pygame.time.Clock()
        self.levels = {"mainMenu": MainMenu(self), "ingame":InGame(self)}
        self.currentLevel = self.levels["mainMenu"]

    def update(self):
        self.currentLevel.update()

    def render(self):
        self.screen.fill((0,0,0))
        self.currentLevel.render()
        pygame.display.flip()

    def close(self):
        pygame.quit()

    def changeLevel(self, newGame):
        if newGame == self.currentLevel.name:
            return
        
        self.currentLevel.quit()
        self.currentLevel = self.levels[newGame]

if __name__ == "__main__":
    game = Game()
    game.init()
    
    while game.running:
        game.clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game.running = False
        game.update()
        game.render()
    
    game.close()

    