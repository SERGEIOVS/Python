import pygame as pg , pyautogui , time , random , math , sys , pickle , sys

pg.font.init()

screen_width   = 800

screen_height  = 600

picture_width  = 1920

picture_height = 1080

sc = pg.display.set_mode ( ( screen_width , screen_height ) ) 

welcome = 'Привет!'

pg.display.set_caption( welcome )

pos = pg.mouse.get_pos()

fontsize = 25

shapes = [ 'circle' , 'rectangle' , 'line' , 'elipse' , 'polygon' ]

shape = shapes[ 4 ]

f1 = pg.font.Font( None , fontsize ) 

radius = 10

radius1 = 10

rect_width = 50

rect_height = 50

line_width1 = 50

line_width2 = 0

draw_dist = 25

horizontal_offset = 10

vertical_offset   = 10

cancel_icon_x = screen_width - 50

cancel_icon_y = 10

cancel_icon_width = 25

cancel_icon_height = 25

cancel_icon_image = pg.image.load('картинки/cancel_icon.png')

pos = pg.mouse.get_pos()

WHITE = ( 255 , 255 , 255 )

RED = ( 255 , 0 , 0 )

ORANGE  = ( 255 , 125 , 0 )

YELLOW  = ( 255 , 255 , 0 )

GREEN = ( 0 , 225 , 0 )

LIGHT_BLUE = ( 0 , 125 , 255 )

BLUE    = ( 0 , 0 , 255 )

PURPLE  = ( 128 , 0 , 255 )



LIME = ( 0 , 255 , 0 )

OLIVE = ( 128 , 128 , 0 )

GREY    = ( 128 , 128 , 128 )

BLACK   = ( 0 , 0 , 0 ) 

BROWN   = ( 101 , 67 , 33 )

AQUA    = ( 0 , 255 , 255 )

SILVER  = ( 192 , 192 , 192 )

MAGENTA = ( 255 , 0 ,255 )

GOLD    = ( 255 , 215 , 0 )

BGCOLOR = WHITE

measure_units = ['|Радиус : ' , '|Длина : ' , '|Ширина : ' , '|Кол-во вершин : '   ]

measure_unit = measure_units[ 0 ]

text_color = ( 180 , 0 , 0 )

text1 = f1.render( measure_unit + str( radius )  + ' | ' , True , text_color )

Colors = [ RED , ORANGE , YELLOW , GREEN , LIGHT_BLUE , BLUE , PURPLE ]

ColorsCoords_x = [ ]

ColorsCoords_y = [ ]

for i in range( len( Colors ) ) :

    i = ColorsCoords_x.append( 20 + i * draw_dist + radius1 )

    i = ColorsCoords_y.append( radius1 * 2 )


main_color = Colors[ 1 ]

colors_max = len( Colors )

step = 1

panel_width = screen_width

panel_height = 80

panel_x = 0

panel_y = 0

Fontname = 'serif'

f = pg.font.SysFont( Fontname , fontsize )

sc.fill( BGCOLOR )

def Update():

    panel = pg.draw.rect( sc , ( GREY ) , ( panel_x , panel_y , screen_width , panel_height ) )

    for i in range( len( Colors ) ):

        i = pg.draw.circle( sc , Colors[ i ] , ( ColorsCoords_x[ i ] , ColorsCoords_y[ i ] ) , radius1 )

    sc.blit( text1 , ( 20 , 50 ) )

    current_color_num = 0

    current_color_selector = pg.draw.circle( sc , Colors[ current_color_num ] , ( ColorsCoords_x[ 0 ] , 35 ) , 5 )

    sc.blit(cancel_icon_image , ( cancel_icon_x,cancel_icon_y ) ) 

    pg.display.update()


def make_screenshot() :

    screenshot = pyautogui.screenshot( 'снимки экрана/screenshot.png' , region = ( panel_x , panel_height , picture_width , picture_height ) )

while True:
    
    for event in pg.event.get() :

        pressed = pg.mouse.get_pressed()

        pos = pg.mouse.get_pos()

        if pressed[ 2 ] and shape == shapes[ 0 ] :

            Update()

            pg.draw.circle ( sc , main_color , event.pos , radius )


        if pressed[ 2 ] and shape == shapes[ 2 ] :

            Update()

            pg.draw.line( sc , main_color , [ 10 , 30 ] , [ 290 , 15 ] , 1 ) 



        if pressed[ 2 ] and shape == shapes[ 3 ] :

            Update()

            pg.draw.ellipse( sc , main_color , ( 10 , 50 , 280 , 100 ) , 1 )


        if pressed[ 2 ] and shape == shapes[ 4 ] :

            Update()

            pg.draw.polygon( sc , main_color , [ [ 250 , 110 ] , [ 280 , 150 ] , [ 190 , 190 ] , [ 130 , 130 ] , [ 0 , 300 ] ] )
        


        if event.type == pg.QUIT :

            sys.exit()

        if event.type == pg.KEYDOWN :

            if event.key == pg.K_1 and shape == shapes[ 0 ] :

                step = ColorsCoords_x[ 0 ]

                main_color = Colors[ 0 ]

                text1 = f1.render( measure_unit + str( radius )  + ' | ' , True , text_color )

                current_color_num = 0

                Update()


            
            if event.key == pg.K_2 :

                step = ColorsCoords_x[ 1 ]

                main_color = Colors[ 1 ]

                text1 = f1.render( measure_unit + str( radius )  + ' | ' , True , text_color )

                current_color_num = 1

                Update()



            if event.key == pg.K_3 :

                step = ColorsCoords_x[ 2 ]

                main_color = Colors[ 2 ]

                text1 = f1.render( measure_unit + str( radius )  + ' | ' , True , text_color )

                current_color_num = 2

                Update()



            if event.key == pg.K_4 :

                step = ColorsCoords_x[ 3 ]
                
                main_color = Colors[ 3 ]
                
                text1 = f1.render( measure_unit + str( radius )  + ' | ' , True , text_color )
                
                current_color_num = 3
                
                Update()



            if event.key == pg.K_5 :

                step = ColorsCoords_x[ 4 ]

                main_color = Colors[ 4 ]

                text1 = f1.render( measure_unit + str( radius )  + ' | ' , True , text_color )

                current_color_num = 4

                Update()



            if event.key == pg.K_6 :

                step = ColorsCoords_x[ 5 ]

                main_color = Colors[ 5 ]

                text1 = f1.render( measure_unit + str( radius )  + ' | ' , True , text_color )

                current_color_num = 5

                Update()
        


          
            if event.key == pg.K_c :

                shape = shapes[ 0 ]

                Update()



            if  event.key == pg.K_r :

                shape = shapes[ 1 ]

                Update()



            if  event.key == pg.K_l :

                shape = shapes[ 2 ]

                Update()



            if  event.key == pg.K_e :

                shape = shapes[ 3 ]

                Update()



            if  event.key == pg.K_p:

                shape = shapes[ 4 ]

                Update()



            if event.key == pg.K_s :

                make_screenshot()


            if event.key == pg.K_F12 :

                quit()


            
            if event.key == pg.K_F5 :

                screen_width = 1920

                screen_height = 1080

                sc = pg.display.set_mode ( ( screen_width , screen_height ) )

                welcome = 'Привет!'

                pg.display.set_caption( welcome )


            if event.key == pg.K_b :

                BGCOLOR = main_color


        if event.type == pg.MOUSEBUTTONDOWN :

            if event.button == 1:

                pg.draw.rect(sc, main_color, ( pos[ 0 ] - rect_width / 2 , pos[ 1 ] - rect_height / 2  , rect_width, rect_height ) )

                pg.display.update()



            if event.button == 4  and shape == shapes[0] :

                radius -= 3
                
                text1 = f1.render( measure_unit + str( radius )  + ' | ' , True , text_color )

                Update()

            
            if event.button == 4  and shape == shapes[1] :

                rect_width += 3

                rect_height +=3

                text1 = f1.render( measure_units[1] + str( rect_width )  + ' / ' + measure_units[2] + str ( rect_height ) + ' | ' , True , text_color )

                Update()













            if event.button == 5 and shape == shapes[0] :
                radius += 3
                text1 = f1.render( measure_unit + str( radius )  + ' | ' , True , text_color )
                Update()

            if event.button == 2 :
                sc.fill( BGCOLOR )
                Update()
