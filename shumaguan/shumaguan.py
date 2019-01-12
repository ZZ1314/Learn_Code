import turtle
import time

def drawgap():
    turtle.pu()
    turtle.fd(5)


def drawLine(draw):
    drawgap()
    turtle.pd() if draw else turtle.pu()
    turtle.fd(40)
    drawgap()
    turtle.right(90)


def drawDigit(digit):
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)


def drawDate(date):
    for i in date:
        if i == "-":
            turtle.write("年", font=("Arial", 18, "normal"))
            turtle.color("blue")
        elif i == "=":
            turtle.write("月", font=("Arial", 18, "normal"))
            turtle.color("green")
        elif i == "+":
            turtle.write("日", font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))
        turtle.pu()
        turtle.fd(40)


def main():
    turtle.setup(1000, 350, 200, 200)
    turtle.speed(0)
    turtle.color("red")
    turtle.hideturtle()
    turtle.pu()
    turtle.fd(-400)
    turtle.pensize(5)
    drawDate(time.strftime("%Y-%m=%d+", time.gmtime()))
    turtle.done()


main()
