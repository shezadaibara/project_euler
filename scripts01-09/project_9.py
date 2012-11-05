#Problem 9
'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
from Queue import Queue


#brute force method
def main():
    '''
        since a + b + c = 1000,
        1 : a and b cannot be greater than 500
        2 : c = 1000 - b - a
    '''
    for a in xrange(1, 500 + 1):
        for b in xrange(1, 500 + 1):
            c = 1000 - b - a
            if a * a + b * b == c * c:
                return a, b, c
            

# alternate method of by finding Pythagorean Triples:
def plato_triplets():
    # Plato's formula for Pythagorean Triples:
    #(2m)^2 + (m^2 - 1)^2 = (m^2 + 1)^2
    m = 2
    
    while m < 500:
        a = 2 * m
        b = (m ** 2) - 1
        c = (m ** 2) + 1
        yield a, b, c
        
        if a + b + c > 1000:
            #this will raise a typeError
            yield
        else:
            m += 1
            

def associative_triplets(a, b, c):
    '''
    for a Pythagorean Triple say 3, 4, 5:
    
    3*n, 4*n, 5*n is also a Pythagorean Triple, for all n belong to N
    '''
    mul_counter = 1
    while a + b + c < 1000:
        yield a * mul_counter, b * mul_counter, c * mul_counter
        mul_counter += 1


def triplets():
    
    try:
        for a, b, c in plato_triplets():
            for a, b, c in associative_triplets(a, b, c):
                print a, b, c, " = ", a + b + c
                if a + b + c == 1000:
                    return a, b, c
                elif a + b + c > 1000:
                    break
                
    except TypeError:
        pass
   
   
if __name__ == "__main__":
    
    a, b, c = main()
    print "triplets: {} , product : {}".format((a, b, c), a * b * c)
    a, b, c = triplets()
    print "triplets: {} , product : {}".format((a, b, c), a * b * c)

