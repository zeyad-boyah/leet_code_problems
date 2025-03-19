from typing import List
from collections import defaultdict




# solution using hash table
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_sorted_dict = defaultdict(list)

        for word in strs:
            count = [0] * 26  # count array for letters a to z
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            words_sorted_dict[tuple(count)].append(word)
        return list(words_sorted_dict.values())


# time complexly: O(m * n log n) 
# space complexly: O(m * n ) 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_sorted_dict = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            words_sorted_dict[sorted_word].append(word)
        return list(words_sorted_dict.values())
        


# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Brute force solution
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         output = []
#         sorted_strs_list = list(map(lambda x: sorted(x), strs))
#         list_of_indices_taken = []

#         for i in range(len(sorted_strs_list)):
#             temp_list = []

#             for j in range(i+1, len(strs)):
#                 if sorted_strs_list[i] == sorted_strs_list[j] and j not in list_of_indices_taken:
#                     temp_list.append(strs[j])
#                     list_of_indices_taken.append(j)
#             if i not in list_of_indices_taken:
#                 temp_list.append(strs[i])
#                 output.append(temp_list)
#         return output