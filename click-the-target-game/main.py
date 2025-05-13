import pygame
import random
import time

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Target")

target_image = pygame.image.load("assets/target.png")
target_image = pygame.transform.scale(target_image, (100, 100))
target_rect = target_image.get_rect()

score = 0
game_duration = 30
start_time = time.time()

def place_target():
    max_x = max(0, WIDTH - target_rect.width)
    max_y = max(0, HEIGHT - target_rect.height)
    target_rect.x = random.randint(0, max_x)
    target_rect.y = random.randint(0,max_y)

place_target()

running = True
while running:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > game_duration:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if target_rect.collidepoint(event.pos):
                score += 1
                place_target()

    screen.fill((255, 255, 255))
    screen.blit(target_image, target_rect)

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    time_left = max(0, int(game_duration - elapsed_time))
    timer_text = font.render(f"Time: {time_left}", True, (0, 0, 0))
    screen.blit(timer_text, (WIDTH - 160, 10))

    pygame.display.flip()

pygame.quit()
print(f"Game over! Final score: {score}")

