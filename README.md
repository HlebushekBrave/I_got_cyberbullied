# I_got_cyberbullied
Case study 1
Belozertseva Maria, Raspopova Alexandra, Adristi Fauzi
import turtle


def square(x, y, side, color):
    '''
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param side: side length of a square
    :param color: square's color
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
     turtle.begin_fill()
    turtle.color(color)
     turtle.fillcolor(color)
    turtle.down()
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.end_fill()

def main():
    '''
    Main function.
    :return: None
    '''
    square(-200, 200, 180, "blue")
 
    turtle.done()


if __name__ == '__main__':
    main()
