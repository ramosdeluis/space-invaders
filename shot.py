import pygame


WHITE = (255, 255, 255)


class Shots:
    def __init__(self, surface, x, y) -> None:
        self.shots = []
        self.surface = surface
        self.x = x + 33
        self.y = y - 15
        self.speed = 3
        self.shot = pygame.draw.rect(self.surface, WHITE, pygame.Rect(
            (self.x, self.y), (10, 30)))
        self.draw()
        self.rect = pygame.Rect((self.x, self.y), (10, 30))

    def draw(self):
        pygame.draw.rect(self.surface, WHITE, pygame.Rect(
            (self.x, self.y), (10, 30)))
        self.rect = pygame.Rect((self.x, self.y), (10, 30))

    def move_shot(self):
        self.y -= self.speed


class Damages:
    def __init__(self, surface, x, y) -> None:
        self.damages = []
        self.surface = surface
        self.x = x - 33
        self.y = y + 15
        self.speed = 3
        self.damage = pygame.draw.rect(self.surface, WHITE, pygame.Rect(
            (self.x, self.y), (10, 30)))
        self.draw()
        self.rect = pygame.Rect((self.x, self.y), (10, 30))

    def draw(self):
        pygame.draw.rect(self.surface, WHITE, pygame.Rect(
            (self.x, self.y), (10, 30)))
        self.rect = pygame.Rect((self.x, self.y), (10, 30))

    def move_damage(self):
        self.y += self.speed
