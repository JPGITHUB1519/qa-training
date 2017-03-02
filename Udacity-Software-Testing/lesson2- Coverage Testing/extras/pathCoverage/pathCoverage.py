import random
"""
    Path Coverage
        All possible control paths taken, including all loop paths taken zero, once, and multiple (ideally, maximum) items in path coverage technique
"""

def main(x,y,z):
    "8 Possible Path 2 ** 3 = 8 "
    if x:
        print x
    if y:
        print y
    if z:
        print z

def test():
    main(True, True, True)
    main(True, True, False)
    main(True, False, True)
    main(True, False, False)
    main(False, False, False)
    main(False, True, True)
    main(False, False, True)
    main(False,True, False)

test()
