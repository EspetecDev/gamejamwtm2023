import pygame
import os
import random

class Obstacle:

    def __init__(self, game, isUp, speed) -> None:
        self.game = game

        self.isUp = isUp
        self.speed = speed
        self.frame = pygame.image.load(os.getcwd()+'/assets/levels/games/dodge/mc.png')
        yPos = self.game.ctx.viewportPos['y'] if self.isUp else (self.game.ctx.viewportPos['y'] + self.game.ctx.viewportSize['y'] - self.frame.get_width())
        self.pos = (self.game.ctx.viewportPos['x'] + self.game.ctx.viewportSize['x'] + 10, yPos)

    def update(self):
        self.pos = (self.pos[0] - self.speed, self.pos[1])

    def render(self, screen):
        screen.blit(self.frame, self.pos)

    def checkCollision(self):
        mcPos = self.game.mcPos
        mcSize = self.game.mc.get_size()
        # end check, if collision, self.win = False
        # if self.pos[0] < mcPos[0] and self.pos[0] + self.frame.get_width()


class Dodge:

    def __init__(self, ctx):
        self.ctx =  ctx
        self.name = 'dodge'
        
        self.numObstacles = 7  
        # mc
        self.mc = pygame.image.load(os.getcwd()+'/assets/levels/games/dodge/mc.png')
        self.mcPos = (ctx.viewportPos['x'] + 10, ctx.viewportPos['y'] + (ctx.viewportSize['y']/2) - self.mc.get_height())
        self.mcSpeed = 5

        # obstacles
        self.obstacleSpace = 20
        self.obstacleSpeed = 3
        self.obstacles = []
        for i in range(self.numObstacles):
            o = Obstacle(self, bool(random.getrandbits(1)), self.obstacleSpeed)
            o.pos = (o.pos[0] + (i*(self.obstacleSpace+o.frame.get_width())), o.pos[1])
            self.obstacles.append(o)


    def start(self):
        
        # pygame.time.set_timer(pygame.USEREVENT, self.ctx.game.config['minigame_time'] * 1000)
        self.win = True
    
    def update(self):
        for e in self.ctx.game.events:
            # if e.type == pygame.KEYDOWN:
            #     print(e.unicode)
            #     if e.key == pygame.K_UP:
            #         if self.mcPos[1] > self.ctx.viewportPos['y']:
            #             self.mcPos = (self.mcPos[0], self.mcPos[1] - self.mcSpeed)
            #     elif e.key == pygame.K_DOWN:
            #         if self.mcPos[1] < self.ctx.viewportPos['y'] + self.ctx.viewportSize['y']:
            #             self.mcPos = (self.mcPos[0], self.mcPos[1] + self.mcSpeed)
            if e.type == pygame.USEREVENT:
                if self.win:
                    self.ctx.changeMinigame('success')
                else:
                    self.ctx.changeMinigame('fail')


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.mcPos[1] > self.ctx.viewportPos['y']:
                self.mcPos = (self.mcPos[0], self.mcPos[1] - self.mcSpeed)
        if keys[pygame.K_DOWN]:
            if self.mcPos[1] < self.ctx.viewportPos['y'] + self.ctx.viewportSize['y'] - self.mc.get_height():
                self.mcPos = (self.mcPos[0], self.mcPos[1] + self.mcSpeed)
        self.checkColision()
        for o in self.obstacles:
            o.update()
                    
    def render(self):
        self.ctx.game.screen.blit(self.mc, self.mcPos)
        for o in self.obstacles:
            o.render(self.ctx.game.screen)

    def close(self):
        pass

    def checkColision(self):
        pass