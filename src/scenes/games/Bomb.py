import pygame
import random
import string
import os

class Bomb:
    def __init__(self, ctx):
        self.ctx =  ctx
        self.name = 'bomb'
        self.codeSize = 5

        # self.bombSound = pygame.mixer.Sound(os.getcwd()+'/assets/levels/games/bomb/bomb-ticking.wav')
        self.bg = pygame.image.load(os.getcwd()+'/assets/levels/games/bomb/bg.png')
        self.codePos = [
            (486, 185),
            (566, 187),
            (646, 190),
            (727, 190),
            (807, 188)
        ]
        self.inputPos = [
            (488, 290),
            (572, 290),
            (646, 296),
            (723, 290),
            (805, 290)
        ]

    def start(self):
        self.code = ''.join(random.choices(string.ascii_uppercase, k=self.codeSize)) #'testo'
        print(self.code)
        self.codeSurfaces = []
        for i in range(len(self.code)):
            self.codeSurfaces.append(self.ctx.game.fonts['clock'].render(self.code[i].upper(), True, (0,255,0)))

        self.inputSurfaces = []
        self.currentInput = ''
        pygame.time.set_timer(pygame.USEREVENT, self.ctx.game.config['minigame_time'] * 1000)
        self.win = False
        # self.bombSound.play()
    
    def update(self):
        for e in self.ctx.game.events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    self.currentInput = self.currentInput[:-1]
                elif len(self.currentInput) < self.codeSize and e.unicode.isalpha():
                    self.currentInput = self.currentInput + e.unicode.upper()
                self.generateInputArray()
            
            elif e.type == pygame.USEREVENT:
                # self.bombSound.stop()
                if self.currentInput == self.code:
                    self.ctx.changeMinigame('success')
                else:
                    self.ctx.changeMinigame('fail')

    def render(self):
        self.ctx.game.screen.blit(self.bg, (self.ctx.viewportPos['x'], self.ctx.viewportPos['y']))
        for i in range(len(self.codeSurfaces)):
            self.ctx.game.screen.blit(self.codeSurfaces[i],self.codePos[i])

        for i in range(len(self.inputSurfaces)):
            self.ctx.game.screen.blit(self.inputSurfaces[i], self.inputPos[i])

    def close(self):
        pass

    def generateInputArray(self):
        self.inputSurfaces = []
        for i in range(len(self.currentInput)):
            self.inputSurfaces.append(self.ctx.game.fonts['clock'].render(self.currentInput[i].upper(), True, (0,255,0)))
        
