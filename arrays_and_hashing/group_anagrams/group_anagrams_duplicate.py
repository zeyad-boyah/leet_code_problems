from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a 26 character hashmap of every word in the list with the index of the word
        # group the hashmap by it's unique hashed value and index keys
        hash_map= defaultdict(list)
        for word in strs:
            hashed_word = [0]*26
            for letter in word:
                hashed_word[ord(letter)-ord("a")]+=1
            
            key = tuple(hashed_word)

            # add the word to a list in that unique hashed_map key
            hash_map[key].append(word)
            
        return list(hash_map.values())
    
strs = ["eat","tea","tan","ate","nat","bat"]
test = Solution()
print(test.groupAnagrams(strs=strs))