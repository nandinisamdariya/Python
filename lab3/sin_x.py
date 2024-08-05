import math

def sin_x(x, n):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        sine += sign * (x**(2*i + 1)) / math.factorial(2*i + 1)
    return sine

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
print(sin_x(x, n))
