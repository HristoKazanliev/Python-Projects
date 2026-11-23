from random import Random
from turtle import Turtle, Screen

random = Random()
test_turtle = Turtle()
screen = Screen()

test_turtle.shape("turtle")
test_turtle.color("green")

# Draw a square
# for i in range(4):
#     test_turtle.forward(100)
#     test_turtle.left(90)

# Draw a dashed line
# for i in range(10):
#     test_turtle.forward(10)
#     test_turtle.penup()
#     test_turtle.forward(10)
#     test_turtle.pendown()

# Draw different shapes
# for i in range(3, 11):
#     test_turtle.color(random.random(), random.random(), random.random())
#     for j in range(i):
#         test_turtle.forward(100)
#         test_turtle.right(360 / i)

# Draw random walk
# def forward():
#     test_turtle.forward(100)
#
# def back():
#     test_turtle.back(100)
#
# def left():
#     test_turtle.left(90)
#
# def right():
#     test_turtle.right(90)
#
# movements = [forward, back, right, left]
#
# for steps in range(50):
#     test_turtle.color(random.random(), random.random(), random.random())
#     random.choice(movements)()

# Draw random color
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# screen.colormode(255)
# movements = [0, 90, 180, 270]
#
# for i in range(50):
#     test_turtle.color(random_color())
#     test_turtle.forward(20)
#     test_turtle.setheading(random.choice(movements))

# Draw a spirograph
test_turtle.speed("fastest")

def draw_spirograph(size):
    for i in range(int(360 / size)):
        test_turtle.circle(100)
        current_heading = test_turtle.heading()
        test_turtle.setheading(current_heading + 10)

draw_spirograph(5)

screen.exitonclick()