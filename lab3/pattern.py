def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(" / \\")
            print("/___\\" * (j + 1))

n = int(input("Enter the number of lines: "))
print_pattern(n)
