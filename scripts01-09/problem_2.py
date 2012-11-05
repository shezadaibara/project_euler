#Problem 2

'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''


def fibo():
    a, b = 1, 2
    while 1:
        yield a
        a, b = b, a + b


def main():
    total = 0
    fib = fibo()
    while 1:
        num = fib.next()
        
        if num >= 4000000:
            break
        
        if num % 2 == 0:
            total += num
            
    return total

if __name__ == '__main__':
    
    total = main()
    print total