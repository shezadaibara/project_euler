'''
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, 
then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
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


def d(no):
    return sum(factor(no)[:-1])


def main(limit):
    '''
    Note that number like 6 whose sum of factors is the number itself is not considered amicable
    '''
    total = 0            
    for a in range(1, limit+1):
        b = d(a)
        if b > a and a == d(b):
#            print a , b
            total += a + b
    return total 
    
    
if __name__ == '__main__':
    total = main(10000)
    print 'sum of all numbers under 10000 is {}'.format(total)
            
        
        
    