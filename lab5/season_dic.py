month_season = {
    1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'
}

# Input: Month number
month_number = int(input("Enter the month number (1-12): "))
season = month_season.get(month_number, 'Invalid month number')
print(f"The season is: {season}")
