def prod(a,b):
    # TODO change output to the product of a and b
    output = a * b
    return output

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        n = output
        i += 1
        
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120


"""
Exercise 2
In the next exercise, you will write a function that checks sudoku squares for correctness.

Sudoku is a logic puzzle where a game is defined by a partially filled 9 x 9 square of digits where each square contains one of the digits 1, 2, 3, 4, 5, 6, 7, 8, 9. For this question we will generalize and simplify the game.

Define a procedure, check_sudoku, that takes as input a square list of lists representing an n x n sudoku puzzle solution and returns the boolean True if the input is a valid sudoku square and returns the boolean False otherwise.

A valid sudoku square satisfies these two properties:

Each column of the square contains each of the whole numbers from 1 to n exactly once.

Each row of the square contains each of the whole numbers from 1 to n exactly once.

You may assume that the input is square and contains at least one row and column.
"""

# An example solution for the check_sudoku() function

def check_sudoku(square):
    for row in square:
        # Create a list with the integers 1, 2, ..., n.
        # We will check that each number in the row is in the list
        # and remove the numbers from the list once they are verified
        # to ensure that each number only occurs once in the row.
        check_list = list(range(1, len(square[0]) + 1))
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
    for n in range(len(square[0])):
        # We do the same here for each column in the square.
        check_list = list(range(1, len(square[0]) + 1))
        for row in square:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])
    return True