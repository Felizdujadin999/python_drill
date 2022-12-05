number_to_guess = 55
guess = int(input("Enter a number  :"))
number_of_guesses = 0

while number_of_guesses < 3:
    if guess == number_to_guess:
        print("You got it right.")
        break

    else:
        if guess < number_to_guess:
            print("Number is lesser, try again")
        elif guess > number_to_guess:
            print("Number is greater, try again")
        guess = int(input("Enter a number:"))
    number_of_guesses += 1
if number_to_guess != guess:
    print("Sorry, you couldn't guess", number_to_guess)
