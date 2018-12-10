#!/usr/bin/env python
import sys

def parseInput():
    with open("input.txt", "r") as myfile:
        myInput = myfile.read()
    return myInput

lowerToUpperDiff = ord('a') - ord('A')
def react(charArray):
    i = 0
    reacted = False
    while (i < len(charArray) - 1):
        if abs(charArray[i] - charArray[i+1]) == lowerToUpperDiff:
            charArray.pop(i)
            charArray.pop(i)
            reacted = True
            i -= 1
        i += 1
    return reacted

def part1():
    my_input = parseInput()
    charArray = [ord(i) for i in my_input]
    while react(charArray):
        pass
    print "Part 1", len(charArray)

def removeAllOccasionsOfLetter(charArray, capital, lower):
    alternativeArray = [c for c in charArray]
    i = 0
    while (i < len(alternativeArray)):
        if alternativeArray[i] == capital or alternativeArray[i] == lower:
            alternativeArray.pop(i)
            i -= 1
        i += 1

    return alternativeArray
        
def part2():
    my_input = parseInput()
    charArray = [ord(i) for i in my_input]
    shortestPolymerChar = None
    shortestPolymerLen = len(charArray)
    for (capital, lower) in zip(xrange(ord('A'), ord('Z') + 1),
                                xrange(ord('a'), ord('z') + 1)):
        alternativeArray = removeAllOccasionsOfLetter(charArray, capital, lower)
        print "Testing w/o", chr(capital)
        while react(alternativeArray):
            pass
        reactedLen = len(alternativeArray)
        if reactedLen < shortestPolymerLen:
            shortestPolymerLen = reactedLen
            shortestPolymerChar = capital
    
    print "Part 2", shortestPolymerLen
    print chr(shortestPolymerChar)

part1()
part2()
