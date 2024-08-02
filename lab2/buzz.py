def is_buzz_number(n):
    return n % 7 == 0 or str(n).endswith('7')

number = int(input("Enter a number: "))
if is_buzz_number(number):
    print(f"{number} is a Buzz number")
else:
    print(f"{number} is not a Buzz number")
