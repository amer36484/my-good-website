import pygame
import random
import math

# ------------------------------
# Setup
# ------------------------------
pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Realistic Universe Simulator")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 100)
RED = (255, 50, 50)
BLUE = (50, 100, 255)
ORANGE = (255, 150, 50)
PURPLE = (150, 50, 255)
LIGHTGRAY = (200, 200, 200)

# ------------------------------
# Classes
# ------------------------------
class Star:
    def __init__(self, x, y, color, size, star_type="main"):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.type = star_type
        self.planets = []

    def draw(self, screen, zoom, offset_x, offset_y):
        pygame.draw.circle(screen, self.color,
                           (int(self.x*zoom + offset_x), int(self.y*zoom + offset_y)),
                           max(int(self.size*zoom),1))

class Planet:
    def __init__(self, star, distance, size, speed, color):
        self.star = star
        self.distance = distance
        self.size = size
        self.speed = speed
        self.angle = random.uniform(0, 2*math.pi)
        self.color = color
        self.moons = []

    def update(self):
        self.angle += self.speed

    def draw(self, screen, zoom, offset_x, offset_y):
        # Orbit calculation with simple circular motion
        x = self.star.x + self.distance*math.cos(self.angle)
        y = self.star.y + self.distance*math.sin(self.angle)
        pygame.draw.circle(screen, self.color,
                           (int(x*zoom + offset_x), int(y*zoom + offset_y)),
                           max(int(self.size*zoom),1))
        for moon in self.moons:
            moon.draw(screen, zoom, offset_x + (x - self.star.x)*zoom,
                      offset_y + (y - self.star.y)*zoom)

class Moon:
    def __init__(self, planet, distance, size, speed, color):
        self.planet = planet
        self.distance = distance
        self.size = size
        self.speed = speed
        self.angle = random.uniform(0, 2*math.pi)
        self.color = color

    def update(self):
        self.angle += self.speed

    def draw(self, screen, zoom, offset_x, offset_y):
        self.angle += self.speed
        x = offset_x + self.distance*math.cos(self.angle)
        y = offset_y + self.distance*math.sin(self.angle)
        pygame.draw.circle(screen, self.color, (int(x), int(y)), max(int(self.size*zoom),1))

# ------------------------------
# Create galaxies
# ------------------------------
stars = []
galaxy_centers = [(-400, -300), (500, 200), (0, 0)]
for gx, gy in galaxy_centers:
    for i in range(50):  # 50 stars per galaxy
        angle = random.uniform(0, 2*math.pi)
        radius = random.uniform(50, 200)
        # Spiral rotation effect
        x = gx + radius * math.cos(angle)
        y = gy + radius * math.sin(angle)
        star_type = random.choices(
            ["main", "neutron", "blackhole", "quasar"], weights=[70,15,10,5])[0]
        if star_type == "main":
            color, size = random.choice([YELLOW, ORANGE, BLUE]), random.randint(2,4)
        elif star_type == "neutron":
            color, size = PURPLE, 3
        elif star_type == "blackhole":
            color, size = BLACK, 5
        else:  # quasar
            color, size = RED, 4
        star = Star(x, y, color, size, star_type)
        stars.append(star)

        # Add planets for main stars
        if star_type=="main":
            num_planets = random.randint(1, 4)
            for j in range(num_planets):
                distance = 15 + j*15
                size = random.randint(1,3)
                speed = 0.01 + random.random()*0.03
                color = random.choice([BLUE, RED, LIGHTGRAY, ORANGE])
                planet = Planet(star, distance, size, speed, color)

                # Add moons randomly
                if random.random()<0.5:
                    moon_distance = 5
                    moon_size = 0.5
                    moon_speed = 0.05
                    moon = Moon(planet, moon_distance, moon_size, moon_speed, LIGHTGRAY)
                    planet.moons.append(moon)

                star.planets.append(planet)

# ------------------------------
# Camera / Zoom
# ------------------------------
zoom = 0.05
offset_x = WIDTH//2
offset_y = HEIGHT//2
zoom_speed = 0.01
camera_speed = 15

# ------------------------------
# Main loop
# ------------------------------
running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    keys = pygame.key.get_pressed()
    # Camera movement
    if keys[pygame.K_a]:
        offset_x += camera_speed
    if keys[pygame.K_d]:
        offset_x -= camera_speed
    if keys[pygame.K_w]:
        offset_y += camera_speed
    if keys[pygame.K_s]:
        offset_y -= camera_speed
    # Zoom
    if keys[pygame.K_q]:
        zoom += zoom_speed
    if keys[pygame.K_e]:
        zoom -= zoom_speed
        if zoom < 0.01:
            zoom = 0.01

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rotate galaxies slightly for realism
    for i, (gx, gy) in enumerate(galaxy_centers):
        for star in stars[i*50:(i+1)*50]:
            dx, dy = star.x - gx, star.y - gy
            angle = 0.002  # Galaxy rotation speed
            cos_ang = math.cos(angle)
            sin_ang = math.sin(angle)
            star.x = gx + dx*cos_ang - dy*sin_ang
            star.y = gy + dx*sin_ang + dy*cos_ang

    # Draw stars and planets
    for star in stars:
        star.draw(screen, zoom, offset_x, offset_y)
        for planet in star.planets:
            planet.update()
            planet.draw(screen, zoom, offset_x, offset_y)

    pygame.display.flip()

pygame.quit()
