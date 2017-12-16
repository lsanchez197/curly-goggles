# Takes in a credit card number from a common credit card vendor (Visa,
# MasterCard, American Express, Discover) and validates it to make sure that
# it is a valid number (hecksum).
#
# GitHub: https://github.com/karan/Projects-Solutions/blob/master/README.md
#
# Lacey Sanchez


def is_valid_card_number(card_number):
    '''
    Inputs: (integer) credit card number

    Returns: (boolean) True if valid, False if not
    '''
    num_list = [int(n) for n in str(card_number)]
    num_list.reverse()
    card_sum = 0
    for i in range(len(num_list)):
        if i % 2 != 0:
            num_list[i] *= 2
            if num_list[i] >= 10:
                digits = [int(n) for n in str(num_list[i])]
                for d in digits:
                    card_sum += d
            else:
                card_sum += num_list[i]
        else:
            card_sum += num_list[i]
    if card_sum != 0 and card_sum % 10 == 0:
        return True
    return False


# Valid Card Number: 1234567890123452