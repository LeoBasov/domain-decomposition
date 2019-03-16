import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('../.')

import domain_decomposition.common as common
import domain_decomposition.load_balancing as balance

def main():
	number_elements  = 10000
	number_processes = 80
	value_range = (0, 100)
	loads = []

	elements = []
	processes = []

	for i in range(number_processes):
		process = common.Process()
		processes.append(process)

	for i in range(number_elements):
		element = common.Element(np.random.uniform(*value_range))
		elements.append(element)

	mean_load, max_load = balance.simple(processes, elements)

	for i in range(number_processes):
		loads.append(processes[i].load)

	plt.plot(loads)
	plt.ylim(bottom=0, top=1.1*max_load)
	plt.axhline(y=mean_load, linestyle='--', color='red', linewidth=1)
	plt.show()

if __name__ == '__main__':
	main()