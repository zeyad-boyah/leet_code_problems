from typing import List
import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        product_of_all_nums = 1
        number_of_zero_elements = 0
        answer = [0] * len_nums
        for num in nums:
            if num != 0:
                product_of_all_nums *= num
            else:
                number_of_zero_elements += 1

        if number_of_zero_elements > 1:
            return answer

        for i in range(len_nums):
            if number_of_zero_elements > 0:
                answer[i] = 0 if nums[i] != 0 else product_of_all_nums
            else:
                answer[i] = product_of_all_nums // nums[i]

        return answer


# bad solution due to overall time complexity of n^2
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         answer = [0] * len(nums)
#         for i in range(len(nums)):
#             answer[i] = math.prod(nums[:i]) * math.prod(nums[i+1:])
#         return answer


# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
