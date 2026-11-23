import colorgram
from turtle import Turtle, Screen
import random

# rgb_colors = []
# colors = colorgram.extract("20_001.jpg", 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

#print(rgb_colors)

colors_list = [(229, 228, 226), (225, 222, 224), (199, 175, 117), (125, 36, 24), (169, 106, 56), (186, 158, 52), (206, 219, 210), (5, 57, 84), (222, 224, 227), (109, 67, 84), (41, 36, 35), (111, 161, 175), (20, 122, 175), (64, 153, 137), (88, 141, 55), (75, 39, 47), (9, 67, 47), (182, 97, 79), (133, 40, 43), (179, 201, 186)]
test_turtle = Turtle()
test_turtle.shape("turtle")

screen = Screen()
screen.colormode(255)

for step in range(10):
    test_turtle.dot(20, random.choice(colors_list))
    test_turtle.forward(100)

screen.exitonclick()