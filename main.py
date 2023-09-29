# Load and initialise modules
import pygame, sys, pixelsort
from pygame.locals import *
pygame.init()
pygame.display.init()
clock = pygame.time.Clock()

# Request and format user input
uInput = False
print("Input image name to pixel sort:")
print("------------------------------¬")
while uInput == False:
    imageName = input(">>>")
    try:
        # Load image
        image = pygame.image.load(imageName + ".png")
        uInput = True
    except:
        # Image fails to load
        print()
        print("Image not found in working directory!")

uInput = False
print()
print("Input colour component to pixel sort (r, g or b):")
print("------------------------------------------------¬")
while uInput == False:
    sortType = input(">>>").lower()
    if sortType in ['r', 'g', 'b']:
        uInput = True
    else:
        print()
        print("Input not of form 'r', 'g' or 'b'!")

uInput = False
print()
print("Input sorting direction (ascend/descend):")
print("----------------------------------------¬")
while uInput == False:
    direction = input(">>>").lower()
    if direction in ["ascend", "descend"]:
        uInput = True
    else:
        print()
        print("Input not of form 'ascend' or 'descend'!")

uInput = False
print()
print("Input sorting axis (x/y):")
print("------------------------¬")
while uInput == False:
    axis = input(">>>").lower()
    if axis in ['x', 'y']:
        uInput = True
    else:
        print()
        print("Input not of form 'x' or 'y'!")

# Debug variables
debug = True

# Create screen and display surface
screen = pygame.surface.Surface((image.get_width(),image.get_height()))
display = pygame.display.set_mode((image.get_width(),image.get_height()),0,32)
pygame.display.set_caption(imageName + " | Sort Type: " + sortType +" | Direction: " + direction)
pygame.display.set_icon(image)

# Perform pixel sort
if axis == "x":
    sortedSurface = pixelsort.SortHor(image, sortType, direction, debug)
else:
    sortedSurface = pixelsort.SortVer(image, sortType, direction, debug)

while True:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(sortedSurface, "Sorted\\" + imageName + "_sorted(" + sortType + ", " + direction + ", " + direction +").png")
            pygame.quit()
            sys.exit()
    screen.blit(sortedSurface, (0,0))
    display.blit(screen, (0,0))
    pygame.display.update()
