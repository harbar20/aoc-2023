# Part 1
with open("4.txt") as f:
    total = 0
    for line in f:
        splits = line.split(": ")
        numbers = splits[1].strip().replace("  ", " ").split(" | ")

        winningNumbers = set(numbers[0].split(" "))
        cardNumbers = numbers[1].split(" ")

        numWins = 0
        for num in cardNumbers:
            if num in winningNumbers:
                numWins += 1

        total += 0 if 2**numWins == 1 else 2**(numWins-1)

    print(total)


# Part 2
numCopies = {}
wins = {}
with open("4.txt") as f:
    for line in f:
        splits = line.split(": ")
        cardNum = int(splits[0].replace(" ", "").split("Card")[1])
        numbers = splits[1].strip().replace("  ", " ").split(" | ")

        winningNumbers = set(numbers[0].split(" "))
        cardNumbers = numbers[1].split(" ")

        numWins = 0
        for num in cardNumbers:
            if num in winningNumbers:
                numWins += 1

        wins[cardNum] = numWins


        for i in range(cardNum+1, cardNum+1+numWins):
            if i not in numCopies:
                numCopies[i] = 1
            else:
                numCopies[i] += 1

for card in wins.keys():
    numWins = wins[card]

    if card not in numCopies: continue

    for j in range(numCopies[card]):
        for i in range(card + 1, card + 1 + numWins):
            if i not in numCopies:
                numCopies[i] = 1
            else:
                numCopies[i] += 1

print(numCopies)
print(sum(numCopies.values()) + len(wins.keys()))