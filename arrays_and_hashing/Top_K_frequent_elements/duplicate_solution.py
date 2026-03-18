from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans_dict = {}
        for num in nums:
            if num in ans_dict.keys():
                ans_dict[num] +=17
            else: ans_dict[num] = 1
        freq = [[]for _ in range(len(nums)+1)]
        for key,value in ans_dict.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


test = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(test.topKFrequent(nums=nums,k=k))