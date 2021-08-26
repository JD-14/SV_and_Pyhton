def sillyfunction(a, b, c):
    if ( ((not a) & (not b) & (not c)) | (a & (not b) & (not c)) | (a & (not b) & c) ):
        return 1
    else:
        return 0
