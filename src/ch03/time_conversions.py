from datetime import timedelta, datetime

from dateutil.relativedelta import relativedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a+b
print(c)

print(c.total_seconds())

time_diff = timedelta(days=1, minutes=30)
print(time_diff.total_seconds())

date_time = datetime(year=2019, month=1, day=30, hour=13, minute=23)
print(date_time)
print(date_time.timestamp())
print(date_time + c)

dt2 = date_time + relativedelta(months=+3, days=-3, minutes=+872782)
print(dt2)

diff = dt2-date_time
print(diff)