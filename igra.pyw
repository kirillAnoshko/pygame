import pygame
import sys
from degrees_to_velocity import degrees_to_velocity
import random

pygame.init()  # Инициализация методов

clock = pygame.time.Clock()  # часы для контроля FPS


WHITE = (255, 255, 255)  # Цвет белый
BLACK = (0, 0, 0)  # Цвет чёрный
FPS = 60

# Экран
screen_width = 800  # Ширина экрана
screen_hight = 600  # Высота экрана
screen = pygame.display.set_mode((screen_width, screen_hight)) # Создание дисплея
pygame.display.set_caption("Моя программа")  # Название программы

# Игрок 1
player_width = 20  # Ширина игрока
player_high = 105  # Высота игрока
player_score = 0
player_speed = 10
player_x = 50  # положение х
player_y = screen_hight // 2 - player_high // 2  # положение у
player = pygame.Rect((player_x, player_y, player_width, player_high))  # x, y, ширина, высота


# Игрок 2
player_2_width = 20  # Ширина игрока
player_2_high = 105  # Высота игрока
player_2_score = 0
player2_speed = 10
player_2_x = screen_width - player_2_width - 50  # положение х
player_2_y = screen_hight // 2 - player_2_high // 2  # положение у
player_2 = pygame.Rect((player_2_x, player_2_y, player_2_width, player_2_high))  # х, у, ширина, высота


# Мяч
ball_width = 15  # Ширина мяча
ball_high = 15  # Высота мяча
ball_x = screen_width // 2 - ball_width // 2  # положение х
ball_y = screen_hight // 2 - ball_high // 2  # положение у
velocity = degrees_to_velocity(50, 7)
ball_speed_x = velocity[0]  # Скорость мяча x
ball_speed_y = velocity[1]  # Скорость мяча у
ball = pygame.Rect(
    ball_x, ball_y, ball_width, ball_high
)  # х, у, ширина, высота


# Табло
score_left = pygame.font.Font(None, 60)
score_right = pygame.font.Font(None, 60)


# Сбрасывание мяча
def ball_to_center():
    ball.x = ball_x
    ball.y = ball_y



while True:  # Главный цикл
    """
    Главный цикл игры
    Ловит события
    Отрисовывает экран
    """

    # События
    for event in pygame.event.get():  # опрос событий
        if event.type == pygame.QUIT:  # обработка события
            pygame.quit()  # выгрузили модули pygame из компа
            sys.exit()  # Вышли из игры
        if event.type == pygame.KEYDOWN:  # Выходим с помощью клавиши esc
            if event.key == pygame.K_ESCAPE:
                pygame.quit() 
                sys.exit()
                        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # ход вверх player1
        player.y -= player_speed
        if player.y < 0:
            player.y = 0
    if keys[pygame.K_s]:  # ход вниз player1
        player.y += player_speed
        if player.y > screen_hight - player_high:
            player.y = screen_hight - player_high

    if keys[pygame.K_UP]:  # ход вверх player2
        player_2.y -= player2_speed
        if player_2.y < 0:
            player_2.y = 0
    if keys[pygame.K_DOWN]:  # ход вниз player2
        player_2.y += player2_speed
        if player_2.y > screen_hight - player_2_high:
            player_2.y = screen_hight - player_2_high

    # логика
    ball.x += ball_speed_x  # мяч всегда движется со своей скоростью по x
    ball.y += ball_speed_y  # мяч всегда движется со своей скоростью по y
    if ball.x < 0:  # гол, TODO: засчитывать голы
        player_2_score += 1  
        ball_to_center()
    if ball.x > screen_width - ball_width:  # гол, TODO: засчитывать голы
        player_score += 1  
        ball_to_center()
    if ball.y < 0:  # Мяч вылетел вверх
        ball_speed_y *= -1
    if ball.y > screen_hight - ball_high:  # Мяч вылетел вниз
        ball_speed_y *= -1 
    if ball.colliderect(player) or ball.colliderect(player_2):
        ball_speed_x *= -1              


    # отрисовка
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, player)  # рисуем игрока
    pygame.draw.rect(screen, WHITE, player_2)  # рисуем игрока 2
    pygame.draw.rect(screen, WHITE, ball)  # рисуем мяч
    line = pygame.draw.line( 
        screen,
        WHITE,
        [screen_width // 2, 0],
        [screen_width // 2, screen_hight],
        2                    
    )
    score_left_img = score_left.render(str(player_score), True, WHITE)
    score_right_img = score_right.render(str(player_2_score), True, WHITE)
    screen.blit(score_left_img, (screen_width * 0.23, 10))
    screen.blit(score_right_img, (screen_width * 0.75, 10))
    pygame.display.flip()  # обновляем экран

    clock.tick(FPS)  # количество кадров в секунду
