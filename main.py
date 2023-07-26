import sys
import pygame
from player import Player
from objects import Tree, Coin
from background import show_sky, show_ground
    
def show_score(init_score, playing):
    if playing:
        cur_time = pygame.time.get_ticks() - start_time
        score = cur_time // 500
        score += bonus
    else: 
        score = init_score
    score_text = font.render(f"Best: {best_score}  Score: {score}", False, "Black")
    score_text_rect = score_text.get_rect(topright=(770, 30))
    screen.blit(score_text, score_text_rect)
    return score

pygame.init() # initialize pygame
screen = pygame.display.set_mode((800, 400)) # display surface (the window to draw on)
pygame.display.set_caption("Dino Parkour")
clock = pygame.time.Clock() # create a clock object to track time

font = pygame.font.Font("./assets/font/Pixeltype.ttf", 40)
start_text = font.render("Press SPACE to start", False, "Black")
start_text_rect = start_text.get_rect(center=(400, 100))
sky = show_sky()
ground = show_ground()
dino = pygame.sprite.GroupSingle(Player())
tree_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

music = pygame.mixer.Sound("./assets/audio/background.wav")
music.set_volume(0.5)
music.play(loops=-1)

tree_time = 1600
coin_time = 4000
tree_timer = pygame.USEREVENT + 1
pygame.time.set_timer(tree_timer, tree_time)
coin_timer = pygame.USEREVENT + 2
pygame.time.set_timer(coin_timer, coin_time)

game_start = False
game_failed = False
start_time = 0
bonus = 0
best_score = 0
add_speed = 0
minus_time = 0
threshold = 50

while True: # to keep the game running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # exit pygame
            sys.exit() # exit the program

        if game_start == False or game_failed == True:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_start = True
                game_failed = False
                start_time = pygame.time.get_ticks()
                bonus = 0
                add_speed = 0
                minus_time = 0
                threshold = 50
                tree_group.empty()
                coin_group.empty()

        if game_start and not game_failed:
            if event.type == tree_timer:
                tree_group.add(Tree(add_speed))
            if event.type == coin_timer:
                coin_group.add(Coin(add_speed))

    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 300))
    dino.draw(screen)
    dino.update(game_start, game_failed)
    tree_group.draw(screen)
    tree_group.update(game_start, game_failed)
    coin_group.draw(screen)
    coin_group.update(game_start, game_failed)

    if game_start == True and game_failed == False:
        score = show_score(0, playing=True)
        if score > best_score:
            best_score = score
        if score >= threshold:
            add_speed = score // 100
            minus_time = score
            pygame.time.set_timer(tree_timer, tree_time - minus_time)
            pygame.time.set_timer(coin_timer, coin_time - minus_time)
            threshold += 50

        for obj in tree_group:
            if pygame.sprite.collide_circle(dino.sprite, obj):
                game_failed = True
                dino.sprite.die()

        for coin in coin_group:
            if pygame.sprite.collide_circle(dino.sprite, coin):
                coin.coin_sound.play()
                coin.kill()
                bonus += 10

    elif game_start == False: 
        screen.blit(start_text, start_text_rect)

    elif game_failed == True:
        score = show_score(score, playing=False)
        screen.blit(start_text, start_text_rect)
         
    pygame.display.update() # update the display
    clock.tick(60) # not run faster than 60 fps