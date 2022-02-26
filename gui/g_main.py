import pygame
import sys
from pygame.locals import *

from gui.g_common import *
from gui.g_graph import *
from gui.g_particle import *

class GUI_G:
    def __init__(self, ncount: int, edges) -> None:
        self.graph = Graph_G(ncount=ncount, edges=edges)

        # init pygame
        pygame.init()
        self.surface = pygame.display.set_mode(size=SCREEN_SIZE)
        self.fps_clock = pygame.time.Clock()

    def run(self) -> None:
        while True:
            # poll events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # display
            self.surface.fill(color=COLOR["white"])
            self.graph.draw_graph(surface=self.surface)
            pygame.display.update()
            self.fps_clock.tick(FPS)