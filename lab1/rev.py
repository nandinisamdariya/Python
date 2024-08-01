def rev_number(n):
    return int(str(n)[::-1])

num = int(input("Enter a number:"))
reversed_number = rev_number(num)
print(f"The reverse of {num} is {reversed_number}")
