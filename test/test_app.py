import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('../.')

import domain_decomposition.common as common

def main():
	number_elements = 10
	number_processes = 10
	value_range = (0, 100)
	loads = []

	elements = []
	processes = number_processes*[common.Process()]

	for i in range(number_elements):
		element = common.Element(np.random.uniform(*value_range))
		elements.append(element)

	for i in range(number_processes):
		loads.append(processes[i].load)

	plt.plot(loads)
	plt.show()

if __name__ == '__main__':
	main()