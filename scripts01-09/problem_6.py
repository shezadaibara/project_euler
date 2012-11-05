#Problem 6
'''
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural number
and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
'''


def main(N):
    
    sum_of_sq = sum([x ** 2 for x in xrange(1, N + 1)])
    
    sq_of_sum = sum(xrange(1, N + 1)) ** 2
    
    differance = sq_of_sum - sum_of_sq
    
    print sum_of_sq, sq_of_sum, differance


if __name__ == "__main__":
    main(100)
