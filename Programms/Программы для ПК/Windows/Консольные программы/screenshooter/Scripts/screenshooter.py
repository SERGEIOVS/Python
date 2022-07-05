import pyautogui,datetime,time
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
    print('MENU')

    print('Make screenshot/s without interval ')
    print('Make screenshot/s with interval ')

    screenshots_num = int(input('screenshots? (number)  : '))

    for i in range(screenshots_num):

        x1 , y1 = int(input('x1 : '))

        x2 , y2 = int(input('screenshots : '))


        #making a screenshot without name
        screenshot = pyautogui.screenshot()


        #making a screenshot name and path
        screenshot_name = input('Screenshot name : ')
        screenshot_path = input('Screenshot path : ')

        #saving the  screnshot/s 
        screenshot.save(str(screenshot_path) + str(screenshot_name) + '.jpg')

    for i in minutes:
        if current_time_unit == i:
            time.sleep(1)
            print('TEST',time_units[i])
            screenshot = pyautogui.screenshot()
            screenshot = pyautogui.screenshot('скриншоты/test' +str(i)+ '.png',region=(x1 , y2, x2 , y2))



