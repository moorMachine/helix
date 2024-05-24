import pygame
import os
from rocket import Rocket


class Enemy:

    def __init__(self,):
        pygame.init()
        self.enemyImg = pygame.image.load(os.path.join('img','rocketLAN.png'))
        self.enemyImg = pygame.transform.scale(self.enemyImg,(128,64))


        self.enemyHp = 100
        self.enemyRect = pygame.Rect(800,590,32,32)

        self.empty = pygame.Color(0,0,0,0)
        self.enemySpriteFragment = pygame.Surface((64,64))
        self.enemySpriteFragment.set_colorkey((0,0,0)) 

        self.lastUpdate = pygame.time.get_ticks()
        self.currentTime = pygame.time.get_ticks()
        self.animationStep = 0

        self.rocket = Rocket((self.enemyRect.x,self.enemyRect.y))


    def animEnemy(self,):
        self.currentTime = pygame.time.get_ticks()
        if self.currentTime - self.lastUpdate >= 150: #cooldown

            self.animationStep += 1
            self.lastUpdate = self.currentTime

            self.enemySpriteFragment.fill(self.empty)
            self.enemySpriteFragment.blit(self.enemyImg,(0,0), ((64*self.animationStep) ,0,128,64))
        if self.animationStep >= 1:
            self.animationStep = -1
        else:
            pass

        return self.enemySpriteFragment

    def moveEnemy(self,):
        self.enemyRect.x -= 2

        if self.enemyRect.x == -64:
            self.enemyRect.x = 1290

    def rocketLaunch(self,target):
        
        rocket = Rocket()
        rocket.rocketTarget=target
        return rocket


        
        
    




