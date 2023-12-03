import re

allChars = []
allGears = {}
with open("3.txt") as f:
    allChars = [[c for c in line.strip()] for line in f]

def checkAbove(currOuter, currInner, fullNum):
    if currOuter == 0: 
        return False

    outerIndex = currOuter-1
    topMinInner = max(currInner-1, 0)
    topMaxInner = min(currInner+1, len(allChars[currOuter])-1)
    
    arrToSearch = allChars[outerIndex][topMinInner:topMaxInner+1]
    stringToSearch = "".join(arrToSearch)
    
    # containsSymbols = any(not c.isalnum() and c != "." for c in stringToSearch)
    containsSymbols = False
    for i in range(len(stringToSearch)):
        c = stringToSearch[i]
        
        if not c.isalnum() and c != ".":
            containsSymbols = True
        
        if c == "*":
            coords = (outerIndex, topMinInner+i)
            if coords not in allGears:
                allGears[coords] = [fullNum]
            else:
                allGears[coords].append(fullNum)

    return containsSymbols

def checkMiddle(currOuter, currInner, fullNum):
    topMinInner = max(currInner-1, 0)
    topMaxInner = min(currInner+1, len(allChars[currOuter])-1)
    
    arrToSearch = allChars[currOuter][topMinInner:topMaxInner+1]
    stringToSearch = "".join(arrToSearch)
    
    # containsSymbols = any(not c.isalnum() and c != "." for c in stringToSearch)
    containsSymbols = False
    for i in range(len(stringToSearch)):
        c = stringToSearch[i]
        
        if not c.isalnum() and c != ".":
            containsSymbols = True
        
        if c == "*":
            coords = (currOuter, topMinInner+i)
            if coords not in allGears:
                allGears[coords] = [fullNum]
            else:
                allGears[coords].append(fullNum)

    return containsSymbols

def checkBelow(currOuter, currInner, fullNum):
    if currOuter == len(allChars)-1: 
        return False

    outerIndex = currOuter+1
    topMinInner = max(currInner-1, 0)
    topMaxInner = min(currInner+1, len(allChars[currOuter])-1)
    
    arrToSearch = allChars[outerIndex][topMinInner:topMaxInner+1]
    stringToSearch = "".join(arrToSearch)
    
    # containsSymbols = any(not c.isalnum() and c != "." for c in stringToSearch)
    containsSymbols = False
    for i in range(len(stringToSearch)):
        c = stringToSearch[i]
        
        if not c.isalnum() and c != ".":
            containsSymbols = True
        
        if c == "*":
            coords = (outerIndex, topMinInner+i)
            if coords not in allGears:
                allGears[coords] = [fullNum]
            else:
                allGears[coords].append(fullNum)

    return containsSymbols

def extractWholeNum(outer, inner):
    newInner = inner
    wholeNum = ""
    while newInner < len(allChars[outer]) and allChars[outer][newInner].isnumeric():
        wholeNum += allChars[outer][newInner]
        newInner += 1
    
    return int(wholeNum)

def containsSymbols(outer, inner, fullNum):
    valid = False
    for i in range(len(str(fullNum))):
        valid = valid or checkAbove(outer, inner+i, fullNum) or checkMiddle(outer, inner+i, fullNum) or checkBelow(outer, inner+i, fullNum)
    
    return valid

sumOfValid = 0
for i in range(len(allChars)):
    placeholder = 0
    for j in range(len(allChars[i])):      
        if placeholder != 0:
            placeholder -= 1
            continue
        
        if allChars[i][j].isnumeric():
            fullNum = extractWholeNum(i, j)
            
            if containsSymbols(i, j, fullNum):
                sumOfValid += fullNum
                placeholder = len(str(fullNum))

finalSum = 0
for value in allGears.values():
    if len(value) == 2:
        finalSum += value[0] * value[1]

print(sumOfValid)
print(finalSum)