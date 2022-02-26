import sys

from gui.g_common import *
from gui.g_graph import *
from gui.g_particle import *
from gui.g_text import *


class GUI_G:
    def __init__(self, ncount: int, edges: Dict[Tuple[int, int], int], particles) -> None:
        pygame.init()

        self.graph = Graph_G(ncount=ncount, edges=edges)
        self.particles = Particles_G(particles=particles, graph=self.graph)

        self.surface = pygame.display.set_mode(size=SCREEN_SIZE)
        self.fps_clock = pygame.time.Clock()
        self.iter_text = Text_G(text="Iteration: 0", pos=(10, 10),
                                size=40, color=COLOR["red"], pos_wrt_center=False)

        # check imports
        if not pygame.font:
            print("Warning: Fonts disabled")

    def run(self) -> None:
        soln_iter = 0
        while True:
            # poll events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.particles.solve(
                            surface=self.surface, fps_clock=self.fps_clock)
                        soln_iter += 1

            # display
            self.surface.fill(color=COLOR["white"])
            self.graph.draw_graph(self.surface)
            self.particles.draw_particles(self.surface)
            self.iter_text.draw_updated_text(
                self.surface, "Iteration: " + str(soln_iter))

            pygame.display.update()
            self.fps_clock.tick(FPS)
