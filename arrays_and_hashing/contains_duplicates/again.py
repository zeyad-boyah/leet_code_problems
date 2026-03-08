from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # make a hash set with the array as it will guarntee there is no duplicates in it
        # then iterate over the array while constructing that hash set if it's aleady there then 
        # the array contains a duplicate
        nums_hash_set = set()
        for num in nums:
            if num in nums_hash_set: return True
            nums_hash_set.add(num)

        return False 
    
nums = [1,2,3,1]
test = Solution()
test.containsDuplicate(nums=nums)