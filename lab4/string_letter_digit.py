def count_letters_digits(s):
    letters = sum(c.isalpha() for c in s)
    digits = sum(c.isdigit() for c in s)
    return letters, digits

s = input("Enter a sentence: ")
letters, digits = count_letters_digits(s)
print(f"LETTERS {letters}")
print(f"DIGITS {digits}")
