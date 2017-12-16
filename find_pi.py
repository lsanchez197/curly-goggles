# Enter a number and have the program generate PI up to that many decimal
# places. Keep a limit to how far the program will go.
#
# GitHub: https://github.com/karan/Projects-Solutions/blob/master/README.md
#
# Lacey Sanchez


import math


def find_pi_to_nth_digit(n):
    '''
    '''
    if n > 15:
        raise ValueError("digit n must be less than or equal to 15")
    return float(str(math.pi)[:2 + n])
