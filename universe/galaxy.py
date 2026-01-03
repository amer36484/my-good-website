import turtle
import random
import math
import time

# ------------------------------
# Screen setup
# ------------------------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Galaxy Zoom Simulation")
screen.setup(width=800, height=600)
screen.tracer(0)

# ------------------------------
# Create stars in the galaxy
# ------------------------------
num_stars = 100
stars = []

for _ in range(num_stars):
    star = turtle.Turtle()
    star.shape("circle")
    star.color("white")
    star.shapesize(random.uniform(0.1, 0.3))
    star.penup()
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    star.goto(x, y)
    stars.append(star)

screen.update()
time.sleep(1)

# ------------------------------
# Zoom to a chosen star
# ------------------------------
target_star = random.choice(stars)
target_x, target_y = target_star.xcor(), target_star.ycor()
zoom_steps = 100

for step in range(zoom_steps):
    for star in stars:
        x, y = star.xcor(), star.ycor()
        # Move stars closer to target to simulate zoom
        new_x = target_x + (x - target_x) * (1 - 0.02)
        new_y = target_y + (y - target_y) * (1 - 0.02)
        star.goto(new_x, new_y)
    screen.update()
    time.sleep(0.02)

# ------------------------------
# After zoom: show star system
# ------------------------------
# Main star (zoomed in)
main_star = turtle.Turtle()
main_star.shape("circle")
main_star.color("yellow")
main_star.shapesize(1.5)
main_star.penup()
main_star.goto(0, 0)

# Planets around the star
planets_data = [
    [50, 0.3, 0.04, "gray"],
    [80, 0.5, 0.03, "blue"],
    [110, 0.4, 0.02, "red"]
]

planets = []

for pdata in planets_data:
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(pdata[3])
    planet.shapesize(pdata[1])
    planet.penup()
    planet.goto(pdata[0], 0)
    planet.speed(0)
    planet.pendown()
    planets.append({
        "turtle": planet,
        "distance": pdata[0],
        "angle": 0,
        "speed": pdata[2]
    })

# Moons for the first planet
moon = turtle.Turtle()
moon.shape("circle")
moon.color("lightgray")
moon.shapesize(0.15)
moon.penup()
moon.goto(planets[0]["distance"] + 10, 0)
moon.speed(0)
moon.pendown()
moons = [{
    "turtle": moon,
    "planet": planets[0],
    "distance": 10,
    "angle": 0,
    "speed": 0.06
}]

# ------------------------------
# Animate planets and moons
# ------------------------------
while True:
    for planet in planets:
        planet["angle"] += planet["speed"]
        x = planet["distance"] * math.cos(planet["angle"])
        y = planet["distance"] * math.sin(planet["angle"])
        planet["turtle"].goto(x, y)

    for m in moons:
        m["angle"] += m["speed"]
        px, py = m["planet"]["turtle"].xcor(), m["planet"]["turtle"].ycor()
        mx = px + m["distance"] * math.cos(m["angle"])
        my = py + m["distance"] * math.sin(m["angle"])
        m["turtle"].goto(mx, my)

    screen.update()
    time.sleep(0.01)
