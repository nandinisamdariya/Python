def miles_to_kilometers(miles):
    return miles * 1.60934

miles = float(input("Enter miles: "))
print(f"{miles} miles is equal to {miles_to_kilometers(miles)} kilometers")
