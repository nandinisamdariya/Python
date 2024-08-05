def print_pattern(n):
    print(".")
    for i in range(n-2):
        print("/ \\")
    print("/" + "_" * (n-1) + "\\")

print_pattern(2)
print_pattern(3)
print_pattern(4)
