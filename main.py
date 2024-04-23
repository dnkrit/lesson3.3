import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600  # Исправлено с SCREEN_WEIGHT на SCREEN_HEIGHT для консистентности
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра Тип')
icon = pygame.image.load('img/f_-WPCFdC0Y.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/Remove-bg.ai_1713911164456.png')
target_width = 50
target_height = 50

# Начальное расположение цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Таймер для контроля видимости цели
last_update_time = pygame.time.get_ticks()
display_time = 2000  # 2000 миллисекунд = 2 секунды
target_visible = True

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Цель сразу перемещается если на неё кликнули
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                last_update_time = pygame.time.get_ticks()  # Сброс таймера после клика

    current_time = pygame.time.get_ticks()
    if current_time - last_update_time > display_time:
        target_visible = not target_visible
        last_update_time = current_time
        if target_visible:
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    if target_visible:
        screen.blit(target_img, (target_x, target_y))

    pygame.display.update()

pygame.quit()