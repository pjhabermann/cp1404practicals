"""
Word Occurrences
Estimate: 40 mins
Actual:
"""

def main():


    text = input("Input text to be counted here: ")
    print(count_word_frequency(text))



def count_word_frequency(text):
    text_to_frequency = {}
    words = text.lower().split()
    for word in words:
        text_to_frequency[word] = text_to_frequency.get(word, 0) + 1
    return text_to_frequency







main()
