def check_season(month):
    season = {
        'Spring': ['September', 'October', 'November'],
        'Summer': ['December', 'January', 'February'],
        'Autumn': ['March', 'April', 'May'],
        'Winter': ['June', 'July', 'August']
        }
    key = season.keys()
    for k in key:
        if month in season[k]: return k
    return 'invalid month'
 
print(check_season('October'))