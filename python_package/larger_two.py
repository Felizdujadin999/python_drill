count = 0

largest = 0
second_largest = 0

while count < 3:
    num = int(input("Enter a number:"))
    if num > largest:
        second_largest = largest
        largest = num

    elif (num > second_largest) and (num < largest):
        second_largest = num

    count += 1

print()
print("the largest number is", largest)
print("the second largest is", second_largest)

