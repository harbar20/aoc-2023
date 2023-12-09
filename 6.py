# Part 1
timesToDistance = {}
records = {}
with open("6.txt") as f:
    lines = f.read().split("\n")
    times = lines[0].replace("  ", " ").replace("  ", " ").replace("  ", " ").split(": ")[1].split(" ")
    distances = lines[1].replace("  ", " ").replace("  ", " ").replace("  ", " ").split(": ")[1].split(" ")
    
    times = [int(i) for i in times]
    distances = [int(i) for i in distances]
    
    for i in range(len(times)):
        records[times[i]] = distances[i]
        timesToDistance[times[i]] = 0
        
for time in times:
    record = records[time]
    
    for speed in range(time):
        timeLeft = time - speed
        totalDistance = speed * timeLeft
        timesToDistance[time] += 1 if totalDistance >= record else 0

prod = 1
for i in list(timesToDistance.values()):
    prod *= i
print(prod)

# Part 2
result = 0
with open("6.txt") as f:
    lines = f.read().split("\n")
    time = int(lines[0].replace(" ", "").split(":")[1])
    record = int(lines[1].replace(" ", "").split(":")[1])

for speed in range(time):
    timeLeft = time - speed
    totalDistance = speed * timeLeft
    result += 1 if totalDistance >= record else 0

print(result)

