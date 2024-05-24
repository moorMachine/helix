import pygame
import os

class Rocket:

    def __init__(self,spawn):
        pygame.init()

        self.rocketImg = pygame.image.load(os.path.join('img','rocket.png'))
        self.rocketImg = pygame.transform.scale(self.rocketImg,(192,64))

       # self.rocketImg = pygame.transform.rotate(self.rocketImg,45)

        self.rocketRect = pygame.Rect(spawn[0],spawn[1],32,32)
        self.rocketSprite = pygame.Surface((64,64))
        self.rocketSprite.set_colorkey((0,0,0))

        #self.rocketSprite = pygame.transform.rotate(self.rocketSprite,45)


        # flying animation
        self.currentTime = pygame.time.get_ticks()
        self.lastUpdate = pygame.time.get_ticks()
        self.empty = pygame.Color(0,0,0,0)
        self.animationStep = 0

        self.aimLock = False

        #explosion
        self.explosionImg = pygame.image.load(os.path.join('img','explosion.png'))
        #self.explosionImg = pygame.transform.scale(self.explosionImg,(?,?))
        self.expoosionRect = pygame.Rect(spawn[0],spawn[1],32,32)
        self.expolosionSprite = pygame.Surface((64,64))
        self.expolosionSprite.set_colorkey((0,0,0,))

        self.rocketTarget = None

        self.expolosionStep = 0


    def rocketAnime(self,):
        self.currentTime = pygame.time.get_ticks()

        if self.currentTime - self.lastUpdate >= 90: #90 good
            self.animationStep += 1
            self.lastUpdate = self.currentTime

            self.rocketSprite.fill(self.empty)
            self.rocketSprite.blit(self.rocketImg,(0,0), ((64*self.animationStep) ,0,64,64))
            print("---> ",self.rocketSprite.get_width(), " ",self.rocketSprite.get_height() )

            #self.rocketSprite.blit(self.rocketImg,(0,0), ((25*self.animationStep) ,0,64,64))

        if self.animationStep >= 2:
            self.animationStep = -1
        else:
            pass
        print(self.animationStep)
        return self.rocketSprite


    #def rocketLaunch(self,):
    #    pass

    def rocketFly(self,):

        #if self.rocketTarget.x >

        if(self.rocketRect.x < 0):
            self.rocketRect.x = 800

        speed = 3
        
        if(self.aimLock == True):
            self.rocketRect.x -= speed
            return self


        if self.rocketTarget.y <= self.rocketRect.y:
            self.rocketRect.y -= speed
        else:
            #self.rocketRect.x -= speed
            self.aimLock = True

        #if self.rocketTarget.y >= self.rocketRect.y:
        #    self.rocketRect.y += speed
        #else:
        self.rocketRect.x -= speed

        #self.rocketImg = pygame.transform.rotate(self.rocketImg,-30) # ERROR
        
            #self.rocketRect.x = 800
            #self.rocketRect.y = 800
        #print(self.rocketRect.x)
        
        
        #self.rocketRect.y -= 1
        
        print(self.rocketTarget.x,"  ",self.rocketTarget.y)
        return self


    #to do
    def rocketExplosion(self,):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        del self



    def test(self,):
        return self.rocketImg