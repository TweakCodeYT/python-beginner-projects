
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

# Player setup
player_width = 60
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 7

# Falling object setup
object_width = 20
object_height = 20
object_x = random.randint(0, WIDTH - object_width)
object_y = 0
object_speed = 5

# Score and font
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move falling object
    object_y += object_speed

    # Game Over check
    if object_y > HEIGHT:
        print("Game Over")
        pygame.time.wait(2000)
        running = False

    # Collision detection
    if (object_y + object_height > player_y and
        object_y < player_y + player_height and
        object_x + object_width > player_x and
        object_x < player_x + player_width):
        score += 1
        object_x = random.randint(0, WIDTH - object_width)
        object_y = 0

    # Draw everything
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, (255, 0, 0), (object_x, object_y, object_width, object_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update screen
    pygame.display.update()
    clock.tick(60)

# Quit game
pygame.quit()
sys.exit()

