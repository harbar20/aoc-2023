obj = {}

with open("5.txt") as f:
	everything = f.read()
	everything = everything.split("\n\n")

# Original seeds
seeds = everything[0].split(": ")[1].strip().split(" ")
seeds = [int(i) for i in seeds]

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
			"rangeLen": rangeLen
		}

# Keeping only the soils that are values with the seeds as keys
newObj = {}
originalSubKeys = seeds
for key in keys:
    sortedGivenSubKeys = sorted(obj[key].keys())
    
    newObj[key] = {}
    
    # Finding the closest sub key to each seed
    for subkey in originalSubKeys:
        if subkey < sortedGivenSubKeys[0]:
            newObj[key][subkey] = subkey
            continue
        
        closestSubKey = None
        
        for givenSubKey in sortedGivenSubKeys:            
            if obj[key][givenSubKey]["srcRangeStart"] + obj[key][givenSubKey]["rangeLen"] > subkey:
                closestSubKey = givenSubKey
                break
        
        if closestSubKey == None:
            newObj[key][subkey] = subkey
            continue
        
        newObj[key][subkey] = obj[key][closestSubKey]["destRangeStart"] + (subkey - closestSubKey)
    
    originalSubKeys = newObj[key].values()
    
print(min(newObj["location"].values()))