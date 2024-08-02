def series(n):
    result = [1]
    for i in range(1, n):
        result.append(result[-1] * i)
    return result

terms = int(input("Enter number of terms: "))
print(f"Series up to {terms} terms:", series(terms))
