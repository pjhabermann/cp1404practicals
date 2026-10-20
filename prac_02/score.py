"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = categorise_score(score)
    print(result)

    if result == "Excellent":
        print("You Get a prize!\n")

    random_score = round(random.uniform(0,100), 2)
    random_result = categorise_score(random_score)
    print(f"Random: {random_score} = {random_result}")

def categorise_score(score: float) -> str:
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()