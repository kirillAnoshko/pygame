import pygame
import sys

pygame.init()

# Экран
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Моя программа")

# Игрок
player_width = 50
player_high = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height // 2 - player_high // 2
player_color = (255, 0, 0) # RGB
player = pygame.Rect((player_x, player_y, player_width, player_high)) # x, y, ширина, высота

while True:  # главный цикл

    # События
    for event in pygame.event.get():  # опрос событий
        if event.type == pygame.QUIT:  # обработка события
            pygame.quit()  # выгрузили модули pygame из компа
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= 1
        player_color = (0, 255, 0)
    if keys[pygame.K_DOWN]:
        player.y += 1
        player_color = (255, 0, 0)
    if keys[pygame.K_LEFT]:
        player.x -= 1
        player_color = (0, 0, 255)
    if keys[pygame.K_RIGHT]:
        player.x += 1
        player_color = (255, 255, 0)            

    # отрисовка
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, player_color, player) # рисуем игрока
    pygame.display.flip() # обновляем экран
