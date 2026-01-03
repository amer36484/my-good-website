import turtle
import math
import time

# ------------------------------
# Screen setup
# ------------------------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System Simulation with Pluto")
screen.tracer(0)

# ------------------------------
# Sun
# ------------------------------
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)
sun.penup()
sun.goto(0, 0)

# ------------------------------
# Planets + Pluto: [name, color, distance, size, speed]
# ------------------------------
planets_data = [
    ["Mercury", "gray", 50, 0.3, 0.04],
    ["Venus", "orange", 80, 0.5, 0.03],
    ["Earth", "blue", 110, 0.6, 0.02],
    ["Mars", "red", 150, 0.4, 0.015],
    ["Jupiter", "brown", 200, 1.2, 0.01],
    ["Saturn", "gold", 250, 1.0, 0.008],
    ["Uranus", "lightblue", 300, 0.8, 0.006],
    ["Neptune", "blue", 350, 0.8, 0.005],
    ["Pluto", "lightgray", 400, 0.2, 0.003]  # Pluto added
]

planets = []

# ------------------------------
# Moons: [planet_index, color, distance, size, speed]
# Example: Earth's Moon and Jupiter's big moon
# ------------------------------
moons_data = [
    [2, "lightgray", 20, 0.15, 0.05],  # Earth's Moon
    [4, "white", 30, 0.2, 0.02]        # Jupiter moon
]

moons = []

# ------------------------------
# Create planet turtles
# ------------------------------
for data in planets_data:
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(data[1])
    planet.shapesize(data[3])
    planet.penup()
    planet.goto(data[2], 0)
    planet.speed(0)
    planet.pendown()
    planets.append({
        "turtle": planet,
        "distance": data[2],
        "angle": 0,
        "speed": data[4]
    })

# ------------------------------
# Create moon turtles
# ------------------------------
for mdata in moons_data:
    moon = turtle.Turtle()
    moon.shape("circle")
    moon.color(mdata[1])
    moon.shapesize(mdata[3])
    moon.penup()
    planet_index = mdata[0]
    moon.goto(planets[planet_index]["distance"] + mdata[2], 0)
    moon.speed(0)
    moon.pendown()
    moons.append({
        "turtle": moon,
        "planet_index": planet_index,
        "distance": mdata[2],
        "angle": 0,
        "speed": mdata[4]
    })

# ------------------------------
# Animation loop
# ------------------------------
while True:
    # Move planets
    for planet in planets:
        planet["angle"] += planet["speed"]
        x = planet["distance"] * math.cos(planet["angle"])
        y = planet["distance"] * math.sin(planet["angle"])
        planet["turtle"].goto(x, y)

    # Move moons
    for moon in moons:
        moon["angle"] += moon["speed"]
        planet = planets[moon["planet_index"]]
        px, py = planet["turtle"].xcor(), planet["turtle"].ycor()
        mx = px + moon["distance"] * math.cos(moon["angle"])
        my = py + moon["distance"] * math.sin(moon["angle"])
        moon["turtle"].goto(mx, my)

    screen.update()
    time.sleep(0.01)
