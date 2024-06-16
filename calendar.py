# Coding by Kanishk Raj

import calendar
def print_year_calendar(year):
    cal = calendar.TextCalendar().formatyear(year)
    print(cal)
year = 1980
print_year_calendar(year)