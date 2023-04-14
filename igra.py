import pygame
import sys

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Экран
screen_width = 800
screen_hight = 600
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Моя программа")

# Игрок
player_width = 20
player_high = 100
player_x = 50
player_y = screen_hight // 2 - player_high // 2
player = pygame.Rect((player_x, player_y, player_width, player_high)) # x, y, ширина, высота


# Игрок 2
player_2_width = 20
player_2_high = 100
player_2_x = screen_width - player_2_width - 50
player_2_y = screen_hight // 2 - player_2_high // 2
player_2 = pygame.Rect((player_2_x, player_2_y, player_2_width, player_2_high))

# Мяч

ball_width = 10
ball_high = 10
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_hight // 2 - ball_high // 2
ball = pygame.Rect(ball_x, ball_y, ball_width, ball_high)


while True:  # главный цикл

    # События
    for event in pygame.event.get():  # опрос событий
        if event.type == pygame.QUIT:  # обработка события
            pygame.quit()  # выгрузили модули pygame из компа
            sys.exit()
        if event.type == pygame.KEYDOWN: # Выходим с помощью клавиши esc
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= 1
        if player.y < 0:
            player.y = 0
    if keys[pygame.K_s]:
        player.y += 1
        if player.y > screen_hight - player_high:
            player.y = screen_hight - player_high

    if keys[pygame.K_UP]:
        player_2.y -= 1
        if player_2.y < 0:
            player_2.y = 0
    if keys[pygame.K_DOWN]:
        player_2.y += 1
        if player_2.y > screen_hight - player_2_high:
            player_2.y = screen_hight - player_2_high

     
                    



    # отрисовка
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, player) # рисуем игрока
    pygame.draw.rect(screen, WHITE, player_2)
    pygame.draw.rect(screen, WHITE, ball)
    pygame.display.flip() # обновляем экран
