def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

number = int(input("Enter a number to generate its multiplication table: "))
multiplication_table(number)
