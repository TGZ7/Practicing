'''
The program will print the solution of a simple sudoku (1 unknown number per row and column) of any length, given in the form of list.

For example:
X=0
sudoku = [[2, 4, 3, X],
         [3, X, 2, 4],
         [X, 3, 1, 2],
         [1, 2, X, 3]] 
'''
def sudoku_simple(sudoku):

    total=sum(range(1,len(sudoku)+1))  # The sum of each row is calculated

    for i in range(len(sudoku)):
        s=sum(sudoku[i])
        for j in range(len(sudoku)):
            if sudoku[i][j]==X:
                sudoku[i][j]=total-s   # Replace each X with the correct number
        print(sudoku[i])
  
