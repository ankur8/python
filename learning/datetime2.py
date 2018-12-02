import datetime
t1=datetime.datetime.now()

print(t1.hour)
print(t1.minute)
print(t1.second)
print(t1.microsecond)

print(datetime.datetime.resolution)

from datetime import date   #import only date submodule from datetime module

print(date.today())
