from typing import Any
import pygame
from random import randint

init_speed = 4.3

class Tree(pygame.sprite.Sprite):
    def __init__(self, add_speed):
        super().__init__()
        tree_g = pygame.image.load("./assets/graphics/dotown/small_g.png").convert_alpha()
        tree_y = pygame.image.load("./assets/graphics/dotown/small_y.png").convert_alpha()
        tree_yg = pygame.image.load("./assets/graphics/dotown/small_yg.png").convert_alpha()
        size = tree_g.get_size()
        m = 65
        tree_g = pygame.transform.scale(tree_g.subsurface(m, m, size[0]-2*m, size[1]-2*m), (40, 50))
        tree_y = pygame.transform.scale(tree_y.subsurface(m, m, size[0]-2*m, size[1]-2*m), (40, 50))
        tree_yg = pygame.transform.scale(tree_yg.subsurface(m, m, size[0]-2*m, size[1]-2*m), (40, 50))
        self.tree_frames = [tree_g, tree_y, tree_yg]

        self.tree_idx = randint(0, 2)
        self.image = self.tree_frames[self.tree_idx]
        self.rect = self.image.get_rect(midbottom=(randint(800, 1000), 300))
        self.radius = 40 // 2
        self.game_start = False
        self.game_failed = False
        self.speed = init_speed + add_speed

    def move(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.kill()
    
    def stop(self):
        self.rect.x = self.rect.x

    def update(self, game_start, game_failed):
        self.game_start = game_start
        self.game_failed = game_failed
        if self.game_start == True and self.game_failed == False:
            self.move()
        elif self.game_failed == True:
            self.stop()

class Coin(pygame.sprite.Sprite):
    def __init__(self, add_speed):
        super().__init__()

        coin_1 = pygame.image.load("./assets/graphics/pixel_platformer/Tiles/tile_0151.png").convert_alpha()
        coin_2 = pygame.image.load("./assets/graphics/pixel_platformer/Tiles/tile_0152.png").convert_alpha()
        coin_1 = pygame.transform.scale(coin_1, (45, 45))
        coin_2 = pygame.transform.scale(coin_2, (45, 45))
        self.image = coin_1
        self.rect = self.image.get_rect(midbottom=(randint(800, 1000), 120))
        self.radius = 45 / 2
        self.coin_frames = [coin_1, coin_2]
        self.coin_idx = 0
        self.game_start = False
        self.game_failed = False
        self.speed = init_speed + add_speed
        self.coin_sound = pygame.mixer.Sound("./assets/audio/coin.wav")
        self.coin_sound.set_volume(0.5)

    def move(self):
        self.coin_idx += 0.07
        if self.coin_idx >= len(self.coin_frames): self.coin_idx = 0
        self.image = self.coin_frames[int(self.coin_idx)]
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.kill()

    def stop(self):
        self.rect.x = self.rect.x

    def update(self, game_start, game_failed):
        self.game_start = game_start
        self.game_failed = game_failed
        if self.game_start == True and self.game_failed == False:
            self.move()
        elif self.game_failed == True:
            self.stop()
