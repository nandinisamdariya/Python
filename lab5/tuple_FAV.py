fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'yogurt')

# I. Joining the three tuples and assigning to food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products

# II. Changing the food_stuff_tp tuple to a list
food_stuff_lt = list(food_stuff_tp)

# III. Slicing out the middle item or items
n = len(food_stuff_lt)
if n % 2 == 0:
    middle_items = food_stuff_lt[n//2 - 1:n//2 + 1]
else:
    middle_items = food_stuff_lt[n//2]

# IV. Slicing out the first three and last three items
first_three_items = food_stuff_lt[:3] 
last_three_items = food_stuff_lt[-3:]

# V. Deleting the food_staff_tp tuple;-
del food_stuff_tp

print(food_stuff_lt , middle_items , first_three_items , last_three_items)
