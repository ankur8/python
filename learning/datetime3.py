from datetime import datetime


a=datetime(2011,11,24,11,20,21)    #date(2011,11,24) if only date needs to be findout not time
b=datetime(2011,10,23,12,34,55)
c=b-a    #date time give diff in seconds
print (c.seconds)   #return timedelta object
print(c.days)



