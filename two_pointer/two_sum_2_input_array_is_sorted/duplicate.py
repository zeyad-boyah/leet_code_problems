class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # make a fast and slow pointers and iterate over the list for every posible comp of slow and fast
        slow , fast = 0,1
        while slow < len(numbers):
            for fast in range(slow,len(numbers),1):
                if numbers[slow] + numbers[fast] == target:
                    return [slow+1,fast+1]
            slow+=1