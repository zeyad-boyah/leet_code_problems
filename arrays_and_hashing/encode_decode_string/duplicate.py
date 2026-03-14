from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_word = ""
        for word in strs:
            word_length = len(word)
            encoded_word = encoded_word + f"{word_length}#" + word 
        return encoded_word
    def decode(self, s: str) -> List[str]:
        # check if the current pointer is pointing to and number or not
        # and stop on the "#"
        # take the number from the pointer start to the '#' and that's the number
        # of letter in the current word 
        # move the start pointer to the letter right after # 
        # slice the numbers from the start pointer to the pointer + lenght of the word 
        decoded_word_list = []
        current_word_length_string = ""
        start_pointer = 0
        while start_pointer < len(s):
            if s[start_pointer].isdigit():
                    current_word_length_string +=s[start_pointer] 
                    start_pointer +=1
            else:
                    word_start = start_pointer + 1
                    word_end = word_start + int(current_word_length_string )
                    decoded_word_list.append(s[word_start: word_end]) 
                    # clear the word lenght and move the poitner
                    start_pointer= word_end
                    current_word_length_string = ""

        return decoded_word_list


test = Solution()
dummy_input = ["Hello","World"]
dummy_input2=["",""]
word =test.encode(dummy_input2)
test.decode(s=word)