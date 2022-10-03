import pygame
pygame.init()

fonts = pygame.font.get_fonts()

window = pygame.display.set_mode((1200, 400))
iteration = 0

start_ticks = pygame.time.get_ticks() #starter tick

running = True

while running:

    ticks = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
    seconds = int(ticks)

    window.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    font = pygame.font.SysFont(fonts[seconds], 60)

    x = font.render("The QUICK Brown fox JUMPED Over the LAZY", True, (0, 0, 0))
    y = font.render("dOg 123456789:/?><()", True, (0, 0, 0))
    z = font.render(fonts[seconds], True, (0, 0, 0))
    window.blit(x, (0, 2))
    window.blit(y, (0, 100))
    window.blit(z, (0, 200))

    print(seconds, fonts[seconds])

    pygame.display.flip()

