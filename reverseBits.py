def reverseBits(n):
    res = 0 # the result is 0 for what we want to input
    for i in range(32): # for i in the 32 bit range 
        bit = (n >> 1) & 1 # right shift bit AND 1, so 0 AND 1 is 0 
        res += (bit << (31 - i)) # res is left shift bit of the new value

    return res

if __name__ == "__main__":

    bits = "00000000000000000000000000010101"
    n = reverseBits(bits)
    print(n)