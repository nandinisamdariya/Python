def rem_duplicates_sort(s):
    words = set(s.split())
    sorted_words = sorted(words)
    return ' '.join(sorted_words)

input_string = input("Enter a sequence of words: ")
print(rem_duplicates_sort(input_string))
