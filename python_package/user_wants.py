largest_number = float("-inf")
smallest_number = float("+inf")
yes = 1
Submit = 2
user_input = int(input("Enter a number:"))
while user_input <= 1000:
    if user_input < largest_number:
        largest_number = user_input
    if user_input < smallest_number:
        smallest_number = user_input
    user_input2 = int(input("Would you like to enter another number sir/ma?:", yes, " yes", Submit, " Submit"))
    if user_input2 == Submit:
        print(largest_number)
        print(smallest_number)
        break
    else:
        if user_input2 != yes and user_input2 != Submit:
            print("You entered a wrong number, please pick again....")
            print("Would you like to enter another number sir/ma?:", yes, Submit,)


