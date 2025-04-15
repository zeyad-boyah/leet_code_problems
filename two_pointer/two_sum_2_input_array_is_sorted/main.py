from typing import List

# O(N)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # initialize 2 pointers
        left_pointer = numbers[0] 
        left_pointer_index = 0 
        right_pointer = numbers[n-1] 
        right_pointer_index = n -1 

        for i in range(n):
            if left_pointer + right_pointer == target:
                # +1 to indices because it is a 1-indexed array
                return [ left_pointer_index+1, right_pointer_index+1]
            elif left_pointer + right_pointer > target:
                right_pointer_index = right_pointer_index - 1
                right_pointer = numbers[right_pointer_index]
            elif left_pointer + right_pointer < target:
                left_pointer_index = left_pointer_index + 1 
                left_pointer = numbers[left_pointer_index]


# brute force 
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         # initialize 2 pointers
#         pointer_1_key = None
#         pointer_1_value = None
#         pointer_2_key = None
#         pointer_2_value = None

#         # enumerate from 1 because it is  1-indexed array
#         for key, value in enumerate(numbers, 1):
#             pointer_1_value = value
#             pointer_1_key = key
#             for i in range(-1, -len(numbers) , -1):
#                 pointer_2_value = numbers[i]
#                 # since i is from the back (negative) 
#                 pointer_2_key = len(numbers) + i + 1

#                 if pointer_1_value + pointer_2_value == target:
#                     return [pointer_1_key, pointer_2_key]
                
#         return []
    