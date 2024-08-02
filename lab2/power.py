def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    else:
        result = 1
        for _ in range(exp):
            result *= base
        return result

base = float(input("Enter base number: "))
exp = int(input("Enter exponent: "))
print(f"{base} to the power of {exp} is: {power(base, exp)}")
