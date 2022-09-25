import turtle as t
import random

tim = t.Turtle()

colours = ["medium aquamarine", "DarkOrchid", "CornflowerBlue", "DeepSkyBlue", "wheat"]


def draw_shap(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shap(shape_side_n)
