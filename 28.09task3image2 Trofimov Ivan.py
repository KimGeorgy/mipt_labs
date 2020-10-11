import pygame
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
BROWN = (65, 25, 0)
PINK = (243, 0, 191)
LIGHTBLUE_LAS_1 = (111, 205, 252)
LIGHTBLUE_LAS_2 = (4, 138, 205)
GREEN_BLACK = (4, 138, 1)
PINK_LIGHT = (254, 169, 163)


# Foliage (surface, color, coordinates of the tree, radius of circles, number of leaves, shape of the tree [1 or -1])
def draw_foliage(surface, color, x_0, y_0, radius,  num, shape):
    abs_x = x_0
    abs_y = y_0
    for i in range((shape+1)//2*(num//2 + 2) + (-shape+1)//2 * 1):
        pygame.draw.circle(surface, color, (x_0 - 10 - shape*10, y_0 + 20), radius)
        pygame.draw.circle(surface, BLACK, (x_0 - 10 - shape*10, y_0 + 20), radius, 1)
        x_0 += 10
    x_0 = abs_x
    y_0 = abs_y
    for i in range(num // 2):
        pygame.draw.circle(surface, color, (x_0 - 10, y_0), radius)
        pygame.draw.circle(surface, BLACK, (x_0 - 10, y_0), radius, 1)
        x_0 += 10
    x_0 = abs_x
    y_0 = abs_y
    for i in range((-shape+1)//2 * (num//2 + 2) + (shape+1)//2 * 1):
        pygame.draw.circle(surface, color, (x_0 - 10 + shape*10, y_0 - 20), radius)
        pygame.draw.circle(surface, BLACK, (x_0 - 10 + shape*10, y_0 - 20), radius, 1)
        x_0 += 10


# Tree (surface, color, coordinates, trunk width, radius of leaves, number of leaves, shape of the tree [1 or -1])
def draw_tree(surface, color, x, y, width, height, radius_leave, num_leaves, shape):
    pygame.draw.rect(surface, BLACK, (x, y, width, height))
    x_0 = x + 10
    y_0 = y - 10
    draw_foliage(surface, color, x_0, y_0, radius_leave, num_leaves, shape)


# Cloud coordinates, radius of the circles, color, number of circles
def draw_cloud(surface, x_0, y_0, radius, cloud_color, num):
    abs_x = x_0
    for i in range(num[0]):
        pygame.draw.circle(surface, cloud_color, (x_0 - radius, y_0), radius)
        pygame.draw.circle(surface, BLACK, (x_0 - radius, y_0), radius, 1)
        x_0 += radius
    x_0 = (abs_x + x_0)/2 - (num[1]+2)*radius/2
    for i in range(num[1]):
        pygame.draw.circle(surface, cloud_color, (x_0, y_0 - radius), radius)
        pygame.draw.circle(surface, BLACK, (x_0, y_0 - radius), radius, 1)
        x_0 += radius


# House (coordinates, w, h, color of walls, number of windows per flat, color of windows, number of flats)
def draw_house(x_0, y_0, width, height, wall_color, num_windows, wind_color, num_flats):
    pygame.draw.rect(screen, wall_color, (x_0, y_0, (num_flats[1]) * width, (num_flats[0]) * height))
    for k in range(num_flats[1]):
        for j in range(num_flats[0]):
            pygame.draw.rect(screen, wind_color, (x_0 + k*width + width // 3, y_0 + j*height + height // 3,
                                                  width // 3, height // 3))
            for i in range(num_windows):
                pygame.draw.rect(screen, wall_color, (x_0 + k*width + width//3 + i*width//(3*num_windows),
                                                      y_0 + j*height + height//3,
                                                      width // 30,
                                                      height // 3))
            for i in range(num_windows):
                pygame.draw.rect(screen, wall_color, (x_0 + k*width + width//3,
                                                      y_0 + j*height + height//3 + i*height//(3*num_windows),
                                                      width // 3,
                                                      height // 30))
    pygame.draw.polygon(screen, PINK, [(x_0, y_0), (x_0 + num_flats[1] * width // 2, y_0 - width // 2),
                                       (x_0 + num_flats[1]*width, y_0)])


# Sun (coordinates, color, radius of the circles)
def draw_sun(surface, x_0, y_0, color, radius):
    phi = 0
    for i in range(360):
        pygame.draw.polygon(surface, color, ((x_0 + 5 - int(radius*np.cos(2*np.pi / 3 - phi)),
                                              y_0 + 5 + int(radius*np.sin(2*np.pi/3 - phi))),
                                             (x_0 + 5 + int(radius*np.sin(phi)),
                                              y_0 + 5 - int(radius*np.cos(phi)) // 4),
                                             (x_0 + 5 + int(radius*np.cos(2*np.pi/3 + phi)),
                                              y_0 + 5 + int(radius*np.sin(2*np.pi/3 + phi)))))
        phi += 10


screen = pygame.display.set_mode((800, 800))
screen.fill(WHITE)


# Background
pygame.draw.rect(screen, GREEN, (0, 400, 800, 400))
pygame.draw.rect(screen, LIGHTBLUE_LAS_1, (0, 0, 800, 400))

# Houses
draw_house(50, 450, 200, 150, PINK_LIGHT, 2, LIGHTBLUE_LAS_2, [2, 2])
draw_house(500, 330, 100, 100, BROWN, 3, PINK_LIGHT, [3, 2])
draw_house(380, 350, 50, 50, GREEN_BLACK, 3, WHITE, [1, 2])

# Trees
draw_tree(screen, RED, 720, 380, 15, 80, 25, 8, 1)
draw_tree(screen, GREEN_BLACK, 500, 550, 20, 150, 25, 6, -1)
draw_cloud(screen, 400, 200, 50, WHITE, [3, 1])
draw_cloud(screen, 600, 250, 20, LIGHTBLUE, [2, 0])
draw_cloud(screen, 200, 300, 34, PINK_LIGHT, [5, 3])
draw_cloud(screen, 600, 150, 15, YELLOW, [4, 6])
draw_sun(screen, 100, 150, PINK_LIGHT, 70)


pygame.init()
FPS = 30

pygame.display.flip()

pygame.display.update()
clock = pygame.time.Clock()


finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()
