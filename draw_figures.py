import turtle
import figures

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

positions = [
    (-200, 150), (50, 150),
    (-200, 0),   (50, 0),
    (-200, -150),(50, -150)
]

pen.penup()
pen.goto(*positions[0])
pen.pendown()
figures.draw_square(pen, 80)

pen.penup()
pen.goto(*positions[1])
pen.pendown()
figures.draw_square(pen, 60)

pen.penup()
pen.goto(*positions[2])
pen.pendown()
figures.draw_triangle(pen, 80)

pen.penup()
pen.goto(*positions[3])
pen.pendown()
figures.draw_triangle(pen, 60)

pen.penup()
pen.goto(*positions[4])
pen.pendown()
figures.draw_rectangle(pen, 100, 50)

pen.penup()
pen.goto(*positions[5])
pen.pendown()
figures.draw_rectangle(pen, 80, 40)

pen.hideturtle()
window.mainloop()
