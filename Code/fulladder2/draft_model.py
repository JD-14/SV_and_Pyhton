import random

p, g = 0, 0
delay = 0
def fulladder2(a, b, cin):
    global delay
    global  p, g
    psum, pcout = 0, 0
    
    print(a, b, cin, "---->", p, g)
    if delay==0:
        p = a^b
        g = a&b
        delay = 1
        print("x x x --->", p, g)
        print("delay applied")
        return p, g, psum, pcout

    else:
        
        psum = p ^ cin
        pcout = g | (p & cin)
        p = a^b
        g = a&b
        print("x x x --->", p, g)
        print("after delay")
        return p, g, psum, pcout
    
        

for i in range(3):
        print("LOOP",i )
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        c = random.randint(0,1)
        p, g, psum, pcout = fulladder2(a, b, c)
        print(p, g, psum, pcout, "\n\n")


'''
    p, g = 0, 0

    p = a ^ b
    g = a & b
    psum = p ^ cin
    pcout = g | (p & cin)

    return p, g, psum, pcout
'''

