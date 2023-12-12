with open("9.txt") as f:
    seqs = []
    for line in f:
        seqs.append([int(i) for i in line.strip().split(" ")])
        
def allZeroes(l):
    for i in l:
        if i != 0:
            return False
    
    return True

total = 0
for j in range(len(seqs)):
    seq = seqs[j]
    
    extraItem = 0
    subSeqs = [seq]
    while not allZeroes(subSeqs[-1]):
        subSubSeq = []
        for i in range(len(subSeqs[-1])-1):
            subSubSeq.append(subSeqs[-1][i+1] - subSeqs[-1][i])
        
        subSeqs.append(subSubSeq)
    
    
    for i in range(len(subSeqs)):
        backwardsIndex = len(subSeqs) - i - 1
        extraItem = subSeqs[backwardsIndex][0] - extraItem
    
    total += extraItem

print(total)
        