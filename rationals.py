def make_rat(num, denom):
    if num < 0 and denom < 0 or num > 0 and denom < 0:
        return (-1 * num, -1 * denom)
    else:
        return (num, denom)

def get_denom(rat):
    return rat[1]

def get_num(rat):
    return rat[0]

def print_rat(rat):
    print(str(get_num(rat)) + " / " + str(get_denom(rat)))

one_third = make_rat(1,-3)
print_rat(one_third)