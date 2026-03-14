from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create a prefix and postfix arrays with the values 
        # prefix: last value in the array or 1 if it doesn't exist times the value right before the current index or 1
        nums_length = len(nums)
        pre_fix  = [1] * (nums_length +1)
        post_fix = [1] * (nums_length +1)
        ans= []
        for i in range(len(nums)):
            # to handle the first case of the prefix where the array is empty i need a default value to check from
            # currently 1 should work
            if i-1 >= 0:
                pre_fix [i+1] = pre_fix[i]* nums[i-1]

        
        for i in range(nums_length,-1,-1):
            if (i+1 < nums_length):
                post_fix[i] = post_fix[i+1] * nums[i+1]

        for i in range(nums_length):
            ans.append(pre_fix[i+1]* post_fix[i])
            
        return ans



test = Solution()
nums = [1,2,4,6]
nums2=[-1,0,1,2,3]

test.productExceptSelf(nums=nums2)


