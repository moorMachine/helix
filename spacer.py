import pygame
import os
from player import Player
from level import Level
from enemy import Enemy
from rocket import Rocket

pygame.init()
pygame.mixer.init()




def damageCheck(player,enemyList,enemyBulletList):
    remove= None
    
    for i in player.bulletList:
        
        for j in enemyList:

            if i.colliderect(j.enemyRect):
                player.bulletList.remove(i)
                j.enemyHp -= 10
                pygame.event.post(pygame.event.Event(ENEMY_HIT))
                del j ######

    for i in enemyBulletList:

        if( isinstance(i,Rocket)):
            if i.rocketRect.colliderect(player.playerRect):
                i.rocketExplosion()
                #remove = i
                #enemyBulletList.remove(i)
                del i
        else:

            if i.clliderect(player.playerRect):
            
        
                enemyBulletList.remove(i)

                pygame.event.post(pygame.event.Event(PLAYER_HIT_HARD))


#py.font.init()
#py.mixer.init()

ENEMY_HIT = pygame.USEREVENT + 1
PLAYER_HIT_WEAK = pygame.USEREVENT + 2
PLAYER_HIT_HARD = pygame.USEREVENT + 2

WINDOW_WIDTH = 1280 
WINDOW_HEIGHT = 720
WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

#COLORS
WHITE = (255,255,255)
GRAY = (123,123,123)
PURPLE = (54,12,128)
RED = (255,0,0)
YELLOW = (245,190,30)
ORANGE = (235,97,35)

FPS = 60
clock = pygame.time.Clock()


#BACKGROUND

background = pygame.image.load(os.path.join('img','test.png'))
background = pygame.transform.scale(background,(1280,720))
level1 = Level(background)






player = Player()

rocket1 = Rocket((800,600))
rocket1.rocketTarget = player.playerRect


klatka=1

enemyScudFrame = None

bullets = None

enemyScud1 = Enemy()

enemyList = []
enemyBulletList = []

enemyList.append(enemyScud1)
enemyBulletList.append(rocket1)

game_loop = True
while game_loop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        if(event.type == ENEMY_HIT):
            print("HIT HIT HIT !")
    damageCheck(player,enemyList, enemyBulletList)

    key_pressed = pygame.key.get_pressed()

    player.playerMovement(key_pressed)
    WINDOW.fill(PURPLE)

    level = level1.moveBackground()
    WINDOW.blit(level[0],(level[2],0))
    WINDOW.blit(level[1],(1280+level[2],0))

    

    #WINDOW.blit(playerFrame,(yellow.x,yellow.y))


    klatka = player.animePlayer()
    #player.say()
    WINDOW.blit(klatka,player.playerRect)
    rocket1.rocketFly()

    WINDOW.blit(rocket1.test(),(0,0))

    #print(rocket1.rocketFly())
    klatka = rocket1.rocketAnime()
    WINDOW.blit(klatka,rocket1.rocketRect)

    # TEST
    #WINDOW.blit(SCUD,(200,200))
    enemyScud1.moveEnemy()
    enemyScudFrame = enemyScud1.animEnemy()
    WINDOW.blit(enemyScudFrame,(enemyScud1.enemyRect))

    player.playerShoot(key_pressed)
    #player.bulletMove()
    #bullets = player.displayBullets()

    for i in player.displayBullets():           # Yellow color
        pygame.draw.rect(WINDOW,(255,255,0),i)

    pygame.draw.rect(WINDOW,(255,0,0),pygame.Rect(0,0,64,64))
    pygame.display.update()
    #pygame.display.flip()

    clock.tick(FPS)

pygame.quit()


print("bye bye")