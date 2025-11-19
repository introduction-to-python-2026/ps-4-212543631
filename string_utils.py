def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


def split_at_first_digit(formula):
    digit_location = 1
    for i in formula[1:]:
        if i.isdigit():
            prefix = formula[:digit_location]
            numeric_part = int(formula[digit_location:])
            return (prefix , numeric_part)
        digit_location += 1
    prefix = formula
    return (prefix , 1)
