from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert the list into a set and keep track of the smallest numbers in a set
        # iterate over the smallest numbers set while looking for the current iterable +1 in the num set
        if nums == []: return 0
        sequnce_starters = set()
        nums_set = set(nums)
        ans_set = set()
        for num in nums:
            if num -1 in nums_set:
                continue
            sequnce_starters.add(num)
        
        for num in sequnce_starters:
            current_sequence_head = num
            current_sequence_length = 0
            while current_sequence_head in nums_set:
                current_sequence_length+=1
                current_sequence_head +=1
            ans_set.add(current_sequence_length)
        return max(ans_set)

test = Solution()
nums = [2,20,4,10,3,4,5]
test.longestConsecutive(nums=nums)