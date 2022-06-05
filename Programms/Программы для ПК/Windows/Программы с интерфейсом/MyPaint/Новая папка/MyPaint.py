import pygame as pg , pyautogui , time , random , math , sys , pickle , sys

pg.font.init()

screen_width , screen_height  = 1920 , 1080

picture_width , picture_height = 1920 , 1080

fontsize = 25

f1 = pg.font.Font( None , fontsize ) 

sc = pg.display.set_mode ( ( screen_width , screen_height ) ) 

welcome = 'My Paint'

pg.display.set_caption( welcome )

pos = pg.mouse.get_pos()




shapes = [ 

'circle' , 'rectangle' , 'line' , 'elipse' , 'polygon' , 'star' ,'squareframe' , 'sun' , 'grid' , 'door' ,

'window' , 'text' , 'plus' , 'cross' , 'messageicon' , 'circleframe', 'cilinder'

]




shape = shapes[1]

radius , radius1 = 5 , 5

rect_width , rect_height = 50, 50

line_width1 , line_width2 = 50 , 0

draw_dist = 25

horizontal_offset , vertical_offset = 10 , 10

cancel_icon_x ,cancel_icon_y = screen_width - 50 , 10

cancel_icon_width , cancel_icon_height = 25 , 25

pos = pg.mouse.get_pos()

WHITE = ( 255 , 255 , 255 ) ; RED = ( 255 , 0 , 0 ) ; ORANGE  = ( 255 , 125 , 0 ) ; YELLOW  = ( 255 , 255 , 0 ) ; GREEN = ( 0 , 225 , 0 ) ; 

LIGHT_BLUE = ( 0 , 125 , 255 ) ; BLUE = ( 0 , 0 , 255 ) ; PURPLE  = ( 128 , 0 , 255 )



LIME = ( 0 , 255 , 0 ) ; OLIVE = ( 128 , 128 , 0 ) ; GREY = ( 128 , 128 , 128 ) ; BLACK = ( 0 , 0 , 0 ) ; BROWN = ( 101 , 67 , 33 ) ; AQUA = ( 0 , 255 , 255 )

SILVER  = ( 192 , 192 , 192 );MAGENTA = ( 255 , 0 ,255 );GOLD = ( 255 , 215 , 0 )

BGCOLOR = WHITE

measure_units = [

'Radius : ','lenght : ','width : ','Points : ','Verticles : '

]

measure_unit = measure_units[0]

value = 3

text_color = (180 , 0 , 0)

text1 = f1.render( measure_unit + str( radius ) , True , text_color )

Show_screen_size = f1.render( 'Window : ' + str(screen_width) + ' * ' + str(screen_height) , True , text_color )

Show_image_size = f1.render( 'Image : ' + str(screen_width) + ' * ' + str(screen_height) , True , text_color )

Colors = [

RED , ORANGE , YELLOW , GREEN , LIGHT_BLUE , BLUE , PURPLE 

]

ColorsCoords_x = []

ColorsCoords_y = []

for i in range( len( Colors ) ) :

    i = ColorsCoords_x.append(20 + i * draw_dist + radius1)
    
    i = ColorsCoords_y.append(radius1 * 2)



main_color = Colors[0]

colors_max = len(Colors)

step = 0

panel_width , panel_height = screen_width , 100

panel_x , panel_y = 0 , 0
Fontnames = ['serif']
Fontname = Fontnames[0]

f = pg.font.SysFont( Fontname , fontsize )

class interface :
    def __init__( self, x , y , width , height , image ) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
cell = interface( screen_width / 2 ,50 , 50 , 50 , pg.image.load( 'картинки/cell.png' ) )

currentcell = interface( screen_width / 2 ,50 , 50 , 50 , pg.image.load( 'картинки/current_cell.png' ) )

button = interface(2100,210,200,50,pg.image.load( 'картинки/button.png' ) )

left_pointer = interface(  50 , 100 ,20 , 20 , pg.image.load( 'картинки/pointer_left.png' ) )

right_pointer = interface(200 , 100 , 20 , 20 , pg.image.load( 'картинки/pointer_right.png' ) )

cancel_icon = interface(  50 , 25 , 20 , 20 , pg.image.load( 'картинки/cancel_icon.png' ) )

MyShapesList = []

sc.fill( BGCOLOR )


def Update():

    panel1 = pg.draw.rect( sc , ( GREY ) , ( panel_x , panel_y , screen_width , panel_height ) )

    panel2 = pg.draw.rect( sc , ( GREY ) , ( 0 ,panel_height , 150,screen_height ) )

    for i in range( len( Colors ) ) :

        sc.blit(cell.image , ( i * 25 , 0 ) )

        sc.blit(cell.image , (  0 ,panel_height + i * 75 ) )
        
        sc.blit(cell.image , ( 0 ,panel_height) )

        i = pg.draw.circle( sc , Colors[ i ] , ( radius1 * 2 + 2 + i * 25 , radius1 * 2 + 2 ) , radius1 )

    sc.blit( text1 , ( 20 , 75 ) )

    sc.blit( Show_screen_size , ( 20 , 50 ) )

    sc.blit(cancel_icon.image , ( cancel_icon_x,cancel_icon_y ) )

    image = sc.blit(cell.image ,( 0 , 0 )  )

    for i in range(len(MyShapesList)):
        i

    pg.display.update()

def make_screenshot() :
    screenshot = pyautogui.screenshot( 'снимки экрана/screenshot.png' , region = ( 100 , 100 ,1920,1080 ) )

while True:
    for event in pg.event.get() :
        pressed = pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()

        #Правая кнопка мыши
        #Круг
        if pressed[ 2 ] and shape == shapes[ 0 ] :
            MyShapesList.append(pg.draw.circle ( sc , main_color , event.pos , radius ))
            Update()
            print(MyShapesList)

        #Правая кнопка мыши
        #квадрат    
        if pressed[ 2 ] and shape == shapes[ 1 ] :
            MyShapesList.append(pg.draw.rect(sc, main_color, ( pos[ 0 ] - rect_width / 2 , pos[ 1 ] - rect_height / 2  , rect_width, rect_height ) ))
            Update()
            print(MyShapesList)
            



        #Правая кнопка мыши
        #линия
        if pressed[ 2 ] and shape == shapes[ 2 ] :
            MyShapesList.append(pg.draw.line( sc , main_color , event.pos , [ 290 , 15 ] , 1 ) )
            Update()
            print(MyShapesList)


        #Правая кнопка мыши
        #полигон
        if pressed[ 2 ] and shape == shapes[ 4 ] :
            MyShapesList.append(pg.draw.polygon( sc , main_color , [ [ 250 , 110 ] , [ 280 , 150 ] , [ 190 , 190 ] , [ 130 , 130 ] , [ 0 , 300 ] ] ))
            Update()
            print(MyShapesList)
        


        if event.type == pg.QUIT :
            sys.exit()



        if event.type == pg.KEYDOWN :

            if event.key == pg.K_c :
                shape = shapes[ 0 ]
                Update()
                print(MyShapesList)



            if  event.key == pg.K_r :

                shape = shapes[ 1 ]

                Update()
                print(MyShapesList)



            if  event.key == pg.K_l:

                shape = shapes[ 2 ]

                Update()
                print(MyShapesList)



            if  event.key == pg.K_e :
                shape = shapes[ 3 ]
                Update()
                print(MyShapesList)



            if  event.key == pg.K_p:
                shape = shapes[ 4 ]
                Update()
                print(MyShapesList)
            


            if  event.key == pg.K_z:
                for i in MyShapesList:
                    MyShapesList.remove(MyShapesList[0])
                
                Update()
                

                
                print(MyShapesList)

        

            if event.key == pg.K_s :
                make_screenshot()



            if event.key == pg.K_F12 :
                quit()



            if event.key == pg.K_F5 :

                screen_width = 1920

                screen_height = 1080

                sc = pg.display.set_mode ( ( screen_width , screen_height ) )

                welcome = welcome

                pg.display.set_caption( welcome )


            if event.key == pg.K_b :

                BGCOLOR = main_color



        if event.type == pg.MOUSEBUTTONDOWN :


            #левая кнопка мыши

            if event.button == 1 and pos[0] >= 50 and pos[1] >= panel_height:
                MyShapesList.append(pg.draw.rect(sc, main_color, ( pos[ 0 ] - rect_width / 2 , pos[ 1 ] - rect_height / 2  , rect_width, rect_height ) ))
                pg.display.update()

                for i in range(len(MyShapesList)):
                    i



            #колесо мыши к монитору

            if event.button == 4  and shape == shapes[0] :

                radius -= value

                text1 = f1.render( measure_unit + str( radius ) , True , text_color )

                Update()



            #колесо мыши к себе

            if event.button == 5  and shape == shapes[0] :

                radius += value

                text1 = f1.render( measure_unit + str( radius ) , True , text_color )

                Update()

            

            #колесо мыши к монитору

            if event.button == 4  and shape == shapes[1] :

                rect_width -= value

                rect_height -= value

                text1 = f1.render( measure_units[1] + str( rect_width )  + ' / ' + measure_units[2] + str ( rect_height ) , True , text_color )

                Update()



            #колесо мыши к себе

            if event.button == 5  and shape == shapes[1] :

                rect_width += value

                rect_height += value

                text1 = f1.render( measure_units[1] + str( rect_width )  + ' / ' + measure_units[2] + str ( rect_height )  , True , text_color )

                Update()



            #колесо мыши к себе

            if event.button == 5 and shape == shapes[0] :

                radius += 3

                text1 = f1.render( measure_unit + str( radius )   , True , text_color )

                Update()



            #колесо мыши / средняя кнопка мыши

            if event.button == 2 :

                sc.fill( BGCOLOR )

                Update()
                
                print(MyShapesList)