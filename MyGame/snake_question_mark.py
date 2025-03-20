import pygame
import random
from pygame.constants import QUIT, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

FONT = pygame.font.SysFont('Verdana', 50)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 95)

player_size = (20, 20)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Surface((player_size))
player.fill((COLOR_WHITE))
player_rect = player.get_rect()
player_speed = [1, 1]

platform_size = (300, 20)
platform = pygame.Surface((platform_size))
platform.fill(COLOR_WHITE)
# platform_rect = platform.get_rect()
platform_rect = pygame.Rect(WIDTH - 300, HEIGHT - 20, *platform_size)
platform_move_right = [1, 0]
platform_move_left = [-1, 0]

CREATE_BONUS = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_BONUS, 600)

bonuses = []

score = 0

playing = True
while playing:

    FPS.tick(900)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
    main_display.fill(COLOR_BLACK)

    keys = pygame.key.get_pressed()

    # if platform_rect.colliderect(player[1]):
    # idk how to implement plat vs payer collide to keep game go on, otherwise playing=False

    if player_rect.bottom >= HEIGHT:
        player_speed[1] = -player_speed[1]

    if player_rect.right >= WIDTH:
        player_speed[0] = - player_speed[0]

    if player_rect.top < 0:
        player_speed[1] = -player_speed[1]

    if player_rect.left < 0:
        player_speed[0] = -player_speed[0]

    if keys[K_RIGHT] and platform_rect.right > 0 and platform_rect.right < WIDTH:
        platform_rect = platform_rect.move(platform_move_right)

    if keys[K_LEFT] and platform_rect.left < WIDTH and platform_rect.left > 0:
        platform_rect = platform_rect.move(platform_move_left)

    main_display.blit(player, player_rect)

    player_rect = player_rect.move(player_speed)

    main_display.blit(platform, platform_rect)

    pygame.display.flip()

    for bonus in bonuses:
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))
