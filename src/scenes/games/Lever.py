import pygame
import os
import random

class LeverActor:

    def __init__(self, symbolId, symbol, leverPos, leverSound):
        self.symbolId = symbolId
        self.symbolFrame = symbol
        self.leverPos = leverPos
        self.leverSound = leverSound
        self.state = 0
        self.leverFrames = [
            pygame.image.load(os.getcwd()+'/assets/levels/games/lever/lever_up.png'),
            pygame.image.load(os.getcwd()+'/assets/levels/games/lever/lever_down.png')
        ]
        self.symbolPos = ((leverPos[0] + (self.leverFrames[0].get_width()/2) - (self.symbolFrame.get_width()/2)), 
                          leverPos[1] - 30 - self.symbolFrame.get_width()) 

    def clickLever(self):
        self.state = 1 if self.state == 0 else 0
        self.leverSound.play()

    def render(self, screen):
        screen.blit(self.symbolFrame, self.symbolPos)
        screen.blit(self.leverFrames[self.state], self.leverPos)

class Lever:

    def __init__(self, ctx):
        self.ctx =  ctx
        self.name = 'lever'

        self.numLevers = 4
        self.leverSound = pygame.mixer.Sound(os.getcwd()+'/assets/levels/games/lever/lever.wav')
        self.bg = pygame.image.load(os.getcwd()+'/assets/levels/games/lever/bg.jpg')
        self.symbols = [
            pygame.image.load(os.getcwd()+'/assets/levels/games/lever/symbol1.png'),
            pygame.image.load(os.getcwd()+'/assets/levels/games/lever/symbol2.png'),
            pygame.image.load(os.getcwd()+'/assets/levels/games/lever/symbol3.png')
        ]
        self.levers = []
        # lever asset : 125 x 254
        leversmargin = 75
        # sub a lever margin for the final its not necessart
        totalLeversSize = (self.numLevers * (125 + leversmargin)) - (leversmargin)
        startPosX = (self.ctx.viewportPos['x'] + (self.ctx.viewportSize['x']/2)) - (totalLeversSize/2)

        for i in range(self.numLevers):
            leverPos = (startPosX + ((125 + leversmargin)*i),  230)
            symbolIdx = random.randint(0, len(self.symbols)-1)
            self.levers.append(LeverActor(symbolIdx, self.symbols[symbolIdx], leverPos, self.leverSound))
        
        self.mainSymbolId = random.randint(0, len(self.symbols) - 1)
        self.mainSymbol = self.symbols[self.mainSymbolId]
        self.mainSymbolPos = ((self.ctx.viewportPos['x'] + (self.ctx.viewportSize['x']/2)) - (self.mainSymbol.get_width()/2), self.ctx.viewportPos['y'] + 20)

    def start(self):
        
        pygame.time.set_timer(pygame.USEREVENT, self.ctx.game.config['minigame_time'] * 1000)
        self.win = False
        self.currLeverOver = -1

    def update(self):
        self.checkLeverHit()
        for e in self.ctx.game.events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    self.win = True
                elif e.key == pygame.K_o:
                    self.win = False
            elif e.type == pygame.USEREVENT:
                self.win = True 
                i = 0
                for l in self.levers:
                    sameCondition = (l.symbolId == self.mainSymbolId and l.state == 1)
                    diffCondition = (l.symbolId != self.mainSymbolId and l.state == 0)
                    self.win = self.win and (sameCondition or diffCondition)
                    print('lever '+str(i)+' correct:'+str((sameCondition or diffCondition)))
                print('win: '+str(self.win))
                if self.win:
                    self.ctx.changeMinigame('success')
                else:
                    self.ctx.changeMinigame('fail')
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if self.currLeverOver != -1:
                    self.levers[self.currLeverOver].clickLever()
        
    def render(self):
        self.ctx.game.screen.blit(self.bg, (self.ctx.viewportPos['x'], self.ctx.viewportPos['y']))
        self.ctx.game.screen.blit(self.mainSymbol, self.mainSymbolPos)
        for l in self.levers:
            l.render(self.ctx.game.screen)

    def close(self):
        pass

    def checkLeverHit(self):
        showCursor = False
        idx = 0
        for l in self.levers:
            checkLeft = pygame.mouse.get_pos()[0] <= l.leverPos[0] + l.leverFrames[0].get_width()
            checkRight = pygame.mouse.get_pos()[0] > l.leverPos[0]
            checkUp = pygame.mouse.get_pos()[1] > l.leverPos[1]
            checkDown = pygame.mouse.get_pos()[1] <= l.leverPos[1] +  l.leverFrames[0].get_height()
            currLevelPressed = checkLeft and checkRight and checkUp and checkDown
            showCursor = showCursor or currLevelPressed
            if currLevelPressed:
                self.currLeverOver = idx
            idx = idx+1

        if showCursor:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            self.currLeverOver = -1
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
