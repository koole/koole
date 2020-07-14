import bpy
import random

canvas = bpy.data.objects["Plane"]
tree = canvas.active_material.node_tree

noise = tree.nodes["Noise Texture"]
noise.inputs["Scale"].default_value = random.randint(15, 30) / 100

mapping = tree.nodes["Group"]
mapping.inputs["Value"].default_value = random.randint(0, 1000)
