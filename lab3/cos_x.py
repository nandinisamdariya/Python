import math

def cos_x(x, n):
    cosine = 0
    for i in range(n):
        sign = (-1)**i
        cosine += sign * (x**(2*i)) / math.factorial(2*i)
    return cosine

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
print(cos_x(x, n))
