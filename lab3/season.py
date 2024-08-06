def check_season(month):
    season = {
        'Autumn': ['August','September', 'October'],
        'Winter': ['November','December', 'January'],
        'Spring': ['February','March', 'April'],
        'Summer': ['May','June', 'July']
        }
    key = season.keys()
    for k in key:
        if month in season[k]: return k
    return 'invalid month'

print(check_season('October'))