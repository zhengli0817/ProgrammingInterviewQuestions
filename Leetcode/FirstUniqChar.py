# https://leetcode.com/problems/first-unique-character-in-a-string/
#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#Examples:
#
#s = "leetcode"
#return 0.
#
#s = "loveleetcode",
#return 2.
#Note: You may assume the string contain only lowercase letters.

#ref: http://bookshadow.com/weblog/2016/08/21/leetcode-first-unique-character-in-a-string/
#ref: http://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/

import collections

def FirstUniqChar(s):
    d = collections.Counter(s)
    ans = -1
    for x, c in enumerate(s):
        if d[c] == 1:
            ans = x
            break
    return ans
    
# Here is another faster but not so elegant solution
NO_OF_CHARS = 256

def GetCharCountArray(s):
    count = [0] * NO_OF_CHARS
    for i in s:
        count[ord(i)]+=1
    return count
    
def FirstUniqChar2(s):
    count = GetCharCountArray(s)
    index = -1
    k = 0
 
    for i in s:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
 
    return index