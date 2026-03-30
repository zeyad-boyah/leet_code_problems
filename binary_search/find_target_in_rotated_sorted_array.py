from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # since the array is originally sorted and now it will have 2 sorted parts
        # and every element is unique 
        # the goal is to find that split
        l,r = 0, len(nums)-1
        # in case of zero rotations
        if nums[l] < nums[r]:
            inflection_point = l
        else:
            ans = nums[r]
            inflection_point = r
            while l <= r:
                m= (l+r)//2
                if ans > nums[m]:
                    ans = nums[m]
                    inflection_point = m
                if nums[m] < nums[r]:
                    r = m-1
                elif nums[l] <= nums[m]:
                    l = m+1
        # now that i have the inflection point i can do 
        # a binary search on the part that might contain the target
        if target <= nums[-1]:
            l,r = inflection_point,len(nums)-1
        else:
            l,r = 0, inflection_point-1
        while l <=r :
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] <= target:
                l = m +1
            else:
                r = m-1
        return -1
             
    
    
test = Solution()
nums=[5,1,3]
target=5
test.search(nums=nums, target=target)