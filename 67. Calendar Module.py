import calendar

full_date = list(map(int, input().split()))
month = full_date[0]
date = full_date[1]
year = full_date[2]


print(calendar.day_name[calendar.weekday(year, month, date)].upper())