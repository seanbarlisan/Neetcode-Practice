def reverseBits(n):
    n = int(n)
    res = 0
    for i in range(32):
        bit = (n >> 1) & 1
        res += (bit << (31 - i))

    return res

if __name__ == "__main__":

    bits = "00000000000000000000000000010101"
    n = reverseBits(bits)
    print(n)