from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(target):
            if target == 0: return []
            if target <0: return None

            for num in candidates:
                remainder = target - num
                remainder_res = helper(remainder)
                if remainder_res:
                    return remainder_res +[num]
            ans = [remainder_res, target]
            return ans

        return helper(target)
    

cls = Solution()
candidates = [2,3,6,7]
target = 7
print(cls.combinationSum(candidates, target))
# candidates = [7,14]
# target = 300
# print(cls.canSum(tuple(candidates), target))