import turtle

def star(color, sides, length, angle, distance):
    galileo = turtle.Turtle()
    galileo.color(color)  # colorful!
    galileo.width(4)  # visible!
    galileo.speed(0)  # fast!
    galileo.penup()
    galileo.left(angle)  # away from center
    galileo.forward(distance)
    galileo.pendown()  # start drawing
    for side in range(sides):
        galileo.forward(length)
        galileo.left(600 / sides)#720 --> stars
    galileo.hideturtle()  # just the star

for angle in [315,270,225,180, 135, 90, 45, 0]:
    star("red", 5, 50, angle, 100)

for angle in [315,270,225,180, 135, 90, 45, 0]:
    star("blue", 5, 30, angle, 60)

for angle in [315,270,225,180, 135, 90, 45, 0]:
    star("green", 5, 20, angle, 30)

for angle in [315,270,225,180, 135, 90, 45, 0]:
    star("#222", 5, 10, angle, 10) 

    