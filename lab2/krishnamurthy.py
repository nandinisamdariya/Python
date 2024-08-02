import math

def is_krishnamurthy_number(n):
    digits = [int(d) for d in str(n)]
    sum_of_factorials = sum(math.factorial(d) for d in digits)
    return sum_of_factorials == n

number = int(input("Enter a number to check if it is a Krishnamurthy number: "))
if is_krishnamurthy_number(number):
    print(f"{number} is a Krishnamurthy number.")
else:
    print(f"{number} is not a Krishnamurthy number.")
