count = 0
largest = 0
smallest = float("+inf")
second_largest = 0
while count < 5:
    num = int(input("Give me a number:"))
    if num > largest:
        second_largest = largest
        largest = num
    if num < smallest:
        smallest = num

    count += 1

print()
print("the largest number is", largest)
print("the smallest number is", smallest)
print("the second largest number is", second_largest)
print("Thanks for using my small app")