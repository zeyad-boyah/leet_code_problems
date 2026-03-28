from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a monotonic stack where we maintain descending order
        stack = []
        ans =[0]* len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                day= stack.pop()
                ans[day[0]]= i - day[0]
            stack.append((i,temp))
        return ans

    

test = Solution()
temperatures=[30,38,30,36,35,40,28]
test.dailyTemperatures(temperatures=temperatures)