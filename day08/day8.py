#!/usr/bin/env python
import sys
metaCount = 0
nodeValue = 0
def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    
    myInput = myInput.split('\n')
    return myInput

def handleNode(node_l, stackP):
    global metaCount, nodeValue
    numChilds = node_l[stackP]
    numMetas  = node_l[stackP+1]
    stackP = stackP + 2
    childValues = []
    for _ in range(numChilds):
        (stackP, childVal) = handleNode(node_l, stackP)
        childValues.append(childVal)
    nodeMetaCount = 0
    metas = []
    for m in range(stackP, stackP + numMetas):
        metas.append(node_l[m])
        nodeMetaCount += node_l[m]
    metaCount +=  nodeMetaCount
    value = 0
    if numChilds == 0:
        value = nodeMetaCount
    else:
        for m in range(stackP, stackP + numMetas):
            index = node_l[m] - 1
            if index < len(childValues):
                value += childValues[index]
    return (stackP + numMetas, value)

def part1and2():
    my_input = [int(x) for x in parseInput()[0].split()]
    stackP = 0
    value = 0
    (stackP, value) = handleNode(my_input, stackP)
    print "Part 1, sum of meta entries", metaCount
    print "Part2, value of root node", value
part1and2()
