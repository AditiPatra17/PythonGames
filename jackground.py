import pygame

# Define the game window
screen = pygame.display.set_mode((640, 480))

# Load the game sprites
jack_sprite = pygame.image.load("jack.png")
ground_sprite = pygame.image.load("ground.png")

# Initialize the game variables
jack_x = 100
jack_y = 200
jack_vel = 0
ground_y = 400

# Start the game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jack_vel = -10

    # Update the game logic
    jack_y += jack_vel
    if jack_y > ground_y:
        jack_y = ground_y
        jack_vel = 0

    # Draw the game sprites
    screen.fill((255, 255, 255))
    screen.blit(ground_sprite, (0, ground_y))
    screen.blit(jack_sprite, (jack_x, jack_y))

    # Update the display
    pygame.display.flip()
