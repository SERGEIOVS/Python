"""
#import bpy
#input = int(input('enter a num:'))
#bpy.data.objects.remove(bpy.data.objects[input])
#bpy.ops.mesh.primitive_cube_add()

#import bpy
#input = int(input('enter a num:'))
#bpy.data.objects.remove(bpy.data.objects[input])
#bpy.ops.mesh.primitive_cube_add()

if action == 'add':

	objtype = input('enter a type : ')

	num=int(input('enter a num : '))

	for i in range(num):

		if objtype == 'cube':

			bpy.ops.mesh.primitive_cube_add()


if action == 'del':

	objtype = input('enter a type : ')
	num=int(input('enter a num : '))

	for i in range(num):
		if objtype == 'cube':
			bpy.data.objects.remove(bpy.data.objects[objtype])

            
"""

