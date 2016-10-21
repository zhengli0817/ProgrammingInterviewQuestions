# Given a string representation of a number, check if it is hexspeak. A string is hexspeak if it only contains letters from "ABCDEFIO". 
# For example, given "257", it is "0x101" in hex, then it is hexspeak, while "8" is "0x8" in hex, so it is not.
def IsHexspeak(n):
    hexn = hex(int(n))
    hexn = hexn[2:]
    for c in ['2', '3', '4', '5', '6', '7', '8', '9']:
        if c in hexn: return 'ERROR'
    hexn = hexn.replace('1', 'I')
    hexn = hexn.replace('0', 'O')
   
    return hexn.upper()