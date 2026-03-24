class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # the problem:
        # i need to extract the lenght of the longest substring with unique chars
        # no need for the string itself 
        # sol:
        # try a sliding window approche
        l= 0
        charSet = set()
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res



x = Solution()
y = x.lengthOfLongestSubstring(s="abba")
print(y)
