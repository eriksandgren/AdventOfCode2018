#!/usr/bin/env python
import sys

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    myInput = myInput.split('\n')
    return myInput

def part1():
    my_input = parseInput()

    steps_set = set()
    for l in my_input:
        steps_set.add(l[5])
        steps_set.add(l[-12])

    finished_steps_set = set()
    finished_steps_l = []
    while finished_steps_set != steps_set:
        dependant_steps_set = set()
        for l in my_input:
            if l[5] not in finished_steps_set:
                dependant_steps_set.add(l[-12])
        non_dependant_steps_l = sorted(list(steps_set-dependant_steps_set-finished_steps_set))
        if len(non_dependant_steps_l) == 0:
            break
        step_to_do = non_dependant_steps_l[0]
        finished_steps_set.add(step_to_do)
        finished_steps_l.append(step_to_do)
    print ''.join(finished_steps_l)

def part2():
    my_input = parseInput()
    num_workers = 5
    num_active_workers = 0
    time_offset = 60
    steps_set = set()
    for l in my_input:
        steps_set.add(l[5])
        steps_set.add(l[-12])

    steps_time_left = [ord(x) - ord('A') + 1 + time_offset for x in sorted(list(steps_set))]
    print steps_time_left
    finished_steps_set = set()
    steps_in_progress_set = set()
    finished_steps_l = []
    prev_num_finished = -1
    time = 0
    while finished_steps_set != steps_set:
        if len(finished_steps_l) > prev_num_finished:
            prev_num_finished = len(finished_steps_l)
            dependant_steps_set = set()
            for l in my_input:
                if l[5] not in finished_steps_set:
                    dependant_steps_set.add(l[-12])
            non_dependant_steps_l = sorted(list(steps_set-dependant_steps_set-finished_steps_set-steps_in_progress_set))

            while num_active_workers != num_workers and len(non_dependant_steps_l) != 0:
                steps_in_progress_set.add(non_dependant_steps_l[0])
                non_dependant_steps_l.pop(0)
                num_active_workers += 1
            
        finished_steps_iter = set()
        for x in steps_in_progress_set:
            s = ord(x) - ord('A')
            steps_time_left[s] -= 1
            if steps_time_left[s] == 0:
                num_active_workers -= 1
                finished_steps_iter.add(s)
                finished_steps_set.add(chr(s + ord('A')))
                finished_steps_l.append(chr(s + ord('A')))
        steps_in_progress_set -= finished_steps_iter
        time += 1
    print ''.join(finished_steps_l)
    print time

part2()