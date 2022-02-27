# class that represents a particle
class Particle:

	def __init__(self, solution, cost):
		self.solution = solution
		# set to store all solutions for the particle by iteration
		self.solution_set = []

		self.pbest = solution
		self.cost_current_solution = cost
		self.cost_pbest_solution = cost

		# velocity of a particle is a sequence of 4-tuple i.e. swap sequences
		# (1, 2, 1, 'beta') means SO(1,2), probability 1 and compares with "beta"
		self.velocity = []

	def set_pbest(self, new_pbest):
		self.pbest = new_pbest

	def get_pbest(self):
		return self.pbest

	def set_velocity(self, new_velocity):
		self.velocity = new_velocity

	def get_velocity(self):
		return self.velocity

	def set_current_solution(self, solution):
		self.solution = solution

	def get_current_solution(self):
		return self.solution

	def set_cost_pbest(self, cost):
		self.cost_pbest_solution = cost

	def get_cost_pbest(self):
		return self.cost_pbest_solution

	def set_cost_current_solution(self, cost):
		self.cost_current_solution = cost

	def get_cost_current_solution(self):
		return self.cost_current_solution

	def clear_velocity(self):
		del self.velocity[:]