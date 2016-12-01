# https://www.hackerrank.com/contests/juniper-hackathon/challenges/friend-circles

import os

# DFS, Time Complexity is O(n^2), Space Complexity is O(n)
# Ref: http://www.ideserve.co.in/learn/friend-circles-graph
def GetFriendCircles(friendsMatrix):
    """friendsMatrix is a list of list of chars"""
    if not friendsMatrix or len(friendsMatrix)<1:
        return 0
    numOfCircles = 0
    visited = [ False for row in friendsMatrix ]
    
    for i,row in enumerate(friendsMatrix):
        if not visited[i]:
            numOfCircles += 1
            visited[i] = True
            FindFriends(friendsMatrix, visited, i)
    
    return numOfCircles
    
def FindFriends(friendsMatrix, visited, idx):
    for i,column in enumerate(friendsMatrix[0]):
        if not visited[i] and i != idx and 'Y'==friendsMatrix[idx][i]:
            visited[i] = True
            FindFriends(friendsMatrix, visited, i)

# Union Find - (Weighted) Quick Union (with Path Compression)
# The code commented out are meant to implement weighted version with path compression
# Ref: https://asanchina.wordpress.com/2015/12/29/323-number-of-connected-components-in-an-undirected-graph/ 
# Ref: Princeton's Algorithms, Part I Week 1 on Union-Find         
def GetFriendCircles2(friendsMatrix):
    """friendsMatrix is a list of list of chars"""
    if not friendsMatrix or len(friendsMatrix)<1:
        return 0
    
    roots = [-1 for row in friendsMatrix]
    #roots = range(len(friendsMatrix))
    sizes = [1 for row in friendsMatrix]
    numOfCircles = len(friendsMatrix)
    for i,row in enumerate(friendsMatrix):
        for j, columun in enumerate(friendsMatrix[0]):
            if i<j and 'Y'==friendsMatrix[i][j]:
                u, v = i,j
                uroot = FindRoot(roots, u)
                vroot = FindRoot(roots, v)
                if (uroot != vroot):
                    numOfCircles -= 1
                    UnionSet(roots, sizes, uroot, u, vroot, v)
            
    return numOfCircles
       
def FindRoot(roots, idx):
    while roots[idx] == -1: return idx
    roots[idx] = FindRoot(roots, roots[idx])
    return roots[idx]
    #while idx != roots[idx]:
    #    roots[idx] = roots[roots[idx]]
    #    idx = roots[idx]
    #return idx
    
def UnionSet(roots, sizes, uroot, u, vroot, v):
    roots[uroot] = vroot
    #if uroot == vroot: return
    #if sizes[uroot]<sizes[vroot]:
    #    roots[uroot] = vroot
    #    sizes[vroot] += sizes[uroot]
    #else:
    #    roots[vroot] = uroot
    #    sizes[uroot] += sizes[vroot]        
        
        
# Test function                    
def Test(func):
    try:
        os.chdir('C:/Users/Apple/Google Drive/ProgrammingInterviewQuestions/HackerRank/friend-circles-testcases')
    except OSError:
        pass
    testResults = []
    expectedResults = []
    for i in xrange(10):
        infileName = 'input/input0' + str(i) + '.txt'
        with open(infileName, 'r') as inputFile:
            lines = [line.rstrip('\n') for line in inputFile]
        numPeople =  int(lines[0])
        friendsMatrix = [list(row) for row in lines[1:]]
        assert numPeople==len(friendsMatrix)==len(friendsMatrix[0])
        #print numPeople
        #print friendsMatrix
        res = func(friendsMatrix)
        testResults.append(res)
        print 'Your Output: ' + str(res)
        
        outfileName = 'output/output0'+ str(i) + '.txt'
        with open(outfileName, 'r') as outputFile:
            res = int(outputFile.read())
            expectedResults.append(res)
            print 'Expected Output: ' + str(res)
            
    if testResults==expectedResults:
        print 'All tests passed!'
    else:
        print 'Test failed!'
    

#if __name__ == '__main__':            
#    # IO code for HackerRank         
#    n = int(raw_input())
#    friendsMatrix = list()
#    for i in range(n):
#        row = list(raw_input())
#        friendsMatrix.append(row)
#    print GetFriendCircles(friendsMatrix)
