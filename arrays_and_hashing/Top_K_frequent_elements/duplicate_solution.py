from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a hash map of every unique num in the array and the number of it's repition 
        hash_map = {}

        for num in nums:
            if num not in hash_map.keys(): hash_map [num] = 0
            hash_map[num] +=1
        sorted_hash_map_by_values = dict(sorted(hash_map.items(), key=lambda item: item[1]))
        # get the first k elements on the sorted hash map
        keys_list = list(sorted_hash_map_by_values.keys())

        return  keys_list[-k:]


test = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(test.topKFrequent(nums=nums,k=k))