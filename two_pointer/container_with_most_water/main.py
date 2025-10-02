from typing import List

# O(n) sol
class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer1,pointer2 =0,len(height)-1
        max_area= 0
        while pointer1 < len(height)  and pointer1 < pointer2:
            current_area = min(height[pointer1], height[pointer2]) * (pointer2 - pointer1)
            max_area = current_area if current_area > max_area else max_area
            if height[pointer1] < height[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1
        # print(max_area)
        return max_area
    
"""
brute force 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer1,pointer2 =0,0
        max_area= 0
        for pointer1 in range(len(height)):
            for pointer2 in range(pointer1 +1, len(height)):
                current_area = min(height[pointer1], height[pointer2]) * (pointer2 - pointer1)
                max_area = current_area if current_area > max_area else max_area
        return max_area
"""
    
sus = Solution()
# height = [1,8,6,2,5,4,8,3,7]
# height = [8,7,2,1]
height = [3,6,1]
sus.maxArea(height)