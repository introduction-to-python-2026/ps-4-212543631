def split_before_each_uppercases(formula):
    start = 0
    split_formula = []
    for i in range(1,len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start = i
    if formula != "":
        split_formula.append(formula[start:])
    return split_formula


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
