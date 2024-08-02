def geometric_sequence(a, r, n):
    sequence = [a * (r ** i) for i in range(n)]
    return sequence

first_term = 3
common_ratio = 3
terms = 6
print("First 6 terms of the geometric sequence:", geometric_sequence(first_term, common_ratio, terms))
