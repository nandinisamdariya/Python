def check_positive_negative():
    number = float(input("Enter a number: "))
    if number > 0:
        print(f"{number} is positive")
    elif number < 0:
        print(f"{number} is negative")
    else:
        print(f"{number} is zero")

check_positive_negative()
