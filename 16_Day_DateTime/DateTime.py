#Day16 : Date time - 30 days of python learning

from datetime import datetime 
now = datetime.now()        
print(now)                 # 2021-09-24 22:49:20.895147     
day = now.day                   
month = now.month               
year = now.year                 
hour = now.hour                 
minute = now.minute             
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)   # 24 9 2021 22 49
print('timestamp: ', timestamp)         # timestamp:  1632503960.895147
print(f'{day}/{month}/{year}, {hour}:{minute}')  #  24/9/2021, 22:49

#using strftime method
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)                               # time: 22:54:26
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)                    # time one: 09/24/2021, 22:54:26
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)                    # time two: 24/09/2021, 22:54:26

#Difference Between Two Points in Time using date
from datetime import date
today = date(year=2021, month=9, day=24)
new_year = date(year=2022, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)    #Time left for new year:  99 days, 0:00:00

t1 = datetime(year = 2021, month = 9, day = 24, hour = 23, minute = 0, second = 0)
t2 = datetime(year = 2022, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff)  #Time left for new year: 98 days, 1:00:00

