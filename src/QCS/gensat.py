import random

#generate initial truth assignments for variables
def initialTruths(numVars) -> list :
    return [random.choice([True, False]) for num in range(numVars)]

# fitness value (the number of unsatisfied clauses that have no qubit-variable) = 0
def getFitness(truthAssignment, formula, qubitList) -> int : 
    count = 0
    noQubitClauses = list(filter(lambda qubit: qubit in qubitList, formula))
    for clause in noQubitClauses :
        for literal in clause :
            if literal > 0 :
                if truthAssignment[literal] is True :
                   break    # break the first time we see a True value 
            else :
                # the negative of False is True 
                if truthAssignment[literal] is False :
                    break
        count += 1
    numUnSatisfied = noQubitClauses - count 
    return numUnSatisfied

def hillClimb(truthAssignment, formula, fitness) -> int :
    bestFitness = fitness
    indexToFlip = -1 
    for i in range(len(truthAssignment)):
        newAssignment = truthAssignment.copy() # for every variable, we are going to make a new list and only flip that variable
        newAssignment[i] = not newAssignment[i]
        newFitness = getFitness(truthAssignment, formula, qubitList)
        
        if newFitness < bestFitness:
            indexToFlip = i
    return indexToFlip


numVars = 0
numQubits = 0
queries = 0 

# in the paper, which variables are chosen as qubits is calculated using the 'the crashing probability'
# for sake of time, just choose randomly? 
qubitList = random.choices(population=range(1, numVars, 1), k=numQubits)
        
# this is the modified version of GSAT as described in the paper 
def GenSAT(formula, qubitList, maxTries, maxFlips) -> list:
    for i in range(1, maxTries) :
        truthAssignment = initialTruths(numVars) 
        for j in range(1, maxFlips) :
            fitness = getFitness(truthAssignment, formula, qubitList)
            if fitness == 0 :   # want fitness to be minimized (0)
                return truthAssignment
            else :
                # variable whose assigned is to be changed is chosen at random from those that would give an equally good improvement
                index = hillClimb(truthAssignment, formula, fitness)

                if index != -1 :    # if we found a better fitness value 
                    # flip truth value
                    formula[index] = not formula[index]
                
    print("no satisfying assignment found")
    return []


