import pygame
import os
import json
import random
from .games.Fly import Fly
from .games.Bomb import Bomb
from .games.Clock import Clock


class InGame:

    def __init__(self, game):
        self.name = 'ingame'
        self.game = game

        #init minigames
        self.minigames = self.generateMinigames()
        # init texts
        self.startTextCoords = {'x': 455, 'y': 530}
        self.limitchars = 25
        self.dialogVerticalSpacing = 30
        f = open(os.getcwd()+'/assets/texts.json')
        self.texts = json.load(f)

        # assets
        self.bg = pygame.image.load(os.getcwd()+'/assets/levels/ingame/Placeholder-big.png')

    def start(self):
        self.currentState = 'start'
        self.currMinigame = 0
        self.currText = self.texts['start']
        self.currTextIdx = 0
        self.currLives = self.game.config['lives']

    def update(self):
        for e in self.game.events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    self.nextDialog()
                elif e.key == pygame.K_ESCAPE:
                    self.game.running = False
                elif e.key == pygame.K_F1:
                    self.game.changeLevel('mainMenu')

            if e.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        
        if self.currentState == 'playing':
            self.minigames[self.currMinigame].update()

    def render(self):
        # 305 116 star minigame vp
        # 316 548 start text
        # 80x40 square minigame
        # checker if text is empty
        if self.currText[0]:
            dialogObj = self.currText[self.currTextIdx]

        dbgtext = self.game.fonts['regular'].render('Current minigame: '+str(self.currMinigame), True, (255,255,255))
        dbgtext2 = self.game.fonts['regular'].render('Current state: '+str(self.currentState), True, (255,255,255))
        # dialogs
        dialogStr = dialogObj['character'] + ': '+dialogObj['text'] if self.currText[0] else ""
        dialogs = self.formatText(dialogStr)

        self.game.screen.blit(self.bg, (0,0))

        ## RENDER DEBUG
        self.game.screen.blit(dbgtext, (305, 116))
        self.game.screen.blit(dbgtext2, (305, 130))

        # render dialogs
        for i in range(len(dialogs)):
            self.game.screen.blit(dialogs[i], (self.startTextCoords['x'], self.startTextCoords['y'] + (i*self.dialogVerticalSpacing)))

    def changeMinigame(self, state):
        print('game '+self.minigames[self.currMinigame].name+' state: '+state)
        if state == 'fail':
            self.currLives = self.currLives - 1
            if self.currLives == 0:
                self.currentState = 'gameover'
            else:
                self.currentState = 'failed'
                self.minigames[self.currMinigame].start()
        elif state == 'success':
            if self.currMinigame < self.game.config['minigame_num']-1:
                self.currMinigame = self.currMinigame + 1
                self.currentState = 'mg_start'
                self.minigames[self.currMinigame].start()
        self.nextDialog()
            



    def generateMinigames(self):
        minigames = []
        choices = random.choices(self.game.config['minigame_list'], k=self.game.config['minigame_num'])
        for choice in choices:
            if choice == "fly":
                game = Fly(self)
            elif choice == "bomb":
                game = Bomb(self)
            elif choice == "clock":
                game = Clock(self)
            else:
                continue
            minigames.append(game)
        print("generated map: ")
        print(choices)
        return minigames
    
    def nextDialog(self):
        if self.currentState == 'playing':
            return
        
        if self.currTextIdx < len(self.currText)-1:
            self.currTextIdx = self.currTextIdx + 1
        else:
            if self.currentState == 'start':
                self.currentState = 'mg_start'
                self.currTextIdx = 0
                self.currText = self.texts[self.minigames[0].name+'_start']
            elif self.currentState == 'mg_start':
                self.currTextIdx = 0
                self.currText = self.texts['empty']
                self.currentState = 'playing'
            elif self.currentState == 'failed':
                self.currTextIdx = 0
                self.currText = self.texts['fail'+str(random.randint(1,2))]
                self.currentState = 'mg_start'
            elif self.currentState == 'gameover':
                self.currTextIdx = 0
                self.currText = self.texts['gameover']
                self.currentState = 'tomenu'
            elif self.currentState == 'tomenu':
                self.game.changeLevel('mainMenu')
                

    def formatText(self, text):
        lines = []
        text_rects = []
        curr_line = ""
        splitted_text = text.split(" ")
        for word in splitted_text:
            temp_curline = curr_line + ' ' + word
            if len(temp_curline) > self.limitchars:
                lines.append(curr_line)
                curr_line = ' ' + word
            elif word == splitted_text[-1]:
                lines.append(temp_curline)
            else:
                curr_line = curr_line + ' ' + word
        # lines[-1] = lines[-1] + temp_curline
        for l in lines:
            text_rects.append(self.game.fonts['dialog'].render(l, True, (255,255,255)))
        return text_rects

            

    # def renderGameMap(self):
    #     basePos = {'x': 200, 'y': 15}
    #     squareSize = {'w': 80, 'h': 40}
    #     for i in range(self.numMinigames):
    #         pygame.draw.rect(self.game.screen, (200, 0, 0), pygame.Rect(
    #             basePos['x'] + (i*squareSize['w']*2), 
    #             basePos['y'],
    #             squareSize['w'],
    #             squareSize['h']))
    #         if i != self.numMinigames-1:
    #             pygame.draw.line(self.game.screen, (200, 0, 0),
    #                             [basePos['x'] + (i*squareSize['w']*2) + squareSize['w'], basePos['y'] + (squareSize['h']/2)],
    #                             [basePos['x'] + (i*squareSize['w']*2) + squareSize['w'] + squareSize['w'], basePos['y'] + (squareSize['h']/2)], 2)
            
            
        
            

        
        


