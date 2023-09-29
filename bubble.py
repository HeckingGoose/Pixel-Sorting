# Code adapted from a progam called 'bubbie.py'
# that I wrote on a Casio FX-CG50.
# I couldn't be bothered to make another bubble
# sort from scratch lol

def Sort(asorted, direction):
    # direction:
    # 0 - descending
    # 1 - ascending
    if direction == 0:
        for val in range(len(asorted)):
            asorted[val] = asorted[val] * -1
    print("Sorting...")
    shift = True
    while shift:
        shift = False
        for ind in range(len(asorted)):
            if ind > 0:
                if asorted[ind-1] > asorted[ind]:
                    shift = True
                    temp = asorted[ind]
                    asorted[ind] = asorted[ind-1]
                    asorted[ind-1] = temp
    if direction == 0:
        for val in range(len(asorted)):
            asorted[val] = asorted[val] * -1
    return asorted

def SortIndex(asorted, direction, loop = 0, debug = False):
    # direction:
    # 0 - descending
    # 1 - ascending
    indices = []
    for ind in range(len(asorted)):
        indices.append(ind)
    if direction == 0:
        for val in range(len(asorted)):
            asorted[val] = asorted[val] * -1
    if debug:
        if loop != 0:
            print("Sorting (Loop " + str(loop) + ")...")
        else:
            print("Sorting...")
    shift = True
    while shift:
        shift = False
        for ind in range(len(asorted)):
            if ind > 0:
                if asorted[ind-1] > asorted[ind]:
                    shift = True
                    temp = asorted[ind]
                    asorted[ind] = asorted[ind-1]
                    asorted[ind-1] = temp
                    
                    temp = indices[ind]
                    indices[ind] = indices[ind-1]
                    indices[ind-1] = temp
    if direction == 0:
        for val in range(len(asorted)):
            asorted[val] = asorted[val] * -1
    return indices
