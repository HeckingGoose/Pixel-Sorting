# Load and initialise modules
import pygame, sys, pixelsort
from pygame.locals import *
pygame.init()
pygame.display.init()
clock = pygame.time.Clock()

# Define variables
imageName = "TestImage"
sortType = "g"
direction = "ascend"
debug = False

# Load image
image = pygame.image.load(imageName + ".png")

# Create screen and display surface
screen = pygame.surface.Surface((image.get_width(),image.get_height()))
display = pygame.display.set_mode((image.get_width(),image.get_height()),0,32)
pygame.display.set_caption(imageName + " | Sort Type: " + sortType +" | Direction: " + direction)
pygame.display.set_icon(image)

# Perform pixel sort
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
