def convertTo8BitBinary(n):
    return list('{0:08b}'.format(n))

a0, a1, a2, a3, a4, a5, a6, a7 = convertTo8BitBinary(100)

print a5

