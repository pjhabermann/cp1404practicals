MIN_NUMBER_OF_CHARACTERS = 4

password = input("Input Password Here: ")
length_of_password = len(password)

while MIN_NUMBER_OF_CHARACTERS > length_of_password:
    password = input("Passwords too Short, Try Again Here: ")
    length_of_password = len(password)

print("*" * length_of_password)
print("where the length is: ", length_of_password)
