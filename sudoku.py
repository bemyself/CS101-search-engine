#THREE GOLD STARS

#Sudoku [http://en.wikipedia.org/wiki/Sudoku]
#is a logic puzzle where a game
#is defined by a partially filled
#9 x 9 square of digits where each square
#contains one of the digits 1,2,3,4,5,6,7,8,9.
#For this question we will generalize
#and simplify the game.


#Define a procedure, check_sudoku,
#that takes as input a square list
#of lists representing an n x n
#sudoku puzzle solution and returns
#True if the input is a valid
#sudoku square and returns False
#otherwise.

#A valid sudoku square satisfies these
#two properties:

#   1. Each column of the square contains
#       each of the numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the numbers from 1 to n exactly once.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4,5],
             [2,4,1,3,3],
             [4,1,2,3,5],
             [2,3,1,4,5],
             [1,5,4,3,1]]


def check_sudoku(p):
    n = len(p)
    cnt = 0
    for i in range(n):
        for item in range(1, n+1):
            if item in p[i]:
                cnt += 1
    if cnt == n ** 2:
        return True
    else:
        return False
        
print check_sudoku(correct)
print check_sudoku(incorrect)
    
