import turtle
import random

class Polygons:
    def __init__(self, sides):
        self.size = 0
        self.sides = sides
        self.orient = 0
        self.color = (0, 0, 0)
        self.location = (0, 0)
        self.pen_size = 1

    def random_sides(self):
        self.sides = random.randint(3, 5)

    def random_orientation(self):
        self.orient = random.randint(0, 90)
        return self.orient

    def random_location(self):
        self.location = (random.randint(-400, 400), random.randint(-300, 300))

    def get_new_color(self):
        turtle.colormode(255)
        self.color = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))

    def random_size(self):
        self.size = random.randint(30, 100)

    def random_pensize(self):
        self.pen_size = random.randint(1, 4)

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orient)
        turtle.color(self.color)
        turtle.pensize(self.pen_size)

        turtle.pendown()
        for _ in range(self.sides):
            turtle.forward(self.size)
            turtle.left(360/self.sides)
        turtle.penup()

    def draw_multi(self, num_nested=3):
        original_size = self.size
        original_location = self.location

        for i in range(num_nested):
            current_size = original_size * (1 - (i / num_nested))
            if current_size < 5:
                break

            size_reduction = original_size - current_size

            if self.sides == 3:
                 adj_factor = 0.25
            elif self.sides == 4:
                 adj_factor = 0.5
            else:
                 adj_factor = 0.4

            shift_distance = size_reduction * adj_factor

            angle_rad = math.radians(self.orient)

            shift_x = shift_distance * math.cos(angle_rad)
            shift_y = shift_distance * math.sin(angle_rad)

            self.location = (original_location[0] + shift_x, original_location[1] + shift_y)

            self.size = current_size
            self.draw_polygon()

        self.location = original_location

    def mass_draw_polygon(self, times):
        for _ in range(times):
            self.random_size()
            self.get_new_color()
            self.random_location()
            self.random_orientation()
            self.random_pensize()
            self.draw_polygon()

    def random_draw_polygon(self, times):
        for _ in range(times):
            self.random_sides()
            self.random_size()
            self.get_new_color()
            self.random_location()
            self.random_orientation()
            self.random_pensize()
            self.draw_polygon()

    def mass_draw_multi(self, times, num_nested=3):
        for _ in range(times):
            self.random_size()
            self.get_new_color()
            self.random_location()
            self.random_orientation()
            self.random_pensize()
            self.draw_multi(num_nested)

import math
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")
turtle.tracer(0)

triangle_outline = Polygons(3)
square_outline = Polygons(4)
penta_outline = Polygons(5)
rand_outline = Polygons(0)

triangle_nested = Polygons(3)
square_nested = Polygons(4)
penta_nested = Polygons(5)
rand_nested = Polygons(0)

# Main
choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))

FIXED_LAYERS = 3

if choice == 1:
    triangle_outline.mass_draw_polygon(30)
elif choice == 2:
    square_outline.mass_draw_polygon(30)
elif choice == 3:
    penta_outline.mass_draw_polygon(30)
elif choice == 4:
    rand_outline.random_draw_polygon(30)
elif choice == 5:
    triangle_nested.mass_draw_multi(30, num_nested=FIXED_LAYERS)
elif choice == 6:
    square_nested.mass_draw_multi(30, num_nested=FIXED_LAYERS)
elif choice == 7:
    penta_nested.mass_draw_multi(30, num_nested=FIXED_LAYERS)
elif choice == 8:
    for _ in range(30):
        rand_nested.random_sides()
        rand_nested.random_size()
        rand_nested.get_new_color()
        rand_nested.random_location()
        rand_nested.random_orientation()
        rand_nested.random_pensize()
        rand_nested.draw_multi(FIXED_LAYERS)
elif choice == 9:
    for _ in range(30):
        if random.choice([True, False]):
            rand_outline.random_sides()
            rand_outline.random_size()
            rand_outline.get_new_color()
            rand_outline.random_location()
            rand_outline.random_orientation()
            rand_outline.random_pensize()
            rand_outline.draw_polygon()
        else:
            rand_nested.random_sides()
            rand_nested.random_size()
            rand_nested.get_new_color()
            rand_nested.random_location()
            rand_nested.random_orientation()
            rand_nested.random_pensize()
            rand_nested.draw_multi(FIXED_LAYERS)

turtle.update()
turtle.done()