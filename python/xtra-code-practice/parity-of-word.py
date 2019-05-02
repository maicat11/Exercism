# The parity of a word is 1 if the number of 1s in the binary representation of the word is odd, else it is 0.


# count bits
def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

# print(count_bits(12)) #1100
# print(count_bits(150)) #1111

def parity(x: int) -> int:
    if count_bits(x) % 2 == 0:
        return 0
    return 1

print(parity(11))