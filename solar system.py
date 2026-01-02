import turtle
import math
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Simple Solar System")

# Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)
sun.penup()
sun.goto(0, 0)

# Planets data: [name, color, distance from sun, size, speed]
planets_data = [
    ["Mercury", "gray", 50, 0.3, 0.04],
    ["Venus", "orange", 80, 0.5, 0.03],
    ["Earth", "blue", 110, 0.6, 0.02],
    ["Mars", "red", 150, 0.4, 0.015]
]

planets = []

# Create planet turtles
for data in planets_data:
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(data[1])
    planet.shapesize(data[3])
    planet.penup()
    planet.goto(data[2], 0)
    planets.append({
        "turtle": planet,
        "distance": data[2],
        "angle": 0,
        "speed": data[4]
    })

# Animation loop
while True:
    for planet in planets:
        planet["angle"] += planet["speed"]
        x = planet["distance"] * math.cos(planet["angle"])
        y = planet["distance"] * math.sin(planet["angle"])
        planet["turtle"].goto(x, y)
    screen.update()
    time.sleep(0.01)
