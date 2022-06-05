import pygame as pg, pyautogui,time,random,math,sys,pickle

pg.font.init()

import sys

Screen_width = 1024

Screen_height = 768

sc = pg.display.set_mode((Screen_width,Screen_height))

pos = pg.mouse.get_pos()

Fontsize = 25

Fontname = 'serif'

f1 = pg.font.Font(None, Fontsize)

pos = pg.mouse.get_pos()

WHITE = (255, 255, 255)

RED = ( 255 , 0 , 0 )

ORANGE  = ( 255 , 125 , 0 )

YELLOW  = ( 255 , 255 , 0 )

GREEN = ( 0 , 225 , 0 )

LIGHT_BLUE = ( 0 , 125 , 255 )

BLUE    = ( 0 , 0 , 255 )

PURPLE  = ( 128 , 0 , 255 )

bgcolor = WHITE

an_exercises = ['Отжимания' , 'Подъемы со штангой' , 'бёрпи' , 'приседания' ]

Sport_inventory = ['Штанга' , 'Гантели' , 'Резиновый эпандер', 'Пружинный эспандер', 'Теннисный мяч' , 'Футбольный мяч' , 'Гимнастический коврик' ]

pushupsyoumade = 0

max_pushups = 20

approaches = 5

approach = 1

text1 = f1.render( 'Упражнение' + ' : ' + an_exercises[ 0 ] , True , ( 180 , 0 , 0 ) )

timer = f1.render( 'Кол-во отжиманий' + ' : ' + str( pushupsyoumade ) + '   ' + 'Кол-во подходов' + '   ' + str(approach) + ' / ' + str(approaches), True , ( 180 , 0 , 0 ) )

WhatYouNeed = f1.render( 'Инвентарь' ' : ' + str( 'Не требуется' ) , True , ( 180 , 0 , 0 ) )

meuntext1 = f1.render( 'Упражнения' , True , ( 180 , 0 , 0 ) )

timer_x = 200

timer_y = 30


sc.fill( bgcolor )

pg.draw.rect( sc , ( 150 , 150 , 150 ) , ( 0 , 0 ,  1920 , 80 ) )

pg.draw.rect( sc , ( 150 , 150 , 150 ) , ( 0 , 0 , 180 , Screen_height ) )



sc.blit(text1, ( 200 , 10 ) )

sc.blit( timer , ( timer_x , timer_y ) )

sc.blit( WhatYouNeed , ( 200 , 50 ) )

sc.blit( meuntext1 , ( 0 , 100 ) )

pg.display.update()



def make_screenshot() :

    screenshot = pyautogui.screenshot('снимки экрана/screenshot.png',region=( 0 , 80 , 1920 , 1000 ) ) 


while True:

    for event in pg.event.get():

        if event.type == pg.QUIT:

            sys.exit()

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_s:
                
                make_screenshot()


            if event.key == pg.K_q:

                quit()


