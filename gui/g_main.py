import sys

from gui.g_common import *
from gui.g_graph import *
from gui.g_particle import *


class GUI_G:
    def __init__(self, ncount: int, edges: Dict[Tuple[int, int], int], particles) -> None:
        self.graph = Graph_G(ncount=ncount, edges=edges)
        self.particles = Particles_G(particles=particles, graph=self.graph)

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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.particles.solve(surface=self.surface, fps_clock=self.fps_clock) 

            # display
            self.surface.fill(color=COLOR["white"])
            self.graph.draw_graph(surface=self.surface)
            self.particles.draw_particles(surface=self.surface)
            pygame.display.update()
            self.fps_clock.tick(FPS)
