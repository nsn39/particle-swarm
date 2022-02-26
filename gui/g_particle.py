from typing import List, Type
from gui.g_graph import Graph_G, Node_G
from gui.g_common import *


class Particle_G:
    def __init__(self, starting_node: int, nodes: List[Type[Node_G]], solution: List[int]) -> None:
        self.nodes = nodes
        self.pos = nodes[starting_node].vertex
        self.radius = nodes[starting_node].radius / 10
        self.color = COLOR["black"]
        self.solution = solution
        self.speed = 0.001  # equal in both x and y axis

    def render_travel_to_node(self, surface: Type[pygame.Surface], nindex: int, graph: Type[Graph_G], fps_clock: Type[pygame.time.Clock]) -> None:
        node = self.nodes[nindex]
        px, py = self.pos
        vx, vy = node.vertex
        dx, dy = vx - px, vy - py

        # render particle traveling motion
        while True:
            px, py = self.pos
            if int(px) == int(vx) and int(py) == int(vy):
                break
            self.pos = (px + dx * self.speed, py + dy * self.speed)

            surface.fill(color=COLOR["white"])
            graph.draw_graph(surface=surface)
            self.draw_particle(surface=surface)
            pygame.display.update()
            fps_clock.tick(FPS)
            

    def draw_particle(self, surface: Type[pygame.Surface]) -> None:
        pygame.draw.circle(surface=surface, color=self.color,
                           center=self.pos, radius=self.radius)
