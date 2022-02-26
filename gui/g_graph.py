from typing import List, Type, Dict, Tuple
from gui.g_common import *
from gui.g_text import Text_G


class Node_G:
    def __init__(self, px: float, py: float, tag: int) -> None:
        self.vertex = (px, py)
        self.radius = 40
        self.color = COLOR["red"]
        self.neighbours = set()

        self.tag = tag
        self.tag_text = Text_G(text=str(tag), pos=(px, py), size=25,
                               color=COLOR["white"], pos_wrt_center=True)

    def draw_node(self, surface: Type[pygame.Surface]) -> None:
        pygame.draw.circle(surface, self.color, self.vertex, self.radius)
        self.tag_text.draw_text(surface)


class Edge_G:
    def __init__(self, v1: tuple, v2: tuple, weight: float) -> None:
        self.start = v1
        self.end = v2
        self.color = COLOR["red"]

        self.weight = weight
        self.weight_text = Text_G(text=str(weight), pos=self.get_midpoint(),
                                  size=25, color=COLOR["red"], pos_wrt_center=True)

    def get_midpoint(self):
        ax, ay = self.start
        bx, by = self.end
        return ((ax + bx) / 2, (ay + by) / 2)

    def draw_edge(self, surface: Type[pygame.Surface]):
        pygame.draw.line(surface=surface, color=self.color,
                         start_pos=self.start, end_pos=self.end)
        self.weight_text.draw_text(surface=surface)


class Graph_G:
    def __init__(self, ncount: int, edges: Dict[Tuple[int, int], int]) -> None:
        self.ncount = ncount
        self.radius = 300
        self.vertices = regular_polygon_points(
            ncount, self.radius, tuple(d/2 for d in SCREEN_SIZE))
        self.nodes = self.__build_nodes()
        self.edges = self.__build_edges(edges)
        self.color = COLOR["red"]
        self.stroke = 2

    def __build_edges(self, edges: Dict[Tuple[int, int], int]) -> List[Type[Edge_G]]:
        edge_list = []
        for edge, weight in edges.items():
            n1, n2 = edge
            v1, v2 = self.nodes[n1].vertex, self.nodes[n2].vertex
            edge_list.append(Edge_G(v1=v1, v2=v2, weight=weight))
        return edge_list

    def __build_nodes(self) -> List[Type[Node_G]]:
        nodes = []
        for i in range(len(self.vertices)):
            px, py = self.vertices[i]
            nodes.append(Node_G(px=px, py=py, tag=i))
        return nodes

    def draw_graph(self, surface: Type[pygame.Surface]) -> None:
        for node in self.nodes:
            node.draw_node(surface=surface)
        for edge in self.edges:
            edge.draw_edge(surface=surface)
