import random

#generate initial truth assignments for only classical bit variables
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

# the specific implementation of hillClimbing is never specified in the paper
# we went for the brute force approach for the sake of time
def hillClimb(truthAssignment, formula, qubitList, fitness) -> int :
    bestFitness = fitness
    indexToFlip = -1 
    count = 0
    for i in range(len(truthAssignment)):
        # only flipping the values of the classical bits 
        if i+1 not in qubitList : 
            newAssignment = truthAssignment.copy() # for every variable, we are going to make a new list and only flip that variable
            newAssignment[i] = not newAssignment[i]
            newFitness = getFitness(truthAssignment, formula, qubitList)
            
            if newFitness < bestFitness:
                indexToFlip = i
            count += 1
    return indexToFlip, count
        
# this is the modified version of GSAT as described in the paper 
def GenSAT(formula, qubitList, numVars, maxTries, maxFlips) -> list:
    for i in range(1, maxTries) :
        truthAssignment = initialTruths(numVars) 
        for j in range(1, maxFlips) :
            fitness = getFitness(truthAssignment, formula, qubitList)
            if fitness == 0 :   # want fitness to be minimized (0)
                return truthAssignment
            else :
                # variable whose assigned is to be changed is chosen at random from those that would give an equally good improvement
                index, count = hillClimb(truthAssignment, formula, qubitList, fitness)

                if index != -1 :    # if we found a better fitness value 
                    # flip truth value
                    formula[index] = not formula[index]
                
    print("no satisfying assignment found")
    return []


