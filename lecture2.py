
#Python Dates and Times
'''
 In this course, we're not going to delve too deeply into time series analysis, but I wanted to show you some of the basics in Python.
Start transcript at 34 seconds0:34
First, you should be aware that date and times can be stored in many different ways. One of the most common legacy methods for storing the date and time in online transactions systems is based on the offset from the epoch, which is January 1, 1970. There's a lot of historical cruft around this, but it's not uncommon to see systems storing the date of a transaction in seconds or milliseconds since this date. So if you see large numbers where you expect to see date and time, you'll need to convert them to make much sense out of the data.
Start transcript at 1 minute 6 seconds1:06
In Python, you can get the current time since the epoch using the time module. You can then create a time stamp using the from time stamp function on the date time object. When we print this value out, we see that the year, month, day, and so forth are also printed out.
Start transcript at 1 minute 22 seconds1:22
The date time object has handy attributes to get the representative hour, day, seconds, etc.
Start transcript at 1 minute 30 seconds1:30
Date time objects allow for simple math using time deltas. For instance, here, we can create a time delta of 100 days, then do subtraction and comparisons with the date time object. This is commonly used in data science for creating sliding windows. For instance, where you might want to look for any five day span of time where sales were highest, and flag that for follow up.
Start transcript at 1 minute 54 seconds1:54
This is just a little glimpse at dates and times in Python. In week three of this course, we're going to investigate dates and times a bit more using the pandas date time library.
'''

#Working with Date and Time
import datetime as dt
import time as tm

print(tm.time())
#CurrenTtime will be printed

#Convert the timestamp to datetime.
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow,"Hi")

print(dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second)
# get year, month, day, etc.from a datetime

#timedelta is a duration expressing the difference between two dates
delta = dt.timedelta(days = 10) # create a timedelta of 10 days
print(delta,"hello")


today = dt.date.today()
print(today)
print('After 10 days: '+str(today + delta)) # the date 10 days 
print(today > today-delta) # compare dates