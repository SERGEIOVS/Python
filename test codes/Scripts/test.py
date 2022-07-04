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

