import cmath

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return root1, root2

print(solve_quadratic_eqn(1,3,2))