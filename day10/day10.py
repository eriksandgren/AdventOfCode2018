#!/usr/bin/env python
import sys

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    
    myInput = myInput.split('\n')
    return myInput

def part1and2():
    my_input = parseInput()
    x_positions = []
    y_positions = []
    x_velocities = []
    y_velocities = []
    x_init_pos = []
    y_init_pos = []
    for l in my_input:
        x_pos, y_pos = int(l.split('<')[1].split(',')[0]), int(l.split('<')[1].split(', ')[1].split('>')[0])
        x_vel, y_vel = int(l.split('<')[2].split(',')[0]), int(l.split('<')[2].split(', ')[1].split('>')[0])
        x_positions.append(x_pos)
        x_init_pos.append(x_pos)
        y_positions.append(y_pos)
        y_init_pos.append(y_pos)

        x_velocities.append(x_vel)
        y_velocities.append(y_vel)
    num_positions = len(x_positions)
    max_sum = 0
    max_second = 0
    for s in xrange(20000):
        for i in xrange(num_positions):
            x_positions[i] +=  x_velocities[i]
            y_positions[i] += y_velocities[i]
        same_x = num_positions - len(list(set(x_positions)))
        same_y = num_positions - len(list(set(y_positions)))
        same_sum = same_x + same_y
        if same_sum > max_sum:
            max_sum = same_sum
            max_second = s + 1
    
    for second in (max_second, max_second):
        x_min, x_max, y_min, y_max = 0,0,0,0
        x_positions[0] = x_init_pos[0] + second * x_velocities[0]
        x_min = x_positions[0]
        x_max = x_positions[0] 
        y_positions[0] = y_init_pos[0] + second * y_velocities[0]
        y_min = y_positions[0]
        y_max = y_positions[0]
        for i in xrange(num_positions):
            x_positions[i] = x_init_pos[i] + second * x_velocities[i]
            x_min = min(x_min, x_positions[i])
            x_max = max(x_max, x_positions[i]) 
            y_positions[i] = y_init_pos[i] + second * y_velocities[i]
            y_min = min(y_min, y_positions[i])
            y_max = max(y_max, y_positions[i]) 
    
        print "Max sum, max second",max_sum, second

        print "x_min", x_min, "x_max", x_max, "y_min", y_min, "y_max", y_max

        matrix = [[" " for x in xrange(x_max - x_min + 1)]  for y in xrange(y_max - y_min + 5)]
        count = 0

        for i in xrange(num_positions):
            x, y = x_positions[i] - x_min, y_positions[i] - y_min
            matrix[y][x] = "#"
        for y in matrix:
            count +=1
            print ''.join(y)

part1and2()
