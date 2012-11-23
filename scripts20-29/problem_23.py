'''

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known 
that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

def factor(n):
    result=[] 
    limit = n ** 0.5
    i = 1
    while i <= limit:
        if n % i == 0:
            result.append(i)
            result.append(n/i)
        i += 1
    return sorted(set(result))


def find_abundunts(limit):
    abundunts = []
    for num in xrange(1, limit+1):
        factors = factor(num)
        sum_of_factors = sum(factors[:-1]) 
        if sum_of_factors > num:
            abundunts.append(num)
    return abundunts

def main():
    limit = 28123
    abundunts = set()
    total = 0
    for num in xrange(1, limit+1):
        print num
        factors = factor(num)
        sum_of_factors = sum(factors[:-1]) 
        if sum_of_factors > num:
            abundunts.add(num)
        if not any( (num-a in abundunts) for a in abundunts):
            total += num
            
    return total


if __name__ == '__main__':
    total = main()
    print 'sum of non abandunt numbers is : {}'.format(total)