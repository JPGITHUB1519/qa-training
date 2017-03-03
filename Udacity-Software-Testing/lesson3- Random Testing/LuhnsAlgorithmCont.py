# concise definition of the Luhn checksum:
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.htm
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
# 
# Implement the Luhn Checksum algorithm as described above.

# is_luhn_valid takes a credit card number as input and verifies 
# whether it is valid or not. If it is valid, it returns True, 
# otherwise it returns False.


def numberToList(num):
    lst = [int(i) for i in str(num)]
    return lst


def is_luhn_valid(n):
    sum = 0
    numbers = numberToList(n)
    if(len(numbers) % 2 == 0):
        for i in range(0, len(numbers)):
            num = numbers[i]
            # if the position is odd
            if((i + 1) % 2 != 0):
                num = num * 2
                print num
                if(num <= 9 and num >= 0):
                    sum += num
                else:
                    sum += (num - 9)
        # if is modulo of 10
        return sum % 10 == 0
    else:
        for i in range(0, len(numbers)):
            num = numbers[i]
            # if the position is odd
            if((i + 1) % 2 == 0):
                num = num * 2
                if(num <= 9 and num >= 0):
                    sum += num
                else:
                    sum += (num - 9)
        # if is modulo of 10
        return sum % 10 == 0

print is_luhn_valid(7992739871)