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
screen_info = pygame.display.Info()
screen_width = screen_info.current_w  # Ширина экрана
screen_hight = screen_info.current_h # Высота экрана
screen = pygame.display.set_mode((screen_width, screen_hight), pygame.FULLSCREEN) # Создание дисплея
screen_rect = screen.get_rect()
pygame.display.set_caption("Моя программа")  # Название программы


def players_to_center():
    player.x = screen_width * 0.10
    player.y = screen_hight // 2 - player_high // 2
    player_2.x = screen_width * 0.9 - player_2_width
    player_2.y = screen_hight // 2 - player_2_high // 2


# Игрок 1
player_width = 20  # Ширина игрока
player_high = 105  # Высота игрока
player_score = 0
player_speed = 10
player = pygame.Rect((0, 0, player_width, player_high))  # x, y, ширина, высота
player1_y_prew = player.y


# Игрок 2
player_2_width = 20  # Ширина игрока
player_2_high = 105  # Высота игрока
player_2_score = 0
player2_speed = 10
player_2 = pygame.Rect((0, 0, player_2_width, player_2_high))  # х, у, ширина, высота
player2_y_prew = player_2.y

players_to_center()


# Сбрасывание мяча
def ball_to_center():
    ball.x = screen_width // 2 - ball_width // 2
    ball.y = screen_hight // 2 - ball_high // 2
    

def rotate_ball():
    """
    Поворачивает мяч
    возвращает кортеж(tuple)
    """
    if random.randint(0, 1) == 0:
        direction = random.randint(225, 315)
    else:
        direction = random.randint(90, 135) 
    velocity = degrees_to_velocity(direction, 10)
    return (velocity[0], velocity[1], direction)


# Мяч
ball_width = 15  # Ширина мяча
ball_high = 15  # Высота мяча
ball = pygame.Rect(
    0, 0, ball_width, ball_high
)  # х, у, ширина, высота
ball_to_center()
velocity = rotate_ball()
ball_speed_x = velocity[0]
ball_speed_y = velocity[1]
ball_direction = velocity[2]



# Табло
score_left = pygame.font.Font(None, 60)
score_right = pygame.font.Font(None, 60)   


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
    """
    if keys[pygame.K_UP]:  # ход вверх player2
        player_2.y -= player2_speed
        if player_2.y < 0:
            player_2.y = 0
    if keys[pygame.K_DOWN]:  # ход вниз player2
        player_2.y += player2_speed
        if player_2.y > screen_hight - player_2_high:
            player_2.y = screen_hight - player_2_high
    """        

    # логика
    ball.x += ball_speed_x  # мяч всегда движется со своей скоростью по x
    ball.y += ball_speed_y  # мяч всегда движется со своей скоростью по y
    if ball.x < 0:  # гол, TODO: засчитывать голы
        player_2_score += 1  
        ball_to_center()
        velocity = rotate_ball()
        ball_speed_x = velocity[0]
        ball_speed_y = velocity[1]
        players_to_center()        
    if ball.x > screen_width - ball_width:  # гол, TODO: засчитывать голы
        player_score += 1  
        ball_to_center()
        velocity = rotate_ball()
        ball_speed_x = velocity[0]
        ball_speed_y = velocity[1]
        players_to_center()
    if ball.y < 0:  # Мяч вылетел вверх
        ball_speed_y *= -1
    if ball.y > screen_hight - ball_high:  # Мяч вылетел вниз
        ball_speed_y *= -1 
    if ball.colliderect(player) or ball.colliderect(player_2):
        ball_speed_x *= -1

    
    if ball.centery < player_2.centery:
        player_2.y -= player2_speed
    if ball.centery > player_2.centery:
        player_2.y += player2_speed

    # Печатаем движения левого игрока
    if player.y > player1_y_prew:
        print("Еду вниз")
    elif player.y < player1_y_prew:
        print("Еду вверх")
    player1_y_prew = player.y

    # ограничения компа
    if player_2.top < 0:
        player_2.top = 0
    if player_2.bottom > screen_rect.bottom:
        player_2.bottom = screen_rect.bottom


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
    screen.blit(score_left_img, (screen_width * 0.25, 10))
    screen.blit(score_right_img, (screen_width * 0.75, 10))
    pygame.display.flip()  # обновляем экран

    clock.tick(FPS)  # количество кадров в секунду
