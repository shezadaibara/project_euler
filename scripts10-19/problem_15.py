#Problem 15
'''
Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.


How many routes are there through a 20x20 grid?
'''
from pprint import pprint

def main(size):
    
    #create the grid
    grid = list(list(0 for y in range(size+1) ) for x in range(size+1))
    
    #initializing the first row and first col with 1
    for i in range(0, size+1):
        grid[0][i] = 1
        grid[i][0] = 1
    
    for i in range(1, size+1):
        for j in range(1, size+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
            
    
    return grid[size][size]
        
if __name__ == '__main__':
    result = main(20)
    pprint(result)
