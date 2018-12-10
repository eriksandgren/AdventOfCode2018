#!/usr/bin/env python
import sys

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    
    myInput = myInput.split('\n')
    return myInput

def part1and2():
    my_input = parseInput()
    fabric = {}
    overriddenClaims = set()
    allClaims = set()
    for l in my_input:
        k = l.split()
        index = int(k[0][1:])
        allClaims.add(index)
        fromLeft = int(k[2].split(',')[0])
        fromTop = int(k[2].split(',')[1][:-1])
        width = int(k[3].split('x')[0])
        height = int(k[3].split('x')[1])
        for i in xrange(fromLeft, fromLeft + width):
            for j in xrange(fromTop, fromTop + height):
                if (i,j) not in fabric:
                    fabric[(i,j)] = index
                elif fabric[(i,j)] == 'X':
                    overriddenClaims.add(index)
                else:
                    overriddenClaims.add(index)
                    overriddenClaims.add(fabric[(i,j)])
                    fabric[(i,j)] = 'X'

    doubleBookedSqInches = sum(value == 'X' for value in fabric.values())
    print doubleBookedSqInches
    print allClaims - overriddenClaims

part1and2()
