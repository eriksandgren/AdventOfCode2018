#!/usr/bin/env python
import sys

class Node():
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    
    myInput = myInput.split('\n')
    return myInput

def play(numPlayers, lastMarble):
    firstMarble = Node(0, None, None)
    secondMarble = Node(1, firstMarble, firstMarble)
    firstMarble.prev = secondMarble
    firstMarble.next = secondMarble
    currentMarble = secondMarble
    points = [0] * numPlayers
    percent = lastMarble / 100
    for i in xrange(2, lastMarble+1):
        startNode = firstMarble
        startValue = startNode.value
        if i % 23 == 0:
            for j in xrange(7):
                currentMarble = currentMarble.prev
            points_marble = i + currentMarble.value
            previous = currentMarble.prev
            nextone = currentMarble.next
            previous.next = nextone
            nextone.prev = previous
            currentMarble = nextone
            points[i % numPlayers] += points_marble
        else:
            for j in xrange(2):
                currentMarble = currentMarble.next
            previous = currentMarble.prev
            newNode = Node(i, previous, currentMarble)
            previous.next = newNode
            currentMarble.prev = newNode
            currentMarble = newNode
        if i % percent == 0:
            print "Percent", i / percent
    
    return max(points)
            

def part1and2():
    my_input = parseInput()
    for l in my_input:
        numPlayers = int(l.split()[0])
        lastMarble = int(l.split('last marble is worth ')[1].split()[0])
        if "high score is" in l:
            highScore = int(l.split('high score is ')[1].split()[0])
            playScore = play(numPlayers, lastMarble)
            print "Play score", playScore, "High score", highScore
        else:
            playScore = play(numPlayers, lastMarble * 100)
            print "Play score", playScore
        print l

part1and2()
