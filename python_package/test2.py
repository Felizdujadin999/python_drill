number = int(input("Enter a number or press 0 to quit:"))
largest = smallest = number

while number != 0:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
    number = int(input("Enter a number or press 0 to quit:"))

print(smallest)
print(largest)