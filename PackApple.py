# -*- coding: utf-8 -*-
#5000 capacity的篮子 里面已经有了一些重量 有一些水果 问最多放几个. 1point3acres.com/bbs
#[4650, 100, 200, 150] 表示已经有4650了 后面三个是三个苹果的重量 所以最多放2个

basketAndApples = [ 5, 1, 2, 3, 4 ]

BASKETCAPACITY = 5000

def PackApple(basketAndApples):
    if len(basketAndApples)<=1: return 0
    basketSize = BASKETCAPACITY - basketAndApples[0]
    apples = basketAndApples[1:]
    count = 0
    totalWeight = 0
    for apple in sorted(apples):
        totalWeight += apple
        if totalWeight>basketSize: break
        count += 1
    return count
    