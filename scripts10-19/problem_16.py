#Problem 16
'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def main(power):
    return sum([int(x) for x in str(2 ** power)])

if __name__ == "__main__":
    result = main(1000)
    print 'the sum is {}'.format(result)