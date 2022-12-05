import string

user_input = input("Enter message to decipher: ")
key = int(input("What key would you like to use to code?: "))

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_lowercase
decoded_lower_letters = lower_letters[key:] + lower_letters[:key]
decoded_upper_letters = lower_letters[key:] + lower_letters[:key]

letters = lower_letters + upper_letters + string.whitespace
decoded_letters = decoded_lower_letters + decoded_upper_letters + string.whitespace
encoded = user_input.translate(str.maketrans(letters, decoded_letters))
decoded = encoded.translate(str.maketrans(decoded_letters, letters))

print(encoded)
print(decoded)
