import pygame
import os

class MainMenu:

    def __init__(self, game) -> None:
        self.name = 'mainMenu'
        self.game = game

        self.effectTime = 3
        self.btnEffect = False
        self.framesToSkip = 1
        self.currentFrame = 0
        self.showBtn = True
        # self.currentSkipFrames = 0
        # self.maxSkipFrames = 20

        self.bg = pygame.image.load(os.getcwd()+'/assets/levels/mainmenu/Main_menu.png')
        self.btn = pygame.image.load(os.getcwd()+'/assets/levels/mainmenu/btn_start.png')
        self.girl = pygame.image.load(os.getcwd()+'/assets/levels/mainmenu/girl.png')
        
        self.btnCoords = ((self.game.config['res'][0] / 2) - self.btn.get_size()[0]/2,
                          (self.game.config['res'][1] / 2) + 200 - self.btn.get_size()[1]/2)
        
        self.girlCoords = (self.game.config['res'][0] - self.girl.get_size()[0],
                           self.game.config['res'][1] - self.girl.get_size()[1])
        

    def start(self):
        pass

    def update(self):
        for e in self.game.events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    # pygame.time.set_timer(pygame.USEREVENT, self.effectTime * 1000)
                    # self.btnEffect = True
                    self.game.changeLevel('ingame')    
            if e.type == pygame.USEREVENT: 
                self.game.changeLevel('ingame')
        

    def render(self):
        self.game.screen.blit(self.bg, (0,0))
        self.game.screen.blit(self.girl, self.girlCoords)

        if self.btnEffect:
            self.flickerEffect()
        else:
            self.game.screen.blit(self.btn, self.btnCoords)

    def flickerEffect(self):
        # self.currentSkipFrames = pygame.math.lerp(0, 60, self.currentSkipFrames/self.maxSkipFrames)
        self.currentFrame = self.currentFrame + 1
        if self.currentFrame % self.framesToSkip == 0:
            self.currentFrame = 0
            if self.showBtn:
                self.game.screen.blit(self.btn, self.btnCoords)
            self.showBtn = not self.showBtn