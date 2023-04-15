import pygame

class Bomb:

    def __init__(self, ctx):
        self.ctx =  ctx
        self.name = 'bomb'

    def start(self):
        pass

    def update(self):
        for e in self.ctx.game.events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    self.ctx.changeMinigame('fail')
                elif e.key == pygame.K_o:
                    self.ctx.changeMinigame('success')

    def render(self):
        pass

    def close(self):
        pass
