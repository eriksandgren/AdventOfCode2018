#!/usr/bin/env python
import sys

my_input = 1309

def part1():
    matrix = [[0 for x in xrange(300)] for y in xrange(300)]
    for x in xrange(300):
        for y in xrange(300):
            rackID = x + 1 + 10
            powerLevel = rackID * (y + 1)
            powerLevel += my_input
            powerLevel *= rackID
            powerLevel = str(powerLevel)
            if len(powerLevel) < 3:
                powerLevel = 0
            else:
                powerLevel = int(powerLevel[-3])
            powerLevel -= 5
            matrix[y][x] = powerLevel
    maxSquarePower = -500
    maxCoordinate = (-1, -1)
    for x in xrange(300-3):
        for y in xrange(300-3):
            squarePower = 0
            for x_offset in xrange(3):
                for y_offset in xrange(3):
                    squarePower += matrix[y+y_offset][x+x_offset]
            if squarePower > maxSquarePower:
                maxSquarePower = squarePower
                maxCoordinate = (x+1, y+1)
    print maxSquarePower, maxCoordinate

def part2():
    matrix = [[0 for x in xrange(300)] for y in xrange(300)]

    for x in xrange(300):
        for y in xrange(300):
            rackID = x + 1 + 10
            powerLevel = rackID * (y + 1)
            powerLevel += my_input
            powerLevel *= rackID
            powerLevel = str(powerLevel)
            if len(powerLevel) < 3:
                powerLevel = 0
            else:
                powerLevel = int(powerLevel[-3])
            powerLevel -= 5
            matrix[y][x] = powerLevel
    
    maxSquarePower = -500
    maxSquareSize = 0
    maxCoordinate = (-1, -1)
    maxSize = 0
    for x in xrange(300):
        print (x+1, y+1)
        for y in xrange(300):
            maxSquareSize = 300 - max(x, y)
            squarePower = matrix[y][x]
            for squareSize in xrange(2, maxSquareSize+1):
                for x_offset in xrange(squareSize):
                    squarePower += matrix[y+squareSize-1][x+x_offset]
                for y_offset in xrange(squareSize-1):
                    squarePower += matrix[y+y_offset][x+squareSize-1]
                if squarePower > maxSquarePower:
                    maxSquarePower = squarePower
                    maxCoordinate = (x+1, y+1)
                    maxSquareSize = squareSize
                    maxSize = squareSize
        print "squarePower, coordinate, size", maxSquarePower, maxCoordinate, maxSize

part1()
part2()
