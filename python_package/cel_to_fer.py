# cel = int(input("Enter a number in celsius: "))


def cel_to_fer(cel_val):
    '''
    :param cel_val: float
    :return: float

    >>> cel_to_fer(16)
    60.8
    '''
    F = cel_val * 1.8 + 32.0
    return F


print(cel_to_fer(16))
print(cel_to_fer(32))
# print(cel_to_fer(cel))
