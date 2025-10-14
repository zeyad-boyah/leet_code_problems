from typing import List
from functools import cache

class Solution:
    @cache
    def canSum(self, candidates: tuple[int], target: int) -> List[List[int]]:
        if target == 0: return True
        if target <0: return False

        for num in candidates:
            remainder = target - num
            if self.canSum(candidates, remainder) == True:
                return True
        
        return False
    

cls = Solution()
# candidates = [2,3,6,7]
# target = 7
# print(cls.combinationSum(candidates, target))
candidates = [7,14]
target = 300
print(cls.canSum(tuple(candidates), target))
# candidates = [2,3,6,7]
# target = 7
# candidates = [2,3,6,7]
# target = 7
# candidates = [2,3,6,7]
# target = 7