obj = {}

with open("5.txt") as f:
	everything = f.read()
	everything = everything.split("\n\n")

# Original seeds
oldSeeds = everything[0].split(": ")[1].strip().split(" ")
oldSeeds = [int(i) for i in oldSeeds]
seeds = {}
for i in range(0, len(oldSeeds), 2):
    seeds[oldSeeds[i]] = {
        "srcRangeStart": oldSeeds[i],
        "rangeLen": oldSeeds[i+1]
    }

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
  
newObj = {}
originalSubKeys = seeds
# Keeping only the soils that are values with the seeds as keys
for key in keys:
    sortedGivenSubKeys = sorted(obj[key].keys())
    
    newObj[key] = {}
    
    for subkey in originalSubKeys:
        subkeyKey = subkey["srcRangeStart"]
        subkeyRange = subkey["rangeLen"]
        
        if subkeyKey < sortedGivenSubKeys[0]:
            newObj[key][(0)] = subkey
            continue
        
        