# Part 1
maxes = {
    "red": 12,
    "green": 13,
    "blue": 14
}
with open("2.txt") as f:
    allIDs = set()
    for line in f:
        splits = line.split(": ")
        gameID = int(splits[0].split(" ")[1])
        games = splits[1].split("; ")
        
        valid = True
        for game in games:
            colors = game.strip().split(", ")
            
            for color in colors:
                colorSplits = color.split(" ")
                colorNum = int(colorSplits[0])
                colorName = colorSplits[1]
                
                if colorNum > maxes[colorName]:
                    valid = False
        
        if valid:
            allIDs.add(gameID)

print(sum(allIDs))

# Part 2
with open("2.txt") as f:
    powers = []
    for line in f:
        maxes = {
            "red": 0,
            "blue": 0,
            "green": 0
        }
        splits = line.split(": ")
        gameID = int(splits[0].split(" ")[1])
        games = splits[1].split("; ")
        
        for game in games:
            colors = game.strip().split(", ")
            
            for color in colors:
                colorSplits = color.split(" ")
                colorNum = int(colorSplits[0])
                colorName = colorSplits[1]
                
                if colorNum > maxes[colorName]:
                    maxes[colorName] = colorNum
        
        power = maxes["red"] * maxes["green"] * maxes["blue"]
        powers.append(power)

print(sum(powers))
        