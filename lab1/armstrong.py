def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    return sum([int(digit) ** num_len for digit in num_str]) == n

num = int(input("Enter a number to check if it is an Armstrong number: "))
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
