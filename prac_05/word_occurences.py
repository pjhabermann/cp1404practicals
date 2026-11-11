"""
Word Occurrences
Estimate: 40 mins
Actual: so far 1 hour and 25mins
"""


def main():
    # text = input("Input text to be counted here: ")
    text = "this is a collection of words of nice words this is a fun thing it is"
    word_to_frequency = count_word_frequency(text)
    display_frequency_in_columns(word_to_frequency)


def count_word_frequency(text):
    word_to_frequency = {}
    words = text.lower().split()
    for word in words:
        word_to_frequency[word] = word_to_frequency.get(word, 0) + 1
    return word_to_frequency


def display_frequency_in_columns(word_to_frequency):
    print(word_to_frequency)
    width = [len(word) for word in word_to_frequency.keys()]
    for word in sorted(word_to_frequency.keys()):
        print(f"{word:{max(width)}} : {word_to_frequency[word]}")


main()
