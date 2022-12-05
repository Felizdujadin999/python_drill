for f in range(1, 101):
    if f % 15 == 0:
        print(f, "Fizzbuzz")
    elif f % 5 == 0:
        print(f, "Fizz")
    elif f % 3 == 0:
        print(f, "Buzz")
    else:
        print(f)
