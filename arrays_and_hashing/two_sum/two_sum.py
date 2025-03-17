from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter1 =0
        counter2 =1
        for num1 in nums:
            counter2 = counter1 +1
            for num2 in nums[counter2:]:
                if num1 + num2 == target:
                    return([counter1, counter2]) 
                counter2 += 1
            counter1 +=1  
        