from operator import attrgetter
import random
import sys
import copy

from pso.pso_graph import *
from pso.pso_particle import *


class PSO:

    def __init__(self, graph, iterations, size_population, beta=1, alpha=1):
        self.graph = graph
        self.iterations = iterations
        self.particles = []

        # the probability that swap operator is accepted from swap sequence (gbest - x(t-1))
        self.beta = beta
        # the probability that all swap operator is accepted from swap sequence (pbest - x(t-1))
        self.alpha = alpha
        
        self.evolutions = []  # store the evolutions of gbest path traversal order
        self.annotatedEvolutions = []  # store the evolutions of gbest path costs

        solutions = self.graph.get_random_paths(size_population)
        if not solutions:
            print('Initial population empty! Try run the algorithm again...')
            sys.exit(1)

        # creates one particle per random solution in solutions
        for solution in solutions:
            particle = Particle(solution=solution,cost=graph.get_cost_path(solution))
            self.particles.append(particle)

        self.size_population = len(self.particles)


    def set_gbest(self, new_gbest):
        self.gbest = new_gbest


    def get_gbest(self):
        return self.gbest


    # shows the info of the particles
    def show_particles(self):
        pindex = 0
        for particle in self.particles:
            print('particle:%d - pbest: %s\t|\tcost pbest: %d\t|\tcurrent soln: %s\t|\tcost soln: %d'
              % (pindex, str(particle.get_pbest()), particle.get_cost_pbest(), str(particle.get_current_solution()),
                 particle.get_cost_current_solution()))
            pindex += 1

    def run(self):
        for _ in range(self.iterations):
            # updates gbest (best particle of the population)
            self.gbest = min(self.particles, key=attrgetter('cost_pbest_solution'))
            self.evolutions.append(self.gbest.get_pbest())
            self.annotatedEvolutions.append(self.gbest.get_cost_pbest())

            for particle in self.particles:
                particle.clear_velocity()  
                solution_gbest = copy.copy(self.gbest.get_pbest())
                solution_pbest = particle.get_pbest()[:]
                solution_particle = particle.get_current_solution()[:]

                temp_velocity = []

                # swap operators to calculate (pbest - x(t-1))
                for i in range(self.graph.amount_vertices):
                    if solution_particle[i] != solution_pbest[i]:
                        # generates swap operator
                        swap_operator = (i, solution_pbest.index(
                            solution_particle[i]), self.alpha)

                        temp_velocity.append(swap_operator)

                        # makes the swap
                        aux = solution_pbest[swap_operator[0]]
                        solution_pbest[swap_operator[0]
                                       ] = solution_pbest[swap_operator[1]]
                        solution_pbest[swap_operator[1]] = aux

                # swap operators to calculate (gbest - x(t-1))
                for i in range(self.graph.amount_vertices):
                    if solution_particle[i] != solution_gbest[i]:
                        # generates swap operator
                        swap_operator = (i, solution_gbest.index(
                            solution_particle[i]), self.beta)

                        temp_velocity.append(swap_operator)

                        # makes the swap
                        aux = solution_gbest[swap_operator[0]]
                        solution_gbest[swap_operator[0]
                                       ] = solution_gbest[swap_operator[1]]
                        solution_gbest[swap_operator[1]] = aux

                particle.set_velocity(temp_velocity)

                # generates new solution for particle
                for swap_operator in temp_velocity:
                    if random.random() <= swap_operator[2]:
                        # makes the swap
                        aux = solution_particle[swap_operator[0]]
                        solution_particle[swap_operator[0]
                                          ] = solution_particle[swap_operator[1]]
                        solution_particle[swap_operator[1]] = aux

                particle.set_current_solution(solution_particle)
                particle.solution_set.append(solution_particle)

                cost_current_solution = self.graph.get_cost_path(solution_particle)
                particle.set_cost_current_solution(cost_current_solution)

                # checks if current solution is pbest solution
                if cost_current_solution < particle.get_cost_pbest():
                    particle.set_pbest(solution_particle)
                    particle.set_cost_pbest(cost_current_solution)
