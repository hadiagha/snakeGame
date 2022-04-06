
import pygame
import time

black = (0,0,0)
white = (255,255,255)
surfaceWidth = 800
surfaceHeight = 500

pygame.init()
surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Helicopter')
clock = pygame.time.Clock()

img = pygame.image.load('Helicopter.png')
x = 150
y = 200

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf',20)
    largeText = pygame.font.Font('freesansbold.ttf',150)

    titleTextSurf, titleTextRect = makeTextObjs(text,largeText)
    titleTextRect.center = surfaceWidth / 2 , surfaceHeight / 2
    surface.blit(titleTextSurf,titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue!', smallText)
    typTextRect.center = surfaceWidth / 2 , ((surfaceHeight / 2)+100)
    surface.blit(typTextSurf, typTextRect)
    pygame.display.update()
    time.sleep(1)

def gameOver():
    msgSurface('Kaboom!')

def helicopter(x,y,image):
    surface.blit(image,(x,y))

# sourcery skip: merge-nested-ifs, merge-repeated-ifs, swap-nested-ifs
y_move = 0

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_move = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_move = 5

    y += y_move

    surface.fill(black)
    helicopter(x,y,img)

    if y > (surfaceHeight - 40) or y <0:
        gameOver()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
