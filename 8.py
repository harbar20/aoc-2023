import functools
import math

instructions = []
nodes = {}
with open("8.txt") as f:
    lines = f.read().split("\n")
    lines.remove("")
    
    instructions = [i for i in lines[0]]
    
    for i in range(1, len(lines)):
        splits = lines[i].split(" = ")
        source = splits[0]
        directions = {
            "L": splits[1].split(", ")[0][1:], 
            "R": splits[1].split(", ")[1][:-1]
        }
        nodes[source] = directions


def allZ(list):
    for i in list:
        if i[-1] != "Z":
            return False
        
    return True
    
def numZ(list):
    num = 0
    for i in list:
        if i[-1] == "Z":
            num += 1
        
    return num

startNodes = list(filter(lambda x: x[-1] == "A", list(nodes.keys())))
numTurnsList = []
numTurns = 0
index = 0
for node in startNodes:
    current = node
    while current[-1] != "Z":
        current = nodes[current][instructions[index]]
        numTurns += 1
        index = (index + 1) % len(instructions)
    
    numTurnsList.append(numTurns)
    numTurns = 0
    index = 0

print(functools.reduce(math.lcm, numTurnsList))