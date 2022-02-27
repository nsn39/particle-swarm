import random
import sys


class Graph:

    def __init__(self, amount_vertices, starting_vertex):
        self.edges = {}  # dictionary of edges
        self.vertices = set()  # set of vertices
        self.amount_vertices = amount_vertices  # amount of vertices
        self.starting_vertex = starting_vertex

    def generate_random_complete_graph(self):
        for i in range(self.amount_vertices):
            for j in range(self.amount_vertices):
                if i != j:
                    weight = random.randint(1, 10)
                    self.add_edge(i, j, weight)

    # adds a edge linking "src" in "dest" with a "cost"
    def add_edge(self, src, dest, cost=0):
        if not self.edge_exists(src, dest):
            self.edges[(src, dest)] = cost
            self.edges[(dest, src)] = cost
            self.vertices.add(src)
            self.vertices.add(dest)

    def edge_exists(self, src, dest):
        return (True if (src, dest) in self.edges else False)

    def show_graph(self):
        print('Showing the graph:\n')
        for edge in self.edges:
            print('%d linked in %d with cost %d' %
                  (edge[0], edge[1], self.edges[edge]))

    def get_cost_path(self, path):
        total_cost = 0
        for i in range(self.amount_vertices - 1):
            total_cost += self.edges[(path[i], path[i+1])]

        # add cost of the last edge
        total_cost += self.edges[(path[self.amount_vertices - 1], path[0])]
        return total_cost

    # gets random unique paths - returns a list of lists of paths
    def get_random_paths(self, max_size):
        random_paths, list_vertices = [], list(self.vertices)
        initial_vertice = self.starting_vertex

        if initial_vertice not in list_vertices:
            print('Error: initial vertice %d not exists!' % initial_vertice)
            sys.exit(1)

        list_vertices.remove(initial_vertice)
        list_vertices.insert(0, initial_vertice)

        for i in range(max_size):
            list_temp = list_vertices[1:]
            random.shuffle(list_temp)
            list_temp.insert(0, initial_vertice)

            if list_temp not in random_paths:
                random_paths.append(list_temp)

        return random_paths
