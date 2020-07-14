import bpy
import random

o  = bpy.data.objects['Plane'] # Replace with your actual object's name
t  = o.active_material.node_tree
noise = t.nodes['Noise Texture']
noise.inputs['Scale'].default_value = random.randint(15, 30) / 100

mapping = t.nodes['Group']
mapping.inputs['Value'].default_value = random.randint(0, 1000)