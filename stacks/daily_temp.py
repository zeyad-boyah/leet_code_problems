from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # the problem:
        # i need to make an array that tells when will a higher
        # temp occur from the curret iterable without being O(n^2)
        # suggested solution is to use a monotonic stack
        # by building the stack so that it keeps Desc order we can keep track of the day
        # by simply poping the elements when we reach a higher temp and 
        # calculating the difference between it's index and the current element
        res = [0]* len(temperatures)
        mono_stack = []
        for i,t in enumerate(temperatures):
            while mono_stack and t > mono_stack[-1][0]:
                head_temp, head_index = mono_stack.pop()
                res[head_index] = i - head_index
            mono_stack.append((t,i))
        return res
    

test = Solution()
temperatures=[30,38,30,36,35,40,28]
test.dailyTemperatures(temperatures=temperatures)