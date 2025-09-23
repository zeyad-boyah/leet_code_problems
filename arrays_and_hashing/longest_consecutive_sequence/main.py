from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq_len = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_longest = 1
                while num + current_longest in num_set:
                    current_longest += 1
                max_seq_len = (
                    current_longest if current_longest > max_seq_len else max_seq_len
                )
        # print (max_seq_len)
        return max_seq_len


test = Solution()
test.longestConsecutive(nums=[0, -1])
# test.longestConsecutive(nums=[100,4,200,1,3,2])
