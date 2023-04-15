import pygame

class GameComplete:

    def __init__(self, ctx):
        self.ctx =  ctx
        self.verticalSpacing = 30
        self.moveCredits = True
        self.startTextCoords = {"x": self.ctx.game.config['res'][0]/2, "y": 500}
        self.name = 'gamecomplete'
        self.textgr1 = [
            self.ctx.game.fonts['credits_h1'].render('GAMEJAM WTM 2023', True, (255,255,255)),
            self.ctx.game.fonts['credits_h2'].render('WOMEN VS AI', True, (255,255,255)),
        ]

        self.textgr2 = [
            self.ctx.game.fonts['credits_h1'].render('FUET STUDIOS', True, (255,255,255)),
            self.ctx.game.fonts['credits_h2'].render('ART - @Kalther', True, (255,255,255)),
            self.ctx.game.fonts['credits_h2'].render('DESING - @RandomGios', True, (255,255,255)),
            self.ctx.game.fonts['credits_h2'].render('CODE - @Espetec', True, (255,255,255)),
        ]

    def start(self):
        self.startTextCoords = {"x": self.ctx.game.config['res'][0]/2, "y": 500}
        self.moveCredits = True

    def update(self):
        for e in self.ctx.game.events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    self.ctx.game.changeLevel('mainMenu')
                if e.key == pygame.K_KP_ENTER:
                    self.moveCredits = False
                    self.startTextCoords['y'] = 115

        if self.moveCredits:
            self.startTextCoords['y'] = self.startTextCoords['y'] - 1
            self.startTextCoords['y'] = self.startTextCoords['y'] - 1

    def render(self):
        for i in range(len(self.textgr1)):
            self.ctx.game.screen.blit(self.textgr1[i], (self.startTextCoords['x'] - self.textgr1[i].get_width()/2, self.startTextCoords['y'] + (i*self.verticalSpacing)))
        for i in range(len(self.textgr2)):
            self.ctx.game.screen.blit(self.textgr2[i], (self.startTextCoords['x'] - self.textgr2[i].get_width()/2, self.startTextCoords['y'] + (len(self.textgr2)*self.verticalSpacing) + 50 + (i*self.verticalSpacing)))

    def close(self):
        pass
