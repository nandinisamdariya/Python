ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# I. Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)

# II. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)

# III. Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]

# IV. Find the average age
average_age = sum(ages) / len(ages)

# V. Find the range of the ages (max - min)
age_range = max_age - min_age

# VI. Compare the value of (min - average) and (max - average), use abs() method
min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)

print (min_age, max_age, median_age, average_age, age_range, min_avg_diff, max_avg_diff)
