import pprint

obj = {}

with open("5.txt") as f:
    everything = f.read()
    everything = everything.split("\n\n")

# Original seeds
oldSeeds = everything[0].split(": ")[1].strip().split(" ")
oldSeeds = [int(i) for i in oldSeeds]
seeds = {}
for i in range(0, len(oldSeeds), 2):
    seeds[oldSeeds[i]] = (oldSeeds[i], oldSeeds[i + 1])

# Adding everything to the object
obj["seed"] = seeds
keys = []
for i in range(1, len(everything)):
    mapSection = everything[i]
    parts = mapSection.split("\n")

    title = parts[0]
    titleParts = title.split(" ")[0].split("-")
    first = titleParts[0]
    last = titleParts[2]

    keys.append(last)

    obj[last] = {}
    numbers = parts[1:]

    for line in numbers:
        lineParts = line.strip().split(" ")
        destRangeStart = int(lineParts[0])
        srcRangeStart = int(lineParts[1])
        rangeLen = int(lineParts[2])

        obj[last][srcRangeStart] = {
            "destRangeStart": destRangeStart,
            "srcRangeStart": srcRangeStart,
            "rangeLen": rangeLen,
        }

newObj = {}
previousSubKeys = list(seeds.values())
for key in keys:
    newObj[key] = {}

    j = 0
    while j < len(previousSubKeys):
        subkey = previousSubKeys[j]
        subkeyStart = subkey[0]
        subkeyRange = subkey[1]

        found = False
        for currentSubKey in obj[key].keys():
            currentSubValue = obj[key][currentSubKey]

            if subkeyStart in range(currentSubKey, currentSubKey + currentSubValue["rangeLen"]):
                found = True
                
                if subkeyStart+subkeyRange in range(currentSubKey, currentSubKey + currentSubValue["rangeLen"]):
                    newObj[key][(subkeyStart, subkeyRange)] = (
                        currentSubValue["destRangeStart"],
                        subkeyRange,
                    )
                else:
                    subSubRange = subkeyStart+currentSubValue["rangeLen"]
                    newObj[key][(subkeyStart, subSubRange)] = (
                        currentSubValue["destRangeStart"],
                        subSubRange,
                    )
                    previousSubKeys.insert(j+1, (subkeyStart+subSubRange+1, subSubRange+subkeyRange+1))
                
                break
        
        if not found:
            newObj[key][(subkeyStart, subkeyRange)] = (subkeyStart, subkeyRange)
        
        j += 1
    
    previousSubKeys = list(newObj[key].values())

print(min([i[0] for i in list(newObj["location"].values())]))
