import pygame

class Game():

    def __init__(self) -> None:
        self.running = True

    def init(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def close(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.init()
    
    while game.running:
        game.update()
        game.render()
    
    game.close()

    