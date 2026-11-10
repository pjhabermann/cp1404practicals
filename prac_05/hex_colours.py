COLOUR_TO_HEX = {
    "Dark Green": "#006400", "Dartmouth Green": "#00703c", "Deep Cerise": "#da3287", "Deep Champagne": "#fad6a5",
    "Deep Fuchsia": "#c154c1", "Deep Jungle Green": "#004b49", "Deep Peach": "#ffcba4", "Deep Saffron": "#ff9933",
    "Deep Space Sparkle": "#4a646c", "Deep Chestnut": "#b94e48"
}


def main():
    colour_name = input("Enter colour name: ").title()
    while colour_name != "":
        try:
            print(f"The Hex of {colour_name} is {COLOUR_TO_HEX[colour_name]}\n")
        except KeyError:
            print("Enter a correct colour!\n")
        colour_name = input("Enter colour name: ").title()


main()
