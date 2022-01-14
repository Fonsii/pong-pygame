import pygame
from Racket import Racket
from Ball import Ball
from sys import exit

WIDTH, HEIGHT = 800, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
fontText = pygame.font.SysFont('lucidaconsole', 20)
fontScores = pygame.font.SysFont('lucidaconsole', 50)

def main():
    surface = pygame.Surface((WIDTH,HEIGHT))

    racketLeft = Racket(15,25)
    racketRight = Racket(785,158)
    ball = Ball()
  
    IDLE = True
    WINNING = False

    while True:
        surface.fill('Red')
        screen.blit(surface, (0,0))

        ball.draw(screen)
        racketRight.draw(screen)
        racketLeft.draw(screen)

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == 115: #S_KEY 
                    racketLeft.hold(0)
                elif event.key == 119: #W_KEY
                    racketLeft.hold(1)
                elif event.key == 1073741914: #DOWN_ARROW
                    racketRight.hold(0)
                elif event.key == 1073741917: #UP_ARROW
                    racketRight.hold(1)
                elif event.key == 27:
                    exit()
                pass
            if event.type == pygame.KEYUP:
                if event.key == 115:
                    racketLeft.release(0)
                elif event.key == 119:
                    racketLeft.release(1)
                elif event.key == 1073741914:
                    racketRight.release(0)
                elif event.key == 1073741917:
                    racketRight.release(1)
                elif event.key == 32 and not WINNING: #SPACE_KEY
                    IDLE = False
                elif event.key == 114 and WINNING: #Restart game R_KEY
                    racketLeft = Racket(15,25)
                    racketRight = Racket(785,158)
                    ball = Ball()

                    IDLE = True
                    WINNING = False
            drawRackets(screen, surface, racketLeft, racketRight)
        if not IDLE:
            screen.blit(surface, ball.position, ball.position)
            refreshRackets, score = ball.doMove([racketLeft, racketRight])
            if not score:
                ball.draw(screen)
                if refreshRackets:
                    drawRackets(screen, surface, racketLeft, racketRight)
            else:
                if ball.position.x < 15:
                    racketLeft.score += 1
                elif ball.position.x > 785:
                    racketRight.score += 1

                winning = checkScores(racketLeft, racketRight)
                if winning is not None:
                    WINNING = True
                else:
                    ball = Ball()
                    IDLE = True
        elif not WINNING:
            text = fontText.render('Press SPACE to start the game', False, "White")
            screen.blit(text, (229 , 215))

            scoreLeft = fontScores.render(str(racketLeft.score), False, "White")
            screen.blit(scoreLeft, (125, 100))

            scoreRight = fontScores.render(str(racketRight.score), False, "White")
            screen.blit(scoreRight, (675, 100))
        else:
            winningText = fontText.render(getWinningMessage(racketLeft), False, "White")
            screen.blit(winningText, (335 , 215))

            resetText = fontText.render('Press R to restart the game or ESC to close the game', False, "White")
            screen.blit(resetText, (85 , 255))
        pygame.display.flip()


def drawRackets(screen, surface, racketLeft, racketRight):
    screen.blit(surface, racketLeft.position, racketLeft.position)
    screen.blit(surface, racketRight.position, racketRight.position)

    racketLeft.doMove()
    racketRight.doMove()

    racketRight.draw(screen)
    racketLeft.draw(screen)
    

def checkScores(racketLeft, racketRight):
    if racketLeft.score == 7 or racketRight.score == 7:
        return True
    return None


def getWinningMessage(racketLeft):
    if racketLeft.score >= 7:
        return "Left wins!"
    else:
        return "Right wins!"


if __name__ == '__main__':
    main()