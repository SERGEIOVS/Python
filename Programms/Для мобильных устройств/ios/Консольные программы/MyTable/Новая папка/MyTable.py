from concurrent.futures.process import _ThreadWakeup,os

from tabulate import tabulate

run = True
menu_points = [ 'Новая таблица' , 'Показать таблицу' , 'Обновить таблицу' , 'Удалить таблицу' ]
while True:

    print('- Меню - ')
    for i in range(len(menu_points)):
        print(str(i) + ' - ' + menu_points[i])

    action = input('Что делаем? ')

    if action == menu_points[0]:

        table=[]

        tablename=table

        headerscount= int(input('Количество столбцов : '))

        rowcount = int(input('Количество рядов : '))

        cells_in_row_count = headerscount
        table.append([])
        
        table[0].append('x')
        for i in range(headerscount):
            i+=1
            table[0].append(str(i))

        for i in range(rowcount):
            table.append([])
            i+=1
            table[i].append(str(i))
        print(tabulate(table, tablefmt="grid"))

    if action == menu_points[1]:
        print(tabulate(table, tablefmt="grid"))

    if action == menu_points[2]:

        cells_in_row_count+=headerscount

        column = int(input('Колонка : '))
        
        row_name= input('Значение : ')

        if column > 1:

            table[column] = row_name
        else:
            print('Ошибка! Выберите число больше чем 0 !')

    print(tabulate(table, tablefmt="grid"))

    if action == menu_points[3]:
        table.remove(table[0:len(table)])
        print('Table removed!')

    if action == 'Обновить экран':
        os.system('cls||clear')