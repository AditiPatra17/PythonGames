import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

# Player attributes
player_width = 50
player_height = 50
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height

# Object attributes
object_width = 50
object_height = 50
object_x = random.randint(0, WIDTH - object_width)
object_y = 0
object_speed = 5

# Score
score = 0

# Lives
lives = 3

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

    # Update object position
    object_y += object_speed

    # Collision detection
    if player_x < object_x + object_width and player_x + player_width > object_x:
        if player_y < object_y + object_height and player_y + player_height > object_y:
            object_x = random.randint(0, WIDTH - object_width)
            object_y = 0
            score += 1

    # Check for out-of-screen objects
    if object_y > HEIGHT:
        object_x = random.randint(0, WIDTH - object_width)
        object_y = 0
        # Decrease a life
        lives -= 1

    # If no lives left, end the game
    if lives == 0:
        running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw the object
    pygame.draw.rect(screen, BLUE, (object_x, object_y, object_width, object_height))

    # Display score and lives
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))
    lives_text = font.render(f"Lives: {lives}", True, BLUE)
    screen.blit(lives_text, (10, 50))

    # Update the display
    pygame.display.update()

    # Limit frames per second
    clock.tick(FPS)

# Quit the game
print("You Lose!")
pygame.quit()
