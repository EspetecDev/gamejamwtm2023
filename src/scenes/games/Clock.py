import pygame
import random
import os

class Clock:

    def __init__(self, ctx):
        self.ctx =  ctx
        self.name = 'clock'

        self.turnSound = pygame.mixer.Sound(os.getcwd()+'/assets/levels/games/clock/turn-clock.wav')
        self.bg = pygame.image.load(os.getcwd()+'/assets/levels/games/clock/bg.jpg')
        self.bg2 = pygame.image.load(os.getcwd()+'/assets/levels/games/clock/bg2.png')
        self.hourHandle = pygame.image.load(os.getcwd()+'/assets/levels/games/clock/bg2.png')

        self.handle = pygame.image.load(os.getcwd()+'/assets/levels/games/clock/hourHandle.png')


    def start(self):
        pygame.time.set_timer(pygame.USEREVENT, self.ctx.game.config['minigame_time'] * 1000)
        self.win = True
        # self.objectiveStep = random.randrange(0, 60, 5) / 5
        self.objHour = '16:'
        self.minStep = 1
        self.maxStep = 5
        self.objectiveStep = random.randint(self.minStep, self.maxStep)
        self.objHour = self.objHour + (str(self.objectiveStep*5) if self.objectiveStep > 1 else '05')
        print('currentobjective: '+str(self.objectiveStep))
        print('currentobjective: '+self.objHour)
        self.handleDegree = 30 
        self.handleStep = self.minStep

        self.handlePos = (438,214)

    def update(self):
        for e in self.ctx.game.events:
            if e.type == pygame.USEREVENT:
                if self.handleStep == self.objectiveStep:
                    self.ctx.changeMinigame('success')
                else:
                    self.ctx.changeMinigame('fail')
            elif e.type == pygame.KEYDOWN and self.win == True:
                if e.key == pygame.K_LEFT:
                    if self.handleStep > self.minStep:
                        self.handleStep = self.handleStep - 1
                elif e.key == pygame.K_RIGHT:
                    if self.handleStep < self.maxStep:
                        self.handleStep = self.handleStep + 1
                self.turnSound.play()
                print('currenthandle: '+str(self.handleStep))

    def render(self):
        self.ctx.game.screen.blit(self.bg, (self.ctx.viewportPos['x'], self.ctx.viewportPos['y']))
        self.ctx.game.screen.blit(self.bg2, (self.ctx.viewportPos['x'], self.ctx.viewportPos['y']))
        # (785, 324) text
        objHourText = self.ctx.game.fonts['digital_clock'].render(self.objHour, True, (0,255,255))
        self.ctx.game.screen.blit(objHourText,(785, 324))
        self.rotateHandle()

    def close(self):
        pass

    def rotateHandle(self):
        angle = (-self.handleDegree)*self.handleStep
        pivot = (self.handle.get_width() / 2, self.handle.get_height())
        image_rect = self.handle.get_rect(topleft = (self.handlePos[0] - pivot[0], self.handlePos[1]-pivot[1]))
        offset_center_to_pivot = pygame.math.Vector2(self.handlePos) - image_rect.center
        rotated_offset = offset_center_to_pivot.rotate(-angle)
        rotated_image_center = (self.handlePos[0] - rotated_offset.x, self.handlePos[1] - rotated_offset.y)
        rotated_image = pygame.transform.rotate(self.handle, angle)
        rect = rotated_image.get_rect(center = rotated_image_center)

        self.ctx.game.screen.blit(rotated_image, rect)
