from turtle import Turtle, Screen

test_turtle = Turtle()
test_turtle.shape("turtle")
screen = Screen()
screen.colormode(255)

def move_forward():
    test_turtle.forward(10)

def move_backward():
    test_turtle.backward(10)

def turn_left():
    #test_turtle.left(10)
    new_heading = test_turtle.heading() + 10
    test_turtle.setheading(new_heading)

def turn_right():
    #test_turtle.right(10)
    new_heading = test_turtle.heading() - 10
    test_turtle.setheading(new_heading)

def clear():
    test_turtle.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()