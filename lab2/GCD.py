import math

def gcd(x, y):
    return math.gcd(x, y)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"GCD of {x} and {y} is {gcd(x, y)}")
