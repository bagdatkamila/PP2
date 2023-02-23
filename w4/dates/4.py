"""
Write a Python program to print yesterday, today, tomorrow.
"""
import datetime
def secsdelta():
    date1 = datetime.datetime.now()
    date2 = datetime.datetime.now() - datetime.timedelta(days = 19)
    delta = date2 - date1
    return delta.total_seconds()

print(secsdelta())