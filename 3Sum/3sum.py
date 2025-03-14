from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans= []

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue

            j = i +1
            k = len(nums)-1
            while j<k :
                total = nums[i] +nums[k]+ nums[j]
                if total < 0:
                    j +=1
                elif total > 0:
                    k -=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j +=1
                    while nums[j] == nums[j-1] and j<k:
                        j += 1
        return ans