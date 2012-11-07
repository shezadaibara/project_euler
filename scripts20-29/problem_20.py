#Problem 20
'''
'''

if __name__ == '__main__':
    result = sum([int(x) for x in str(reduce(mul, range(1, 101)))])
    print 'the sum of 100! is {}'.format(result)  