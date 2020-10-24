import turtle
turtle.speed(10)
turtle.screensize(1500, 1500)
turtle.width(2)


def parallelogram(x, y, a, b, color1, color2):

    """
    Function, drawing parallelogram.
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param a: first side length of a parallelogram
    :param b: second side length of a parallelogram
    :param color1: parallelogram border color
    :param color2: parallelogram inner color
    :return: None
    """

    turtle.color(color1, color2)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(45)
    turtle.forward(b)
    turtle.left(135)
    turtle.forward(a)
    turtle.left(45)
    turtle.forward(b)
    turtle.left(135)
    turtle.end_fill()
    turtle.penup()


def square(x, y, side, color1, color2):

    """
    Function, drawing square.
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param side: side length of a square
    :param color1: square's border color
    :param color2: square's inner color
    :return: None
    """

    turtle.up()
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.color(color1, color2)
    turtle.down()
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.end_fill()


def triangle(x, y, length, color1, color2):

    """
    Function, drawing triangle
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param length: side length of a triangle
    :param color1: triangle border color
    :param color2: triangle inner color
    """

    turtle.up()
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.color(color1, color2)
    turtle.down()
    turtle.left(45)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(135)
    turtle.goto(x, y)
    turtle.right(180)
    turtle.end_fill()
    turtle.penup()


def main():

    """
    Main function
    :return: None
    """

#First figure
    turtle.right(45)
    parallelogram(-600, 600, 90, 60, "white", "green")
    turtle.left(45)
    square(-510, 475, 60, "white", "orange")
    turtle.right(135)
    triangle(-510, 505, 120, "white", "red")
    turtle.left(135)
    turtle.left(45)
    triangle(-630, 265, 120, "white", "yellow")
    turtle.right(45)
    turtle.right(135)
    triangle(-540, 355, 90, "white", "blue")
    turtle.left(135)
    turtle.done()
    turtle.mainloop()


if __name__ == '__main__':
    main()
