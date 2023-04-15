import pygame
import os
import random

class LeverActor:

    def __init__(self, symbolId, symbol, leverPos):
        self.symbolId = symbolId
        self.symbolFrame = symbol
        self.leverPos = leverPos
        self.state = 0
        self.leverFrames = [
            pygame.image.load(os.getcwd()+'/assets/levels/games/lever/lever_up.png'),
            pygame.image.load(os.getcwd()+'/assets/levels/games/lever/lever_down.png')
        ]

    def clickLever(self):
        self.state = 1 if self.state == 0 else 0

    def render(self, screen):
        screen.blit(self.leverFrames[self.state], self.leverPos)

class Lever:

    def __init__(self, ctx):
        self.ctx =  ctx
        self.name = 'lever'

        self.numLevers = 4

        self.symbols = [
            pygame.image.load(os.getcwd()+'/assets/levels/games/lever/symbol1.png'),
            pygame.image.load(os.getcwd()+'/assets/levels/games/lever/symbol2.png'),
            pygame.image.load(os.getcwd()+'/assets/levels/games/lever/symbol3.png')
        ]
        self.levers = []
        # lever asset : 125 x 254
        leversmargin = 125
        # sub a lever margin for the final its not necessart
        totalLeversSize = (self.numLevers * (125 + leversmargin)) - (leversmargin/2)
        startPosX = (self.ctx.game.config['res'][0] / 2) - (totalLeversSize/2)

        for i in range(self.numLevers):
            leverPos = (startPosX + (startPosX*i) + leversmargin,  240)
            symbolIdx = random.randint(0, len(self.symbols)-1)
            self.levers.append(LeverActor(symbolIdx, self.symbols[symbolIdx], leverPos))
        
        self.mainSymbolId = random.randint(0, len(self.symbols) - 1)
        self.mainSymbol = self.symbols[self.mainSymbolId]
        self.mainSymbolPos = ((self.ctx.game.config['res'][0] / 2) - (self.mainSymbol.get_width()/2), self.ctx.game.config['res'][1])

    def start(self):
        
        # pygame.time.set_timer(pygame.USEREVENT, self.ctx.game.config['minigame_time'] * 1000)
        self.win = False

    def update(self):
        for e in self.ctx.game.events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    self.win = True
                elif e.key == pygame.K_o:
                    self.win = False
            if e.type == pygame.USEREVENT: 
                if self.win:
                    self.ctx.changeMinigame('success')
                else:
                    self.ctx.changeMinigame('fail')
        
        #                           anim time / num frames * fps

    def render(self):
        self.ctx.game.screen.blit(self.mainSymbol, self.mainSymbolPos)
        for l in self.levers:
            l.render(self.ctx.game.screen)

    def close(self):
        pass

    # TODO: transform to check lever
    def matamoscasHit(self):
        self.matamoscasIdx = 1
        
        checkLeft = self.flyPos['x'] <= self.matamoscasPos[0] + self.matamoscas[0].get_width()
        checkRight = self.flyPos['x'] > self.matamoscasPos[0]
        checkUp = self.flyPos['y'] > self.matamoscasPos[1]
        checkDown = self.flyPos['y'] <= self.matamoscasPos[1] + self.matamoscas[0].get_height()

        if checkLeft and checkRight and checkUp and checkDown:
            #win
            # TODO: splash sound
            self.win = True
