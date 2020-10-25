# Case-study #1
# Developers:   Belozertseva M. (20%),
#               Raspopova A. (60%),
#               Fauzi A. (30%)

import turtle
turtle.speed(40)
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

    #rabbit figure
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
    turtle.left(135)
    triangle(-480, 265, 60, "white", "purple3")
    turtle.right(135)
    turtle.right(90)
    triangle(-510, 415, 60, "white", "maroon1")
    turtle.left(90)
    # fish figure
    turtle.right(45)
    triangle(-150, 600, 120, "white", "red")
    turtle.left(-90)
    triangle(-30, 480, 120, "white", "yellow")
    turtle.left(45)
    triangle(-28, 550, 90, "white", "blue")
    turtle.right(45)
    square(-80, 530, 70, "white", "orange")
    turtle.right(-90)
    parallelogram(-251, 542, 90, 60, "white", "green")
    turtle.right(-90)
    triangle(-189, 417, 60, "white", "maroon1")
    turtle.right(180)
    triangle(-191, 470, 50, "white", "purple3")

    # camel figure
    turtle.right(-135)
    triangle(250, 500, 60, "white", "maroon1")
    square(250, 430, 70, "white", "orange")
    turtle.left(45)
    triangle(200, 310, 120, "white", "yellow")
    turtle.left(-90)
    triangle(80, 500, 120, "white", "red")
    turtle.left(45)
    triangle(80, 500, 85, "white", "blue")
    turtle.left(90)
    parallelogram(130, 360, 90, 60, "white", "green")
    triangle(272, 285, 70, "white", "purple3")
    turtle.right(90)

    # human1 figure
    turtle.right(135)
    square(-540, 200, 60, "white", "orange")
    turtle.left(135)
    turtle.left(45)
    triangle(-570, -5, 120, "white", "red")
    turtle.right(45)
    turtle.left(45)
    parallelogram(-635, -5, 90, 60, "white", "green")
    turtle.right(45)
    turtle.right(135)
    triangle(-540, 25, 120, "white", "yellow")
    turtle.left(135)
    turtle.left(45)
    triangle(-680, -115, 60, "white", "maroon1")
    turtle.right(45)
    turtle.right(90)
    triangle(-540, -35, 90, "white", "blue")
    turtle.left(90)
    turtle.left(90)
    triangle(-540, -195, 60, "white", "purple3")
    turtle.right(90)

    # ship figure
    turtle.left(135)
    triangle(-510, -315, 60, "white", "purple3")
    turtle.right(135)
    turtle.right(90)
    triangle(-570, -315, 120, "white", "red")
    turtle.left(90)
    turtle.right(135)
    triangle(-570, -345, 120, "white", "yellow")
    turtle.left(135)
    turtle.right(135)
    square(-485, -400, 60, "white", "orange")
    turtle.left(135)
    triangle(-570, -485, 60, "white", "maroon1")
    turtle.right(180)
    triangle(-480, -485, 90, "white", "blue")
    turtle.left(180)
    turtle.right(45)
    parallelogram(-660, -485, 90, 60, "white", "green")
    turtle.left(45)

    # helicopter figure
    turtle.left(90)
    triangle(-130, -545, 120, "white", "yellow")
    turtle.right(90)
    turtle.right(90)
    triangle(-130, -375, 120, "white", "red")
    turtle.left(90)
    parallelogram(-130, -375, 90, 60, "white", "green")
    triangle(-255, -375, 90, "white", "blue")
    triangle(-260, -500, 60, "white", "purple3")
    turtle.left(180)
    triangle(-215, -460, 60, "white", "maroon1")
    turtle.right(180)
    turtle.left(45)
    square(-325, -485, 60, "white", "orange")
    turtle.right(45)


    # hhumaan2 figure
    turtle.right(45)
    square(300, 170, 70, "white", "orange")
    triangle(231, 121, 120, "white", "red")
    turtle.right(-90)
    triangle(350, 0, 120, "white", "yellow")
    parallelogram(285, -118, 90, 60, "white", "green")
    turtle.left(90)
    triangle(440, -88, 90, "white", "blue")
    turtle.right(-180)
    triangle(410, -89, 60, "white", "purple3")
    turtle.right(90)
    triangle(310, -95, 60, "white", "maroon1")

    # rocket figure
    turtle.left(135)
    triangle(300, -260, 70, "white", "maroon1")
    turtle.right(45)
    triangle(300, -262, 100, "white", "blue")
    turtle.left(135)
    turtle.left(180)
    triangle(300, -265, 134, "white", "yellow")
    turtle.right(180)
    triangle(395, -552, 134, "white", "red")
    turtle.left(45)
    square(360, -519, 80, "white", "orange")
    turtle.left(-45)
    parallelogram(460, -620, 120, 90, "white", "green")
    turtle.right(-135)
    turtle.left(45)
    triangle(247, -520, 75, "white", "purple3")
    turtle.done()
    turtle.mainloop()


if __name__ == '__main__':
    main()
