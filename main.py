import pygame
from monsters import *
from ship import *
from shot import *
from random import choice, randint


# Constants

BLACK = (0, 0, 0)

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800

FPS = 120

GAME_IS_ON = True

MONSTERS_SIZE = (50, 50)
SHIP_SIZE = (75, 75)

# Basics Settings

pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
win.fill(BLACK)

pygame.display.set_caption('Space Invaders')

clock = pygame.time.Clock()

time_delay = 2000  # 0.5 seconds
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, time_delay)

# Loads

ship_image = pygame.transform.scale(
    pygame.image.load('images/ship.jpeg').convert(), SHIP_SIZE)
ship = Ship(ship_image, win)

font_size = 36
font = pygame.font.SysFont(None, font_size)

score_text = f"Lifes: {ship.life}"
scoreboard_surface = font.render(score_text, True, (255, 255, 255))
scoreboard_rect = scoreboard_surface.get_rect()
scoreboard_rect.bottomleft = (25, 775)

monsters_images = [pygame.transform.scale(pygame.image.load(
    f'images/monster_{number}.tiff'), MONSTERS_SIZE) for number in range(1, 23)]


monsters = [Monsters(75 + 100 * num - 1100 * (num // 11), 25 +
                     75 * (num // 11), choice(monsters_images), win) for num in range(44)]

for monster in monsters:
    monster.draw()

all_shots = []
all_damages = []

ship.draw()

game_win = False

# Game

while GAME_IS_ON:
    win.fill(BLACK)

    win.blit(scoreboard_surface, scoreboard_rect)

    time_elapsed = pygame.time.get_ticks()

    ship.handle_keys()
    ship.draw()

    if len(all_shots) > 0:
        for shot in all_shots:
            shot.move_shot()
            shot.draw()
            if shot.y < 0:
                all_shots.remove(shot)

            for monster in monsters:
                if shot.rect.colliderect(monster.rect):
                    monsters.remove(monster)
                    all_shots.remove(shot)
                    if len(monsters) <= 0:
                        game_win = True
                        GAME_IS_ON = False

    for monster in monsters:
        if randint(1, 1000) == 5:
            damage = Damages(win, monster.x, monster.y)
            damage.draw()
            all_damages.append(damage)
        monster.auto_move()
        monster.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            GAME_IS_ON = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shot = Shots(win, ship.x, ship.y)
                shot.draw()
                all_shots.append(shot)

    if len(all_damages) > 0:
        for damage in all_damages:
            ship.my_rect()
            if damage.rect.colliderect(ship.rect):
                all_damages.remove(damage)
                ship.life -= 1
                scoreboard_surface = font.render(
                    f"Lifes: {ship.life}", True, (255, 255, 255))
                if ship.life <= 0:
                    GAME_IS_ON = False
            if damage.y > 800:
                all_damages.remove(damage)
            damage.move_damage()
            damage.draw()
    pygame.display.flip()
    clock.tick(FPS)

result = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Result")

font_size = 80
font = pygame.font.SysFont(None, font_size)
scoreboard_rect.center = (200, 240)


while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the game loop when the user closes the window
            pygame.quit()
            quit()

    if game_win:
        scoreboard_surface = font.render(
            f"YOU WIN!!", True, (255, 255, 255))
    else:
        scoreboard_surface = font.render(
            f"You lose...", True, (255, 255, 255))

    result.blit(scoreboard_surface, scoreboard_rect)
    pygame.display.update()
