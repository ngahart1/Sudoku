import sys

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
    shape = arr.shape
    for r in range(shape[0]):
        for c in range(shape[1]):
            if arr[r][c] == -1:
                print '_',
            else:
                print arr[r][c],
        print ''

if __name__ == "__main__":
    puzzle = solve_from_file()
    grid_print(puzzle)
    #solution = sudoku_solver(puzzle)
    #array_print(solution)
