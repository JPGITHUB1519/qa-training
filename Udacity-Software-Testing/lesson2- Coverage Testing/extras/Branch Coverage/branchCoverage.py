def analyzeNumber(n):
    if n > 0:
        print "Positive"
    else:
        print "Negative"

# with statement Coverage we are only covering 86%
# def statementCoverage():
#     """
#         Only Cover True
#     """
#     analyzeNumber(5)

# 100% covering with two differentes statements
def branchCoverage():
    """
        It covers both the true and false conditions unlikely the statement coverage.
    """
    analyzeNumber(1)
    analyzeNumber(-1)

#statementCoverage()
branchCoverage()