def IsHexspeak(n):
    hexn = hex(n)
    for c in ['2', '3', '4', '5', '6', '7', '8', '9']:
        if c in hexn: return False
    return True