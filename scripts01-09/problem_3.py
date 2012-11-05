#Problem 3
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


def factor(n):
        if n == 1:
            return [1]
        i = 2
        limit = n ** 0.5  # taking sqrt of the number
        
        while i <= limit:
            if n % i == 0:
                result = factor(n / i)
                result.append(i)
                return result
            i += 1

        return [n]


def main(number):
    pf = factor(number)
    print "Factors for {} : {}".format(number, str(pf))
    print "Height prime factor of {} : {}".format(number, str(pf[0]))


if __name__ == "__main__":
        N = 600851475143
        main(N)
