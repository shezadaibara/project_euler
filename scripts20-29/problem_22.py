'''
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical 
value for each name, multiply this value by its alphabetical position 
in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
'''

import string
import csv

def character_position(char):
    return string.uppercase.index(char.upper()) + 1


def character_sum(string):
    return sum(map(character_position, string))
               

def character_list():
    
    file = open('../tmp/names.txt', 'r')
    csv_reader = csv.reader(file, delimiter=',', quotechar='"')
    names = []
    
    for row in csv_reader:
        [names.append(x) for x in row]
    
    return sorted(names)
    

def main():
    total = 0
    names = character_list()
    for pos, name in enumerate(names):
        total += (pos + 1) * character_sum(name)  
    
    return total
     

if __name__ == '__main__':
    
    total = main()
    print 'the total of all the name scores in the file is {}'.format(total)
    
    