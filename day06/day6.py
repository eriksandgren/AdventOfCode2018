#!/usr/bin/env python
import sys

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    
    myInput = myInput.split('\n')
    return myInput

def isClosest(index, x_coordinates, y_coordinates, x, y):
    x_candidate, y_candidate = x_coordinates[index], y_coordinates[index]
    dist_candidate = abs(x-x_candidate) + abs(y-y_candidate)
    rangeExcludingIndex = range(index) + range(index + 1, len(x_coordinates))
    for i in rangeExcludingIndex:
        dist = abs(x - x_coordinates[i]) + abs(y - y_coordinates[i])
        if dist <= dist_candidate:
            return False
    return True

def isWithinRegion(x_coordinates, y_coordinates, x, y):
    sumDistance = 0
    regionLimit = 10000
    for i in xrange(len(x_coordinates)):
        dist = abs(x - x_coordinates[i]) + abs(y - y_coordinates[i])
        sumDistance += dist
        if sumDistance >= regionLimit:
            return False
    return True

def part1and2():
    my_input = parseInput()

    x_coordinates = []
    y_coordinates = []
    for l in my_input:
        x, y = int(l.split()[0][0:-1]), int(l.split()[1])
        x_coordinates.append(x)
        y_coordinates.append(y)
    # Find boundaries
    x_min, x_max, y_min, y_max = min(x_coordinates), max(x_coordinates), min(y_coordinates), max(y_coordinates)
    # Construct edges
    edges_x = range(x_min, x_max+1)   + range(x_min, x_max + 1) + [x_min]*(y_max+1-y_min) + [x_max]*(y_max+1-y_min)
    edges_y = [y_min]*(x_max+1-x_min) + [y_max]*(x_max+1-x_min) + range(y_min, y_max+1)   + range(y_min, y_max+1)

    # Disqualify all coordinates that are closest to some edges -> infinite region
    disqualifiedCoordinates = set()
    allCoordinates = set(range(len(x_coordinates)))
    for index in range(len(x_coordinates)):
        for (x,y) in zip(edges_x, edges_y):
            if isClosest(index, x_coordinates, y_coordinates, x, y):
                disqualifiedCoordinates.add(index)
    nonDisqualified = allCoordinates - disqualifiedCoordinates
    print disqualifiedCoordinates, len(disqualifiedCoordinates), "out of", len(x_coordinates), "disqualified"
    
    maxClosestPoints = 0
    for index in nonDisqualified:
        numberOfClosest = 0
        for x in xrange(x_min + 1, x_max):
            for y in xrange(y_min + 1, y_max):
                if isClosest(index, x_coordinates, y_coordinates, x, y):
                    numberOfClosest += 1
        if numberOfClosest > maxClosestPoints:
            maxClosestPoints = numberOfClosest
        print "Index", index, "has", numberOfClosest, "closest points, max closest points", maxClosestPoints

    regionSize = 0
    for x in xrange(x_min + 1, x_max):
        for y in xrange(y_min + 1, y_max):
            if isWithinRegion(x_coordinates, y_coordinates, x, y):
                regionSize += 1
    print "region size", regionSize

part1and2()
