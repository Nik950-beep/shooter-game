# player.py
import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 30))
        self.image.fill((0, 255, 0))  # Green color for the spaceship
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def move(self, dx):
        self.rect.x += dx * self.speed
        # Keep player within the screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 800 - self.rect.width:
            self.rect.x = 800 - self.rect.width

    def draw(self, screen):
        screen.blit(self.image, self.rect)
