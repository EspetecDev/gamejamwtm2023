import pygame
import os
import random

class Fly:

    def __init__(self, ctx):
        self.ctx =  ctx
        self.name = 'fly'
        self.fly = [
            pygame.image.load(os.getcwd()+'/assets/levels/games/fly/fly1.png'),
            pygame.image.load(os.getcwd()+'/assets/levels/games/fly/fly2.png'),
            pygame.image.load(os.getcwd()+'/assets/levels/games/fly/fly3.png'),
            pygame.image.load(os.getcwd()+'/assets/levels/games/fly/fly4.png')
        ]
        self.matamoscas = [
            pygame.image.load(os.getcwd()+'/assets/levels/games/fly/matamoscas1.png'),
            pygame.image.load(os.getcwd()+'/assets/levels/games/fly/matamoscas2.png')
        ]
        self.flyAnimTime = 1
        # px / frame
        self.flySpeed = 1
        self.flyMoveCurrentFrame = 0
        self.flyCurrentFrame = 0
        

    def start(self):
        self.flyPos = {'x': random.randint(self.ctx.viewportPos['x'], self.ctx.viewportPos['x'] + self.ctx.viewportSize['x'] - self.fly[0].get_width()),
                            'y': random.randint(self.ctx.viewportPos['y'], self.ctx.viewportPos['y'] + self.ctx.viewportSize['y'] - self.fly[0].get_height())}
        self.flyRandDirPoint = {'x': random.randint(self.ctx.viewportPos['x'], self.ctx.viewportPos['x'] + self.ctx.viewportSize['x'] - self.fly[0].get_width()),
                                'y': random.randint(self.ctx.viewportPos['y'], self.ctx.viewportPos['y'] + self.ctx.viewportSize['y'] - self.fly[0].get_height())}
    
        pygame.time.set_timer(pygame.USEREVENT, self.ctx.game.config['minigame_time'] * 1000)
        self.win = False
        self.matamoscasPos = (0,0)
        self.flyIdx = 0
        self.matamoscasIdx = 0

        print(self.flyPos)
        print(self.flyRandDirPoint)


    def update(self):
        for e in self.ctx.game.events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    self.win = True
                elif e.key == pygame.K_o:
                    self.win = False
            if e.type == pygame.MOUSEBUTTONUP:
                self.matamoscasHit()
            if e.type == pygame.USEREVENT: 
                if self.win:
                    self.ctx.changeMinigame('success')
                else:
                    self.ctx.changeMinigame('fail')
        
        #                           anim time / num frames * fps
        if not self.win:
            if self.flyCurrentFrame % (self.flyAnimTime / len(self.fly) * 60) == 0:
                self.flyIdx = (self.flyIdx + 1) % (len(self.fly)-1)
            self.flyCurrentFrame = self.flyCurrentFrame + 1

            # fly move
            if self.flyRandDirPoint['x'] - self.flyPos['x'] > 0:
                self.flyPos['x'] = self.flyPos['x'] + self.flySpeed
            elif self.flyRandDirPoint['x'] - self.flyPos['x'] == 0:
                pass
            else:
                self.flyPos['x'] = self.flyPos['x'] - self.flySpeed

            if self.flyRandDirPoint['y'] - self.flyPos['y'] > 0:
                self.flyPos['y'] = self.flyPos['y'] + self.flySpeed
            elif self.flyRandDirPoint['y'] - self.flyPos['y'] == 0:
                pass
            else:
                self.flyPos['y'] = self.flyPos['y'] - self.flySpeed

        # matamoscas move
        self.matamoscasPos = pygame.mouse.get_pos()

    def render(self):
        if not self.win:
            self.ctx.game.screen.blit(self.fly[self.flyIdx], (self.flyPos['x'], self.flyPos['y']))
        self.ctx.game.screen.blit(self.matamoscas[0], self.matamoscasPos)
        # dbgrect = pygame.draw.rect(self.ctx.game.screen, (255,0,0), pygame.Rect(
        #     self.flyPos['x'],
        #     self.flyPos['y'],
        #     20,
        #     20), 2)

    def close(self):
        pass


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
