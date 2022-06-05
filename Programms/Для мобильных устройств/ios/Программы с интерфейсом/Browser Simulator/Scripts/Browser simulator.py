import pygame as pg , pyautogui , time , random , math , sys , pickle , sys

pg.font.init()

screen_width   = 800

screen_height  = 600

picture_width  = 1920

picture_height = 1080

sc = pg.display.set_mode ( ( screen_width , screen_height ) ) 

welcome = 'Browser simulator'

pg.display.set_caption( welcome )

pos = pg.mouse.get_pos()

fontsize = 25

f1 = pg.font.Font( None , fontsize ) 

cancel_icon_width = 25

cancel_icon_height = 25

cancel_icon_x = screen_width - cancel_icon_width 

cancel_icon_y = 5

cancel_icon_image = pg.image.load('картинки/cancel_icon.png')

go_back_icon_image = pg.image.load('картинки/стрелка назад.png')

next_page_icon_image = pg.image.load('картинки/стрелка вперед.png')

search_icon_image = pg.image.load('картинки/search_icon.png')

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

sites = ['https://www.MyVideo.com','https://www.MyFoto.com',]

site = sites[ 0 ]

text_color = ( 180 , 0 , 0 )

text1 = f1.render( sites[0] , True , text_color )

text1_x = 200

text1_y = 50

step = 1

panel_width = screen_width

panel_height = 100

panel_x = 0

panel_y = 0

panel_color = GREY

panel_1_width = 300

panel_1_height = fontsize -5

panel_1_x =text1_x

panel_1_y = text1_y

panel_1_color = WHITE

Fontname = 'serif'

f = pg.font.SysFont( Fontname , fontsize )



def Update():
    sc.fill( BGCOLOR )

    panel = pg.draw.rect( sc , ( panel_color ) , ( panel_x , panel_y , screen_width , panel_height ) )
    panel_1 = pg.draw.rect( sc , ( panel_1_color ) , ( panel_1_x , panel_1_y ,panel_1_width , panel_1_height ) )
    sc.blit( text1 , ( text1_x ,text1_y ) )
    sc.blit(cancel_icon_image , ( cancel_icon_x,cancel_icon_y ) )
    sc.blit(go_back_icon_image , ( 25,50 ) ) 
    sc.blit(next_page_icon_image , (75,50 ) ) 
    sc.blit(search_icon_image , (510,50 ) ) 

    pg.display.update()

while True:

    for event in pg.event.get() :

        pressed = pg.mouse.get_pressed()

        pos = pg.mouse.get_pos()

        if event.type == pg.QUIT :
            sys.exit()

        if event.type == pg.KEYDOWN :

            if event.key == pg.K_1 :
                text1 = f1.render( site  , True , text_color )
                current_color_num = 0

                Update()

            if event.key == pg.K_2 :
                text1 = f1.render(site , True , text_color )
                current_color_num = 1

                Update()

            if event.key == pg.K_3 :
                text1 = f1.render( site    , True , text_color )
                current_color_num = 2

                Update()

            if event.key == pg.K_4 :
                text1 = f1.render( site  , True , text_color )
                current_color_num = 3

                Update()

            if event.key == pg.K_5 :
                text1 = f1.render( site   , True , text_color )
                current_color_num = 4

                Update()

            if event.key == pg.K_6 :
                text1 = f1.render( site , True , text_color )
                current_color_num = 5

                Update()
    
            if event.key == pg.K_c :
                Update()

            if event.key == pg.K_F12 :
                quit()

            if event.key == pg.K_F5 :
                screen_width = 1920
                screen_height = 1080
                sc = pg.display.set_mode ( ( screen_width , screen_height ) )
                welcome = welcome
                pg.display.set_caption( welcome )


        if event.type == pg.MOUSEBUTTONDOWN :

            if event.button == 1:
                pg.display.update()

            if event.button == 2 :

                sc.fill( BGCOLOR )
                
                Update()
