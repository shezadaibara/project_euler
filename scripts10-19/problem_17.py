#problem 17

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) 
inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" 
when writing out numbers is in compliance with British usage.'''


numbers = {
           0:'',
           1:'one',
         2:'two',
         3:"three",
         4:"four",
         5:'five',
         6:'six',
         7:'seven',
         8:'eight',
         9:'nine',
         
         10:'ten',
         11:'eleven',
         12:'twelve',
         13:'thirteen',
         14:'fourteen',
         15:'fifteen',
         16:'sixteen',
         17:'seventeen',
         18:'eighteen',
         19:'nineteen',
         
         20:'twenty',
         30:'thirty',
         40:'forty',
         50:'fifty',
         60:'sixty',
         70:'seventy',
         80:"eighty",
         90:'ninety',
         
         100:'hundred',
         1000:'thousand'
         
         }


def getWords(no, word=''):
    if no in numbers.iterkeys() and no not in [100, 1000]:
        word += numbers[no]
        return word
    if no > 20 and no < 100:
        tens = no/10 * 10
        units = no%10
        word += getWords(tens, word) + numbers[units]
        return word
    if no >= 100 and no < 1000:
        hun = no/100
        rest = no%100
        if rest:
            word += getWords(hun, word) + numbers[100] + 'and' + getWords(rest, word)
        else:
            word += getWords(hun, word) + numbers[100]
             
        return word
    
    if no >= 1000 and no < 100000:
        thou = no/1000
        rest = no%1000
        print thou, rest
        if rest:
            word += getWords(thou) + numbers[1000] + getWords(rest, word)
        else:
            word += getWords(thou) + numbers[1000]
            
        return word

def main(limit):
    total_count = 0
    for no in xrange(1, limit+1):
        word = getWords(no)
        print '{}:{}'.format(no, word)
        total_count += len(word)
    print total_count

if __name__ == '__main__':
    main(1000)
#    print getWords(1000)
        