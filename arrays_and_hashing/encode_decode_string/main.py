from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "@" + word
        return encoded_string
    
    def decode(self, s: str) -> List[str]:
        decoded_array = []
        i = 0
        while i < len(s):  
            j = i
            while s[j] != "@":
                j += 1
            current_word_length = int(s[i:j])  
            decoded_array.append(s[j+1 : j+1+current_word_length])  
            i = j + 1 + current_word_length  
        return decoded_array

