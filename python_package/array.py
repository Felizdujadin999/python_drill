def outlier(array):
    odd_num = sum(digit % 2 for digit in array[:3])
    remove = int(odd_num < 2)
    return next(digit for digit in array if digit % 2 == remove)


print(outlier([2, 4, 6, 7, 8, 10]))
