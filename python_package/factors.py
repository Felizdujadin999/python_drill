user_input = int(input("Enter a number:"))
count = 1
counter = 0
while count <= user_input:
    if (user_input % count == 0):
        counter += 1
    count += 1
print(counter, " Factors")
print("Thanks for using my small app")
