"""
    MC /DC COVERAGE (modified codition / decision) = branch coverage + conditions take all posible values + every condition idependently affect
    the outcome of a decision
"""

def main(a, b, c):
    if a or (b and c):
        print True
    else:
        print False

def statementCoverage():
    # Only for True
    main(True, False, True) # True

def BranchCoverage():
    # Only for true and false
    main(True, False, True) # True
    main(False, False, True) # False 

# i think i can use Permutation(2 ** 3) = 8 posibles values
def mcDcCoverage():
    # All Posibles Values
    main(True, False, True) # True
    main(False, False, True) # False
    main(False, True, True) # True
    main(False, True, False) #False

mcDcCoverage()