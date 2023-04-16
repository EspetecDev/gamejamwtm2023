import pygame
import os
import random

class Obstacle:

    def __init__(self, game, isUp, speed) -> None:
        self.game = game

        self.isUp = isUp
        self.speed = speed
        cat_color = random.choice(['blue', 'green', 'red'])
        self.catSound = pygame.mixer.Sound(os.getcwd()+'/assets/levels/games/dodge/dodge-catsound.wav')
        self.soundMade = False
        self.frame = pygame.image.load(os.getcwd()+'/assets/levels/games/dodge/o_'+cat_color+'1.png')
        yPos = self.game.ctx.viewportPos['y'] if self.isUp else (self.game.ctx.viewportPos['y'] + self.game.ctx.viewportSize['y'] - self.frame.get_width())
        self.pos = (self.game.ctx.viewportPos['x'] + self.game.ctx.viewportSize['x'] + 10, yPos)
        self.colliderRect = pygame.Rect(self.pos[0], self.pos[1], self.frame.get_width(), self.frame.get_height())

    def update(self):
        self.pos = (self.pos[0] - self.speed, self.pos[1])
        if self.soundMade == False:
            if self.pos[0] + self.frame.get_width() < self.game.ctx.viewportPos['x']:
                self.catSound.play()
                self.soundMade = True
        self.colliderRect.x = self.pos[0]
        if self.checkCollision():
            self.game.win = False
            print('collide from obs: '+str(self)+' , lose')

    def render(self, screen):
        screen.blit(self.frame, self.pos)

    def checkCollision(self):
        return pygame.Rect.colliderect(self.colliderRect, self.game.mcColliderRect)
        # end check, if collision, self.win = False
        # if self.pos[0] < mcPos[0] and self.pos[0] + self.frame.get_width()


class Dodge:

    def __init__(self, ctx):
        self.ctx =  ctx
        self.name = 'dodge'
        
        self.bg = pygame.image.load(os.getcwd()+'/assets/levels/games/dodge/bg.jpeg')

        self.numObstacles = 7  
        # mc
        self.mc = pygame.image.load(os.getcwd()+'/assets/levels/games/dodge/mc.png')
        self.mcSpeed = 20

        # obstacles
        self.obstacleSpace = 20
        self.obstacleSpeed = 10


    def start(self):
        self.mcPos = (self.ctx.viewportPos['x'] + 10, self.ctx.viewportPos['y'] + (self.ctx.viewportSize['y']/2) - self.mc.get_height())
        self.mcColliderRect = pygame.Rect(self.mcPos[0], self.mcPos[1], self.mc.get_width(), self.mc.get_height())

        self.obstacles = []
        for i in range(self.numObstacles):
            o = Obstacle(self, bool(random.getrandbits(1)), self.obstacleSpeed)
            o.pos = (o.pos[0] + (i*(self.obstacleSpace+o.frame.get_width())), o.pos[1])
            self.obstacles.append(o)
        
        pygame.time.set_timer(pygame.USEREVENT, self.ctx.game.config['minigame_time'] * 1000)
        self.win = True
    
    def update(self):
        for e in self.ctx.game.events:
            if e.type == pygame.USEREVENT:
                if self.win:
                    self.ctx.changeMinigame('success')
                else:
                    self.ctx.changeMinigame('fail')

        if self.win == True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                if self.mcPos[1] > self.ctx.viewportPos['y']:
                    self.mcPos = (self.mcPos[0], self.mcPos[1] - self.mcSpeed)
                    self.mcColliderRect.y = self.mcPos[1]
            if keys[pygame.K_DOWN]:
                if self.mcPos[1] < self.ctx.viewportPos['y'] + self.ctx.viewportSize['y'] - self.mc.get_height():
                    self.mcPos = (self.mcPos[0], self.mcPos[1] + self.mcSpeed)
                    self.mcColliderRect.y = self.mcPos[1]
            
            for o in self.obstacles:
                o.update()


                    
    def render(self):
        self.ctx.game.screen.blit(self.bg, (self.ctx.viewportPos['x'], self.ctx.viewportPos['y']))
        self.ctx.game.screen.blit(self.mc, self.mcPos)
        for o in self.obstacles:
            o.render(self.ctx.game.screen)

    def close(self):
        pass