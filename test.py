import pygame
import os
import sys
import random
from math import *
from pygame.locals import *
from sys import exit

class Main(object):
    def __init__(self):
        pygame.init()
        self.size = (800, 600)
        self.screen = pygame.display.set_mode((800,600),0,32)
        pygame.display.set_caption("Mmmmm Gobble, gobble")
        self.clock = pygame.time.Clock()

        self.turkeys = pygame.sprite.Group()
        self.roasts = pygame.sprite.Group()
        for i in range(6):
            x = random.randint(100, 700)
            y = random.randint(100, 500)
            self.turkeys.add(Turkey((x,y)))

        self.background = pygame.Surface((self.size), 0, 32)
        self.b_ground = pygame.image.load("table.jpg")
        
    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            self.clock.tick(60)
            self.background.fill((255,255,255))
            self.background.blit(self.b_ground, (0,0))

            self.m_pos = pygame.mouse.get_pos()

            self.turkeys.update()
            self.roasts.update()

            for t in self.turkeys:
                if t.rect.collidepoint(self.m_pos):
                    if pygame.mouse.get_pressed()[0] is 1:
                        pos = t.rect.center
                        t.kill()
                        self.turkeys.remove(t)
                        self.roasts.add(Roast(pos))

            self.roasts.draw(self.background)
            self.turkeys.draw(self.background)

            self.screen.blit(self.background, (0,0))

            pygame.display.flip()

            

class Turkey(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("turkey.jpeg").convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.x_speed = random.randint(3,5)
        if random.randint(0,1) == 0:
            self.x_speed = -self.x_speed
        self.y_speed = random.randint(3,5)
        if random.randint(0,1) == 0:
            self.y_speed = -self.y_speed

    def update(self):
        x, y = self.rect.center
        x += self.x_speed
        y += self.y_speed
        if x <= 0:
            self.x_speed = -self.x_speed
        if x >= 800:
            self.x_speed = -self.x_speed
        if y <= 0:
            self.y_speed = -self.y_speed
        if y >= 600:
            self.y_speed = -self.y_speed

        self.rect.center = x,y

class Roast(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("roast.jpeg").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.speed = 4

    def update(self):
        x,y = self.rect.center
        y += self.speed

        self.rect.center = x,y

        if  x > 600:
            self.kill()

        
            
        
if __name__ =="__main__":
    main = Main()
    main.main()
   
