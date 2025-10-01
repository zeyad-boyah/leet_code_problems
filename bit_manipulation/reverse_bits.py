class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = '{:032b}'.format(n)
        bits = []
        i = len(bin_n) - 1
        while i >= 0:
            bits.append(bin_n[i])
            i -= 1
        return int("".join(bits), 2)
