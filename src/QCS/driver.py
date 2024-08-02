#from scipy.special import lambertw
#from math import log, pi, pow
#from functools import cache

import gensat
import qcs
import os
import random

n2nq = dict([(25, 13), (30, 14), (35, 14), (40, 15), (50, 16), (80, 18)])
#@cache 
def get_qubit_num(n: int) -> int:
	return n2nq[n]
	#num: float = n * log(2) - (2 * lambertw(pow(2, -5 + n / 2) * pi * pow(log(2), 2) / 1))
	#return round(num / log(2))

if __name__ == "__main__":
	directory = "/Users/jess/Documents/GitHub/QCS/src/QCS/formulas/formulas"
	print(get_qubit_num(25))
	#print(get_qubit_num2(23))
	noise_model = NoiseModel.from_backend("ibm_cleveland")
	backend = AerSimulator(noise_model=noise_model)


	# open each CNF file which contains randomly generated formulas for a specified index of test cases (called a problem instance)
	# total of 180 test cases used in the paper
	for file in os.scandir(directory):
		with open(file, 'r') as input :
			raw = input.readlines(7)	# skip the first 7 lines which are comments 
			params = raw.split(" ")

			# each instance has a set number of variables and number of clauses 
			# each clause has only 3 literals 
			numVars = params[2]
			numClauses = params[3]
			formula = []

			# get all of the clauses, aka the "formula"
			for line in input :
				clause = line.split(" ")
				clause.pop()
				formula.append(clause)

		numVars = 0
		numQubits = 0
		queries = 0 
		maxTries = 0
		maxFlips = 0
		maxQueries = 0
		numGenerations = 0

		# in the paper, which variables are chosen as qubits is calculated using the 'the crashing probability'
		# for sake of time, just choose randomly? 
		qubitList = random.choices(population=range(1, numVars, 1), k=numQubits)

		bestAssignment = gensat.GenSAT(formula, qubitList, numVars, maxTries, maxFlips)

	qcs.QCS(file, numVars, numQubits, formula, qubitList, maxQueries, numGenerations)
	
