# enemy.py
import pygame
import random

class Enemy:
    def __init__(self):
        self.image = pygame.Surface((50, 30))
        self.image.fill((255, 0, 0))  # Red color for the enemy
        self.rect = self.image.get_rect(x=random.randint(0, 800 - 50), y=0)
        self.speed = 3

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self):
        return self.rect.y > 600
