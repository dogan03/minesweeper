import pygame

class c:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.m = False
        self.r = False
        self.f = False
        self.n = 0

    def drawCell(self, screen, x, y):
        if not self.r:
            pygame.draw.rect(screen, (189,189,189), (x*40, y*40, 40, 40))
            pygame.draw.rect(screen, (255,255,255), (x*40, y*40, 40, 2))
            pygame.draw.rect(screen, (255,255,255), (x*40, y*40, 2, 40))
            pygame.draw.rect(screen, (128,128,128), (x*40+38, y*40, 2, 40))
            pygame.draw.rect(screen, (128,128,128), (x*40, y*40+38, 40, 2))
            if self.f:
                font = pygame.font.SysFont("Arial", 20)
                t = font.render("F", True, (255,0,0))
                screen.blit(t, (x*40+12, y*40+10))
        else:
            pygame.draw.rect(screen, (192,192,192), (x*40, y*40, 40, 40))
            pygame.draw.rect(screen, (128,128,128), (x*40, y*40, 40, 1))
            if self.m:
                pygame.draw.circle(screen, (0,0,0), (x*40+20, y*40+20), 10)
            elif self.n > 0:
                colors = [(0,0,255),(0,128,0),(255,0,0),(0,0,128),(128,0,0),(0,128,128),(0,0,0),(128,128,128)]
                font = pygame.font.SysFont("Arial", 20)
                t = font.render(str(self.n), True, colors[self.n-1])
                screen.blit(t, (x*40+13, y*40+10))
