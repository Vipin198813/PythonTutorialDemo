import datetime
mytime = datetime.time(2,20)
print(mytime)
print(mytime.minute)
print(mytime.hour)
print(type(mytime))

today = datetime.date.today()
print(today.year)
print(today.day)
print(today.month)
print(today.ctime())
from datetime import datetime
mydatetime = datetime(2021,3,15,14,20,10)
print(mydatetime)

datetime1 = datetime(2025,12,13,3,15,00)
datetime2 = datetime(2024,12,13,3,15,50)
result = datetime1 - datetime2
print(result.seconds)