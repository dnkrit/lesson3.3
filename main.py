import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_WEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WEIGHT))

pygame.display.set_caption('Игра Тип')
icon = pygame.image.load('img/Group 236150.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 50
target_weight = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_WEIGHT - target_weight)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


running = True
while running:
    pass

 pygame.quit()

