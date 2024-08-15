def string_operation(s, specific_substring="", other_string=""):
    # 1. Reverse the string
    reversed_s = s[::-1]
    
    # 2. Check if palindrome
    is_palindrome = s == reversed_s
    
    # 3. Check if it ends with specific substring
    ends_with_substring = s.endswith(specific_substring)
    
    # 4. Capitalize first letter of each word
    capitalized = s.title()
    
    # 5. Check if two strings are anagrams
    is_anagram = sorted(s.replace(" ", "")) == sorted(other_string.replace(" ", ""))
    
    # 6. Remove vowels from the string
    vowels = "aeiouAEIOU"
    no_vowels = ''.join([c for c in s if c not in vowels])
    
    # 7. Find the length of the longest word in a sentence
    words = s.split()
    longest_word_length = len(max(words, key=len))
    
    return {
        'reversed': reversed_s,
        'is_palindrome': is_palindrome,
        'ends_with_substring': ends_with_substring,
        'capitalized': capitalized,
        'is_anagram': is_anagram,
        'no_vowels': no_vowels,
        'longest_word_length': longest_word_length
    }

s = input("Enter a string: ")
specific_substring = input("Enter a specific substring to check: ")
other_string = input("Enter another string to check anagram: ")

results = string_operation(s, specific_substring, other_string)
for key, value in results.items():
    print(f"{key}: {value}")
