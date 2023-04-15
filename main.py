import pygame
import os
from src.scenes.MainMenu import MainMenu
from src.scenes.InGame import InGame

os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

config = {
    "title": "AI Crush - GameJam WTM 2023",
    "res": (1280, 720),
    "minigame_res": (345, 670),
    "minigame_list": ["fly", "bomb", "clock"],
    "minigame_num": 5,
    "minigame_time": 3,
    "lives": 3
}

class Game():

    def __init__(self) -> None:
        pass

    def init(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(config["title"])
        self.config = config
        self.fonts = {
            "regular": pygame.font.Font(os.getcwd()+'/assets/fonts/pixeloid.ttf', 12),
            "dialog": pygame.font.Font(os.getcwd()+'/assets/fonts/pixeloid.ttf', 20),
            "credits_h1": pygame.font.Font(os.getcwd()+'/assets/fonts/pixeloid.ttf', 24),
            "credits_h2": pygame.font.Font(os.getcwd()+'/assets/fonts/pixeloid.ttf', 20),
        }
        self.screen = pygame.display.set_mode(config["res"], pygame.SCALED | pygame.RESIZABLE)
        self.running = True
        self.clock = pygame.time.Clock()
        self.levels = {"mainMenu": MainMenu(self), "ingame":InGame(self)}
        self.currentLevel = self.levels["mainMenu"]
        self.events = []

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
        
        self.currentLevel = self.levels[newGame]
        self.currentLevel.start()

if __name__ == "__main__":
    game = Game()
    game.init()
    
    while game.running:
        game.clock.tick(60)
        game.events = pygame.event.get()
        for e in game.events:
            if e.type == pygame.QUIT:
                game.running = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_F11:
                    pass
                    # pygame.display.toggle_fullscreen()
        game.update()
        game.render()
    
    game.close()

    