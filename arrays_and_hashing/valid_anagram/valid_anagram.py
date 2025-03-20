class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashed_s = [0] * 26  # from a-z
        hashed_t = [0] * 26
        for L in range(len(s)):
            hashed_s[ord(s[L]) - ord("a")] += 1
            hashed_t[ord(t[L]) - ord("a")] += 1

        return hashed_s == hashed_t
