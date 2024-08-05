def display_table(m):
    for i in range(1, m+1):
        print(f"{i} {1} {i} {i**2} {i**3}")

m = int(input("Enter the number of rows: "))
display_table(m)
