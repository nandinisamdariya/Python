import math

# a) sin of 60 degrees
result_a = math.sin(math.radians(60))
print("sin(60 degrees) is:", result_a)

# b) cos of pi
result_b = math.cos(math.pi)
print("cos(pi) is:", result_b)

# c) sin of 0.8660254037844386
result_c = math.sin(0.8660254037844386)
print("sin(0.8660254037844386) is:", result_c)

# d) tan of 90 degrees
try:
    result_d = math.tan(math.radians(90))
except ValueError:
    result_d = "undefined"  
print("tan(90 degrees) is:", result_d)
