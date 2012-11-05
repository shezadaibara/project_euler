#problem 10
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


def calculatePrime():
    try:
        num = 9
        prime_numbers = [2, 3, 5, 7]
        count = 4
        total = 0
        
        while True:
            for p in prime_numbers:
                if num % p == 0:
                    num += 2
                    break
                else:
                    continue
            else:
                
                if num < 2000000:
                    prime_numbers.append(num)
                    total += num
                    count += 1
                    if count % 10000 == 0:
                        print count, total
                        print '===========' * 4
                else:
                    break
                
                num += 2
        
        return total, count
        
    except Exception:
        print Exception
    
if __name__ == "__main__":
    result, count = calculatePrime()
    print result, count
    
    


