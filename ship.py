import pygame


WHITE = (255, 255, 255)


class Ship:
    def __init__(self, image, surface) -> None:
        self.image = image
        self.surface = surface
        self.x = 550
        self.y = 700
        self.speed = 3
        self.life = 5
        self.rect = self.image.get_rect()

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = self.speed
        if key[pygame.K_DOWN]:
            if self.y < 725:
                self.y += dist
        elif key[pygame.K_UP]:
            if self.y > 550:
                self.y -= dist
        if key[pygame.K_RIGHT]:
            if self.x < 1125:
                self.x += dist
        elif key[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= dist

    def my_rect(self):
        my_rect = pygame.Rect((self.x, self.y), (self.image.get_width() + 15, self.image.get_height() + 15))
        return my_rect