import sorters, time, pygame # import modules

def SortHor(image, sortType, direction, debug = False):
    direction = direction.lower()
    sortType = sortType.lower()
    startTime = time.time() # useful for calculating how long this took
    width = image.get_width()
    height = image.get_height() # store some values for later use
    newSurf = pygame.surface.Surface((width,height)) # create a new surface that will be returned at the end
    loop = 0
    for y in range(height): # iterate through every column of the image
        loop += 1
        if debug:
            print("Sorting (loop " + str(loop) + ")")
        # Fetch row of pixels as rgb
        rR = []
        rG = []
        rB = []
        for x in range(width):
            rR.append(image.get_at((x, y)).r)
            rG.append(image.get_at((x, y)).g)
            rB.append(image.get_at((x, y)).b)
        # Sort based on sortType
        match sortType:
            case "r":
                newOrder = sorters.merge.SortIndex(rR, direction)
            case "g":
                newOrder = sorters.merge.SortIndex(rG, direction)
            case "b":
                newOrder = sorters.merge.SortIndex(rB, direction)

        # Draw new row to surface
        for x in range(width):
            newSurf.set_at((x,y), (rR[newOrder[x]], rG[newOrder[x]], rB[newOrder[x]]))
    totalTime = time.time() - startTime
    if debug:
        print("Sort took " + str(totalTime) + " seconds.")
    return newSurf # Return new surface

def SortVer(image, sortType, direction, debug = False):
    direction = direction.lower()
    sortType = sortType.lower()
    startTime = time.time() # useful for calculating how long this took
    width = image.get_width()
    height = image.get_height() # store some values for later use
    newSurf = pygame.surface.Surface((width,height)) # create a new surface that will be returned at the end
    loop = 0
    for x in range(width): # iterate through every row of the image
        loop += 1
        if debug:
            print("Sorting (loop " + str(loop) + ")")
        # Fetch column of pixels as rgb
        rR = []
        rG = []
        rB = []
        for y in range(height):
            rR.append(image.get_at((x, y)).r)
            rG.append(image.get_at((x, y)).g)
            rB.append(image.get_at((x, y)).b)
        # Sort based on sortType
        match sortType:
            case "r":
                newOrder = sorters.merge.SortIndex(rR, direction)
            case "g":
                newOrder = sorters.merge.SortIndex(rG, direction)
            case "b":
                newOrder = sorters.merge.SortIndex(rB, direction)

        # Draw new column to surface
        for y in range(height):
            newSurf.set_at((x,y), (rR[newOrder[y]], rG[newOrder[y]], rB[newOrder[y]]))
    totalTime = time.time() - startTime
    if debug:
        print("Sort took " + str(totalTime) + " seconds.")
    return newSurf # Return new surface
