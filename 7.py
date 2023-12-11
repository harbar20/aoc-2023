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

def jCheck(string, count):
    if "J" in string:
        for i in range(count["J"]):
            

def hand(string):    
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
    
    values = {
        1: "Five of a kind",
        4: "One Pair",
        5: "High card"
    }
    
    return values[len(numbers)]

def evaluate(h):
    value = values[hand(h)]
    
    for i in range(len(h)):
        c = h[i]
        value += cardRanks[c] * (100**(len(h) - i - 1))
    
    return value

def compare(handOne, handTwo):
    valueOne = values[hand(handOne)]
    valueTwo = values[hand(handTwo)]
    
    if valueOne > valueTwo:
        return valueOne
    elif valueOne < valueTwo:  
        return valueTwo

    i = 0
    while valueOne[i] == valueTwo[i]:
        i += 1
    
    if cardRanks[handOne[i]] > cardRanks[handTwo[i]]:
        return valueOne
    else:
        return valueTwo

cards = {}
with open("7.txt") as f:
    for line in f:
        splits = line.strip().split(" ")
        cards[splits[0]] = int(splits[1])

hands = sorted(list(cards.keys()), key=evaluate)
print(hands)
total = 0
for i in range(1, len(hands)+1):
    print(hands[i-1])
    print(evaluate(hands[i-1]))
    print()
    total += cards[hands[i-1]] * i

print(total)