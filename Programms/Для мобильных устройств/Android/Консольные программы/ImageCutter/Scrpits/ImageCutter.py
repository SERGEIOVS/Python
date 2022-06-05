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


            picture_directory = input('picture directory : ')

            picture_name = input('picture name : ')

            im = Image.open(str(picture_directory) + picture_name)

            newpicture_width1  = int(input('width1  : '))

            newpicture_height1 = int(input('height1 : '))

            newpicture_width2  = int(input('widt2  : '))

            newpicture_height2 = int(input('height2 : '))

            newpicture_name = input('new picture name : ')

            picture_directory = input('new picture directory : ')

            im_crop = im.crop( ( newpicture_width1 , newpicture_height1 , newpicture_width2 , newpicture_height2 ) )

            im_crop.save(str(picture_directory) + newpicture_name )

            print('----------------------------------------------------------------------------------------------------------')




