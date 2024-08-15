def extract_digit_words(s):
    words = s.split()
    digit_words = [word for word in words if word.isdigit()]
    return digit_words

s = input("Enter a sentence: ")
print(extract_digit_words(s))
