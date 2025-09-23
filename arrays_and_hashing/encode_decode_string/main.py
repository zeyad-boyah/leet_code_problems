from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_word = ""
        for word in strs:
            encoded_word += str(len(word)) + "&" + word
        return encoded_word

    def decode(self, s: str) -> List[str]:
        encoded_word_pointer = 0
        decoded_arr = []
        while encoded_word_pointer < len(s):
            dec_word_pointer = encoded_word_pointer
            while s[dec_word_pointer] != "&":
                dec_word_pointer += 1
            current_word_length = int(s[encoded_word_pointer:dec_word_pointer])
            decoded_arr.append(
                s[dec_word_pointer + 1 : dec_word_pointer + current_word_length + 1]
            )
            encoded_word_pointer = dec_word_pointer + current_word_length + 1
        return decoded_arr


# sus = Solution.encode(["neet","code","love","you"])

# Solution.decode(sus)
