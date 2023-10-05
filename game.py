import random
import pygame

from game_platform import Platform
from player import Player

CLR_BACKGROUND = (176, 134, 200)
CLR_WHITE = (250, 250, 250)
WIDTH, HEIGHT = 450, 700
CAMERA_THRESHOLD = int(HEIGHT / 3) * 2
POS_INIT_PLATFORM = (WIDTH - Platform.width,
                     HEIGHT - Platform.height)
POS_INIT_PLAYER = (WIDTH - 100,
                   HEIGHT - Platform.height
                   - Player.height)
DIST_BETWEEN_PLATFORMS = 60
TXT_WINDOW = "Doodle Jump Corgi Edition"
FPS = 30

pygame.init()

FONT = pygame.font.SysFont('Futura PT', 36, True)
IMG_DEAD = pygame.image.load('static/dead.png')

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TXT_WINDOW)
CLOCK = pygame.time.Clock()


def new_game():
    global player
    global platforms
    global camera_top
    global score
    player = Player(*POS_INIT_PLAYER)
    platforms = [Platform(*POS_INIT_PLATFORM)]
    camera_top = 0
    score = 0


def generate_platforms():
    current_hgt = platforms[-1].y

    while abs(current_hgt - camera_top) > DIST_BETWEEN_PLATFORMS:
        platforms.append(Platform(random.randint(0, WIDTH - Platform.width),
                                  current_hgt - DIST_BETWEEN_PLATFORMS))
        current_hgt -= DIST_BETWEEN_PLATFORMS

    while platforms[0].y > HEIGHT + camera_top:
        platforms.pop(0)


def draw_platforms():
    for platform in platforms:
        if camera_top <= platform.y <= HEIGHT:
            WINDOW.blit(Platform.IMG, (platform.x, platform.y - camera_top))


def detect_collisions():
    for platform in platforms:
        if platform.get_rect().colliderect(player.get_rect()) \
                and not player.jump_cap \
                and player.y + player.height < platform.y + platform.height:
            return True
    return False


def draw_score():
    text_render = FONT.render("Score: %d" % int(score / 10), 1, CLR_WHITE)
    text_pos = text_render.get_rect()
    text_pos.x, text_pos.y = 10, 10
    WINDOW.blit(text_render, text_pos)


def draw_final_score():
    text_render = FONT.render("Final Score: %d" % int(score / 10), 1,
                              CLR_WHITE)
    text_pos = text_render.get_rect()
    text_pos.centerx = int(WIDTH / 2)
    text_pos.y = 100
    WINDOW.blit(text_render, text_pos)


run = True
dead = False
new_game()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_SPACE:
                if dead:
                    new_game()
                    dead = False
    if not dead:
        p_keys = pygame.key.get_pressed()

        if p_keys[
            pygame.K_RIGHT] and player.x < WIDTH - Player.width:
            player.move('R')
        elif p_keys[pygame.K_LEFT] and player.x > 0:
            player.move('L')

        WINDOW.fill(CLR_BACKGROUND)

        if player.y - camera_top < 400:
            camera_top -= 5

        generate_platforms()
        draw_platforms()
        WINDOW.blit(player.image(), [player.x, player.y - camera_top])

        player.update()

        if detect_collisions():
            player.bounce()

        if player.y > HEIGHT + camera_top:
            dead = True

        if HEIGHT - player.y > score:
            score = HEIGHT - player.y

        draw_score()

    else:
        WINDOW.blit(IMG_DEAD, (0, 0))
        draw_final_score()

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()

if __name__ == '__main__':
    pass