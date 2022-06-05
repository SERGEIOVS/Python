import pygame as pg , pyautogui , time , random , math , sys , pickle , sys

pg.font.init()

screen_width   = 1600

screen_height  = 800

picture_width  = 1920

picture_height = 1080

sc = pg.display.set_mode ( ( screen_width , screen_height ) ) 

welcome = 'MyPythonMusicPlayer'

pg.display.set_caption( welcome )

pos = pg.mouse.get_pos()

fontsize = 25

f1 = pg.font.Font( None , fontsize ) 

cancel_icon_width , cancel_icon_height = 25 , 25

cancel_icon_x , cancel_icon_y = screen_width - cancel_icon_width , 5



cancel_icon_image = pg.image.load('картинки/cancel_icon.png')

go_back_icon_image = pg.image.load('картинки/стрелка назад.png')

next_page_icon_image = pg.image.load('картинки/стрелка вперед.png')

search_icon_image = pg.image.load('картинки/search_icon.png')

pos = pg.mouse.get_pos()



WHITE = (255 , 255 , 255) ; RED = (255 , 0 , 0) ; ORANGE = (255 , 125 , 0) ; YELLOW  = (255 , 255 , 0)  ; GREEN = (0 , 225 , 0) ; LIGHT_BLUE = (0 , 125 , 255) ; 
BLUE = (0 , 0 , 255) ; PURPLE  = (128 , 0 , 255)

LIME = (0 , 255 , 0) ; OLIVE = (128 , 128 , 0) ; GREY    = (128 , 128 , 128) ; BLACK   = (0 , 0 , 0) ; BROWN  = (101 , 67 , 33) ; AQUA    = (0 , 255 , 255) ; 
SILVER  = (192 , 192 , 192) ; MAGENTA = (255 , 0 ,255) ; GOLD = (255 , 215 , 0) ; 

BGCOLOR = WHITE

path = ['folder = ' + 'Music']

site = path[ 0 ]

text_color = ( 180 , 0 , 0 )

text1 = f1.render( path[ 0 ] , True , text_color )

text2 = f1.render('Performers' , True , text_color )

text3 = f1.render('Tracks' , True , text_color )

text1_x , text1_y = 200 , 50

step = 1

panel_width , panel_height = screen_width , 100

panel_x,panel_y = 0 , 0

panel_color = GREY

panel_1_width,panel_1_height = 300 , fontsize -5

panel_1_x  , panel_1_y = text1_x , text1_y

panel_1_color = WHITE

Fontname = 'serif'

next_page_icon_image_width , next_page_icon_image_height= 15 , 15

f = pg.font.SysFont( Fontname , fontsize )

def Update():

    sc.fill( BGCOLOR )

    panel = pg.draw.rect( sc , ( panel_color ) , ( panel_x , panel_y , screen_width , panel_height ) )
    panel_1 = pg.draw.rect( sc , ( panel_1_color ) , ( panel_1_x , panel_1_y ,panel_1_width , panel_1_height ) )
    panel_2 = pg.draw.rect( sc , ( panel_color ) , ( 0 , 0 ,200 , screen_height ) )
    sc.blit( text1 , ( text1_x , text1_y ) )
    sc.blit( text2 , ( 25 , 100 ) )
    sc.blit( text3 , ( 200 , 100 ) )
    sc.blit(cancel_icon_image , ( cancel_icon_x,cancel_icon_y ) )
    sc.blit(go_back_icon_image , ( 220 , 25 ) ) 
    sc.blit(next_page_icon_image , ( 250 , 25) ) 
    sc.blit(search_icon_image , ( 510 , 50 + panel_1_height / 2  - next_page_icon_image_height / 2  ) )
    ( sc , (0 , 0 , 0) , ( 0 , 0 ,100 ,100 ) )

    pg.display.update()

while True:

    for event in pg.event.get() :

        pressed = pg.mouse.get_pressed()

        pos = pg.mouse.get_pos()

        if event.type == pg.QUIT :
            sys.exit()

        if event.type == pg.KEYDOWN :

            if event.key == pg.K_p :
                Update()

            if event.key == pg.K_s :
                Update()
            
            if event.key == pg.K_m :
                Update()
            
            if event.key == pg.K_u :
                Update()

            if event.key == pg.K_F12 :
                quit()

        if event.type == pg.MOUSEBUTTONDOWN :

            if event.button == 2 :
                Update()
