def decimal_to_binary(n):
    return bin(n).replace("0b", "")

number = int(input("Enter a decimal number: "))
print(f"Binary representation of {number} is: {decimal_to_binary(number)}")
