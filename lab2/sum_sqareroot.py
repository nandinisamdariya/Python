import math

def sum_of_square_roots(a, b, c):
    return math.sqrt(a) + math.sqrt(b) + math.sqrt(c)

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
print("Sum of square roots:", sum_of_square_roots(a, b, c))
