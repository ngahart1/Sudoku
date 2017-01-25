import sys
import time

def can_have(arr, r, c):
    # given the sudoku arr, and the location
    # (r,c) of the cell in question, return 
    # a list of all possible values that cell
    # can hold
    
    can_hold = range(1,10)

    # first, check all elements in the column
    # remove from can_hold if found in column
    for i in range(9):
        here = arr[i, c]
        if here in can_hold:
            can_hold.remove(here)

    # next, check all elements in the row
    # remove from can_hold if found in row
    for j in range(9):
        here = arr[r, j]
        if here in can_hold:
            can_hold.remove(here)
    
    # lastly, remove from can_hold all values
    # present in the same box as cell of interest
    # box_row is 0 if in top row of boxes, etc
    box_row = r // 3
    box_col = c // 3
    for i in range(3 * box_row, 3 + 3 * box_row):
        for j in range(3 * box_col, 3 + 3 * box_col):
            here = arr[i, j]
            if here in can_hold:
                can_hold.remove(here)
    
    return can_hold


# candidate checking method: looks through all non-solved
# cells, and checks to see if there is only one possible
# value that can be put there
# -1 is the "code" for an unsolved cell
def candidate_check(puzzle):
    while True:
        switched = False
        for r in range(0,9):
            for c in range(0,9):
                if puzzle[r,c] == -1:
                    possible = can_have(puzzle, r, c)
                    if len(possible) == 1:
                        puzzle[r,c] = possible[0]
                        switched = True
        if (not switched):
            return puzzle

def placefinder_sudoku(arr):
    #check all rows
    check=1;
    counter=0;
    index=-1;
    
    for i in range(9):
        while (check < 10):
            for j in range(9):
                #check can have
                if arr[i][j]==-1:
                    pos=can_have(arr, i, j)
                    nums=len(pos)
                    for c in range(nums):
                        if pos[c]==check:
                            counter+=1
                            index=j
                          
            if counter == 1:
                arr[i][index]=check
            check+=1
            counter = 0
            index = -1
        check=1
    
    #check all columns
    for j in range(9):
        while (check < 10):
            for i in range(9):
                #check can have
                if arr[i][j]==-1:
                    pos=can_have(arr, i, j)
                    nums=len(pos)
                    for c in range(nums):
                        if pos[c]==check:
                            counter+=1
                            index=i
  
                          
            if counter == 1:
                arr[index][j]=check
            check+=1
            counter = 0
            index = -1
        check=1
    


    #check boxes
    # box_row is 0 if in top row of boxes, etc
    r=0
    c=0
    while (c<9):
        while (r<9):
            while (check < 10):
                for i in range(r, 2 + r):
                    for j in range(c, 2 + c):
                        if arr[i][j]==-1:
                            pos=can_have(arr, i, j)
                            nums=len(pos)
                            for c in range(nums):
                                if pos[c]==check:
                                    counter+=1
                                    indexi=i
                                    indexj=j
                if counter == 1:
                    arr[indexi][indexj]=check
                check+=1
                counter=0;indexi=-1;indexj=-1;
            r+=3
        c+=3

    return arr
        
# returns true if the sudoku puzzle is solved. Otherwise,
# returns false
def solved(puzzle):
    for r in range(0,9):
        for c in range(0,9):
            if puzzle[r,c] == -1:
                return False
    return True


# Solves the sudoku!
def sudoku_solver(puzzle):
    if not(puzzle.shape == (9,9)):
        print('puzzle must be 9x9!')
        sys.exit()
    while (not solved(puzzle)):
        puzzle = candidate_check(puzzle)
        print 'Candidate check: '
        grid_print(puzzle)
        puzzle = placefinder_sudoku(puzzle)
        print 'Placefinder:'
        grid_print(puzzle)
    return puzzle

# Reads the sudoku from the file, creates an
# array where -1 is coded for unsolved cells
def solve_from_file():
    from numpy import zeros
    puzzle = zeros((9, 9), dtype = int)
    f = open('puzzle2.txt', 'r')
    counter = 0
    for line in f:
        spl = line.split()
        for i in range(len(spl)):
            if spl[i] == '_':
                puzzle[counter][i] = -1
            else:
                puzzle[counter][i] = spl[i]
        counter += 1
    f.close()
    return puzzle


# prints a 2-D array representing a sudoku
def grid_print(arr):
    for r in range(9):
        for c in range(9):
            if arr[r][c] == -1:
                print '_',
            else:
                print arr[r][c],
        print ''
    print ''

if __name__ == "__main__":
    puzzle = solve_from_file()
    print 'Puzzle from websudoku.com: '
    grid_print(puzzle)
    print ''
    solved = sudoku_solver(puzzle)
    print 'Solved puzzle:'
    grid_print(solved)
