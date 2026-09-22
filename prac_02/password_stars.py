"""Convert Password to Asterisks """

MIN_NUMBER_OF_CHARACTERS = 4

def main():

    password = get_password()

    print_stars(password)


def print_stars(password: str):
    print("*" * len(password))
    print("where the length is: ", len(password))


def get_password() -> str:
    password = input("Input Password Here: ")
    while MIN_NUMBER_OF_CHARACTERS > len(password):
        password = input("Passwords too Short, Try Again Here: ")
    return password


main()