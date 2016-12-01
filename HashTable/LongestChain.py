# https://instant.1point3acres.com/thread/189098
# http://massivealgorithms.blogspot.com/2016/05/like-coding-mj-56-longest-string-chain.html
# http://buttercola.blogspot.com/2015/10/zenefits-oa-longest-chain.html?m=1

def LongestChain(words):
    if not words or len(words)==0:
        return 0
    
    words = sorted(words, key=len)
    res = 0
    # this dict stores the map: word -> length of its local longest chain
    wordDict = {}
    wordSet = set(words)
    
    for word in words:
        if (len(word)>res):
            res = max(res, dfs(word, wordSet, wordDict)+1)
    
    return res
    
def dfs(word, wordSet, wordDict):
    res = 0
    for i,c in enumerate(word):
        nextWord = word[:i]+word[i+1:]
        if nextWord not in wordSet: continue
        if nextWord in wordDict:
            res = max(res, wordDict[nextWord])
        else:
            res = max(res, dfs(nextWord, wordSet, wordDict)+1)
    
    wordDict[word] = res + 1
    
    return res
    
    
def Test():
    n = int(raw_input())
    words = []
    for i in range(n):
        words.append(raw_input())
    print LongestChain(words)
    