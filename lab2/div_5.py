def is_divisible_by_5(n):
    return n % 5 == 0

number = int(input("Enter a number: "))
if is_divisible_by_5(number):
    print(f"{number} is divisible by 5")
else:
    print(f"{number} is not divisible by 5")
