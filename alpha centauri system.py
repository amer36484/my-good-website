import turtle
import math
import time

# ------------------------------
# Screen setup
# ------------------------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Full Alpha Centauri System Simulation")
screen.tracer(0)  # Turn off auto-update for smooth animation

# ------------------------------
# Stars
# ------------------------------
# Alpha Centauri A
alphaA = turtle.Turtle()
alphaA.shape("circle")
alphaA.color("yellow")
alphaA.shapesize(2)
alphaA.penup()
alphaA.goto(0, 0)

# Alpha Centauri B
alphaB = turtle.Turtle()
alphaB.shape("circle")
alphaB.color("orange")
alphaB.shapesize(1.5)
alphaB.penup()
alphaB_distance = 100
alphaB_angle = 0
alphaB_speed = 0.02

# Proxima Centauri
proxima = turtle.Turtle()
proxima.shape("circle")
proxima.color("red")
proxima.shapesize(1)
proxima.penup()
proxima_distance = 250
proxima_angle = 0
proxima_speed = 0.005

# ------------------------------
# Planets around Alpha Centauri A
# Format: [distance from A, size, speed, color]
# ------------------------------
planets_A_data = [
    [40, 0.3, 0.05, "gray"],
    [70, 0.5, 0.03, "blue"]
]

planets_A = []

for pdata in planets_A_data:
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(pdata[3])
    planet.shapesize(pdata[1])
    planet.penup()
    planet.goto(pdata[0], 0)
    planet.speed(0)
    planet.pendown()
    planets_A.append({
        "turtle": planet,
        "distance": pdata[0],
        "angle": 0,
        "speed": pdata[2]
    })

# ------------------------------
# Planets around Alpha Centauri B
# ------------------------------
planets_B_data = [
    [30, 0.3, 0.04, "lightgreen"],
    [60, 0.4, 0.025, "purple"]
]

planets_B = []

for pdata in planets_B_data:
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(pdata[3])
    planet.shapesize(pdata[1])
    planet.penup()
    planet.goto(alphaB_distance + pdata[0], 0)  # Start relative to B
    planet.speed(0)
    planet.pendown()
    planets_B.append({
        "turtle": planet,
        "distance": pdata[0],
        "angle": 0,
        "speed": pdata[2]
    })

# ------------------------------
# Moons for planets (optional)
# Format: [planet reference, distance, size, speed, color]
# ------------------------------
moons = []
# Moon for first planet of A
moon1 = turtle.Turtle()
moon1.shape("circle")
moon1.color("lightgray")
moon1.shapesize(0.15)
moon1.penup()
moon1.goto(planets_A[0]["distance"] + 10, 0)
moon1.speed(0)
moon1.pendown()
moons.append({
    "turtle": moon1,
    "planet": planets_A[0],
    "distance": 10,
    "angle": 0,
    "speed": 0.08
})

# Moon for first planet of B
moon2 = turtle.Turtle()
moon2.shape("circle")
moon2.color("white")
moon2.shapesize(0.15)
moon2.penup()
moon2.goto(alphaB_distance + planets_B[0]["distance"] + 8, 0)
moon2.speed(0)
moon2.pendown()
moons.append({
    "turtle": moon2,
    "planet": planets_B[0],
    "distance": 8,
    "angle": 0,
    "speed": 0.06
})

# ------------------------------
# Animation loop
# ------------------------------
while True:
    # Alpha Centauri B orbits A
    alphaB_angle += alphaB_speed
    xB = alphaB_distance * math.cos(alphaB_angle)
    yB = alphaB_distance * math.sin(alphaB_angle)
    alphaB.goto(xB, yB)

    # Proxima Centauri orbits system center
    proxima_angle += proxima_speed
    xp = proxima_distance * math.cos(proxima_angle)
    yp = proxima_distance * math.sin(proxima_angle)
    proxima.goto(xp, yp)

    # Planets orbit Alpha Centauri A
    for planet in planets_A:
        planet["angle"] += planet["speed"]
        x = planet["distance"] * math.cos(planet["angle"])
        y = planet["distance"] * math.sin(planet["angle"])
        planet["turtle"].goto(x, y)

    # Planets orbit Alpha Centauri B
    for planet in planets_B:
        planet["angle"] += planet["speed"]
        x = xB + planet["distance"] * math.cos(planet["angle"])
        y = yB + planet["distance"] * math.sin(planet["angle"])
        planet["turtle"].goto(x, y)

    # Moons orbit their planets
    for moon in moons:
        moon["angle"] += moon["speed"]
        px, py = moon["planet"]["turtle"].xcor(), moon["planet"]["turtle"].ycor()
        mx = px + moon["distance"] * math.cos(moon["angle"])
        my = py + moon["distance"] * math.sin(moon["angle"])
        moon["turtle"].goto(mx, my)

    screen.update()
    time.sleep(0.01)
