from fileinput import filename
from typing import List
from openpyxl import load_workbook



List1 = [



'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',

'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',

'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy',
'ttt' , 'xx' , 'yy'



]



start = True
while start:
            # Load in the workbook
            filename = input('nazvanie faila : ')

            wb = load_workbook(str(filename))
            wb.active = 1
            sheet = wb.active
            filemode = 'w'
            f = open(str(filename),filemode)

            # Get sheet names
            for i in range(1,len(List1)):
                sheet['A'+str(i)].value =str(List1[i])
                print(sheet['A'+str(i)].value)

            newfilename = input('kuda sohranjaem fail? : ')
            wb.save(str(newfilename))





"""
from typing import List
from openpyxl import load_workbook

List1 = [ 'ttt' , 'b' , 'a' ]

# Load in the workbook
wb = load_workbook('123.xlsx')
wb.active = 1

sheet = wb.active

# Get sheet names

for i in range(1,len(List1)):
    sheet['A'+str(i)].value =str(List1[i])
    print(sheet['A'+str(i)].value)
    
wb.save('123.xlsx')



#Создаем листы/sheets в файле exel

from openpyxl import load_workbook
# Load in the workbook
wb = load_workbook('расчет.xlsx')
data = 'My'
# Get sheet names
wb.create_sheet(data)
print(wb.get_sheet_names())

"""