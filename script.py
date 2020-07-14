import bpy
import random

canvas = bpy.data.objects["Plane"]
tree = canvas.active_material.node_tree

scale = random.randint(15, 30) / 100
noise = tree.nodes["Noise Texture"]
noise.inputs["Scale"].default_value = scale

noise = tree.nodes["Noise Texture.001"]
noise.inputs["Scale"].default_value = scale

mapping = tree.nodes["Group"]
mapping.inputs["Value"].default_value = random.randint(0, 1000)
