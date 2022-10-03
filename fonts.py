# Import module; initialize module
import pygame
pygame.init()

# Gets the system fonts
fonts = pygame.font.get_fonts()

# Creates window object
window = pygame.display.set_mode((1200, 400))

# Starter tick
start_ticks = pygame.time.get_ticks()

# Main loop variable
running = True

# Main while loop
while running:

    # Calculate how many seconds
    ticks = (pygame.time.get_ticks() - start_ticks) / 1000
    
    # Concatenates from float to integer
    seconds = int(ticks)

    # Sets window color
    window.fill((255, 255, 255))

    # Closes window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

	# Creates the text object with each iteration of the font
    font = pygame.font.SysFont(fonts[seconds], 60)

	# Renders each text example into a blit-able object
    x = font.render("The QUICK Brown fox JUMPED Over the LAZY", True, (0, 0, 0))
    y = font.render("dOg 123456789:/?><()", True, (0, 0, 0))
    z = font.render(fonts[seconds], True, (0, 0, 0))
	
	# Blits/displays the text on the screen
    window.blit(x, (0, 2))
    window.blit(y, (0, 100))
    window.blit(z, (0, 200))

	# Prints the number and the name of each font
    print(seconds, fonts[seconds])

	# Updates the display
    pygame.display.flip()

