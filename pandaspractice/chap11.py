from datetime import datetime
import pandas as pd

ebola = pd.read_csv('/Users/ice_macbookair/Desktop/Ice Data engineer/pandaspractice/pandaspractice/data/country_timeseries.csv')

# now = datetime.now()
# print(now)

# t1 = datetime.now()
# t2 = datetime(1970, 1, 1)

# diff = t1 - t2

# print(diff)

# print(ebola.info())

ms = 1541106106796

date = pd.to_datetime(ms, unit='ms')
print(date)


# day = date.day() # not .dt.date since bot a group of data
# print(day)

# month = date.month()
# print(month)

# year = date.year()
# print(year)

# hr = date.hour()
# print(hr)

# mn = date.minute()
# print(mn)

# sec = date.second()
# print(sec)

time = date.time()
print(time)

day = date.day
print(day)

hrs = date.hour
print(hrs)

mn = date.minute
print(mn)

sc = date.second
print(sc)

month = date.month
print(month)

year = date.year
print(year)

wd = date.dayofweek
print(wd)




# time = date.time()
# print(date)