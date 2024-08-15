def count_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char, count in char_count.items():
        print(f"{char},{count}")

s = input("Enter a string: ")
count_char(s)
