import pygame

def show_sky():
    sky = pygame.surface.Surface((800, 300)).convert()
    sky_1 = pygame.image.load("./assets/graphics/pixel_platformer/Background/background_0000.png").convert()
    sky_2 = pygame.image.load("./assets/graphics/pixel_platformer/Background/background_0001.png").convert()
    sky_3 = pygame.image.load("./assets/graphics/pixel_platformer/Background/background_0002.png").convert()

    for x in range(0, 800, 20):
        for y in range(0, 180, 20):
            sky.blit(sky_1, (x, y))
        sky.blit(sky_2, (x, 180))
        for y in range(200, 300, 20):
            sky.blit(sky_3, (x, y))
    return sky

def show_ground():
    ground = pygame.surface.Surface((800, 100)).convert()
    grond_1 = pygame.image.load("./assets/graphics/pixel_platformer/Tiles/tile_0022.png").convert()
    ground_2 = pygame.image.load("./assets/graphics/pixel_platformer/Tiles/tile_0122.png").convert()

    for x in range(0, 800, 18):
        ground.blit(grond_1, (x, 0))
        for y in range(18, 100, 18):
            ground.blit(ground_2, (x, y))
    return ground