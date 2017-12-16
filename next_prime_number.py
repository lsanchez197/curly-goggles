# Find prime numbers until the user chooses to stop asking for the next one.
#
# GitHub: https://github.com/karan/Projects-Solutions/blob/master/README.md
#
# Lacey Sanchez


import math


# Function method
def find_prime_numbers(starting_number=2, ending_number=math.inf):
    '''
    '''
    if type(starting_number) != int:
        starting_number = int(starting_number) + 1

    if starting_number == 2 and starting_number <= ending_number:
        print(starting_number)
        starting_number = starting_number + 1

    while starting_number <= ending_number:
        upper_bound = starting_number / 2
        if type(upper_bound) != int:
            upper_bound = int(upper_bound) + 1

        if upper_bound >= 2:
            is_prime = True
            for i in range(2, upper_bound):
                if starting_number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(starting_number)
        starting_number += 1


# Class method
class PrimeNumber:
    '''
    '''
    def __init__(self, starting_number=2):
        '''
        '''
        if type(starting_number) != int:
            self.starting_number = int(starting_number) + 1
        else:
            self.starting_number = starting_number
        self.prime = self.next()


    def next(self):
        '''
        '''
        if self.starting_number == 2:
            self.prime = 2
            self.starting_number = 3
            return self.prime

        no_prime = True
        while no_prime:
            upper_bound = self.starting_number / 2
            if type(upper_bound) != int:
                upper_bound = int(upper_bound) + 1

            if upper_bound >= 2:
                is_prime = True
                for i in range(2, upper_bound):
                    if self.starting_number % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    self.prime = self.starting_number
                    no_prime = False
            self.starting_number += 1
        return self.prime