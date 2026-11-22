def count_words(text):
    text_list = text.split()
    return len(text_list)

def count_characters(text):
    return len(text)

def count_vowels(text):
    count = 0
    text = text.lower()
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    for letter in text:
        if letter in vowels_list:
            count += 1
    return count

def text_analyzer():
    tests = ["Hello", "Education", "PYTHON", "AEIOU", "xyz", ""]
    for val in tests:
        print(count_vowels(val))

text_analyzer()