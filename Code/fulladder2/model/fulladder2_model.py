#Global Variables used to store previous values
a_prev, b_prev, cin_prev = 0, 0, 0
p, g = 0, 0
psum, pcout = 0, 0
delay = 0

def fulladder2(a, b, cin):
    global a_prev, b_prev, cin_prev
    global delay
    global  p, g
    global psum, pcout
    temp_p, temp_g = 0, 0

    temp_p = p
    temp_g = g

    if delay==0:
        delay = 1

        #Store input values
        a_prev = a
        b_prev = b
        cin_prev = cin

        #Compute p & g
        p = a ^ b
        g = a & b
        return p, g, psum, pcout, temp_p, temp_g, 11

    elif (a != a_prev) | (b != b_prev) | (cin != cin_prev):
        #Store input values
        a_prev = a
        b_prev = b
        cin_prev = cin

        #Compute Sum, CarryOut, p, & g
        psum = temp_p ^ cin
        pcout = temp_g | (temp_p & cin)
        p = a ^ b
        g = a & b
        return p, g, psum, pcout, temp_p, temp_g, 22
    else:
        #NO change in inputs, therefore Outputs stays same
        return  temp_p, temp_g, psum, pcout, temp_p, temp_g, 33


