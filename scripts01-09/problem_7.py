#Problem 7
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
'''


def calculatePrime():
    try:
        num = 9
        prime_numbers = [2, 3, 5, 7]
        count = 4
        
        while True:
            for p in prime_numbers:
                if num % p == 0:
                    num += 2
                    break
                else:
                    continue
            else:
                prime_numbers.append(num)
                count += 1
                if count % 1000 == 0:
                    print count
                if count == 10001:
                    print num, count, len(prime_numbers)
                    break
                num += 2
            
    except Exception:
        return count

if __name__ == "__main__":
    res = calculatePrime()
    print res
