def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return 'undefined'
    return (y2 - y1) / (x2 - x1)
