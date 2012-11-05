#problem_5

'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
'''


def main1(N):
    '''
    Almost Brute force method
    '''
    number = N
    while 1:
        temp = []
        for i in xrange(1, N):
            if number % i == 0:
                temp.append(True)
            else:
                temp.append(False)
                break
        
        if all(temp):
            return number
        
        number += N


# Alternate method 2
def main2(N):
    i = 1
    for k in xrange(1, N):
        if i % k > 0:
            for j in xrange(1, N):
#                print 'i = {}, j= {}, k= {}'.format(i, j, k)
                if (i * j) % k == 0:
                    i *= j
                    break
    return i


# Alternate method using gcd and lcm
def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


def main3(N):
    return reduce(lcm, xrange(1, N))


if __name__ == "__main__":
    from datetime import datetime
    start = datetime.now()
    print 'start time', start
    num = main3(20)
    print 'time taken: ', datetime.now() - start
    print " {} is a the smallest positive number divisible by all of the numbers from 1 to 20. ".format(num)