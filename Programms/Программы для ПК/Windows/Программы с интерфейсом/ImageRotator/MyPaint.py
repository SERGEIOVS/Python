from turtle import width
import pygame as pg,datetime,time,random,math,sys,pyautogui,pickle

from PIL import Image

import os

pg.init()

pg.font.init()

vector = [ 0 , 0 ]

pistolmagazine_capacity = 30

pistolmax_magazine_capacity = 300

d1 = datetime.datetime.today()

d1 += datetime.timedelta( hours = 0 )

time_units = [ d1.hour , d1.minute , d1.second ]

current_time_unit = time_units[1] 

screen_width , screen_height= 800 , 600

screen = pg.display.set_mode( ( screen_width , screen_height ) ) 

BGcolors = [ ( 0 , 0 , 255 ) , ( 0 , 0 , 0 ) ]

BGcolor = BGcolors[0]

screen.fill(BGcolor)

Captions = ['Crazy driver simulator']

pg.display.set_caption(Captions[0] )

Icons_list = [ 

pg.image.load('интерфейс/иконки/Game_icon.png') ,

'beltinventorycell' , 'backpackinventorycell' , 'currentinventorycell' , 'achievements_menu' , 'minimap_menu ' , 'cursor_icon ' , 'clock_icon ' , 

'achievements_icon' , 'health_icon ' , 'armor_icon ' , 'current_ammo_icon' , 'button ' , 'MusicIcon ' , 'craft_icon ' , 'energy_icon ' , 'left_pointer ' ,

'right_pointer ' , 'cancel_icon ' , 'cancel_icon1 ' , 'minimap_icon '


]


#pg.display.set_icon(Icons_list[0])

Fontsizes = [ 25 , 15 ]

big_font = pg.font.Font( None , Fontsizes[0] )

small_font = pg.font.Font( None , Fontsizes[1] )



#Показывать  стандартный курсор или или нет
mouse_set_visible = pg.mouse.set_visible( False )

#False - не показывать
#True  - показывать

class cam :

    def __init__( self , x , y ) :
        self.rect = pg.Rect( 2000 , 2000 , 500 , 500 )

    def move( self , vector ) :
        self.rect[ 0 ] += vector[ 0 ]
        self.rect[ 1 ] += vector[ 1 ]

class Player :
    def __init__( self , x , y ) :
        self.rect = pg.Rect( x , y , 10 , 10 ) 

    def move( self , vector ) :
        self.rect[ 0 ] += vector[ 0 ]
        self.rect[ 1 ] += vector[ 1 ]

    def draw( self ) :

        ##  Игрок на самом окне не двигается, двигается мир вокруг него

        pg.draw.rect( screen , ( 0 , 0 , 0 ) , ( 240 , 240 , 10 , 10 ) )


class object :

    ##  Это какой-нибудь объект, отличный игрока (к примеру враг или дерево)

    def __init__( self , x , y , width , height ) :
        self.rect = pg.Rect( x , y , width , height )


    def draw( self ) : 

        ##  Чтобы отрисовка соответствовала позиции объекта его нужно отрисовывать
        ##  на self.rect[0]-camera.rect[0], self.rect[1]-camera.rect[1]

        pg.draw.rect( screen , ( 255 , 0 , 0 ) , ( self.rect[ 0 ] - camera.rect[ 0 ] , self.rect[ 1 ] - camera.rect[ 1 ] , self.rect[ 2 ] , self.rect[ 3 ] ) , 2)

##  P.S. я указывал переменные rect для того, чтобы можно было проверять коллизию между
##  объектами. К примеру: для увеличения производительности, в этой программе отрисовываются лишь те
##  объекты, которые попадают в камеру. (Загугли pg.Rect.colliderect для большего)



environmentsounds = []

soundtracks = [pg.mixer.music.load('Музыка/01 Damned.mp3')]


soundtrack = soundtracks[0]

#environmentsound = environmentsounds[0]

player = Player( 0 , 0)

camera = cam(2,0)

current_ammo = 10

max_current_ammo = 50

achievements_pages = 5

islands_list = []

islands_x_list = [
 
0 , 10000
 
 ]


islands_y_list = [ 
    
0 , 0 

]




Island_types = ['Continent','Continent']

Island_images = [

pg.image.load( 'задний фон/локации/background_1.png' ),

pg.image.load( 'задний фон/локации/background.png' )

]



class Background :
    def __init__( self, x , y , width , height ,type ,  image ) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
        self.image = image

for i in range( len ( islands_x_list) ) :
    i = Background( islands_x_list[i] ,islands_y_list[i] , 5 , 5 ,Island_types[i], Island_images[i] ) 
    islands_list.append( i )



path = 'картинки/hero.png'

im = Image.open(path)

hero_width , hero_height = im.size[0],im.size[1]

hero_x ,hero_y= screen_width /  2 - hero_width  / 2 , screen_height / 2 - hero_height / 2

hero_speed = 3

hero_health , hero_max_health = 10 , 10

hero_armor , hero_max_armor = 10 , 10

hero_angle = 0

hero_image = pg.image.load('картинки/hero.png')

hero_rect = hero_image.get_rect()



cells_num = 10

class interface :
    def __init__( self, x , y , width , height , image ) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

beltinventorycell = interface( screen_width / 2 -cells_num * 50 / 2 , screen_height - 50 , 50 , 50 , pg.image.load( 'интерфейс/иконки/inventory_cell.png' ) )

backpackinventorycell = interface( 710 , 300 , 50 , 50 , pg.image.load( 'интерфейс/иконки/inventory_cell.png' ) )

currentinventorycell = interface( screen_width / 2 -cells_num * 25 , beltinventorycell.y , 50 , 50 , pg.image.load( 'интерфейс/иконки/current_inventory_cell.png' ) )

achievements_menu = interface( 2000 , 100 , 300 , 500 , pg.image.load( 'интерфейс/иконки/achievements_menu.png' ) )

minimap_menu = interface(2000 , 0 , 1500 , 1000 , pg.image.load( 'интерфейс/иконки/mini_map1.png' ) )

cursor_icon = interface( 0 , 0 , 10 , 10 , pg.image.load( 'интерфейс/иконки/crosshair.png' ) )

clock_icon = interface( 900 , 0 , 30 , 30 , pg.image.load( 'интерфейс/иконки/clock_icon.png' ) )

achievements_icon = interface( 3000 , 125 , 30 , 30 , pg.image.load( 'интерфейс/иконки/achievements_icon.png' ) )

health_icon = interface( 0 , screen_height - 50 , 25 , 25 , pg.image.load( 'интерфейс/иконки/health_icon.png' ) )

armor_icon = interface( 0 , screen_height - 25 , 25 , 25 , pg.image.load( 'интерфейс/иконки/armor_icon.png' ) )

current_ammo_icon = interface(0 , screen_height - 75 , 34 , 50 , pg.image.load( 'интерфейс/иконки/pistol_ammo_icon.png' ) )

button = interface(2100,210,200,50,pg.image.load( 'интерфейс/иконки/button.png' ) )

MusicIcon = interface(0,100,30,30,pg.image.load( 'интерфейс/иконки/MusicIcon.png' ) )

craft_icon = interface(2100,125,20,30,pg.image.load( 'интерфейс/иконки/craft_icon.png' ) )

energy_icon = interface( 200 , beltinventorycell.y , 11 , 26 , pg.image.load( 'интерфейс/иконки/energy_icon.png' ) )

left_pointer = interface( achievements_menu.x + 50 , achievements_menu.y + 100 ,20 , 20 , pg.image.load( 'интерфейс/иконки/pointer_left.png' ) )

right_pointer = interface(achievements_menu.x + 200 , achievements_menu.y + 100 , 20 , 20 , pg.image.load( 'интерфейс/иконки/pointer_right.png' ) )

cancel_icon = interface( minimap_menu.x , minimap_menu.y + 25 , 20 , 20 , pg.image.load( 'интерфейс/иконки/cancel_icon.png' ) )

cancel_icon1 = interface( achievements_menu.x + achievements_menu.width - 20 , minimap_menu.y + 25 , 20 , 20 , pg.image.load( 'интерфейс/иконки/cancel_icon.png' ) )

minimap_icon = interface( screen_width - 710 , 1030 , 50 , 50 , pg.image.load( 'интерфейс/иконки/minimap_icon.png' ) )

hero_belt_inventory_cells = []

hero_belt_inventory_cells_x_list = [

screen_width / 2 -cells_num * 50 / 2 + 10  , screen_width / 2 -cells_num * 50 / 2 + 60  , screen_width / 2 -cells_num * 50 / 2 + 110 , screen_width / 2 -cells_num * 50 / 2 + 160 , screen_width / 2 -cells_num * 50 / 2 + 210 ,
screen_width / 2 -cells_num * 50 / 2 + 260 , screen_width / 2 -cells_num * 50 / 2 + 310 , screen_width / 2 -cells_num * 50 / 2 + 360 , screen_width / 2 -cells_num * 50 / 2 + 410 , screen_width / 2 -cells_num * 50 / 2 + 460

]



hero_belt_inventory_cells_y_list = []
hero_belt_inventory_cells_images = []



for i in range( len ( hero_belt_inventory_cells_x_list ) ) :
    hero_belt_inventory_cells_y_list.append(screen_height - 50)
    hero_belt_inventory_cells_images.append(pg.image.load( 'интерфейс/иконки/inventory_cell.png' ))
    i = interface( hero_belt_inventory_cells_x_list[ i ] , hero_belt_inventory_cells_y_list[ i ] , 5 , 5 ,hero_belt_inventory_cells_images[ i ] )
    hero_belt_inventory_cells.append( i )



hero_belt_inventory = []
hero_belt_inventory_items_x_list = [
screen_width / 2 -cells_num * 50 / 2 + 20]
hero_belt_inventory_items_y_list = []
hero_belt_inventory_images = [ pg.image.load( 'предметы/оружие/пистолеты/pistol_turned_right.png' ) ]

for i in range( len ( hero_belt_inventory_items_x_list ) ) :
    hero_belt_inventory_items_y_list.append( screen_height - 40 )
    i = interface( hero_belt_inventory_items_x_list[ i ] , hero_belt_inventory_items_y_list[ i ] , 5  , 5 , hero_belt_inventory_images[ i ] )
    hero_belt_inventory.append( i )


class Vihicles :
    def __init__( self , x , y , width , height , image , speed ) :
        self.x = x
        self.y = y    
        self.width = width
        self.height = height
        self.image = image
        self.speed = speed

vihicles_list = []

vihicles_x_list = [ 

1500  ,  2500  , 3700   , 4500 , 5200 , 9500

]
vihicles_y_list = [

1700  ,  1700  , 1700   , 1700 , 1700 , 3000

]
for i in range( len ( vihicles_x_list ) ) :
    vihicles_images_list = [

pg.image.load( 'техника/citizen_car.png' ) ,

pg.image.load( 'техника/citizen_car.png' ) ,

pg.image.load( 'техника/citizen_car.png' ) ,

pg.image.load( 'техника/police_car.png' ) ,

pg.image.load( 'техника/citizen_truck.png' ) ,

pg.image.load( 'техника/лодка.png' )

]


for i in range( len ( vihicles_x_list ) ) :
    
    i=Vihicles( vihicles_x_list[ i ] , vihicles_y_list[ i ] , 5 , 5 , vihicles_images_list[ i ] , 5 )
    vihicles_list.append( i )


class Buildings :
    def __init__( self , x , y , image , width , height ) :
        self.x = x
        self.y = y    
        self.image = image
        self.width = width
        self.height = height

buildings_list = []

buildings_x_list = [

1000 , 2500 , 3700 , 5000 ,  6500  , 7000 , 9000 , 6000  , 8050 , 1540 , 4000 ,8600 , 3000 ,

1300 , 400 ]

buildings_y_list = [

700  , 700  , 700  , 700  ,  700   , 700  , 1700 , 3000  , 700  , 3540 , 4500 ,5000 , 4000 ,
4800 , 2000 ]

buildings_images_list = [

pg.image.load( 'постройки/кирпичный дом/bedroom.png' ) , 

pg.image.load( 'постройки/кирпичный дом/bedroom.png' ) ,

pg.image.load( 'постройки/кирпичный дом/bedroom.png' ) ,

pg.image.load( 'постройки/база/база.png' ) ,

pg.image.load( 'постройки/дом пришельцев/дом пришельцев.png' ) ,

pg.image.load( 'постройки/полицейский участок/полицейский участок.png' ) ,

pg.image.load( 'задний фон/bridge_road.png' ) , 

pg.image.load( 'постройки/парковки/парковка.png' ) ,

pg.image.load( 'декорации/фонарные столбы/фонарный столб.png' ) ,

pg.image.load( 'задний фон/cave.png' ) ,

pg.image.load( 'задний фон/lake.png' ) ,

pg.image.load( 'постройки/палатка/открытая_палатка.png' ) ,

pg.image.load( 'задний фон/rails.png' ) ,

pg.image.load( 'декорации/Могилы/могила.png' ) , 

pg.image.load( 'декорации/деревья/tree.png' ) 


]

for i in range( len ( buildings_x_list ) ) :
    i = Buildings( buildings_x_list[ i ] , buildings_y_list[ i ] , buildings_images_list[ i ] , 5 , 5 )
    buildings_list.append( i )

class Traps:
    def __init__( self , x , y , image , width , height ) :
        self.x = x
        self.y = y
        self.image= image
        self.width = width
        self.height = height

traps = []

traps_x_list = [ 1000 ]

traps_y_list = [ 3000 ]

traps_images_list = [

pg.image.load( 'ловушки/шипы/шипы.png' ) ]

for i in range( len ( traps_x_list ) ) :
    i = Traps( traps_x_list[ i ] , traps_y_list[ i ] , traps_images_list[ i ] , 5 , 5 )
    traps.append(i)

class Friendly_creatures:
    def __init__( self , x , y , width , height , image , speed , health ) :
        self.x = x
        self.y = y    
        self.width = width
        self.height = height
        self.image = image
        self.speed = speed
        self.health = health

friendly_creatures_list = []

friendly_creatures_x_list = [

1400  , 1700  , 1900   , 2100   , 2300 , 2500 , 2800  , 3700 , 9700 , 2900 , 3100 , 3300 , 400

]

friendly_creatures_y_list = [

3000  , 3000  , 3000   , 3000   , 3000 , 3000 , 3000  , 4000 , 3000 , 3000 , 3000 , 3000 , 400       

] 

friendly_creatures_images_list = [

pg.image.load( 'персонажи/союзники/жители/citizen_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_1_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_2_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_3_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_4_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_5_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/солдаты/soldier_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/погибшие/deadman_left_empty_hands.png' ) ,

pg.image.load( 'персонажи/союзники/рыба/рыба.png' ) ,

pg.image.load( 'персонажи/союзники/солдаты/MG_man_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/нло/alien_turned_right.png' ) ,

pg.image.load( 'персонажи/союзники/нло/alien+rifle_turned_right.png' ) ,

pg.image.load( 'персонажи/союзники/погибшие/dead_man_turned_left.png' ) 

]

for i in range( len ( friendly_creatures_x_list ) ) :
    i = Friendly_creatures( friendly_creatures_x_list[ i ] , friendly_creatures_x_list , 100 , 180 , friendly_creatures_images_list[ i ] , 5 , 5 )
    friendly_creatures_list.append( i )

class Enemies:
    def __init__( self , x , y , width , height , speed , health , image ) : 
        self.x = x
        self.y = y    
        self.width = width
        self.height = height
        self.speed = speed
        self.health = health
        self.image = image

enemies_list = []

enemies_x_list = [

700  , 900   , 1100  , 1300 , 1500 , 3500

]

enemies_y_list = [

2000 , 2000  , 2000  , 2000 , 2000 , 4000

]

enemies_images_list = [

pg.image.load( 'персонажи/противники/thief_run_right.png' ) ,

pg.image.load( 'персонажи/противники/thief1_run_right.png' ) ,

pg.image.load( 'персонажи/противники/mutant1_run_right.png' ) ,

pg.image.load( 'персонажи/противники/Dogman_run_right.png' ) ,

pg.image.load( 'персонажи/противники/hazamat_unit_run_right.png' ) ,

pg.image.load( 'персонажи/противники/yeti_run_right.png' ) 

]

for i in range( len ( enemies_x_list ) ) :
    i =Enemies( enemies_x_list[ i ] ,enemies_y_list[ i ] , 100 , 180 , 5 , 5 , enemies_images_list[ i ] )
    enemies_list.append( i )

class Items:
    def __init__( self , x , y , width , height , image ) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image= image

items_list = []

items_x_list = [ 1400  , 1700  , 1900   , 2100   , 2300 , 2500  , 2800 , 3000  , 3100  , 3200 , 3300 , 3550 , 3700  ]

items_y_list = [ 3500 ,  3500 ,  3500 ,   3500  ,  3500 , 3500  , 3500 , 3500  , 3500  , 3500 , 3500 , 3500 , 3500  ]

items_images_list = [

pg.image.load( 'предметы/оружие/патроны/pistol_ammo.png' ) ,

pg.image.load( 'предметы/оружие/патроны/rifle_ammo.png' ) ,

pg.image.load( 'предметы/инструменты/ящики для инструментов/ящик для инструментов.png' ) ,

pg.image.load( 'предметы/аккумуляторы/аккумулятор_авто.png' ) ,

pg.image.load( 'предметы/зажигалки/газовая_зажигалка.png' ) ,

pg.image.load( 'еда/консервы/консервы(рыба).png' ) ,

pg.image.load( 'предметы/зажигалки/газовая_зажигалка.png' ) ,

pg.image.load( 'еда/сухпай_походный.png' ) ,

pg.image.load( 'напитки/бутылка_воды.png' ) ,

pg.image.load( 'предметы/фонарики/flashlight_turned_right.png' ) ,

pg.image.load( 'предметы/инструменты/топор/axe_turned_right.png' ) ,

pg.image.load( 'предметы/оружие/sniper_rifle.png' ) ,

pg.image.load( 'предметы/оружие/пулемет.png' ) ]

for i in range( len ( items_x_list ) ) :
    i = Items( items_x_list[ i ] , items_x_list[ i ] , 5 , 5 ,items_images_list[ i ] ) 
    items_list.append( i )

pos = pg.mouse.get_pos()



show_health = big_font.render( str( hero_health )  + "/" + str( hero_max_health ) , False , ( 255 , 0 , 0 ) )

show_hero_armor = big_font.render( str( hero_armor ) + "/" +  str( hero_max_armor ) , False , ( 250 , 0, 0 ) )

current_ammo_counter = big_font.render( str( current_ammo ) + "/" + str( max_current_ammo ) , False , ( 250 , 0 , 0 ) )

show_time = big_font.render( ' Время : ' + str( d1.hour ) + " : " + str( d1.minute ) + " : " + str( d1.second ) , False , ( 250 , 0 , 0 ) )



d1 = datetime.datetime.today()

d1 += datetime.timedelta( hours = 0 )


currentinventorycell_number = 1

intreface_icons_list = [ left_pointer , right_pointer , cancel_icon , cancel_icon1 , minimap_menu , minimap_icon ]



def make_screenshot() :
    screenshot = pyautogui.screenshot()
    screenshot.save( 'скриншоты/test' + str( i ) + '.png' )



def draw_level() :

    d1 = datetime.datetime.today()

    show_time = big_font.render( ' Время : ' + str( d1.hour )+ ":" + str( d1.minute ) + ":" + str( d1.second ) , False , ( 250 , 0 , 0 ) )
    for i in range( len ( islands_x_list ) ) :
        screen.blit( Island_images[i] ,   ( -camera.rect[ 0 ] + islands_x_list[i]  , -camera.rect[ 1 ] + islands_y_list[i] ) )

    for i in range( len ( vihicles_list ) ) :
        screen.blit( vihicles_images_list[ i ] , ( -camera.rect[ 0 ] + vihicles_x_list[ i ] , -camera.rect[ 1 ] + vihicles_y_list[ i ] ) ) 

    for i in range( len ( buildings_list ) ) :
        screen.blit( buildings_images_list[ i ] , ( -camera.rect[ 0 ] + buildings_x_list[ i ] , -camera.rect[ 1 ] + buildings_y_list[ i ] ) ) 
    
    screen.blit( hero_image , ( hero_x,hero_y ) )
    hero_rect = hero_image.get_rect()

    for i in range( len ( friendly_creatures_list ) ) :
        screen.blit( friendly_creatures_images_list[i] , ( -camera.rect[ 0 ] + friendly_creatures_x_list[ i ] , -camera.rect[ 1 ] + friendly_creatures_y_list[ i ] ) )   

    for i in range( len ( enemies_list ) ) :
        screen.blit( enemies_images_list[ i ] , ( -camera.rect[ 0 ] + enemies_x_list[ i ] , -camera.rect[ 1 ] + enemies_y_list[ i ] ) ) 

    for i in range(len(items_list ) ) :
        screen.blit(items_images_list[ i ] , ( -camera.rect[ 0 ] + items_x_list[ i ] , -camera.rect[ 1 ] +items_y_list[ i ] ) ) 

    for i in range( len ( traps ) ) :
        screen.blit( traps_images_list[ i ] , ( -camera.rect[ 0 ] + traps_x_list[ i ] , -camera.rect[ 1 ] + traps_y_list[ i ] ) )  

    for i in range( len ( hero_belt_inventory_cells_x_list ) ) : 
        screen.blit ( hero_belt_inventory_cells_images[ i ] , ( hero_belt_inventory_cells_x_list[ i ] ,  hero_belt_inventory_cells_y_list[ i ] ) )

    for i in range( len ( hero_belt_inventory_items_x_list ) ) :
        screen.blit ( hero_belt_inventory_images[ i ] , ( hero_belt_inventory_items_x_list[ i ] ,  hero_belt_inventory_items_y_list[ i ] ) )

    screen.blit( armor_icon.image , ( armor_icon.x , armor_icon.y ) )

    screen.blit( show_hero_armor , (armor_icon.x + armor_icon.width, armor_icon.y ) )

    screen.blit( health_icon.image , (health_icon.x, health_icon.y ) )

    screen.blit( show_health , ( health_icon.x + health_icon.width , beltinventorycell.y ) )

    screen.blit( current_ammo_icon.image , (current_ammo_icon.x , current_ammo_icon.y ) )

    screen.blit( current_ammo_counter , ( current_ammo_icon.x + current_ammo_icon.width , current_ammo_icon.y ) )

    for i in range( 5 ) :
        screen.blit( button.image , ( button.x , button.y + i * button.height * 2 ) )



    screen.blit( show_time , ( screen_width / 2  - len(str(show_time))  , Fontsizes[0] / 2 ) ) 

    show_time = big_font.render( 'Время : ' + str( d1.hour ) + ":" + str( d1.minute )+ ":" + str( d1.second ) , False,( 250 , 0 , 0 ) ) 



run = True

while run :
    
    vector = [ 0 , 0 ]

    for event in pg.event.get() :
        if event.type == pg.MOUSEMOTION :
            pos = pg.mouse.get_pos()

            screen.blit( cursor_icon.image , ( pos[ 0 ] , pos[ 1 ] ) )

            pg.display.update()
            pressed = pg.mouse.get_pressed()
            pos = pg.mouse.get_pos()

            if pressed[ 0 ] and currentinventorycell.x == beltinventorycell.x + beltinventorycell.width * 4 :
                current_ammo -= 1
                current_ammo_counter = big_font.render( str( current_ammo ) + "/" + str( max_current_ammo ) , False , ( 250 , 0, 0 ) ) 
                click_sound = pg.mixer.Sound( 'Звуки/pistol_shot.wav' )
                click_sound.play()



        if event.type == pg.MOUSEBUTTONDOWN :
            if event.button == 1 and current_ammo > 0 :
                current_ammo -= 1
                current_ammo_counter = big_font.render( str( current_ammo ) + "/" + str( max_current_ammo ) , False , ( 250 , 0 , 0 ) )
                gun_shot = pg.mixer.Sound( 'Звуки/pistol_shot.wav' )
                gun_shot.play()

            for i in enemies_list :
                if current_ammo > 0 and  event.button == 1 and  pos[ 0 ] >= i.x and pos[ 0 ] <= i.x + i.width and pos[ 1 ] >= i.y and pos[ 1 ] <= i.y \
                    + i.height and i.health > 0 :
                    i.image = pg.image.load( 'персонажи/союзники/солдаты/soldier_dead_left.png' )
                    i.speed = 0
                    i.health = 0

                if event.button == 3 and pos[ 0 ] >= minimap_icon.x and pos[ 0 ] <= minimap_icon.x + minimap_icon.width \
                        and pos[ 1 ] >= minimap_icon.y and pos[ 1 ] <= minimap_icon.y + minimap_icon.height :
                    minimap_menu.x =  screen_width / 2 - minimap_menu.width / 2
                    minimap_menu.y = screen_height / 2 - minimap_menu.height / 2
                    cancel_icon.x = minimap_menu.x + minimap_menu.width - 50
                    cancel_icon.y = minimap_menu.y + 25

                if event.button == 3 and pos[ 0 ] >= cancel_icon.x and pos[ 0 ] <= cancel_icon.x + cancel_icon.width \
                        and pos[ 1 ] >= cancel_icon.y and pos[ 1 ] <= cancel_icon.y + cancel_icon.height :
                    minimap_menu.x = 2000
                    cancel_icon.x = 2000

            if pos[ 0 ] >= button.x and pos[ 0 ] <= button.x + button.width and pos[1] >= button.y and pos[1] <= button.y + button.height :
                pg.mixer.music.play()

            if pos[ 0 ] >= MusicIcon.x and pos[ 0 ] <= MusicIcon.x + MusicIcon.width and pos[ 1 ] >= MusicIcon.y and pos[ 1 ] <= MusicIcon.y + MusicIcon.height :
                MusicIcon.Image = pg.image.load( 'интерфейс/иконки/NoMusicIcon.png' )
                pg.mixer.music.stop()

            if event.button == 1 and current_ammo <= 0 :
                current_ammo = 0
                current_ammo_counter = big_font.render( str( current_ammo ) + "/" + str( max_current_ammo ) , False , ( 255 , 0 , 0 ) ) 
                no_ammo = pg.mixer.Sound( 'Звуки/no_ammo.wav' )
                no_ammo.play()



            if event.button == 4 :  #колесо мыши от себя
                currentinventorycell_number  += 1
                currentinventorycell.x += beltinventorycell.width
                select1 = pg.mixer.Sound( 'Звуки/select1.wav' )
                select1.play()

            if currentinventorycell.x <= beltinventorycell.x :
                currentinventorycell.x = beltinventorycell.x + beltinventorycell.width

            if event.button == 5 : #олесо мыши на себя
                currentinventorycell_number -= 1
                currentinventorycell.x -= beltinventorycell.width
                select1 = pg.mixer.Sound( 'Звуки/select1.wav' )
                select1.play()

            if currentinventorycell.x >= beltinventorycell.x + ( beltinventorycell.width +  400 ) :
                currentinventorycell.x = beltinventorycell.x + ( beltinventorycell.width +  400 )

            if currentinventorycell.x <= beltinventorycell.x :
                currentinventorycell.x = beltinventorycell.x

        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_a] :
        vector[ 0 ] -= hero_speed

    if keys[pg.K_a] and keys[pg.K_LSHIFT] :
        vector[ 0 ] -= hero_speed

    if keys[pg.K_d] :
        vector[ 0 ] += hero_speed

    if keys[pg.K_d] and keys[pg.K_LSHIFT] :
        vector[ 0 ] += hero_speed

    if keys[pg.K_w] :
        vector[ 1 ] -= hero_speed


    if keys[pg.K_s] :
        vector[ 1 ] += hero_speed
    
    if keys[pg.K_q] :
        hero_angle += 1
        hero_image_rect = hero_image.get_rect(center = (screen_width /2 , screen_height / 2 ))
        im_rotate = im.rotate(hero_angle, center=(hero_width / 2, hero_height / 2))
        im_rotate.save('картинки/hero.png')
        hero_image = pg.image.load('картинки/hero.png')        

        """
        hero_image_rect = hero_image.get_rect(center = (screen_width /2 , screen_height / 2 ),width = 60,height = 60)
        im_rotate = im.rotate(hero_angle, center=(hero_width / 2, hero_height / 2))
        im_rotate.save('картинки/hero.png')
        hero_image = pg.image.load('картинки/hero.png')        
        
        """





    if keys[pg.K_e]:
        hero_angle -= 1
        hero_image_rect = hero_image.get_rect(center = (screen_width /2 , screen_height / 2 ),width = 60,height = 60)
        im_rotate = im.rotate(hero_angle, center=(hero_width / 2, hero_height / 2))
        im_rotate.save('картинки/hero.png')
        hero_image = pg.image.load('картинки/hero.png')        
        

    if keys[pg.K_SPACE] :
        pass


        ##  Если игрок ходил
    if vector != [ 0 , 0 ] :
        player.move( vector )
        camera.move( vector )


    


    if keys [pg.K_F5] :
        make_screenshot()

    if keys [pg.K_r]:
        reload = pg.mixer.Sound( 'Звуки/reload.wav' )
        reload.play()
        current_ammo = 10
        current_ammo_counter = big_font.render( str( current_ammo ) + "/" + str( max_current_ammo ) , False , ( 250 , 0 , 0 ) )

    if keys [pg.K_F12] :
        pg.quit()




            
    screen.fill( BGcolor )

    draw_level()
    
    pg.display.update()








