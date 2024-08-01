def special_numbers():
    special_numbers = []
    for i in range(1000, 2001):
        if i % 7 == 0 and i % 5 != 0:
            special_numbers.append(i)
    return special_numbers

special_numbers = special_numbers()
print("Numbers divisible by 7 but not a multiple of 5 between 1000 and 2000:", special_numbers)
