import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, dino_idx):
        super().__init__()
        dino_y = pygame.image.load("./assets/graphics/dinos/DinoSprites - tard.png").convert_alpha()
        dino_b = pygame.image.load("./assets/graphics/dinos/DinoSprites - doux.png").convert_alpha()
        dino_g = pygame.image.load("./assets/graphics/dinos/DinoSprites - vita.png").convert_alpha()
        dino_r = pygame.image.load("./assets/graphics/dinos/DinoSprites - mort.png").convert_alpha()
        self.dino_imgs = [dino_y, dino_b, dino_g, dino_r]
        self.dino_idx = dino_idx
        self.dino = self.dino_imgs[self.dino_idx]

        m = 3
        res = (72, 72)
        idle_1 = pygame.transform.scale(self.dino.subsurface((m, m, 24-2*m, 24-2*m)), res) # new resolution
        idle_2 = pygame.transform.scale(self.dino.subsurface((24+m, m, 24-2*m, 24-2*m)), res)
        idle_3 = pygame.transform.scale(self.dino.subsurface((48+m, m, 24-2*m, 24-2*m)), res) 
        
        run_1 = pygame.transform.scale(self.dino.subsurface((96+m, m, 24-2*m, 24-2*m)), res)
        run_2 = pygame.transform.scale(self.dino.subsurface((120+m, m, 24-2*m, 24-2*m)), res)
        run_3 = pygame.transform.scale(self.dino.subsurface((144+m, m, 24-2*m, 24-2*m)), res) 
        run_4 = pygame.transform.scale(self.dino.subsurface((168+m, m, 24-2*m, 24-2*m)), res)
        run_5 = pygame.transform.scale(self.dino.subsurface((192+m, m, 24-2*m, 24-2*m)), res)
        run_6 = pygame.transform.scale(self.dino.subsurface((216+m, m, 24-2*m, 24-2*m)), res)

        self.died_img = pygame.transform.scale(self.dino.subsurface((336+m, m, 24-2*m, 24-2*m)), res)

        self.jump_img = pygame.transform.scale(self.dino.subsurface((168+m, m, 24-2*m, 24-2*m)), res)

        self.image = idle_1
        self.rect = self.image.get_rect(midbottom=(150, 300))
        self.radius = (res[0]-2) // 2

        self.idle_frames = [idle_1, idle_2, idle_3]
        self.idle_idx = 0
        self.run_frames = [run_1, run_2, run_3, run_4, run_5, run_6]
        self.run_idx = 0
        self.gravity = 0
        self.game_start = False
        self.game_failed = False
        self.jump_sound = pygame.mixer.Sound("./assets/audio/jump.wav")
        self.jump_sound.set_volume(0.5)

    def input(self):
        keys = pygame.key.get_pressed()
        if self.game_start and keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -16
            self.jump_sound.play()
                
    def idle(self):
        self.idle_idx += 0.1
        if self.idle_idx >= len(self.idle_frames): self.idle_idx = 0
        self.image = self.idle_frames[int(self.idle_idx)]
    
    def run(self):
        self.run_idx += 0.1
        if self.run_idx >= len(self.run_frames): self.run_idx = 0
        self.image = self.run_frames[int(self.run_idx)]
    
    def die(self):
        self.image = self.died_img

    def drop(self):
        self.gravity += 0.8
        self.rect.bottom += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def update(self, game_start, game_failed):
        self.game_start = game_start
        self.game_failed = game_failed
        if not self.game_start: self.idle()
        elif self.game_start and not self.game_failed: self.run()
        elif self.game_failed: self.die()

        if self.rect.bottom < 300:
            self.image = self.jump_img
        self.input()
        self.drop()