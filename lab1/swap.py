def swap_numbers(a, b):
    return b, a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = swap_numbers(a, b)
print(f"After swapping: a = {a}, b = {b}")
