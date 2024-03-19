#все что связанно с датами, временем и их изменения

# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513	
# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# %W	Week number of year, Monday as the first day of week, 00-53	52	
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	Century	20	
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00	
# %%	A % character	%	
# %G	ISO 8601 year	2018	
# %u	ISO 8601 weekday (1-7)	1	
# %V	ISO 8601 weeknumber (01-53)	01

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