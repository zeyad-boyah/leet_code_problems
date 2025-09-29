from typing import List

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         if nums[0]!= 0:
#             return 0
#         for i in range(len(nums)):
#             if nums[i]> nums[i-1] +1:
#                 return nums[i]-1
#         return nums[-1] +1

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        supposed_sum=0
        actual_sum=0
        n=1
        is_there_zero= False
        max_num=0
        for num in nums:
            actual_sum+=num
            supposed_sum += n
            n+=1
            max_num = num if num>max_num else max_num
            if num == 0:
                is_there_zero= True
        if not is_there_zero: return 0
        elif actual_sum == supposed_sum:
            return max_num+1
        else:
            return supposed_sum- actual_sum
