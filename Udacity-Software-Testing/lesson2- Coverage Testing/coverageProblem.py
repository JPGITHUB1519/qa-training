# CORRECT SPECIFICATION:
#
# isPrime checks if a positive integer is prime.
#
# A positive integer is prime if it is greater than 
# 1, and its only divisors are 1 and itself.
#
# TASKS:
#
# 1) Add an assertion to test() that shows
#    isPrime(number) to be incorrect for 
#    some input.
#
# 2) Write isPrime2(number) to correctly 
#    check if a positive integer is prime.

# Note That the Test Coverage is 100% do not mean that the code is well tested, it only analyzes that all the code runscor

import math

def isPrime(number):
    ###Your isPrime2 code here.
    if number == 2:
        return True
    if number<=1 or (number%2)==0:
        return False
    for check in range(3, number - 1):  
        if (number%check) == 0:  
            return False
    return True

def isPrime2(number):  
    ###Your isPrime2 code here.
    if number == 2:
        return True
    if number<=1 or (number%2)==0:
        return False
    for check in range(3, number - 1):  
        if (number%check) == 0:  
            return False
    return True

def test():
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(20) == False
    assert isPrime(21) == False
    assert isPrime(22) == False
    assert isPrime(23) == True
    assert isPrime(24) == False
    # personals assertions
    assert isPrime(9) == False
    assert isPrime(25) == False
    assert isPrime(15) == False
    ###Your test code here.

    pass


test()


# for i in range(1, 100):
#     if(isPrime(i) == True):
#         print "i : " + str(i) + "    " + str(isPrime(i))

# 9 is not prime
# 15 is not prime
# 25 is not prime

