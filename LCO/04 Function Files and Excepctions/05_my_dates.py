import time
import datetime

print(time.localtime())

localtime = time.asctime(time.localtime(time.time()))

print(localtime)

# TODO: print date of a perticular day
# create a date object for the desired date
date_string = "2023-03-8"
date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()

# use strftime() to format the date object into a string with the day of the week
day_of_week = date_obj.strftime("%A")

print(day_of_week)