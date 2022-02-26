import pygame
from typing import List, Type
from gui.g_common import *


class Node_G:
    def __init__(self, px: float, py: float, tag: int) -> None:
        self.vertex = (px, py)
        self.tag = tag
        self.radius = 40
        self.color = COLOR["red"]
        self.neighbours = set()

    def draw_node(self, surface) -> None:
        pygame.draw.circle(surface=surface, color=self.color,
                           center=self.vertex, radius=self.radius)


class Edge_G:
    def __init__(self, v1: tuple, v2: tuple, weight: float) -> None:
        self.start = v1
        self.end = v2
        self.weight = weight
        self.color = COLOR["red"]

    def draw_edge(self, surface):
        pygame.draw.line(surface=surface, color=self.color,
                         start_pos=self.start, end_pos=self.end)


class Graph_G:
    def __init__(self, ncount: int, edges) -> None:
        self.ncount = ncount
        self.radius = 300
        self.vertices = regular_polygon_points(ncount, self.radius, tuple(d/2 for d in SCREEN_SIZE))
        self.nodes = self.__build_nodes()
        self.edges = self.__build_edges(edges)
        self.color = COLOR["red"]
        self.stroke = 2

    def __build_edges(self, edges) -> List[Type[Edge_G]]:
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

    def draw_graph(self, surface) -> None:
        for node in self.nodes:
            node.draw_node(surface=surface)
        for edge in self.edges:
            edge.draw_edge(surface=surface)