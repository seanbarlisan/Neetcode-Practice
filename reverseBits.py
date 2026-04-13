def reverseBits(bits):
    res = 0
    for i in range(32):
        bit = (n >> 1) & 1
        res += (bit << (31 - i))

    return res

if __name__ == "__main__":

    bits = [0, 0, 0, 0, 0, 0, 1]
    n = reverseBits(bits)
    print(n)