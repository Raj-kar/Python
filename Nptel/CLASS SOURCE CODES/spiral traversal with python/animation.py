import turtle
from random import choice
from color import gen_color

spiral = turtle.Turtle()
spiral.speed(10)
spiral.getscreen().bgcolor("black")

spiral.penup()
spiral.goto((-250, 150))
spiral.pendown()


def draw_spiral(size):
    if size == 0:
        return

    spiral.color(gen_color())

    spiral.dot()
    spiral.forward(size)
    spiral.dot()
    spiral.right(90)
    spiral.forward(size)
    spiral.right(90)

    draw_spiral(size - 10)


draw_spiral(400)

turtle.done()
