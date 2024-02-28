#1
import datetime

x = datetime.datetime.now()

from datetime import timedelta

newx = x - timedelta(days=5)

print(newx)



#2
import datetime

x1 = datetime.datetime.now()

from datetime import timedelta

x0 = x1 - timedelta(days=1)

x2 = x1 + timedelta(days=1)

print("Yesterday: " + x0.strftime("%x"))

print("Today: " + x1.strftime("%x"))

print("Tomorrow: " + x2.strftime("%x"))



#3
import datetime

x = datetime.datetime.now()

newx = x.replace(microsecond=0)

print(newx)



#4 and i could just take two dates
import datetime

x = datetime.datetime.now()

x = x.replace(microsecond=0)

x = x.replace(second=0)

x = x.replace(minute=0)

x = x.replace(hour=0)

y = int(input("Year: "))

m = int(input("Month: "))

d = int(input("Day: "))


x1 = datetime.datetime(y, m, d)

x3 = x - x1

sec = x3.total_seconds()

print("Difference in seconds: ", sec)

