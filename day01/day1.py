#!/usr/bin/env python
import sys

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    
    myInput = myInput.split('\n')
    return myInput

def part1():
    my_input = parseInput()
    freq = 0
    for l in my_input:
        if l[0] == '+':
            freq += int(l[1:])
        else:
            freq -= int(l[1:])
    print freq

def part2():
    my_input = parseInput()
    freq = 0
    freqs = []
    while True:
        for l in my_input:
            freqs.append(freq)
            if l[0] == '+':
                freq += int(l[1:])
            else:
                freq -= int(l[1:])
            if freq in freqs:
                print freq
                return


part1()
part2()

