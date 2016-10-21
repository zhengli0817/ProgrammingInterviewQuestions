boxes = [1, 2, 3, 4, 5]
melons = [1, 2, 3, 4, 5]

def  melon_count(boxes, melons):
    lenBoxes = len(boxes)
    maxCount = 0 
    for startIdx, startMelon in enumerate(melons):
        count = 0
        j = 0
        for melon in melons[startIdx:]:
            while(j<lenBoxes and melon<boxes[j]):
                j += 1
            if j == lenBoxes:
                break
            else:
                count += 1
                j += 1
        maxCount = max(maxCount, count)
    return maxCount
            
                

#def  melon_count(boxes, melons):
#    startIndex = len(boxes)
#    curMax = 0
#    for i, melon in enumerate(reversed(melons)):
#        validIndexes = [ j for j,box in enumerate(boxes) if box>=melon and j<startIndex ]
#        print validIndexes
#        print startIndex
#        print curMax
#        if len(validIndexes)==0:
#            continue
#        else:
#            if validIndexes[-1]<startIndex:
#                startIndex = validIndexes[-1]
#                curMax += 1
#    return curMax
        
        