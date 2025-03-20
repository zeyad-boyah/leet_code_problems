from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_num = {}
        for i in nums:
            if i in count_num:
                count_num[i] += 1
            else:
                count_num[i] = 1
        sorted_nums = sorted(count_num.keys(), key=lambda x: count_num[x], reverse=True)
        return sorted_nums[:k]
