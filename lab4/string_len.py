def string_len(s):
    length = len(s)
    
    substring = 'country' in s
    

    words = s.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return length, substring, word_count

s = input("Enter a string: ")
length, country_found, word_count = string_len(s)
print(f"Length of string: {length}")
print(f"Is 'country' found?: {country_found}")
print("Word occurrences: ", word_count)
