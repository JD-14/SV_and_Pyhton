def gates(a, b):
    y1, y2, y3, y4, y5 = 0, 0, 0, 0, 0
    offset = 4
    
    y1 = a & b  #AND
    y2 = a | b  #OR
    y3 = a ^ b  #XOR
    y4 = ~(a & b)+offset #NAND
    y5 = ~(a | b)+offset #NOR

    return y1, y2, y3, y4, y5
