#Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


def calc_sum(n):
    total = 0
    for n in xrange(0, n):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    return total

if __name__ == '__main__':
    total = calc_sum(1000)
    print total
