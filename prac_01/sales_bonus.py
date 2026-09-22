"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Global Variables
BONUSRATE_LOW = 0.1
BONUSRATE_HIGH = 0.15

sales = float(input("Enter sales: $"))

if sales < 1000:
    Bonus = (BONUSRATE_LOW + 1) * sales

else:
    Bonus = (BONUSRATE_HIGH + 1) * sales


print(f"Your bonus: ${Bonus:.2f}")