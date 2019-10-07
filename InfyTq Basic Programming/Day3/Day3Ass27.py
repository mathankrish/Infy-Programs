# Turtle Program


import turtle

my_tur = turtle.Screen()
my_tur = turtle.Turtle()


my_tur.speed(50)

my_tur.color("green")
my_tur.right(60)
my_tur.left(60)
my_tur.circle(50)

for i in range(1,3):
    my_tur.circle(20*i)


my_tur.right(120)
my_tur.color("blue")
my_tur.right(60)
my_tur.left(60)
my_tur.circle(50)

for i in range(1,3):
    my_tur.circle(20*i)

my_tur.right(120)
my_tur.color("red")
my_tur.right(60)
my_tur.left(60)
my_tur.circle(50)

for i in range(1,3):
    my_tur.circle(20*i)


turtle.done()