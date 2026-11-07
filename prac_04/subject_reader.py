"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subject_data = load_data(FILENAME)
    print(subject_data)

    display_subject_details(subject_data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    nested_list = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        details = [parts[0], parts[1], int(parts[2])]
        print(details)  # See if that worked
        print("----------")
        nested_list.append(details)
    input_file.close()

    return nested_list


def display_subject_details(details):
    for detail in details:
        print(f"{detail[0]} is taught by {detail[1]:<12} and has {detail[2]:>3}")


main()
