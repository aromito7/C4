#Neural Network
import pandas as pd
import numpy as np


def main():
	learning_rate = .001
	exploration_rate = .2
	inputs = 2
	layers = 7
	layer_width = 4
	outputs = 1

	data = [[5,4,1]]

	for i in range(10):
		temp = np.random.randint(10, size = 2)
		if temp[0] > temp[1]: temp = np.append(temp, 1)
		else: temp = np.append(temp, -1)
		data = np.concatenate((data, [temp]))

	
	print(data)


	first = np.random.rand(inputs,layer_width)
	middle = np.random.rand(layers-1, layer_width, layer_width)
	last = np.random.rand(layer_width, outputs)


	result = [1,0]
	result = result@first
	#print(result)
	for M in middle:
		result = result@M
		#print(result)

	result = result@last

	#print(result)
	#print(sigmoid(result))

	a = np.array([	[1,0],
					[0,1]])

	b = np.array([	[4,1],
					[2,2]])

def tanh(x):
	e_pos_x = np.exp(x)
	e_neg_x = np.exp(-x)
	result = (e_pos_x - e_neg_x)/(e_pos_x + e_neg_x)

	return result

def sigmoid(x):
	result = 1 / (1+ np.exp(-x))

	return result


if __name__ == '__main__':
	main()