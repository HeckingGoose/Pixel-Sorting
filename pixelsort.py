import bubble, time, pygame # import modules

def SortHor(image, sortType, direction, debug = False):
    if debug:
        print()
        print("---Begin Sort---")
    direction = direction.lower()
    match direction:
        case "ascend":
            direction = 1
        case "descend":
            direction = 0
    sortType = sortType.lower()
    startTime = time.time() # useful for calculating how long this took
    width = image.get_width()
    height = image.get_height() # store some values for later use
    newSurf = pygame.surface.Surface((width,height)) # create a new surface that will be returned at the end
    loop = 0
    for y in range(height): # iterate through every column of the image
        loop += 1
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
                newOrder = bubble.SortIndex(rR, direction, loop, debug)
            case "g":
                newOrder = bubble.SortIndex(rG, direction, loop, debug)
            case "b":
                newOrder = bubble.SortIndex(rB, direction, loop, debug)

        # Draw new row to surface
        for x in range(width):
            newSurf.set_at((x,y), (rR[newOrder[x]], rG[newOrder[x]], rB[newOrder[x]]))
    totalTime = time.time() - startTime
    if debug:
        print("Sort took " + str(totalTime) + " seconds.")
    return newSurf # Return new surface

def SortVer(image, sortType, direction, debug = False):
    direction = direction.lower()
    match direction:
        case "ascend":
            direction = 1
        case "descend":
            direction = 0
    sortType = sortType.lower()
    startTime = time.time() # useful for calculating how long this took
    width = image.get_width()
    height = image.get_height() # store some values for later use
    newSurf = pygame.surface.Surface((width,height)) # create a new surface that will be returned at the end
    loop = 0
    for x in range(width): # iterate through every row of the image
        loop += 1
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
                newOrder = bubble.SortIndex(rR, direction, loop, debug)
            case "g":
                newOrder = bubble.SortIndex(rG, direction, loop, debug)
            case "b":
                newOrder = bubble.SortIndex(rB, direction, loop, debug)

        # Draw new column to surface
        for y in range(height):
            newSurf.set_at((x,y), (rR[newOrder[y]], rG[newOrder[y]], rB[newOrder[y]]))
    totalTime = time.time() - startTime
    if debug:
        print("Sort took " + str(totalTime) + " seconds.")
    return newSurf # Return new surface
