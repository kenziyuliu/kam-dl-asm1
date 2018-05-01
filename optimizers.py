from layers import *

class SGD:
	"""docstring for ClassName"""
	def __init__(self, learning_rate = 0.001, monmentum = 0.9, nesterov = False):
		self.learning_rate = learning_rate
		self.accumlated_v = []
		self.monmentum = monmentum
		self.use_nesterov = nesterov

	def init_shape(shape_list):
		for shape in shape_list:
			self.accumlated_v.append(np.zeros(shape))

	def optimize(self, params_gradient):
		for i in range(len(params_gradient)):
			parameter, gradient = params_gradient[i]
			if self.use_nesterov:
				dervative = accumlated_v[i]
				accumlated_v[i] = self.monmentum * accumlated_v[i] + self.learning_rate * gradient
				dervative = self.monmentum * dervative - (1.0 + self.monmentum) * accumlated_v[i]
			else:
				dervative = self.monmentum * accumlated_v[i] - self.learning_rate * gradient
				accumlated_v[i] = dervative
			parameter += dervative

		


class Adam:
	def __init__(self, learning_rate = 0.001, B1 = 0.9, B2 = 0.999, epsilon = 1e-8):
		self.learning_rate = learning_rate
		self.B1 = B1
		self.B2 = B2
		self.epsilon = epsilon
		self.accumlated_mt = []
		self.accumlated_vt = []
		self.t = 0

	def init_shape(shape_list):
		for shape in shape_list:
			self.accumlated_mt.append(np.zeros(shape))
			self.accumlated_vt.append(np.zeros(shape))

	def optimize(self, params_gradient):
		self.t += 1

		for i in range(len(params_gradient)):
			parameter, gradient = params_gradient[i]
			accumlated_mt[i] *= self.B1
			accumlated_mt[i] += (1 - self.B1) * gradient
			accumlated_vt[i] *= self.B2
			accumlated_vt[i] += (1 - self.B2) * (gradient * gradient)
			mt_W = accumlated_mt[i] / (1 - self.B1 ** t)
			vt_W = accumlated_vt[i] / (1 - self.B2 ** t)
			parameter -= self.learning_rate * mt_W / (np.sqrt(vt_W) + self.epsilon)




		
		