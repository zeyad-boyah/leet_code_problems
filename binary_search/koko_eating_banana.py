from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # problem :
        # we have an array with a varible number of banans for each index
        # we can only eat from one index at a given hour even if we finish early 
        # we have time limit (h) that we need to finish eating banana before 
        # (h) will always be bigger than or equal to len piles 
        # sol:
        #  we can assume that k is equal to max (piles) if h= len(piles)
        # and it will decrease as h increases while len(piles) is constant
        # max k = max (piles)
        max_piles = max(piles)
        len_piles = len(piles)
        l,r = 1, max_piles
        lowest_speed = max_piles
        # search for a valid speed from 1 to max_piles using binary search
        while l <=r:
            m = (l+r)//2
            total_run_time = 0
            for pile in piles:
                total_run_time += math.ceil(pile/m)
            if total_run_time <= h:
                lowest_speed= min(lowest_speed, m)
                r = m-1
            else:
                l = m+1
        return lowest_speed


piles = [1,4,3,2]
h = 9
test = Solution()
test.minEatingSpeed(piles=piles,h=h)
