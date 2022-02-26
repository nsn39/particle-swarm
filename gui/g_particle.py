from tracemalloc import start
from typing import List, Type
from gui.g_graph import Graph_G, Node_G
from gui.g_common import *


class Particle_G:
    def __init__(self, starting_node: int, nodes: List[Type[Node_G]], solution: List[int]) -> None:
        self.nodes = nodes
        self.pos = nodes[starting_node].vertex
        self.curent_node = nodes[starting_node]
        self.radius = nodes[starting_node].radius / 10
        self.color = COLOR["black"]

        self.solution = solution
        self.solution.append(solution[0]) # append initial node to end to complete cycle

        self.speed = 0.1  # particle travels 1/10th of the distance in one iteration

    def travel_towards_node(self, next_node) -> None:
        px, py = self.pos
        sx, sy = self.curent_node.vertex
        vx, vy = next_node.vertex
        dx, dy = vx - sx, vy - sy
        self.pos = (px + dx * self.speed, py + dy * self.speed)

    def draw_particle(self, surface: Type[pygame.Surface]) -> None:
        pygame.draw.circle(surface=surface, color=self.color,
                           center=self.pos, radius=self.radius)

class Particles_G:
    def __init__(self, particles, graph) -> None:
        self.particles = [Particle_G(starting_node=0, nodes=graph.nodes, solution=particle.solution)
                          for particle in particles]
        self.graph = graph
    
    def solve(self, surface: Type[pygame.Surface], fps_clock: Type[pygame.time.Clock]):
        for i in range(1, self.graph.ncount+1): # start from 1 because at 0 is starting node
            for k in range(10): # inverse of particle speed 1/0.1 == 10
                for particle in self.particles:
                    next_node_index = particle.solution[i]
                    particle.travel_towards_node(particle.nodes[next_node_index])
                    particle.draw_particle(surface=surface)

                    if k == 9: # particle has reached destination, update current node
                        particle.curent_node = particle.nodes[next_node_index]
            
                surface.fill(color=COLOR["white"])
                self.graph.draw_graph(surface=surface)
                self.draw_particles(surface=surface)
                pygame.display.update()
                fps_clock.tick(FPS) 
    
    def draw_particles(self, surface):
        for particle in self.particles:
            particle.draw_particle(surface=surface)