#!/usr/bin/env python
import sys

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    
    myInput = myInput.split('\n')
    return myInput

def getMinute(line):
    return int(line[15:17])

def getGuard(line):
    return int(line.split('#')[1].split()[0])

def convertTimeStampToMinutes(line):
    year = int(line[1:5])
    month = int(line[6:8])
    day = int(line[9:11])
    hour = int(line[12:14])
    minute = int(line[15:17])
    timeInMinutes = minute + hour * 60 + day * 60 * 24 + month * 60 * 24 * 31 + year * 60 * 24 * 31 * 365
    return timeInMinutes

def compareLinesByTime(line1, line2):
    return convertTimeStampToMinutes(line1) - convertTimeStampToMinutes(line2)

def part1and2():
    my_input = parseInput()
    sortedInput = sorted(my_input, cmp=compareLinesByTime)
    for l in sortedInput:
        print l

    guards = {}
    guard = None
    asleepMinutes = 0
    fellAsleep = None
    for l in sortedInput:
        if 'Guard' in l:
            if guard is None:
                pass
            elif guard not in guards:
                guards[guard] = asleepMinutes
            else:
                guards[guard] += asleepMinutes
            asleepMinutes = 0
            guard = getGuard(l)
        elif 'asleep' in l:
            fellAsleep = getMinute(l)
        elif 'wakes' in l:
            asleepMinutes += getMinute(l) - fellAsleep
    if guard not in guards:
        guards[guard] = asleepMinutes
    else:
        guards[guard] += asleepMinutes
    mostSleepyGuard = max(guards, key=guards.get)
    print guards
    sleepingMinutes = [0] * 60
    compareString = 'Guard #' + str(mostSleepyGuard)
    isSleepyGuard = False
    print compareString
    for l in sortedInput:
        if compareString in l:
            print l
            isSleepyGuard = True
        elif 'Guard' in l:
            isSleepyGuard = False
        elif 'asleep' in l and isSleepyGuard:
            fellAsleep = getMinute(l)
        elif 'wakes' in l and isSleepyGuard:
            for i in xrange(fellAsleep, getMinute(l)):
                sleepingMinutes[i] += 1
    m = max(sleepingMinutes)
    # Part 1 answer
    print [i * mostSleepyGuard for i, j in enumerate(sleepingMinutes) if j == m]

    sleepingMinutes = {}
    for l in sortedInput:
        if 'Guard' in l:
            guard = getGuard(l)
        if guard not in sleepingMinutes:
            sleepingMinutes[guard] = [0] * 60
        if 'asleep' in l:
            fellAsleep = getMinute(l)
        elif 'wakes' in l:
            for i in xrange(fellAsleep, getMinute(l)):
                sleepingMinutes[guard][i] += 1    
    print sleepingMinutes
    mostSleptMinute = None
    numberOfSleepsMax = 0
    guardWithMostSleptMinute = None
    for guard in sleepingMinutes:
        if max(sleepingMinutes[guard]) > numberOfSleepsMax:
            numberOfSleepsMax = max(sleepingMinutes[guard])
            mostSleptMinute = sleepingMinutes[guard].index(numberOfSleepsMax)
            guardWithMostSleptMinute = guard
    print numberOfSleepsMax
    print mostSleptMinute
    print guardWithMostSleptMinute
    print mostSleptMinute * guardWithMostSleptMinute
part1and2()
