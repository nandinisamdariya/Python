def sort_words(input_string):
    words = input_string.split(',')
    sorted_words = sorted(words)
    return ','.join(sorted_words)

input_string = input("Enter a comma-separated sequence of words: ")
print(sort_words(input_string))
