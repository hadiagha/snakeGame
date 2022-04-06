
import pygame

black = (0,0,0)
white = (255,255,255)
max_x = 800
max_y = 400

pygame.init()
surface = pygame.display.set_mode((max_x,max_y))
pygame.display.set_caption('Helicopter')
clock = pygame.time.Clock()

img = pygame.image.load('Helicopter.png')
x = 150
y = 200

def gameOver():
    pygame.quit()
    quit()

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

    if y > (max_y - 40) or y <0:
        gameOver()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
