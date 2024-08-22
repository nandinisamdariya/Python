A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Set operations on A and B
# I. Join A and B
union_ab = A.union(B)
print(union_ab)

# II. Find A intersection B
intersection_ab = A.intersection(B)
print(intersection_ab )

# III. Is A subset of B
is_subset = A.issubset(B)
print(is_subset)

# IV. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print(are_disjoint)

# V. Join A with B and B with A
a_union_b = A.union(B)
b_union_a = B.union(A)
print (a_union_b , b_union_a)

# VI. Symmetric difference between A and B
symmetric_diff_ab = A.symmetric_difference(B)
print(symmetric_diff_ab)

# VII. Delete the sets completely
del A, B
