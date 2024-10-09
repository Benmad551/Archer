import pygame
from pygame import *
import random

def move(key, player):
    if key[pygame.K_a] == True and key[pygame.K_LSHIFT] == True:
        player.move_ip(-2, 0)
    elif key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    if key[pygame.K_d] == True and key[pygame.K_LSHIFT] == True:
        player.move_ip(2, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    if key[pygame.K_w] == True and key[pygame.K_LSHIFT] == True:
        player.move_ip(0, -2)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    if key[pygame.K_s] == True and key[pygame.K_LSHIFT]:
        player.move_ip(0, 2)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)




    pygame.init()

    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 700

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    player = pygame.Rect((300,250, 50,50))
    Enemy = pygame.Rect((300, 250, 50, 50))



    Bg = (0,0,0)
    Green = (0,255, 0)
    Blue = (0, 0, 255)
    Red = (255, 0 ,0)
    run = True
    while run:
        #Updates the Background
        screen.fill(Bg)
        #checks for collision
        col = Blue


        #Draws all rectangles
        pygame.draw.rect(screen, col, player)
        pygame.draw.rect(screen, Red, Enemy)


    #Key inputs for moving around the screen
        key = pygame.key.get_pressed()
        #movement around screen
        move()




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()