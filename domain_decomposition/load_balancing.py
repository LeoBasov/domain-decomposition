"""Module for load balancing
"""

import math

def simple(processes, elements):
	"""Function providing a simple load balancing

	This function sorts elements to processes to a load in every element which close to the theoretical mean load.

	Parameters
	----------
	processes : list:obj:'process'
		List of processes which can be assigned elements

	elements : list:obj:'element'
		List of elements

	Returns
	-------
	None

	"""
	mean_load = 0
	max_load = 0
	i_p = 0

	for element in elements:
		mean_load += element.load_factor

	mean_load = math.ceil(mean_load/len(processes))

	for element in elements:
		if processes[i_p].load >= mean_load:
			i_p += 1

		processes[i_p].add_element(element)

		if max_load < processes[i_p].load:
			max_load = processes[i_p].load

	return mean_load, max_load

__author__ = "Leo Basov"
__copyright__ = "Copyright (C) 2019, Leo Basov"
__license__ = "GPLv3"