import pygame

class Bomb:

    def __init__(self, ctx):
        self.ctx =  ctx
        self.name = 'bomb'
        self.codeSize = 5

    def start(self):
        self.code = 'testo'
        self.currentInput = ''
        pygame.time.set_timer(pygame.USEREVENT, self.ctx.game.config['minigame_time'] * 1000)
        self.win = False
    
    def update(self):
        for e in self.ctx.game.events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    self.currentInput = self.currentInput[:-1]
                elif len(self.currentInput) < self.codeSize:
                    self.currentInput = self.currentInput + e.unicode
            
            elif e.type == pygame.USEREVENT:
                if self.currentInput == self.code:
                    self.ctx.changeMinigame('success')
                else:
                    self.ctx.changeMinigame('fail')

    def render(self):
        code = self.ctx.game.fonts['regular'].render('code: '+self.code, True, (255,255,255))
        input = self.ctx.game.fonts['regular'].render('len: '+str(len(self.currentInput))+'input: '+self.currentInput, True, (255,255,255))
        self.ctx.game.screen.blit(code,(400, 50))
        self.ctx.game.screen.blit(input, (400, 80))

    def close(self):
        pass
