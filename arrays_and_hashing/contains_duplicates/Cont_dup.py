from typing import List


class SolutionOne:
    def containsDuplicate(self, nums: List[int]) -> bool:
        original_list_size = len(nums)
        set_size = len(set(nums))
        if original_list_size == set_size:
            return False
        else:
            return True
        

class SolutionTwo:
    def containsDuplicate(self, nums: List[int]) -> bool:
        past_numbers_set = set()
        for num in nums:
            if num in past_numbers_set:
                return True
            else:
                past_numbers_set.add(num)
        return False
        