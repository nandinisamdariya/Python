def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
    
base = float(input("Enter base number: "))
exp = int(input("Enter exponent: "))
print(f"{base} to the power of {exp} is: {power(base, exp)}")
