from datetime import date

# 1 Jan 1900 was a Monday.
# Thirty days has September, April, June and November.
# All the rest have thirty-one,
# Saving February alone, which has twenty-eight, rain or shine and on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century(1 Jan 1901 to 31 Dec 2000)?


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


years = range(1901, 2001)
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
first_of_months = [date(year, month, 1) for year in years for month in months]
count_sundays = 0
for d in first_of_months:
    if d.weekday() == 6:
        count_sundays += 1

print(count_sundays)
