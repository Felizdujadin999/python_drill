number = int(input("Enter a number: "))
factor = 1
sum_of_factors = 0
while factor < number:
    if number % factor == 0:
       print(factor)

       sum_of_factors += factor

    factor += 1

if sum_of_factors < number:
    print(number, "is deficient")
elif sum_of_factors > number:
    print(number, "is abundant")
else:
    print(number, "is a perfect number")

