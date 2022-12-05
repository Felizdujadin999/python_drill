user_input = input("Enter list of numbers: ")
divide = (user_input.split(","))
length = len(divide)
out_come: str = "It is unique....."
for count in range(0, length, 1):
    for count_two in range(0, length, 1):
        if divide[count] == divide[count_two] and divide.index(divide[count]) != count_two:
            out_come = "it is not unique......"

print(out_come)
