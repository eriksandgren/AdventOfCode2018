#!/usr/bin/env python
import sys

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    
    myInput = myInput.split('\n')
    return myInput


def countTuplets(sortedBoxId):
    prevC = None
    numDuplicates = 0
    numTriplets = 0
    numRepetitions = 0
    for c in sortedBoxId:
        if prevC == c:
            numRepetitions += 1
        else:
            if numRepetitions == 1:
                numDuplicates = 1
            elif numRepetitions == 2:
                numTriplets = 1
            numRepetitions = 0
        prevC = c

    if numRepetitions == 1:
        numDuplicates = 1
    elif numRepetitions == 2:
        numTriplets = 1
    
    return (numDuplicates, numTriplets)

def difference(id1, id2):
    diff = 0
    for c1, c2 in zip(id1, id2):
        if c1 != c2:
            diff += 1
            if diff > 1:
                return False
    print id1
    print id2
    return True

def part1():
    my_input = parseInput()
    numDuplicates = 0
    numTriplets = 0
    for boxId in my_input:
        sortedBoxId = sorted(boxId)
        (d, t) = countTuplets(sortedBoxId)
        numDuplicates += d
        numTriplets += t

    print numDuplicates
    print numTriplets
    print numDuplicates * numTriplets

def part2():
    my_input = parseInput()
    i = 0
    for boxId1 in my_input:
        i += 1
        for boxId2 in  my_input[i:]:
            difference(boxId1, boxId2)
part1()
part2()
