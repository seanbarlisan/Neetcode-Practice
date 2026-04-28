def getSum(a, b):
    carry = 0 # Carry Bit 
    res = 0 # Result Value 
    mask = 0xFFFFFFFF # 32 bits, F is hexadecimal, so 1111 1111 1111 1111 1111 1111 1111 1111

    for i in range(32): # for each bit
        a_bit = (a >> i) & 1 # Bitwise Shift Right (first number)
        b_bit = (b >> i) & 1 # Bitwise Shift Right (second number)
        cur_bit = a_bit ^ b_bit ^ carry # XOR across all of these
        carry = (a_bit + b_bit + carry) >= 2
        if cur_bit:
            res |= (1 << i)

    if res > 0x7FFFFFFF:
        res = ~(res ^ mask)

    return res 

if __name__ == "__main__":

    value = getSum(1, 1)
    print(value)