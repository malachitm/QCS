import gensat
import math

from qiskit_algorithms import Grover
from qiskit.primitives import Sampler
from qiskit.circuit.library import PhaseOracle
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_algorithms import AmplificationProblem


#performs Grover’s search on the formula with a candidate individual.
# this version searches all possible solutions instead of just the candidate individual
# here is a page that has a closer solution: https://github.com/qiskit-community/qiskit-community-tutorials/blob/master/algorithms/grover_algorithm.ipynb
def QCSearch(fileName, formula, bestCandidate) -> int :
    grover = Grover(sampler=Sampler())
    oracle = PhaseOracle.from_dimacs_file(fileName)

    problem = AmplificationProblem(oracle, is_good_state=oracle.evaluate_bitstring)
    result = grover.amplify(problem)
    print("Success!" if result.oracle_evaluation else "Failure!")
    print("Top measurement:", result.top_measurement)

#Max-queries is the maximum number of queries performing on fitness functions and oracle calls
#Num-Generations is the maximum number of flips performed for evolving a candidate individual. 
def QCS(fileName, numVars, numQubits, formula, qubitList, maxQueries, numGenerations) :
    for i in range (0, maxQueries) :
        candidate = gensat.initialTruths(numVars)
        for j in range(1,numGenerations) :
            bestCandidate, count = gensat.GenSAT(formula, candidate); #select the best candidate by GenSAT
            queries = i + count

        result = QCSearch(formula, bestCandidate)

        # rounded up to nearest power of 10 since the psuedocode uses big O notation 
        queries += math.ceil(math.log10(pow(2,numQubits/2))); # num_q is the number of qubits
        
        fitness = gensat.getFitness(result, formula, qubitList)
        if fitness == 0 :   # want fitness to be minimized (0)
            return candidate
        print("no satisfying assignment found")
    return gensat.hillClimb(candidate, formula, qubitList, fitness) #compute “best” local neighbors with the defined fitness function


	
