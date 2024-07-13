'''
import turtle
t = turtle.Turtle()
r=50
t.circle(r)

for i in range(6):
    t.forward(50)
    #right as degree
    t.speed(-1)
    t.right(60)
for i in range(2):
    t.forward(100)
    t.left(60)
    t.forward(50)
    t.left(120)

star = turtle.Turtle()

star.right(75)
star.forward(100)
star.fillcolor("pink")
star.begin_fill()
for i in range(4):
    star.right(144)
    star.forward(100)
star.end_fill()
star.hideturtle()
# Keep the turtle window open until it is manually closed
turtle.done()
'''

'''
import turtle #Inside_Out
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.color("blue")

def sqrfunc(size):
	for i in range(4):
		skk.fd(size)
		skk.left(90)
		size = size + 5

sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)
'''
'''
# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x//100 + 1)
	t.forward(x)
	t.left(59)
turtle.speed(-3)
'''
'''
import turtle

# Creating turtle
t = turtle.Turtle()

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

while (True):
	for i in range(6):
		for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:
			turtle.color(colors)
			turtle.circle(100)
			turtle.left(10)

turtle.hideturtle()
turtle.mainloop()
'''

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

turtle.pensize(2)

def curve():
	for i in range(200):
		t.right(1)
		t.forward(1)


t.speed(1)
t.color("red", "pink")

t.begin_fill()
t.left(140)
t.forward(111.65)
curve()

t.left(120)
curve()
t.forward(111.65)
t.end_fill()
t.hideturtle()

turtle.mainloop()
turtle.done()