import pygame
from random import getrandbits


class Monsters:
    def __init__(self, x, y, image, win) -> None:
        self.image = image
        self.surface = win
        self.x = x
        self.y = y
        self.speed = 0.5
        self.moved = 0
        self.start_side = bool(getrandbits(1))
        self.rect = pygame.Rect((self.x, self.y), (self.image.get_width(), self.image.get_height()))

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = self.speed  # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]:  # down key
            self.y += dist  # move down
        elif key[pygame.K_UP]:  # up key
            self.y -= dist  # move up
        if key[pygame.K_RIGHT]:  # right key
            self.x += dist  # move right
        elif key[pygame.K_LEFT]:  # left key
            self.x -= dist  # move left

    def auto_move(self):
        if self.start_side:
            if self.moved - self.speed >= -20:
                self.x -= self.speed
                self.moved -= self.speed
            else:
                self.start_side = not self.start_side
        else:
            if self.moved + self.speed <= 20:
                self.x += self.speed
                self.moved += self.speed
            else:
                self.start_side = not self.start_side

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))
