from typing import List

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            # Find the middle index
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Target is in the right half, move low pointer
                low = mid + 1
            else:
                # Target is in the left half, move high pointer
                high = mid - 1
                
        return -1
    

test = Solution()
# nums = [-1,0,3,5,9,12]
# target = 9
nums=[-1,0,3,5,9,12]
target=12

test.search(nums=nums, target=target)
