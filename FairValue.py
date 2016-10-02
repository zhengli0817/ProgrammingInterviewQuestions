def FairValue(n):
    dice = [1, 2, 3, 4, 5, 6]
    lenDice = len(dice)
    fairValues = []
    for i in range(n):
        if i==0:
            fairValues.append(sum(dice)/float(lenDice))
        else:
            bigger = [k for k in dice if k > fairValues[-1]]
            fairValues.append( ( sum(bigger)+(lenDice-len(bigger))*fairValues[-1] ) / float(lenDice) )
            
    return fairValues[-1]
