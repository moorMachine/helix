import pygame


class Level:


    def __init__(self,backGroundIMG):
        pygame.init()

        self.backgroundImage1 = backGroundIMG
        self.backgroundImage2 = backGroundIMG
        self.move = 0



    def moveBackground(self,):
        if self.move == -1280:
            self.move = 0
            print('jump')

        self.move -=1
        return (self.backgroundImage1,self.backgroundImage2 ,self.move)
