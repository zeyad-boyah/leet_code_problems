from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # since the array is originally sorted and now it will have 2 sorted parts
        # and every element is unique 
        # the goal is to find that split
        l,r = 0, len(nums)-1
        # in case of zero rotations
        if nums[l] < nums[r]:
                return nums[l]
        ans = nums[r]
        while l <= r:
            m= (l+r)//2
            ans = min(ans,nums[m])
            if nums[m] < nums[r]:
                r = m-1
            elif nums[l] <= nums[m]:
                l = m+1
        return ans
    
test = Solution()
nums=[4,5,6,7,0,1,2]
test.findMin( nums=nums)