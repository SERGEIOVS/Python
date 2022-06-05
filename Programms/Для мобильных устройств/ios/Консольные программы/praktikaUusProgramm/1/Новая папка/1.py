#sait - https://www.nordpoolgroup.com/Market-data1/Dayahead/Area-Prices/EE/Hourly/?view=table
import datetime,time,pyautogui,webbrowser
webbrowser.open('https://www.nordpoolgroup.com/Market-data1/Dayahead/Area-Prices/EE/Hourly/?view=table')
from turtle import delay
minutes = []
for i in  range(60):
    i+=1
    minutes.append(i)
print(minutes)    
while True:
    d1 = datetime.datetime.today()
    d1 += datetime.timedelta(hours = 0)
    time_units = [d1.hour,d1.minute,d1.second]
    current_time_unit = time_units[1]
    TEST = '123'
    for i in minutes:
        if current_time_unit == i:
            time.sleep(1)
            print('TEST',time_units[0],time_units[1],time_units[2])
            screenshot = pyautogui.screenshot()
            screenshot = pyautogui.screenshot('скриншоты/test' +str(i)+ '.png',region=(210,200, 810, 710))


