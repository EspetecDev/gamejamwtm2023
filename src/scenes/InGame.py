import pygame
import os
import json

class InGame:

    def __init__(self, game):
        self.name = 'ingame'
        self.game = game
        self.numMinigames = 6
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
                    if self.currTextIdx < len(self.currText)-1:
                        self.currTextIdx = self.currTextIdx + 1
            if e.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

    def render(self):
        # 305 116 star minigame vp
        # 316 548 start text
        # 80x40 square minigame
        dialogObj = self.currText[self.currTextIdx]
        text = self.game.fonts['regular'].render('Current minigame: '+str(self.currMinigame), True, (255,255,255))
        # TODO: limit to blocks of 35 chars
        dialog = self.game.fonts['dialog'].render(dialogObj['character'] + ': '+dialogObj['text'], True, (0,0,0))
        # text.get_rect().center = (5, 5)
        self.game.screen.blit(self.bg, (0,0))
        self.game.screen.blit(text, (305, 116))
        self.game.screen.blit(dialog, (316, 548))
        self.renderGameMap()

    def renderGameMap(self):
        basePos = {'x': 200, 'y': 15}
        squareSize = {'w': 80, 'h': 40}
        for i in range(self.numMinigames):
            pygame.draw.rect(self.game.screen, (200, 0, 0), pygame.Rect(
                basePos['x'] + (i*squareSize['w']*2), 
                basePos['y'],
                squareSize['w'],
                squareSize['h']))
            if i != self.numMinigames-1:
                pygame.draw.line(self.game.screen, (200, 0, 0),
                                [basePos['x'] + (i*squareSize['w']*2) + squareSize['w'], basePos['y'] + (squareSize['h']/2)],
                                [basePos['x'] + (i*squareSize['w']*2) + squareSize['w'] + squareSize['w'], basePos['y'] + (squareSize['h']/2)], 2)
            
            
        
            

        
        


