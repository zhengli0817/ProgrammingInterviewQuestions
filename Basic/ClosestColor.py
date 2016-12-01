# http://stackoverflow.com/questions/36793382/how-to-split-the-binary-string
# Sample input:
#5 // The first line contains an integer N(1<=N<=100), which is the number of input pixels to follow.
#101111010110011011100100
#110000010101011111101111
#100110101100111111101101
#010111011010010110000011
#000000001111111111111111
# Sample output:
#White
#White
#White
#Green
#Ambiguous

def GetClosestColor(rgb):
    labels = ("White", "Black", "Red", "Green", "Blue")
    values = ((255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255))
    res = []
    for idx, v in enumerate(values):
        # it's unnecessary to take square root fot this problem
        distanceSquare = (float(rgb[0] - v[0])**2 + float(rgb[1] - v[1])**2 + float(rgb[2] - v[2])**2) 
        res.append(distanceSquare)

    md = min(res)
    c, idx = res.count(md), res.index(md)
    return labels[idx] if c == 1 else "Ambiguous"

# Use the function int(,2) to convert a binary string to decimal
# Ref: http://stackoverflow.com/questions/13656343/python-binary-to-decimal-conversion
def PrintClosestColors(binaryCodes):
    for binaryCode in binaryCodes:
        rc = int(binaryCode[:8],2)
        gc = int(binaryCode[8:16],2)
        bc = int(binaryCode[16:],2)
        print GetClosestColor([rc, gc, bc])
        
# Use bit operations
def PrintClosestColors2(binaryCodes):
    for binaryCode in binaryCodes:
        pixel = int(binaryCode,2)
        rc = (pixel & 0xff0000) >> 16
        gc = (pixel & 0x00ff00) >> 8
        bc = (pixel & 0x0000ff)
        print GetClosestColor([rc, gc, bc])
    
    
# IO code for Hackerrank
#n = int(raw_input())
#binaryCodes = []
#for i in range(n):
#    binaryCodes.append(raw_input())
#PrintClosestColors(binaryCodes)