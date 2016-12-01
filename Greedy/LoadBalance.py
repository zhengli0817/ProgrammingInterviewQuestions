# -*- coding: utf-8 -*-
# https://instant.1point3acres.com/thread/175070?from_discuz=1
# https://instant.1point3acres.com/thread/180774
# https://instant.1point3acres.com/thread/181505?from_discuz=1

# Heap Ref: http://stackoverflow.com/questions/12749622/creating-a-heap-in-python
# Heap Ref: http://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate
# IO Ref: http://stackoverflow.com/questions/2285284/python-basics-how-to-read-n-ints-until-n-is-found-in-stdin
# Ceil Ref: http://stackoverflow.com/questions/8582741/why-do-pythons-math-ceil-and-math-floor-operations-return-floats-instead-of

#from __future__ import division 
from heapq import heappush, heappop
from math import ceil

class Cluster(object):
    def __init__(self, workLoad, aveLoad, idx, numMachine):
        self.workLoad = workLoad
        self.aveLoad = aveLoad
        self.idx = idx
        self.numMachine = numMachine

# Use max heap, gready algorithm, time complexity O(BlogN)
def LoadBalance(loads, b):
    #res = loads[:]
    #if b <= len(loads):
    #    return res
    if b <= len(loads):
        return max(loads)
        
    heap = []
    for i, load in enumerate(loads):
        temp = Cluster(load, load, i, 1)
        heappush(heap, (-temp.aveLoad, temp))
        
    b -= len(loads)
    
    while b:
        b -= 1
        temp = heappop(heap)
        temp[1].numMachine += 1
        temp[1].aveLoad = float(temp[1].workLoad) / temp[1].numMachine
        heappush(heap, (-temp[1].aveLoad, temp[1]))
        
    #while heap:
    #    temp = heappop(heap)
    #    res[temp[1].idx] = temp[1].numMachine
    #
    #
    #return res
    return int(ceil(-heappop(heap)[0]))
    

# Use binary search, time complexity O(Nlog(max(loads)))
# Similar problem: 北大算法设计-二分与贪心-烘晾衣服    
def LoadBalance2(loads, b):
    l, r = 1, max(loads)
    while l<=r:
        mid = (l+r) / 2
        if Check(mid, loads, b):
            r = mid - 1
        else:
            l = mid + 1
    return l
    

def Check(maxLoad, loads, b):
    if b<=len(loads):
        return maxLoad>=max(loads)
    usedMachine = 0
    for i, load in enumerate(loads):
        usedMachine += int(ceil(float(load) / maxLoad))
        if usedMachine>b: return False
    return True
    
# IO code for Hackerrank    
#n, b = map(int, raw_input().split())
#loads = []
#for i in range(n):
#    loads.append(int(raw_input()))
#print LoadBalance(loads, b)