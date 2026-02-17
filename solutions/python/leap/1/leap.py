def leap_year(year):
    if year % 4 is 0:
        if year % 400 is 0 or year % 100 is not 0:
            return True
    return False