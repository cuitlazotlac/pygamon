import pygame
import pytmx
import pyscroll

from player import Player

pygame.init()


class Game:

    def __init__(self):
        # game windows creation
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon - Adventure");

        # load the map
        tmx_data = pytmx.util_pygame.load_pygame('untitled.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # generate a player
        self.player = Player()

        # draw the layers
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def run(self):
        # game loop
        running = True

        while running:
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


pygame.quit()
