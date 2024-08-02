def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

n = int(input("Enter the range: "))
print(f"Sum of natural numbers up to {n} is: {sum_of_natural_numbers(n)}")
