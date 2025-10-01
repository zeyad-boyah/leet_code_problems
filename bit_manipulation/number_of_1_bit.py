class Solution:
    def hammingWeight(self, n: int) -> int:
        # bin_n = bin(n)
        # i=2 # starting from after the header
        # set_bits= 0
        # while i < len(bin_n):
        #     set_bits += int(bin_n[i])
        #     i+=1
        # return set_bits
        # return bin(n).count("1")
        return n.bit_count()