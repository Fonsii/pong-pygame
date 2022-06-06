import pygame

class Racket():
    def __init__(self, postionXStarter:int, positionYStarter:int):
        self.surfaceRacket = pygame.image.load('resources/racket.png').convert()
        self.rect = self.surfaceRacket.get_rect()
        self.position =  self.rect.move(postionXStarter,positionYStarter)
        self.speed = 5
        self.flagsMove = [False, False]
        self.score = 0


    def draw(self, screen):
        screen.blit(self.surfaceRacket, self.position)


    def doMove(self):
        maxPosition =  pygame.display.get_surface().get_size()[1] - self.surfaceRacket.get_size()[1] - 2
        if self.flagsMove[0]:
            self.moveDown(maxPosition)
        if self.flagsMove[1]:
            self.moveUp(2)
            

    def moveDown(self, maxY):
        if self.position.y < maxY:
            self.position.y = self.position.y + self.speed

    
    def moveUp(self, minY):
        if self.position.y > minY:
            self.position.y = self.position.y - self.speed

    
    def hold(self, flag):
        self.flagsMove[flag] = True

    
    def release(self, flag):
        self.flagsMove[flag] = False