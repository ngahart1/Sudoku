import sys

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
    for i in range(3 * box_row, 2 + 3 * box_row):
        for j in range(3 * box_col, 2 + 3 * box_col):
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
                        print 'puzzle[%d,%d] is %d' % (r,c,possible[0])
                        puzzle[r,c] = possible[0]
                        switched = True
        if (not switched):
            return


def sudoku_solver(puzzle):
    if not(puzzle.shape == (9,9)):
        print('puzzle must be 9x9!')
        sys.exit()


def solve_from_file():
    from numpy import zeros
    puzzle = zeros((9, 9), dtype = int)
    f = open('puzzle.txt', 'r')
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

def grid_print(arr):
    # prints a 2-D array representing a sudoku
    for r in range(9):
        for c in range(9):
            if arr[r][c] == -1:
                print '_',
            else:
                print arr[r][c],
        print ''

if __name__ == "__main__":
    puzzle = solve_from_file()
    grid_print(puzzle)
    grid_print(candidate_check(puzzle))
    #solution = sudoku_solver(puzzle)
    #array_print(solution)
