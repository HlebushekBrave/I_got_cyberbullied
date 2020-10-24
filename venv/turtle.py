# Case-study #1
# Developers:   Belozertseva M. (%),
#               Raspopova S. (%),
#               Fauzi A. (%)

import turtle


def parallelogram(x, y, a, b, color1, color2):

    """
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
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
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
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


def main():

    """
    Main function
    :return: None
    """

    parallelogram(0, 0, 100, 60, "black", "orange")
    square(200, 200, 100, "black", "blue")
    turtle.done()
    turtle.mainloop()


if __name__ == '__main__':
    main()
