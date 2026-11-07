from prac_06.programming_language import ProgrammingLanguage


def main():
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)

    print(f"{java}\n {c_plus_plus}\n {python}\n {visual_basic}\n {ruby}\n")

    languages = (java, c_plus_plus, python, visual_basic, ruby)
    print("The dynamically typed languages are")
    for language in languages:
        if language.reflection:
            print(language.name)


main()
