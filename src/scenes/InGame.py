import pygame
import os
import json

class InGame:

    def __init__(self, game):
        self.name = 'ingame'
        self.game = game
        f = open(os.getcwd()+'/assets/texts.json')
        self.texts = json.load(f)
        self.bg = pygame.image.load(os.getcwd()+'/assets/levels/ingame/Placeholder-big.png')

    def start(self):
        self.currMinigame = 0
        self.currText = self.texts['start']
        self.currTextIdx = 0

    def update(self):
        for e in self.game.events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    self.game.changeLevel('mainMenu')
                elif e.key == pygame.K_l:
                    if self.currTextIdx <= len(self.currText)-1:
                        self.currTextIdx = self.currTextIdx + 1
            if e.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

    def render(self):
        # 305 116 star minigame vp
        # 316 548 start text
        text = self.game.font.render('Current minigame: '+str(self.currMinigame), True, (255,255,255))
        dialog = self.game.font.render(self.currText[self.currTextIdx], True, (255,255,255))
        # text.get_rect().center = (5, 5)
        self.game.screen.blit(text, (305, 116))
        self.game.screen.blit(self.bg, (0,0))
        


