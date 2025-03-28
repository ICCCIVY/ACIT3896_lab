import turtle

def koch_curve(t, length, level):
    if level == 0:  # Base case
        t.forward(length)
    else:  # Recursive case
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def koch_snowflake(t, length, level):
    for _ in range(3):  # Koch snowflake has 3 sides
        koch_curve(t, length, level)
        t.right(120)

# Set up Turtle graphics
window = turtle.Screen()
window.bgcolor("white")

t = turtle.Turtle()
t.speed(0)  # Fastest drawing

# Draw Koch snowflake with recursion depth level 4
koch_snowflake(t, 300, 4)

# Finish
turtle.done()
