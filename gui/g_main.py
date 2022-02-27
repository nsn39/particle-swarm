from gui.g_common import *
from gui.g_graph import *
from gui.g_particle import *
from gui.g_text import *


class GUI_G:
    def __init__(self, ncount: int, edges: Dict[Tuple[int, int], int], particles, gbest_evolutions, gbest_evolutions_annotations) -> None:
        pygame.init()

        self.graph = Graph_G(ncount=ncount, edges=edges)
        self.particles = Particles_G(particles=particles, graph=self.graph)
        self.gbest_evolutions = gbest_evolutions
        self.gbest_evolutions_annotations = gbest_evolutions_annotations
        self.window_open = True

        self.surface = pygame.display.set_mode(size=SCREEN_SIZE)
        self.fps_clock = pygame.time.Clock()
        self.iter_text = Text_G(text="Iteration: 0", pos=(10, 10),
                                size=30, color=COLOR["white"], pos_wrt_center=False)

        self.gbest_text = Text_G(text="Global Best: [], Cost: 0", pos=(10, 50), size=30,
                                 color=COLOR["white"], pos_wrt_center=False)

        # check imports
        if not pygame.font:
            print("Warning: Fonts disabled")

    def run(self) -> None:
        current_iteration = 0
        while self.window_open:
            # poll events
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.window_open = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.particles.solve(
                            surface=self.surface, fps_clock=self.fps_clock)
                        current_iteration += 1

            # background
            self.surface.fill(color=COLOR["grey"])

            self.particles.draw_particles(self.surface)
            self.iter_text.draw_updated_text(
                self.surface, "Iteration: " + str(current_iteration))

            if current_iteration > 0:
                self.gbest_text.draw_updated_text(
                    self.surface, "Global Best: " + str(self.gbest_evolutions[current_iteration]) + ", Cost: " + str(self.gbest_evolutions_annotations[current_iteration]))
                self.graph.draw_graph(self.surface, self.gbest_evolutions[current_iteration])
            else:
                self.gbest_text.draw_text(self.surface)
                self.graph.draw_graph(self.surface, [])

            pygame.display.update()
            self.fps_clock.tick(FPS)

        pygame.quit()
    
    def run_path(self) -> None:
        current_iteration = 0
        while self.window_open:
            # poll events
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.window_open = False

                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_SPACE:
                #         self.particles.solve(
                #             surface=self.surface, fps_clock=self.fps_clock)
                #         current_iteration += 1

                


            # background
            self.surface.fill(color=COLOR["grey"])

            # self.particles.draw_particles(self.surface)
            self.iter_text.draw_updated_text(
                self.surface, "Iteration: " + str(current_iteration))

            if current_iteration > 0:
                self.gbest_text.draw_updated_text(
                    self.surface, "Global Best: " + str(self.gbest_evolutions[current_iteration]) + ", Cost: " + str(self.gbest_evolutions_annotations[current_iteration]))
                self.graph.draw_path(self.surface, self.gbest_evolutions[current_iteration])
            else:
                self.gbest_text.draw_text(self.surface)
                self.graph.draw_graph(self.surface, [])
            
            
            if(current_iteration<len(self.gbest_evolutions)-1):
                current_iteration+=1

            pygame.display.update()
            self.fps_clock.tick(5)

        pygame.quit()

