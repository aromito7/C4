#Neural Network
import pandas as pd
import numpy as np


def main():
	learning_rate = .01
	exploration_rate = .2
	inputs = 2
	layers = 3
	layer_width = 4
	outputs = 3

	data = [[5,4,1]]

	for i in range(10):
		temp = np.random.randint(10, size = 2)
		if temp[0] > temp[1]: temp = np.append(temp, 1)
		else: temp = np.append(temp, -1)
		data = np.concatenate((data, [temp]))

	#print(data)

	first = np.random.rand(inputs,layer_width)
	middle = np.random.rand(layers-1, layer_width, layer_width)
	last = np.random.rand(layer_width, outputs)

	result = [1,0]


	result, first_inputs, middle_inputs, last_inputs, first_outputs, middle_outputs, last_outputs = propagate(result, first, middle, last, tanh)
	print(result)

	a = np.array([	[1,0],
					[0,1]])

	b = np.array([	[4,1],
					[2,2]])

def error_function(targets, outputs):
	error = 0
	length = len(outputs)
	for i in range(length):
		temp = (outputs[i] - targets[i])**2
		error += temp

	error/= (length*2)

	return error

def deriv_activation(x):
	return 1 - activation(x)**2

def tanh(x):
	e_pos_x = np.exp(x)
	e_neg_x = np.exp(-x)
	result = (e_pos_x - e_neg_x)/(e_pos_x + e_neg_x)
	return result

def sigmoid(x):
	result = 1 / (1+ np.exp(-x))
	return result

def multiply_activate(inputs, weights, activation):
	inputs = inputs@weights
	outputs = activation(inputs)
	return inputs, outputs

def propagate(inputs, first, middle, last, activation):
	result = inputs
	result = multiply_activate(result, first, activation)
	for i in range(len(middle)):
		 middle_inputs[i], middle= multiply_activate(result, middle[i], activation)
	result = multiply_activate(result, last, activation)

	return result

def back_propagate(inputs, first, middle, last, activation, result):
		

	return [first, middle, last]


if __name__ == '__main__':
	main()