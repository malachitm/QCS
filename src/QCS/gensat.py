'''A 3-SAT formula F(X)=(x1 V x3 V x4 ) ∧ (x2 V x4 V x5) ∧ (x1 V x2 V x4) ∧ (x3 V x4 V x6)
x1, x2, x3 and x4 are classical-bit variables; x5 and x6 are quantum-bit variables.'''

import random

def GenSAT(formula, maxTries, maxFlips, randomWalkProb):
    for i in range(1, maxTries) :
        truth = initial(formula) #generate an initial truth assignment for j := 1 to Max-flips
        for j in range(1, maxFlips) :
            if truth satisfies formula :
                return truth
            else :
                Poss-flips = select(formula, truth, randomWalkProb); #select set of vars to pick from
                V = pick(Post-flips); pick one
                T = T with V’s truth assignment flipped end
    print("no satisfying assignment found")
        
def select(formula, truth, randomWalkProb) :
    if Random[0, 1] < randomWalkProb :
        then all variables in unsatisfied clauses
    else :
        hclimb(formula, truth); #compute “best” local neighbors