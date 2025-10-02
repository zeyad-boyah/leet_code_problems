from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        max_left = [0] * n
        max_right = [0] * n
        
        # fill max_left
        current_max = 0
        for i in range(n):
            max_left[i] = current_max
            current_max = max(current_max, height[i])
        
        # fill max_right
        current_max = 0
        for i in range(n-1, -1, -1):
            max_right[i] = current_max
            current_max = max(current_max, height[i])
        
        # calculate water
        water = 0
        for i in range(n):
            water += max(min(max_left[i], max_right[i]) - height[i], 0)
        
        return water

            
            
sus = Solution()
height =[0,1,0,2,1,0,1,3,2,1,2,1]
sus.trap(height)

            
