# main.py
import random
import pygame
import sys
from player import Player
from bullet import Bullet
from enemy import Enemy

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

# Colors
BLACK = (0, 0, 0)

def main():
    clock = pygame.time.Clock()
    player = Player(WIDTH // 2, HEIGHT - 50)
    bullets = []
    enemies = [] 

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-1)
        if keys[pygame.K_RIGHT]:
            player.move(1)
        if keys[pygame.K_SPACE]:
            bullet = Bullet(player.rect.centerx, player.rect.top)
            bullets.append(bullet)

        # Update bullets
        for bullet in bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                bullets.remove(bullet)

        # Spawn enemies
        if  random.randint(1, 30) == 1:
            enemy = Enemy()
            enemies.append(enemy)

        # Update enemies
        for enemy in enemies[:]:
            enemy.update()
            if enemy.is_off_screen():
                enemies.remove(enemy)

            # Check for collision with bullets
            for bullet in bullets[:]:
                if bullet.rect.colliderect(enemy.rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    break

        # Drawing
        screen.fill(BLACK)
        player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
