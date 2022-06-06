import pygame, random, math

class Ball():
    def __init__(self):
        self.surfaceBall = pygame.image.load('resources/ball.png').convert()
        sizeScreen =  pygame.display.get_surface().get_size()
        self.rect = self.surfaceBall.get_rect()
        self.position =  self.rect.move(sizeScreen[0]/2,sizeScreen[1]/2)
        self.speed = 3
        angle = 360 * random.uniform(0.1, 0.9)
        self.xSpeed = int(self.speed * math.sin(angle))
        if self.xSpeed == 0:
            self.xSpeed = 1
        self.ySpeed = int(self.speed * math.cos(angle))
    
    
    def draw(self, screen):
        screen.blit(self.surfaceBall, self.position)


    def doMove(self, rackets):
        self.position.x += self.xSpeed
        self.position.y += self.ySpeed
        if not self.checkCollision(rackets):
            return False, self.checkBounce()
        return True, False


    def checkBounce(self):
        sizeScreen =  pygame.display.get_surface().get_size()
        if self.position.x >= sizeScreen[0] or self.position.x <= 0:
            return True
        if self.position.y >= sizeScreen[1] or self.position.y <= 0:
            self.ySpeed *= -1
        return False


    def checkCollision(self, rackets):
        for racket in rackets:
            if self.position.colliderect(racket.position):
                self.xSpeed *= -1
                return True
        return False