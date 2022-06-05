import bpy

coordslist = []

action = input('What? : ')

if action == 'add':
    
	objtype = input('enter a type : ')

	num = int(input('enter a num : '))



if objtype == 'cube':
    
    mysize = int(input('enter a size : '))
    
    my_location_x = int(input('enter a location X : '))
    
    my_location_y = int(input('enter a location  Y : '))
    
    my_location_z = int(input('enter a location  Z : '))
    
    
    my_rotation_x = int(input('enter a rotation X : '))
    
    my_rotation_y = int(input('enter a rotation Y : '))
    
    my_rotation_z = int(input('enter a rotation Z : '))
    
    
    for i in range(num):
        
        bpy.ops.mesh.primitive_cube_add(size = mysize , location = (my_location_x , my_location_y , my_location_z) , rotation = (my_rotation_x , my_rotation_y , my_rotation_z) )




if objtype == 'rect':

    my_lenght = int(input('enter a lenght : ') )

    my_width = int(input('enter a width : ') )
    
    my_height = int(input('enter a height : ') )
    
    
    my_location_x = int(input('enter a location X : '))
    
    my_location_y = int(input('enter a location  Y : '))
    
    my_location_z = int(input('enter a location  Z : '))
    
    
    my_rotation_x = int(input('enter a rotation X : '))
    
    my_rotation_y = int(input('enter a rotation Y : '))
    
    my_rotation_z = int(input('enter a rotation Z : '))
    
    
    
    for i in range(num):
        
        bpy.ops.mesh.primitive_cube_add(scale = (my_lenght , my_width , my_height  ) , location =(my_location_x , my_location_y , my_location_z ) )
        
        
        
            
            
if objtype == 'circle':
    
    myradius = int(input('enter a radius : '))
    
    for i in range(num):
        
        bpy.ops.mesh.primitive_circle_add(radius = myradius)
    

    
if objtype == 'plane':

    bpy.ops.mesh.primitive_plane_add()
        

if objtype == 'torus':

    bpy.ops.mesh.primitive_torus_add()
    

if objtype == 'uv':

    bpy.ops.mesh.primitive_uv_sphere_add(radius = mysize)

    

if objtype == 'ico':

    bpy.ops.mesh.primitive_ico_sphere_add(radius = mysize)
        
        
        
if objtype == 'cylinder':
    
    bpy.ops.mesh.primitive_cylinder_add(radius = mysize)
        
        
    if objtype == 'cone':
        
        bpy.ops.mesh.primitive_cone_add()
        
        
        
if action == 'del':

	objtype = input('enter a type : ')

	num = int(input('enter a num : ') )

	for i in range(num):
    
		if objtype == 'cube':
    
			bpy.data.objects.remove(bpy.data.objects[objtype] )



            


