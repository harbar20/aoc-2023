values = {
    "Five of a kind": 7e12,
    "Four of a kind": 6e12,
    "Full house": 5e12,
    "Three of a kind": 4e12,
    "Two pair": 3e12,
    "One Pair": 2e12,
    "High card": 1e12
}
cardRanks = {
    "J": 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    "T": 10,
    "Q": 11,
    "K": 12,
    "A": 13
}

def jCheck(string, count, scoreSoFar):
    newMax = scoreSoFar
    if "J" in string:
        for card in count.keys():
            if card == "J": continue
            
            newString = string.replace("J", card, 1)
            
            newMax = max(hand(newString), newMax)
    
    return newMax

def oldHand(string):    
    # Counting instances of each letter
    count = {}
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    numbers = list(count.values())
    sNums = sorted(numbers)
    
    if len(numbers) == 2:
        if sNums == [2, 3]:
            return "Full house"
        else:
            return "Four of a kind"

    elif len(numbers) == 3:
        if sNums == [1, 2, 2]:
            return "Two pair"
        else:
            return "Three of a kind"
    
    innerValues = {
        1: "Five of a kind",
        4: "One Pair",
        5: "High card"
    }
    
    return innerValues[len(numbers)]

def hand(string):    
    # Counting instances of each letter
    count = {}
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    numbers = list(count.values())
    
    if len(numbers) == 2:
        if numbers == [2, 3] or numbers == [3, 2]:
            return jCheck(string, count, values["Full house"])
        else:
            return jCheck(string, count, values["Four of a kind"])

    elif len(numbers) == 3:
        if numbers == [1, 2, 2] or numbers == [2, 1, 2] or numbers == [2, 2, 1]:
            return jCheck(string, count, values["Two pair"])
        else:
            return jCheck(string, count, values["Three of a kind"])
    
    innerValues = {
        1: "Five of a kind",
        4: "One Pair",
        5: "High card"
    }
    
    return jCheck(string, count, values[innerValues[len(numbers)]])

def evaluate(h):
    value = hand(h)
    
    for i in range(len(h)):
        value += cardRanks[h[i]] * (100**(len(h) - i - 1))
    
    return value

cards = {}
with open("7.txt") as f:
    for line in f:
        splits = line.strip().split(" ")
        cards[splits[0]] = int(splits[1])

hands = sorted(list(cards.keys()), key=evaluate)
total = 0
for i in range(len(hands)):
    total += cards[hands[i]] * (i + 1)

print(total)