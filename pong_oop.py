import pygame as pg
import sys
from random import randint
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Game:
    def __init__(self):
        pg.init()
        screen_info = pg.display.Info()
        
        
        self.screen = pg.display.set_mode(
            (screen_info.current_w, screen_info.current_h),
            pg.FULLSCREEN
        )
        self.rect = self.screen.get_rect()
        player1 = Paddle(
           screen_info.current_w * 0.1,
           self.rect.centery,
           self.rect.width * 0.02,
           self.rect.height * 0.1,
           WHITE,
           pg.K_UP,
           pg.K_DOWN 
        )
        player2 = Paddle(
            screen_info.current_w * 0.9,
            self.rect.centery,
            self.rect.width * 0.02,
            self.rect.height * 0.1,
            WHITE,
            pg.K_w,
            pg.K_s

        )

        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(player1)

    def main_loop(self):
        game = True
        while game:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game = False
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
            
            self.screen.fill(BLACK)
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            pg.display.flip()


class Paddle(pg.sprite.Sprite):
    def __init__(self, center_x, center_y, width, height, color, key_up, key_down):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = center_x
        self.rect.centery = center_y
        self.key_up = key_up
        self.key_down = key_down

    def update(self):
        keys = pg.key.get_pressed()
        if keys[self.key_up]:
            self.rect.y -= 5
        elif keys[self.key_down]:
            self.rect.y += 5        


game = Game()
game.main_loop()
pg.quit()
sys.exit()        
                        
                    