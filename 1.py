import re

# Part 1
with open("1.txt") as f:
    final = 0
    for line in f:
        nums = re.findall(r"\d", line)
        calibration = str(nums[0]) + str(nums[-1])
        final += int(calibration)

print(final)

# Part 2
with open("1.txt") as f:
    final = 0
    for line in f:
        # A dictionary where the key is the number spelled out and the value is the int value of the number
        numbers = {"one": "1", "two": "2", "three": "3", "four": "4",
                   "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
                   "eno": "1", "owt": "2", "eerht": "3", "ruof": "4",
                   "evif": "5", "xis": "6", "neves": "7", "thgie": "8", "enin": "9"}
        
        # Looks for the first instance of a number
        firstNums = re.findall(r"one|two|three|four|five|six|seven|eight|nine|\d", line)
        calibration = str(firstNums[0] if firstNums[0] not in numbers else numbers[firstNums[0]])
        
        # Looks for the last instance of a number
        enil = line[::-1]
        lastNums = re.findall(r"eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d", enil)
        calibration += str(lastNums[0] if lastNums[0] not in numbers else numbers[lastNums[0]])
        
        # Adds it
        final += int(calibration)

print(final)
        