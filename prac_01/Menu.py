# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message

MENU_CHOICES = ["(H)ello", "(G)oodbye", "(Q)uit"]

user_name = input("Enter Name: ")

    # for option in CHOICE:
    #     print(option)

print("\n" .join(MENU_CHOICES))

user_choice = input(">>>").upper()

while user_choice != "Q":
    if user_choice == "H":
        print(f"Hello {user_name}")
    elif user_choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid choice")

    user_choice = input(">>>").upper()
