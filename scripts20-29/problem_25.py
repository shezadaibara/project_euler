'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''
from pprint import pprint

def fibo():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

def main():
    fib = fibo()
    term = 0
    while True:
        
        num = fib.next()
        digit_count = len(str(num))
        term += 1
#        pprint('{}=>{}'.format(term, num))
        if digit_count >= 1000:
            pprint('{}=>{}'.format(term, num))
            break

if __name__ == '__main__':
    main()
        