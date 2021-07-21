import pygame
pygame.init()

#game windows creation
pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygamon - Aventure");

#game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()