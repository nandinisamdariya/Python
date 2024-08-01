def fibonacci_series(n):
    series = [0, 1]
    while series[-1] + series[-2] < n:
        series.append(series[-1] + series[-2])
    return series

n = int(input("Generate Fibonacci series up to: "))
fib_series = fibonacci_series(n)
print(f"Fibonacci series up to {n}: {fib_series}")
