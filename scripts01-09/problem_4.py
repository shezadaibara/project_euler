# Problem 4
'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def is_palindrome(N):
    R = N[::-1]
    if N == R:
        return True
    else:
        return False


def main():
    palindromes = {}
    for i in xrange(999, 100, -1):
        for j in xrange(999, 100, -1):
            if is_palindrome(str(i * j)):
                palindromes.update({i * j: (i, j)})
    max_p = max(palindromes.keys())
    return palindromes.get(max_p), max_p
    
if __name__ == "__main__":
    num, prod = main()
    print "{} * {} = {} ".format(num[0], num[1], prod)
    print " {} is a palindrome ".format(prod)
