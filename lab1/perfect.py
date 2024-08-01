def is_perfect_number(n):
    return sum([i for i in range(1, n) if n % i == 0]) == n

num = int(input("Enter a number to check if it is a perfect number: "))
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
