# The factorial of a positive integer n is defined as the product of the
# sequence , n-1, n-2, ...1 and the factorial of 0 is defined as being 1. Solve
# this using both loops and recursion.
#
# https://github.com/karan/Projects-Solutions/blob/master/README.md
#
# Lacey Sanchez


# Recursion
def find_factorial_rec(n):
    if n == 0:
        return 1
    return n * find_factorial_rec(n - 1)


# Loops
def find_factorial_loop(n):
    '''
    '''
    if n == 0:
        return 1
    elif n >= 1 and type(n) == int:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial