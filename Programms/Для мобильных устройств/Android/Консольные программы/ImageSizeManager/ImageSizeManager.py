from PIL import Image , ImageChops

run = True

while run:

            print()
            print()
            print()

            print('----')

            print('МЕНЮ')

            print('----')

            print()

            picture_directory = input( 'picture directory : ' )

            picture_name = input( 'picture name : ' )

            image = Image.open( str( picture_directory ) + picture_name )

            newpicture_name = input( 'new picture name : ' )

            picture_directory = input('new picture directory : ' )

            new_picture_width = int( input( 'new picture width : ' ) )

            new_picture_height = int( input( 'new picture height : ' ) )

            image = image.resize( ( int(new_picture_width ) , int( new_picture_height ) ) )

            image.save( str( picture_directory ) + newpicture_name )

            print('----------------------------------------------------------------------------------------------------------')



