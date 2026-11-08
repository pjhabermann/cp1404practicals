"""
CP1404 Prac 4
"""


def main():
    numbers = create_list_of_numbers()
    print(f"{numbers}\n")
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average number is {(sum(numbers)) / len(numbers)}")
    print()


def create_list_of_numbers():
    input_number_counter = 5
    numbers = []
    for i in range(input_number_counter):
        number_input = int(input("Number: "))
        numbers.append(number_input)
    return numbers


main()
