name = "felizdujadin"
age = 20

# s = "{0} is {1:10.1f} years old, and {0} loves {2}".format(name, age, "precious")
s = f"{name:#^20} is {age} years old, and {name} loves precious"
print(s)

hello = "Hello Felizdujadin, nice to meet you."
for index, letter in enumerate(hello, start=1):
    print(f"{letter} ----> {index}")

    for i in range(1, 20, 2):
        s = "*" * i
        print(f"{s:20}{s:^20}{s:>20}")
