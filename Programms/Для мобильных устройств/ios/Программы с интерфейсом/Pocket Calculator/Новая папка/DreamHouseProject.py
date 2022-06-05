import math,colorama,random,pygame
#мебель
furniture = []
#устройства
Devices = []
#материалы
Materials = []
#декорации
Decorations = []
#бытовая техника
Appliances = []
wp_roll_width = 0.5
wp_roll_length = 10
run = True
while run:
    print()
    print('Чем могу помочь?')
    print('*добавить')
    print('*удалить')
    print('*показать')
    print('*узнать площадь')
    print('*узнать периметр')
    print('*узнать объем')
    print('*узнать количество')
    user_input = input()
    if user_input == 'добавить':
        print( 'введи название:' )
        name = input()
        print( 'введи количество:' )
        count = input()
        Decorations.append( name + "(" + count + ")" )
        print( Decorations )  
    if user_input == 'удалить':
        print( 'введи название:' )
        name = input()
        print( 'введи количество:' )
        count = input()
        Decorations.remove( name + "(" + count + ")" )
        print( Decorations )
    if user_input == 'показать':
        print( Decorations )
    if user_input == 'узнать площадь':
        print( 'длина:(м)' )
        length = int( input() )
        print('ширина:(м)')
        width = int( input() )
        ploshad = length * width
        print('площадь:' , ploshad , 'м2')
    if user_input == 'узнать периметр':
        print( 'длина:(м)' )
        length = int( input() )
        print(' ширина:(м) ')
        width = int( input() )
        perimetr = 2*( length + width )
        print( 'периметр:' , perimetr , 'м' )
    if user_input == 'узнать объем':
        print( 'длина:(м)' )
        length = int(input())
        print( 'ширина:(м)' )
        width = int( input() )
        print( 'высота:(м)' )
        height = int( input() )
        objem = length * width * height
        print( 'объем:' , objem , 'м3' )
    if user_input == 'расчитать обои':
        print('длина:')
        length = int( input() )
        print('ширина:')
        width = int( input() )
        print('высота:')
        height = float(input())
        count1 = length / wp_roll_width * 2
        count2 = width / wp_roll_width * 2
        wp_rolls_count = (count1 + count2) / (wp_roll_length / height)
        print(wp_rolls_count)
        

    
    
    
    
    
        
        
        
        
        
        



















