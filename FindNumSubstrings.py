
def FindNumSubstrings(s):
    res = 0
    n = len(s)
    i = 0
    while i<n:
        j=1
        while (i+j < n) and (s[i+j] == s[i]):
            j=j+1
        
        print j
        res += sum(range(j+1)) 
        i+=j
    
    return res
        


#def main():
#    print FindNumSubstrings('zzzyz')
    

#if __name__ == '__main__':
#    main()