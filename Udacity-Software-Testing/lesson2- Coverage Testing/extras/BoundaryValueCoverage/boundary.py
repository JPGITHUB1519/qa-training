"""
    Boundary Value Test

        Domain 1- 1000
        Test  below the extreme edges of input domains i.e. values 0 and 999.
        Test data with values just above the extreme edges of input domain i.e. values 2 and 1001.
"""

import math

# Insert a bug of your choosing into the stats function.
def stats(lst):
    min = None
    max = None
    freq = {}
    for i in lst:
        # mannually bug inserted
        i = abs(i)
        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    lst_sorted = sorted(lst)
    if len(lst_sorted)%2 == 0:
        middle = len(lst_sorted)/2
        median = (lst_sorted[middle] + lst_sorted[middle-1]) / 2
    else:
        median = lst_sorted[len(lst_sorted)/2]
    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i
    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append (num)
    print "list = " + str(lst)
    print "min = " + str(min)
    print "max = " + str(max)
    print "median = " + str(median)
    print "mode(s) = " + str(mode)

def boundaryValueCoverage():
    # with boundary value coverage we can found the bug with the negative value    
    stats([-1,0,50,-999])

boundaryValueCoverage()