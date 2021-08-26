def fulladder(a, b, cin):
    psum = a ^ b ^ cin
    pcout = (a & b) |((a^b) & cin)
    return psum, pcout