import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        dino_imgs = pygame.image.load("./assets/graphics/dinos/DinoSprites - tard.png").convert_alpha()
        m = 3
        res = (72, 72)
        idle_1 = pygame.transform.scale(dino_imgs.subsurface((m, m, 24-2*m, 24-2*m)), res) # new resolution
        idle_2 = pygame.transform.scale(dino_imgs.subsurface((24+m, m, 24-2*m, 24-2*m)), res)
        idle_3 = pygame.transform.scale(dino_imgs.subsurface((48+m, m, 24-2*m, 24-2*m)), res) 
        
        run_1 = pygame.transform.scale(dino_imgs.subsurface((96+m, m, 24-2*m, 24-2*m)), res)
        run_2 = pygame.transform.scale(dino_imgs.subsurface((120+m, m, 24-2*m, 24-2*m)), res)
        run_3 = pygame.transform.scale(dino_imgs.subsurface((144+m, m, 24-2*m, 24-2*m)), res) 
        run_4 = pygame.transform.scale(dino_imgs.subsurface((168+m, m, 24-2*m, 24-2*m)), res)
        run_5 = pygame.transform.scale(dino_imgs.subsurface((192+m, m, 24-2*m, 24-2*m)), res)
        run_6 = pygame.transform.scale(dino_imgs.subsurface((216+m, m, 24-2*m, 24-2*m)), res)

        self.died_img = pygame.transform.scale(dino_imgs.subsurface((336+m, m, 24-2*m, 24-2*m)), (72, 72))

        self.jump_img = pygame.transform.scale(dino_imgs.subsurface((168+m, m, 24-2*m, 24-2*m)), res)

        self.image = idle_1
        self.rect = self.image.get_rect(midbottom=(150, 300))
        self.radius = 72 // 2

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
        if self.game_start == True and keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -18
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
        if self.game_start == False: self.idle()
        elif self.game_start and self.game_failed == False: self.run()
        elif self.game_failed == True: self.die()

        if self.rect.bottom < 300:
            self.image = self.jump_img
        self.input()
        self.drop()
        pass