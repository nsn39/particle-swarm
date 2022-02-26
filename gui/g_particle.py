from typing import List, Type
from gui.g_graph import Graph_G, Node_G
from gui.g_common import *


class Particle_G:
    def __init__(self, starting_node: int, nodes: List[Type[Node_G]], solution_set) -> None:
        self.nodes = nodes
        self.pos = nodes[starting_node].vertex
        self.curent_node = nodes[starting_node]
        self.radius = nodes[starting_node].radius / 10
        self.color = COLOR["black"]

        self.solution_set = solution_set 
        self.solution = solution_set[0]
        self.solution_index = 0

        self.speed = 0.1  # particle travels 1/10th of the distance in one iteration

    def next_solution(self) -> None:
        self.solution_index = min(self.solution_index+1, len(self.solution_set)-1)
        if self.solution_index != -1:
            self.solution = self.solution_set[self.solution_index]

    def travel_towards_node(self, next_node: Type[Node_G]) -> None:
        px, py = self.pos
        sx, sy = self.curent_node.vertex
        vx, vy = next_node.vertex
        dx, dy = vx - sx, vy - sy
        self.pos = (px + dx * self.speed, py + dy * self.speed)

    def draw_particle(self, surface: Type[pygame.Surface]) -> None:
        pygame.draw.circle(surface=surface, color=self.color,
                           center=self.pos, radius=self.radius)

class Particles_G:
    def __init__(self, particles, graph: Type[Graph_G]) -> None:
        self.particles = [Particle_G(starting_node=0, nodes=graph.nodes, solution_set=particle.solution_set)
                          for particle in particles]
        self.graph = graph
    
    def solve(self, surface: Type[pygame.Surface], fps_clock: Type[pygame.time.Clock]):
        node_traversal = [x for x in range(0, self.graph.ncount)]
        node_traversal.append(node_traversal[0])  # loop back to first node to complete traversal
        for i in node_traversal: 
            for k in range(10): # inverse of particle speed 1/0.1 == 10
                for particle in self.particles:
                    next_node_index = int(particle.solution[i])
                    particle.travel_towards_node(particle.nodes[next_node_index])
                    particle.draw_particle(surface=surface)

                    if k == 9: # particle has reached destination, update current node
                        particle.curent_node = particle.nodes[next_node_index]
            
                surface.fill(color=COLOR["white"])
                self.graph.draw_graph(surface=surface)
                self.draw_particles(surface=surface)
                pygame.display.update()
                fps_clock.tick(FPS) 
            
        for particle in self.particles:
            particle.next_solution()
    
    def draw_particles(self, surface: Type[pygame.Surface]):
        for particle in self.particles:
            particle.draw_particle(surface=surface)