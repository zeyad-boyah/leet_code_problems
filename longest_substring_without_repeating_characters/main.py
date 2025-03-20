class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # make 2 pointers such that one of them gets updated every letter
        # the other gets updated to be right after any duplicate letter in a set of chars
        char_dict_index = {}
        slow_pointer = 0
        longest_word = 0
        for fast_pointer, char in enumerate(s):
            # slow_pointer must not go lower than it's current value
            if char in char_dict_index and slow_pointer <= char_dict_index[char]:
                slow_pointer = (
                    char_dict_index[char] + 1
                )  # to be right after the duplicate char
            char_dict_index[char] = fast_pointer
            longest_word = max(longest_word, fast_pointer - slow_pointer + 1)
        return longest_word


x = Solution()
y = x.lengthOfLongestSubstring(s="abba")
print(y)
