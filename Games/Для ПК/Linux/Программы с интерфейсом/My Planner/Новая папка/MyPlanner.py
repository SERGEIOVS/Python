import pygame as pg , pyautogui , time , random , math , sys , pickle , sys

pg.font.init()

screen_width , screen_height  = 800 , 600

picture_width , picture_height = 1920 , 1080

sc = pg.display.set_mode ( ( screen_width , screen_height ) ) 

Icons_list = [ 

pg.image.load('интерфейс/иконки/icon.png') ,

'beltinventorycell' , 'backpackinventorycell' , 'currentinventorycell' , 'achievements_menu' , 'minimap_menu' , 'cursor_icon' , 'clock_icon' , 'button' , 
'left_pointer' ,'right_pointer' , 'cancel_icon' , 'cancel_icon1'

]


pg.display.set_icon(Icons_list[0])

captions = ['My planner']

caption = captions[0]

pg.display.set_caption(caption)

pos = pg.mouse.get_pos()


radius , radius1 = 10 , 10

rect_width , rect_height = 50 , 50

line_width1 , line_width2 = 50 , 0

horizontal_offset , vertical_offset= 10 , 10

cancel_icon_x , cancel_icon_y = screen_width - 50 , 10

cancel_icon_width , cancel_icon_height = 25 , 25

draw_dist = 25

cancel_icon_image = pg.image.load('интерфейс/иконки/cancel_icon.png')

pos = pg.mouse.get_pos()

Colors = [

#Цвета радуги в rgb
( 255 , 0 , 0 ) , ( 255 , 125 , 0 ) , ( 255 , 255 , 0 ) , ( 0 , 225 , 0 ) , ( 0 , 125 , 255 ) , ( 0 , 0 , 255 ) , ( 128 , 0 , 255 ),



#Дополнительные цвета
( 255 , 255 , 255 ) , ( 0 , 255 , 0 ) , ( 128 , 128 , 0 ) , ( 128 , 128 , 128 ) , ( 0 , 0 , 0 ) , ( 101 , 67 , 33 ) , ( 0 , 255 , 255 ) , ( 192 , 192 , 192 ) , ( 255 , 0 ,255 ),

( 255 , 215 , 0 )

]

Fontsizes = [ 35 , 25 , 15 ]

fontsize = Fontsizes[0]

Fontnames = [

#нижний регистр	
'serif','academy engraved let','algerian','amaze','arial','arial black','balthazar','bankgothic lt bt','bart','bimini','book antiqua','bookman old style','braggadocio',
'britannic bold','brush script mt','calibri','cambria','candara','century gothic','century schoolbook','chasm','chicago','colonna mt','comic sans ms',
'commercialscript bt','consolas','constantia','coolsville','corbel','courier','courier new','cursive','dayton','desdemona','estrangelo edessa','fantasy','flat brush',
'footlight mt light','franklin gothic medium','futurablack bt','futuralight bt','gabriola','garamond','gautami','gaze','geneva','georgia','georgia italic impact',
'geotype tt','helterskelter','helvetica','herman','highlight let','impact','jester','joan','john handy let','jokerman let','kelt','kids','kino mt',
'la bamba let','latha','lithograph','lucida console','lucida sans console','lucida sans unicode','map symbols','marlett','matteroffact','matisse itc',
'matura mt script capitals','mekanik let','modern','modern ms sans serif','monaco','monospace','monotype sorts','ms linedraw','ms sans serif','ms serif','mv boli',
'new york','nyala','olddreadfulno7 bt','orange let','palatino','palatino linotype','playbill','pump demi bold let','puppylike','roland','roman','sans-serif','script',
'scripts','scruff let','segoe print','segoe script','segoe ui','serif','short hand','signs normal','simplex','simpson','small fonts',
'stylus bt','superfrench','surfer','swis721 bt','swis721 blkoul bt','symap','symbol (symbol)','tahoma','technic','tempus sans itc','terk','times','times new roman',
'trebuchet ms','trendy','txt','tunga','verdana','victorian let','vineta bt','vivian','webdings (webdings)','western','westminster','westwood let','wide latin',
'wingdings (wingding)','zapfellipt bt',



#ВЕРХНИЙ РЕГИСТР
'ACADEMY ENGRAVED LET','ALGERIAN','AMAZE','ARIAL','ARIAL BLACK','BALTHAZAR','BANKGOTHIC LT BT','BART','BIMINI','BOOK ANTIQUA','BOOKMAN OLD STYLE','BRAGGADOCIO',
'BRITANNIC BOLD','BRUSH SCRIPT MT','CALIBRI','CAMBRIA','CANDARA','CENTURY GOTHIC','CENTURY SCHOOLBOOK','CHASM','CHICAGO','COLONNA MT','COMIC SANS MS',
'COMMERCIALSCRIPT BT','CONSOLAS','CONSTANTIA','COOLSVILLE','CORBEL','COURIER','COURIER NEW','CURSIVE','DAYTON','DESDEMONA','ESTRANGELO EDESSA','FANTASY','FLAT BRUSH',
'FOOTLIGHT MT LIGHT','FRANKLIN GOTHIC MEDIUM','FUTURABLACK BT','FUTURALIGHT BT','GABRIOLA','GARAMOND','GAUTAMI','GAZE','GENEVA','GEORGIA','GEORGIA ITALIC IMPACT',
'GEOTYPE TT','HELTERSKELTER','HELVETICA','HERMAN','HIGHLIGHT LET','IMPACT','JESTER','JOAN','JOHN HANDY LET','JOKERMAN LET','KELT','KIDS','KINO MT','LA BAMBA LET',
'LATHA','LITHOGRAPH','LUCIDA CONSOLE','LUCIDA SANS CONSOLE','LUCIDA SANS UNICODE','MAP SYMBOLS','MARLETT','MATTEROFFACT','MATISSE ITC','MATURA MT','MEKANIK LET',
'MODERN','MODERN MS SANS SERIF','MONACO','MONOSPACE','MONOTYPE SORTS','MS LINEDRAW','MS SANS SERIF','MS SERIF','MV BOLI','NEW YORK','NYALA','OLDDREADFULNO7 BT',
'ORANGE LET','PALATINO','PALATINO LINOTYPE','PLAYBILL','PUMP DEMI BOLD LET','PUPPYLIKE','ROLAND','ROMAN','SANS-SERIF','SCRIPT','SCRIPTS','SCRUFF LET','SEGOE PRINT',
'SEGOE SCRIPT','SEGOE UI','SERIF','SHORT HAND','SIGNS NORMAL','SIMPLEX','SIMPSON','SMALL FONTS','STYLUS BT','SUPERFRENCH','SURFER','SWIS721 BT','SWIS721 BLKOUL BT',
'SYMAP','SYMBOL (SYMBOL)','TAHOMA','TECHNIC','TEMPUS SANS ITC','TERK','TIMES','TIMES NEW ROMAN','TREBUCHET MS','TRENDY','TXT','TUNGA','VERDANA','VICTORIAN LET',
'VINETA BT','VIVIAN','WEBDINGS (WEBDINGS)','WESTERN','WESTMINSTER','WESTWOOD LET','WIDE LATIN','WINGDINGS (WINGDINGS)','ZAPFELLIPT BT'

]



Fontname = Fontnames[0]

f = pg.font.SysFont( Fontname , fontsize )


big_font = pg.font.Font( None , Fontsizes[0] )

middle_font = pg.font.Font( None , Fontsizes[1] )

small_font = pg.font.Font( None , Fontsizes[2] )


f1 = pg.font.Font( None , fontsize ) 

text_color = Colors[3]

main_color = Colors[ 1 ]

BGCOLOR = Colors[7]



measure_units = ['Добавить' , 'Подробнее' , 'Обновить' , 'Удалить'   ]

measure_unit = measure_units[ 0 ]

text1 = f1.render( measure_unit   + ' | ' , True , text_color )


class interface :
    def __init__( self, x , y , width , height , image ) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

beltinventorycell = interface( screen_width / 2 , screen_height - 50 , 50 , 50 , pg.image.load( 'интерфейс/иконки/inventory_cell.png' ) )
backpackinventorycell = interface( 710 , 300 , 50 , 50 , pg.image.load( 'интерфейс/иконки/inventory_cell.png' ) )
currentinventorycell = interface( screen_width / 2 , beltinventorycell.y , 50 , 50 , pg.image.load( 'интерфейс/иконки/current_inventory_cell.png' ) )
clock_icon = interface( 900 , 0 , 30 , 30 , pg.image.load( 'интерфейс/иконки/clock_icon.png' ) )
button = interface(2100,210,200,50,pg.image.load( 'интерфейс/иконки/button.png' ) )
left_pointer = interface(  50 ,  100 ,20 , 20 , pg.image.load( 'интерфейс/иконки/pointer_left.png' ) )
right_pointer = interface( 200 ,  100 , 20 , 20 , pg.image.load( 'интерфейс/иконки/pointer_right.png' ) )

colors_max = len( Colors )

step = 1


def make_screenshot() :
    screenshot = pyautogui.screenshot('снимки экрана/screenshot.png' , region = ( 0 , 0 , picture_width , picture_height ) )

sc.fill( BGCOLOR )

def Update():
    for i in range(1):
        panel_x1 , panel_y1 = 0 , 0
        panel_x2 , panel_y2 = screen_width , 80
        panel = pg.draw.rect( sc , (Colors[0]) , ( panel_x1 , panel_y1 , panel_x2 , panel_y2 ) )
    sc.blit( text1 , ( 20 , 50 ) )
    sc.blit(cancel_icon_image , ( cancel_icon_x,cancel_icon_y ) ) 
    pg.display.update()



while True:
    
    for event in pg.event.get() :
        pressed = pg.mouse.get_pressed()
        pos = pg.mouse.get_pos()

        if event.type == pg.QUIT :
            sys.exit()

        if event.type == pg.KEYDOWN :

            if event.key == pg.K_1:
                main_color = Colors[ 0 ]
                text1 = f1.render( measure_unit + str( radius )  , True , text_color )
                current_color_num = 0
                Update()

            if event.key == pg.K_s :
                make_screenshot()

            if event.key == pg.K_F12 :
                quit()

            if event.key == pg.K_b :
                BGCOLOR = main_color

        if event.type == pg.MOUSEBUTTONDOWN :
            if event.button == 1:
                pg.draw.rect(sc, main_color, ( pos[ 0 ] - rect_width / 2 , pos[ 1 ] - rect_height / 2  , rect_width, rect_height ) )
                pg.display.update()
            if event.button == 2 :
                sc.fill( BGCOLOR )
                Update()
