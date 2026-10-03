"""The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen."""

# TODO separate into function (def: main, input and check, calculate, list answer)

total_price = 0

number_of_items = int(input("How many items do you have? "))

while number_of_items <= 0:
    print("Invalid Answer, Number of items should be larger than zero")
    number_of_items = int(input("How many items do you have? "))

for i in range(number_of_items):
    item_price = float(input(f"What is the price of item {i + 1}: "))
    total_price = total_price + item_price

print(f"your total price is {total_price}!")
