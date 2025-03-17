import turtle

screen = turtle.Screen()
screen.bgcolor("black")  


spiral = turtle.Turtle()
spiral.shape("turtle")
spiral.speed(0) 


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


def draw_spiral():
    for i in range(360):
        spiral.pencolor(colors[i % 7])  
        spiral.forward(i * 3 / 2 + i)  
        spiral.left(120)  
        spiral.left(1)  
draw_spiral()


spiral.hideturtle()


turtle.done()
