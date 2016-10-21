# -*- coding: utf-8 -*-
# 给你一个字符串，比如zzzyz，那么他的只包含相同字母子串有多少个，比如"zzz", "y"，同时角标不一样，视为不同子串。
# 比如输入是"zzz",那么有6个子串"z","z","z","zz","zz","zzz"
# 如果是"zzzyz",那么有8个。
def FindNumSubstrings(s):
    res = 0
    n = len(s)
    i = 0
    while i<n:
        j=1
        while (i+j < n) and (s[i+j] == s[i]):
            j=j+1
        
        #print j
        res += (j+1)*j/2 
        i+=j
    
    return res
        


#def main():
#    print FindNumSubstrings('zzzyz')
    

#if __name__ == '__main__':
#    main()