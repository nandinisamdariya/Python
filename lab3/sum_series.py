def compute_series_sum(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum -= 1 / i
        else:
            sum += 1 / i
    return sum

n = int(input("Enter a positive integer: "))
print(compute_series_sum(n))
