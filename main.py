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
maxWidth = 1700
maxHeight = 800

# Load image
image = pygame.image.load(imageName + ".png")

# Calculate values to scale image to
scaleFactor = 1
if image.get_width() > maxWidth:
    if (maxWidth / image.get_width()) * image.get_height() > maxHeight:
        scaleFactor = maxHeight / image.get_height()
    else:
        scaleFactor = maxWidth / image.get_width()

# Create screen and display surface
screen = pygame.surface.Surface((image.get_width(),image.get_height()))
display = pygame.display.set_mode((int(image.get_width() *scaleFactor),int(image.get_height() * scaleFactor)),0,32)
pygame.display.set_caption(imageName + " | Sort Type: " + sortType +" | Direction: " + direction)
pygame.display.set_icon(image)

# Perform pixel sort
sortedSurface = pixelsort.SortVer(image, sortType, direction, debug)

#Scale image for display
displaySurf = pygame.transform.scale(sortedSurface, (int(image.get_width() *scaleFactor),int(image.get_height() * scaleFactor)))

while True:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(sortedSurface, "Sorted\\" + imageName + "_sorted(" + sortType + ", " + direction + ", " + direction +").png")
            pygame.quit()
            sys.exit()
    screen.blit(displaySurf, (0,0))
    display.blit(screen, (0,0))
    pygame.display.update()
