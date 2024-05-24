import pygame
import os

class Player:
    
    cooldown = 70

    playerHealth = 100
    animationStep = 0
    #x = pygame.display.set_mode((40,40))

    playerSpriteFragment = pygame.Surface((103,66))
    playerSpriteFragment.set_colorkey((0,0,0)) #remove background

    def __init__(self,):
        pygame.init()
        pygame.mixer.init()
        self.playerImage = pygame.image.load(os.path.join('img','helix.png'))
        self.playerImage =  pygame.transform.scale(self.playerImage,(309,66))

        self.playerRect = pygame.Rect(100, 300, 103, 66)
        self.last_update = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()

        #BULLETS
        self.lastShoot= pygame.time.get_ticks()
        self.currentShoot = pygame.time.get_ticks()

        self.lastSoundPlay = pygame.time.get_ticks()
        self.currentSoundPlay = pygame.time.get_ticks()
        self.bulletSound = pygame.mixer.Sound(os.path.join('sounds', 'playerMachineGun.ogg'))
        self.bulletList = []
        
        self.empty = pygame.Color(0,0,0,0)

        self.playerHp = 100

    #last_update = pygame.time.get_ticks()
    #current_time = pygame.time.get_ticks()
    
    def animePlayer(self):
        #print("anim step: ", self.animationStep)
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_update >= 90: #cooldown
            self.animationStep += 1
            self.last_update = self.current_time
            self.playerSpriteFragment.fill(self.empty)
            self.playerSpriteFragment.blit(self.playerImage,(0,0), ((103*self.animationStep) ,0,103,66))
                                                                        #((308*self.animationStep) ,0,308,198))
        #self.playerSpriteFragment.fill(self.empty)             
        #self.playerSpriteFragment.blit(self.playerImage,(0,0), ((308*self.animationStep) ,0,308,198))
        #gameWindow.blit(self.playerSpriteFragment,(self.playerRect.x, self.playerRect.y))
        
        if self.animationStep >= 2:
            self.animationStep = -1
        else:
            pass
            #self.animationStep += 1
        return self.playerSpriteFragment

    def playerMovement(self,keys_pressed):
        WINDOW_WIDTH = 1280 
        WINDOW_HEIGHT = 720
        SHIP_SPEED=10
        if keys_pressed[pygame.K_a]:  # left
            if self.playerRect.x >0:
                self.playerRect.x -= SHIP_SPEED
        if keys_pressed[pygame.K_d]:  # right
            if self.playerRect.x < (WINDOW_WIDTH-103):
                self.playerRect.x += SHIP_SPEED
        if keys_pressed[pygame.K_w]:  # top
            if self.playerRect.y >0:
                self.playerRect.y -= SHIP_SPEED
        if keys_pressed[pygame.K_s]:  # down
            if self.playerRect.y < (WINDOW_HEIGHT-66):
                self.playerRect.y += SHIP_SPEED
        if keys_pressed[pygame.K_SPACE]:
            pass
            #Shooting  return (pozycja recta i event np strzal)
        #return()
    
    def playerShoot(self,keysPressed):
        self.currentShoot= pygame.time.get_ticks()
        if keysPressed[pygame.K_SPACE]:
            if len(self.bulletList) <= 10:
                if(self.currentShoot- self.lastShoot) >=170:
                    playerBullet = pygame.Rect(self.playerRect.x+103,self.playerRect.y+40,10,5)
                    self.bulletList.append(playerBullet)
                    self.lastShoot = self.currentShoot
                    self.bulletSound.play()
                    #self.playerBulletSound()
                    

    def playerBulletSound(self,):
        self.currentSoundPlay = pygame.time.get_ticks()
        if self.currentSoundPlay - self.lastSoundPlay  >= 150: #cooldown
            self.bulletSound.play()
            self.lastSoundPlay = self.currentSoundPlay

    def bulletMove(self,):
        
     for i in self.bulletList:
         i.x +=10
         if i.x > 1230:
             self.bulletList.remove(i)
        # elif i.colliderect(Level.enemyList[j])
           # pygame.event.post(pygame.event.Event(RED_HIT))
        
    def displayBullets(self,):
        self.bulletMove()
        return self.bulletList